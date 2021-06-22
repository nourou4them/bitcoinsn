#!/usr/bin/env python3
# Copyright (c) 2017-2020 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from collections import defaultdict
from test_framework.blocktools import (create_block, create_coinbase)
from test_framework.messages import CInv, MSG_BLOCK
from test_framework.p2p import (
    P2PInterface,
    msg_block,
    msg_getdata,
    p2p_lock,
)
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    assert_equal,
)


class BaseNode(P2PInterface):
    def __init__(self):
        super().__init__()
        self.block_receive_map = defaultdict(int)

    def on_block(self, message):
        message.block.calc_sha256()
        self.block_receive_map[message.block.sha256] += 1


class ExampleTest(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 3
        self.extra_args = [[], ["-logips"], []]

    def skip_test_if_missing_module(self):
        self.skip_if_no_wallet()


    def setup_network(self):
        self.setup_nodes()
        self.connect_nodes(0, 1)
        self.sync_all(self.nodes[0:2])


    def run_test(self):
        peer_messaging = self.nodes[0].add_p2p_connection(BaseNode())
        blocks = [int(self.nodes[1].generate(nblocks=1)[0], 16)]
        self.sync_all(self.nodes[0:2])

        self.log.info("Starting test!")

        self.log.info("Create some blocks")
        self.tip = int(self.nodes[1].getbestblockhash(), 16)
        self.block_time = self.nodes[1].getblock(self.nodes[1].getbestblockhash())['time'] + 1

        height = self.nodes[1].getblockcount()

        for _ in range(10):
            block = create_block(self.tip, create_coinbase(height+1), self.block_time)
            block.solve()
            block_message = msg_block(block)
            peer_messaging.send_message(block_message)
            self.tip = block.sha256
            blocks.append(self.tip)
            self.block_time += 1
            height += 1

        self.log.info("Wait for node1 to reach current tip (height 11) using RPC")
        self.nodes[1].waitforblockheight(11)

        self.log.info("Connect node2 and node1")
        self.connect_nodes(1, 2)

        self.log.info("Wait for node2 to receive all the blocks from node1")
        self.sync_all()

        self.log.info("Add P2P connection to node2")
        self.nodes[0].disconnect_p2ps()
        peer_receiving = self.nodes[2].add_p2p_connection(BaseNode())

        self.log.info("Test that node2 propagates all the blocks to us")
        getdata_request = msg_getdata()
        for block in blocks:
            getdata_request.inv.append(CInv(MSG_BLOCK, block))
        peer_receiving.send_message(getdata_request)
        peer_receiving.wait_until(lambda: sorted(blocks) == sorted(list(peer_receiving.block_receive_map.keys())), timeout=5)

        #self.log.options.nocleanup

        self.log.info("Check that each block was received only once")
        with p2p_lock:
            for block in peer_receiving.block_receive_map.values():
                assert_equal(block, 1)


if __name__ == '__main__':
    ExampleTest().main()
