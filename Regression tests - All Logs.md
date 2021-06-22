# Regression tests - Logs

Regression tests have been run by directly call test script : 

        test/functional/test_runner.py    

Here are the testing results :  

        nourou@DESKTOP-II5GT2R:~/bitcoin$ python3 test/functional/feature_rbf.py
        2021-06-20T11:15:37.183000Z TestFramework (INFO): Initializing test directory /tmp/bitcoin_func_test_ozw_p_1j
        2021-06-20T11:15:52.002000Z TestFramework (INFO): Running test simple doublespend...
        2021-06-20T11:15:52.088000Z TestFramework (INFO): Running test doublespend chain...
        2021-06-20T11:15:52.734000Z TestFramework (INFO): Running test doublespend tree...
        2021-06-20T11:15:59.451000Z TestFramework (INFO): Running test replacement feeperkb...
        2021-06-20T11:15:59.586000Z TestFramework (INFO): Running test spends of conflicting outputs...
        2021-06-20T11:15:59.698000Z TestFramework (INFO): Running test new unconfirmed inputs...
        2021-06-20T11:15:59.788000Z TestFramework (INFO): Running test too many replacements...
        2021-06-20T11:16:01.441000Z TestFramework (INFO): Running test opt-in...
        2021-06-20T11:16:01.578000Z TestFramework (INFO): Running test RPC...
        2021-06-20T11:16:01.626000Z TestFramework (INFO): Running test prioritised transactions...
        2021-06-20T11:16:01.818000Z TestFramework (INFO): Running test no inherited signaling...
        2021-06-20T11:16:01.850000Z TestFramework (INFO): Passed
        2021-06-20T11:16:01.901000Z TestFramework (INFO): Stopping nodes
        2021-06-20T11:16:02.463000Z TestFramework (INFO): Cleaning up /tmp/bitcoin_func_test_ozw_p_1j on exit
        2021-06-20T11:16:02.463000Z TestFramework (INFO): Tests successful
        nourou@DESKTOP-II5GT2R:~/bitcoin$
        nourou@DESKTOP-II5GT2R:~/bitcoin$ python3 test/functional/test_runner.py
        Temporary test directory at /tmp/test_runner_₿_🏃_20210620_131826
        Running Unit Tests for Test Framework Modules
        ..........
        ----------------------------------------------------------------------
        Ran 10 tests in 0.635s

        OK
        1/208 - wallet_hd.py --descriptors skipped
        2/208 - wallet_backup.py --descriptors skipped
        3/208 - wallet_hd.py --legacy-wallet passed, Duration: 12 s
        4/208 - wallet_backup.py --legacy-wallet passed, Duration: 62 s
        5/208 - mining_getblocktemplate_longpoll.py passed, Duration: 69 s
        6/208 - rpc_fundrawtransaction.py --descriptors skipped
        7/208 - feature_maxuploadtarget.py passed, Duration: 74 s
        8/208 - p2p_compactblocks.py passed, Duration: 28 s
        9/208 - feature_segwit.py --legacy-wallet passed, Duration: 32 s
        10/208 - wallet_basic.py --descriptors skipped
        11/208 - wallet_labels.py --legacy-wallet passed, Duration: 13 s
        12/208 - wallet_labels.py --descriptors skipped
        13/208 - rpc_fundrawtransaction.py --legacy-wallet passed, Duration: 100 s
        14/208 - feature_block.py passed, Duration: 154 s
        15/208 - p2p_timeouts.py passed, Duration: 9 s
        16/208 - wallet_basic.py --legacy-wallet passed, Duration: 72 s
        17/208 - wallet_dump.py --legacy-wallet passed, Duration: 39 s
        18/208 - p2p_segwit.py passed, Duration: 95 s
        19/208 - wallet_listtransactions.py --descriptors skipped
        20/208 - p2p_tx_download.py passed, Duration: 52 s
        21/208 - rpc_signer.py passed, Duration: 7 s
        22/208 - wallet_signer.py --descriptors skipped
        23/208 - p2p_sendheaders.py passed, Duration: 16 s
        24/208 - wallet_importmulti.py --legacy-wallet passed, Duration: 18 s
        25/208 - mempool_limit.py passed, Duration: 6 s
        26/208 - rpc_txoutproof.py passed, Duration: 4 s
        27/208 - wallet_listtransactions.py --legacy-wallet passed, Duration: 65 s
        28/208 - wallet_listreceivedby.py --descriptors skipped
        29/208 - wallet_listreceivedby.py --legacy-wallet passed, Duration: 23 s
        30/208 - wallet_abandonconflict.py --descriptors skipped
        31/208 - wallet_abandonconflict.py --legacy-wallet passed, Duration: 20 s
        32/208 - feature_csv_activation.py passed, Duration: 20 s
        33/208 - rpc_rawtransaction.py --descriptors skipped
        34/208 - feature_taproot.py passed, Duration: 104 s
        35/208 - wallet_address_types.py --descriptors skipped
        36/208 - rpc_rawtransaction.py --legacy-wallet passed, Duration: 65 s
        37/208 - wallet_address_types.py --legacy-wallet passed, Duration: 48 s
        38/208 - feature_reindex.py passed, Duration: 12 s
        39/208 - p2p_feefilter.py passed, Duration: 16 s
        40/208 - feature_bip68_sequence.py passed, Duration: 69 s
        41/208 - wallet_keypool_topup.py --descriptors skipped
        42/208 - feature_abortnode.py passed, Duration: 35 s
        43/208 - interface_zmq.py skipped
        44/208 - rpc_invalid_address_message.py passed, Duration: 3 s
        45/208 - interface_bitcoin_cli.py passed, Duration: 19 s
        46/208 - mempool_resurrect.py passed, Duration: 3 s
        47/208 - wallet_txn_doublespend.py --mineblock passed, Duration: 8 s
        48/208 - wallet_keypool_topup.py --legacy-wallet passed, Duration: 80 s
        49/208 - tool_wallet.py --descriptors skipped
        50/208 - wallet_txn_clone.py passed, Duration: 6 s
        51/208 - wallet_txn_clone.py --segwit passed, Duration: 6 s
        52/208 - rpc_getchaintips.py passed, Duration: 6 s
        53/208 - tool_wallet.py --legacy-wallet passed, Duration: 31 s
        54/208 - rpc_misc.py passed, Duration: 8 s
        55/208 - mempool_spend_coinbase.py passed, Duration: 2 s
        56/208 - interface_rest.py passed, Duration: 12 s
        57/208 - wallet_avoidreuse.py --descriptors skipped
        58/208 - feature_fee_estimation.py passed, Duration: 103 s
        59/208 - mempool_reorg.py passed, Duration: 5 s
        60/208 - mempool_persist.py passed, Duration: 30 s
        61/208 - wallet_multiwallet.py --descriptors skipped
        62/208 - mempool_updatefromblock.py passed, Duration: 376 s
        63/208 - wallet_createwallet.py --legacy-wallet passed, Duration: 5 s
        64/208 - wallet_avoidreuse.py --legacy-wallet passed, Duration: 69 s
        65/208 - wallet_createwallet.py --descriptors skipped
        66/208 - wallet_multiwallet.py --legacy-wallet passed, Duration: 63 s
        67/208 - wallet_createwallet.py --usecli passed, Duration: 10 s
        68/208 - wallet_watchonly.py --legacy-wallet passed, Duration: 4 s
        69/208 - wallet_watchonly.py --usecli --legacy-wallet passed, Duration: 7 s
        70/208 - interface_http.py passed, Duration: 6 s
        71/208 - wallet_multiwallet.py --usecli passed, Duration: 45 s
        72/208 - rpc_psbt.py --descriptors skipped
        73/208 - interface_rpc.py passed, Duration: 6 s
        74/208 - rpc_whitelist.py passed, Duration: 3 s
        75/208 - wallet_reorgsrestore.py passed, Duration: 15 s
        76/208 - feature_proxy.py passed, Duration: 3 s
        77/208 - rpc_signrawtransaction.py --descriptors skipped
        78/208 - rpc_users.py passed, Duration: 11 s
        79/208 - rpc_signrawtransaction.py --legacy-wallet passed, Duration: 18 s
        80/208 - wallet_groups.py --descriptors skipped
        81/208 - p2p_disconnect_ban.py passed, Duration: 6 s
        82/208 - p2p_addrv2_relay.py passed, Duration: 18 s
        83/208 - rpc_decodescript.py passed, Duration: 2 s
        84/208 - rpc_deprecated.py passed, Duration: 3 s
        85/208 - wallet_disable.py --legacy-wallet passed, Duration: 3 s
        86/208 - wallet_disable.py --descriptors passed, Duration: 1 s
        87/208 - rpc_psbt.py --legacy-wallet passed, Duration: 43 s
        88/208 - rpc_blockchain.py passed, Duration: 16 s
        89/208 - p2p_getdata.py passed, Duration: 2 s
        90/208 - p2p_addr_relay.py passed, Duration: 16 s
        91/208 - p2p_getaddr_caching.py passed, Duration: 17 s
        92/208 - wallet_keypool.py --descriptors skipped
        93/208 - wallet_descriptor.py --descriptors skipped
        94/208 - wallet_keypool.py --legacy-wallet passed, Duration: 4 s
        95/208 - p2p_nobloomfilter_messages.py passed, Duration: 2 s
        96/208 - rpc_net.py passed, Duration: 14 s
        97/208 - rpc_setban.py passed, Duration: 6 s
        98/208 - p2p_filter.py passed, Duration: 9 s
        99/208 - p2p_invalid_locator.py passed, Duration: 3 s
        100/208 - mining_prioritisetransaction.py passed, Duration: 7 s
        101/208 - p2p_invalid_block.py passed, Duration: 3 s
        102/208 - p2p_invalid_tx.py passed, Duration: 8 s
        103/208 - p2p_invalid_messages.py passed, Duration: 13 s
        104/208 - example_test.py passed, Duration: 6 s
        105/208 - feature_assumevalid.py passed, Duration: 14 s
        106/208 - wallet_txn_doublespend.py --legacy-wallet passed, Duration: 5 s
        107/208 - wallet_txn_doublespend.py --descriptors skipped
        108/208 - wallet_groups.py --legacy-wallet passed, Duration: 91 s
        109/208 - feature_backwards_compatibility.py --legacy-wallet skipped
        110/208 - p2p_blocksonly.py passed, Duration: 38 s
        111/208 - feature_backwards_compatibility.py --descriptors skipped
        112/208 - rpc_invalidateblock.py passed, Duration: 5 s
        113/208 - rpc_getblockfilter.py passed, Duration: 8 s
        114/208 - feature_utxo_set_hash.py passed, Duration: 4 s
        115/208 - wallet_txn_clone.py --mineblock passed, Duration: 11 s
        116/208 - feature_rbf.py passed, Duration: 23 s
        117/208 - feature_notifications.py passed, Duration: 40 s
        118/208 - rpc_createmultisig.py --descriptors skipped
        119/208 - rpc_packages.py passed, Duration: 4 s
        120/208 - feature_versionbits_warning.py passed, Duration: 6 s
        121/208 - rpc_createmultisig.py --legacy-wallet passed, Duration: 24 s
        122/208 - rpc_preciousblock.py passed, Duration: 7 s
        123/208 - wallet_importprunedfunds.py --descriptors skipped
        124/208 - p2p_leak_tx.py passed, Duration: 3 s
        125/208 - wallet_importprunedfunds.py --legacy-wallet passed, Duration: 9 s
        126/208 - rpc_signmessage.py passed, Duration: 3 s
        127/208 - mempool_package_onemore.py passed, Duration: 59 s
        128/208 - p2p_eviction.py passed, Duration: 8 s
        129/208 - mempool_packages.py passed, Duration: 61 s
        130/208 - wallet_balance.py --descriptors skipped
        131/208 - rpc_generate.py passed, Duration: 2 s
        132/208 - feature_nulldummy.py --descriptors skipped
        133/208 - rpc_generateblock.py passed, Duration: 6 s
        134/208 - feature_nulldummy.py --legacy-wallet passed, Duration: 3 s
        135/208 - mempool_expiry.py passed, Duration: 5 s
        136/208 - mempool_accept.py passed, Duration: 12 s
        137/208 - wallet_import_with_label.py --legacy-wallet passed, Duration: 7 s
        138/208 - wallet_importdescriptors.py --descriptors skipped
        139/208 - wallet_upgradewallet.py --legacy-wallet skipped
        140/208 - wallet_balance.py --legacy-wallet passed, Duration: 19 s
        141/208 - rpc_bind.py --ipv4 failed, Duration: 3 s

        stdout:
        2021-06-20T11:31:10.023000Z TestFramework (INFO): Initializing test directory /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_66
        2021-06-20T11:31:10.188000Z TestFramework (INFO): Check for linux
        2021-06-20T11:31:10.188000Z TestFramework (INFO): Check for ipv6
        2021-06-20T11:31:10.189000Z TestFramework (INFO): Check for non-loopback interface
        2021-06-20T11:31:10.189000Z TestFramework (INFO): Bind test for ['127.0.0.1']
        2021-06-20T11:31:12.025000Z TestFramework (ERROR): Unexpected exception caught during testing
        Traceback (most recent call last):
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 128, in main
            self.run_test()
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 89, in run_test
            self._run_loopback_tests()
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 97, in _run_loopback_tests
            [('127.0.0.1', self.defaultport)])
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 43, in run_bind_test
            assert_equal(set(get_bind_addrs(pid)), set(expected))
        File "/home/nourou/bitcoin/test/functional/test_framework/netutil.py", line 82, in get_bind_addrs
            for conn in netstat('tcp') + netstat('tcp6'):
        File "/home/nourou/bitcoin/test/functional/test_framework/netutil.py", line 63, in netstat
            content.pop(0)
        IndexError: pop from empty list
        2021-06-20T11:31:12.155000Z TestFramework (INFO): Stopping nodes
        2021-06-20T11:31:13.020000Z TestFramework (WARNING): Not cleaning up dir /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_66
        2021-06-20T11:31:13.020000Z TestFramework (ERROR): Test failed. Test logging available at /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_66/test_framework.log
        2021-06-20T11:31:13.021000Z TestFramework (ERROR):
        2021-06-20T11:31:13.021000Z TestFramework (ERROR): Hint: Call /home/nourou/bitcoin/test/functional/combine_logs.py '/tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_66' to consolidate all logs
        2021-06-20T11:31:13.021000Z TestFramework (ERROR):
        2021-06-20T11:31:13.021000Z TestFramework (ERROR): If this failure happened unexpectedly or intermittently, please file a bug and provide a link or upload of the combined log.
        2021-06-20T11:31:13.021000Z TestFramework (ERROR): https://github.com/bitcoin/bitcoin/issues
        2021-06-20T11:31:13.022000Z TestFramework (ERROR):


        stderr:


        142/208 - rpc_bind.py --ipv6 failed, Duration: 4 s

        stdout:
        2021-06-20T11:31:10.401000Z TestFramework (INFO): Initializing test directory /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_65
        2021-06-20T11:31:10.402000Z TestFramework (INFO): Check for linux
        2021-06-20T11:31:10.402000Z TestFramework (INFO): Check for ipv6
        2021-06-20T11:31:10.403000Z TestFramework (INFO): Check for non-loopback interface
        2021-06-20T11:31:10.403000Z TestFramework (INFO): Bind test for []
        2021-06-20T11:31:12.312000Z TestFramework (ERROR): Unexpected exception caught during testing
        Traceback (most recent call last):
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 128, in main
            self.run_test()
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 89, in run_test
            self._run_loopback_tests()
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 107, in _run_loopback_tests
            [('127.0.0.1', self.defaultport), ('::1', self.defaultport)])
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 43, in run_bind_test
            assert_equal(set(get_bind_addrs(pid)), set(expected))
        File "/home/nourou/bitcoin/test/functional/test_framework/netutil.py", line 82, in get_bind_addrs
            for conn in netstat('tcp') + netstat('tcp6'):
        File "/home/nourou/bitcoin/test/functional/test_framework/netutil.py", line 63, in netstat
            content.pop(0)
        IndexError: pop from empty list
        2021-06-20T11:31:12.549000Z TestFramework (INFO): Stopping nodes
        2021-06-20T11:31:13.874000Z TestFramework (WARNING): Not cleaning up dir /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_65
        2021-06-20T11:31:13.875000Z TestFramework (ERROR): Test failed. Test logging available at /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_65/test_framework.log
        2021-06-20T11:31:13.875000Z TestFramework (ERROR):
        2021-06-20T11:31:13.875000Z TestFramework (ERROR): Hint: Call /home/nourou/bitcoin/test/functional/combine_logs.py '/tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_65' to consolidate all logs
        2021-06-20T11:31:13.875000Z TestFramework (ERROR):
        2021-06-20T11:31:13.875000Z TestFramework (ERROR): If this failure happened unexpectedly or intermittently, please file a bug and provide a link or upload of the combined log.
        2021-06-20T11:31:13.876000Z TestFramework (ERROR): https://github.com/bitcoin/bitcoin/issues
        2021-06-20T11:31:13.876000Z TestFramework (ERROR):


        stderr:


        143/208 - rpc_bind.py --nonloopback failed, Duration: 6 s

        stdout:
        2021-06-20T11:31:12.412000Z TestFramework (INFO): Initializing test directory /tmp/test_runner_₿_🏃_20210620_131826/rpc_bind_64
        2021-06-20T11:31:12.413000Z TestFramework (INFO): Check for linux
        2021-06-20T11:31:12.414000Z TestFramework (INFO): Check for ipv6
        2021-06-20T11:31:12.414000Z TestFramework (INFO): Check for non-loopback interface
        2021-06-20T11:31:12.414000Z TestFramework (INFO): Using interface 169.254.53.173 for testing
        2021-06-20T11:31:12.499000Z TestFramework (INFO): Bind test for ['169.254.53.173']
        2021-06-20T11:31:13.701000Z TestFramework (ERROR): Unexpected exception caught during testing
        Traceback (most recent call last):
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 128, in main
            self.run_test()
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 91, in run_test
            self._run_nonloopback_tests()
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 123, in _run_nonloopback_tests
            [(self.non_loopback_ip, self.defaultport)])
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 41, in run_bind_test
            self.start_node(0, base_args + binds)
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 508, in start_node
            node.wait_for_rpc_connection()
        File "/home/nourou/bitcoin/test/functional/test_framework/test_node.py", line 225, in wait_for_rpc_connection
            'bitcoind exited with status {} during initialization'.format(self.process.returncode)))
        test_framework.test_node.FailedToStartError: [node 0] bitcoind exited with status 1 during initialization
        2021-06-20T11:31:13.816000Z TestFramework (INFO): Stopping nodes


        stderr:
        Traceback (most recent call last):
        File "/home/nourou/bitcoin/test/functional/rpc_bind.py", line 130, in <module>
            RPCBindTest().main()
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 151, in main
            exit_code = self.shutdown()
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 294, in shutdown
            self.stop_nodes()
        File "/home/nourou/bitcoin/test/functional/test_framework/test_framework.py", line 541, in stop_nodes
            node.stop_node(wait=wait, wait_until_stopped=False)
        File "/home/nourou/bitcoin/test/functional/test_framework/test_node.py", line 323, in stop_node
            self.stop(wait=wait)
        File "/home/nourou/bitcoin/test/functional/test_framework/test_node.py", line 183, in __getattr__
            assert self.rpc_connected and self.rpc is not None, self._node_msg("Error: no RPC connection")
        AssertionError: [node 0] Error: no RPC connection


        144/208 - feature_signet.py passed, Duration: 8 s
        145/208 - wallet_bumpfee.py --descriptors skipped
        146/208 - mining_basic.py passed, Duration: 11 s
        147/208 - rpc_named_arguments.py passed, Duration: 2 s
        148/208 - wallet_implicitsegwit.py --legacy-wallet passed, Duration: 14 s
        149/208 - wallet_listsinceblock.py --descriptors skipped
        150/208 - wallet_listdescriptors.py --descriptors skipped
        151/208 - wallet_listsinceblock.py --legacy-wallet passed, Duration: 13 s
        152/208 - p2p_leak.py passed, Duration: 7 s
        153/208 - wallet_encryption.py --descriptors skipped
        154/208 - wallet_encryption.py --legacy-wallet passed, Duration: 7 s
        155/208 - feature_cltv.py passed, Duration: 7 s
        156/208 - feature_dersig.py passed, Duration: 9 s
        157/208 - rpc_uptime.py passed, Duration: 2 s
        158/208 - wallet_resendwallettransactions.py --descriptors skipped
        159/208 - wallet_resendwallettransactions.py --legacy-wallet passed, Duration: 6 s
        160/208 - wallet_fallbackfee.py --descriptors skipped
        161/208 - wallet_fallbackfee.py --legacy-wallet passed, Duration: 5 s
        162/208 - rpc_dumptxoutset.py passed, Duration: 3 s
        163/208 - rpc_estimatefee.py passed, Duration: 2 s
        164/208 - feature_minchainwork.py passed, Duration: 8 s
        165/208 - rpc_getblockstats.py passed, Duration: 3 s
        166/208 - wallet_bumpfee.py --legacy-wallet passed, Duration: 94 s
        167/208 - wallet_send.py --descriptors skipped
        168/208 - wallet_create_tx.py --descriptors skipped
        169/208 - wallet_taproot.py skipped
        170/208 - p2p_fingerprint.py passed, Duration: 3 s
        171/208 - wallet_import_rescan.py --legacy-wallet passed, Duration: 124 s
        172/208 - feature_uacomment.py passed, Duration: 6 s
        173/208 - wallet_coinbase_category.py --descriptors skipped
        174/208 - wallet_coinbase_category.py --legacy-wallet passed, Duration: 3 s
        175/208 - wallet_send.py --legacy-wallet passed, Duration: 55 s
        176/208 - feature_filelock.py passed, Duration: 3 s
        177/208 - wallet_create_tx.py --legacy-wallet passed, Duration: 61 s
        178/208 - feature_loadblock.py passed, Duration: 7 s
        179/208 - p2p_dos_header_tree.py passed, Duration: 6 s
        180/208 - p2p_message_capture.py passed, Duration: 2 s
        181/208 - p2p_add_connections.py passed, Duration: 11 s
        182/208 - p2p_unrequested_blocks.py passed, Duration: 9 s
        183/208 - feature_includeconf.py passed, Duration: 6 s
        184/208 - mempool_compatibility.py skipped
        185/208 - rpc_deriveaddresses.py passed, Duration: 4 s
        186/208 - feature_asmap.py passed, Duration: 11 s
        187/208 - rpc_deriveaddresses.py --usecli passed, Duration: 4 s
        188/208 - p2p_blockfilters.py passed, Duration: 18 s
        189/208 - p2p_ping.py passed, Duration: 6 s
        190/208 - mempool_unbroadcast.py passed, Duration: 17 s
        191/208 - feature_anchors.py passed, Duration: 5 s
        192/208 - feature_logging.py passed, Duration: 11 s
        193/208 - rpc_scantxoutset.py passed, Duration: 17 s
        194/208 - wallet_orphanedreward.py passed, Duration: 8 s
        195/208 - feature_blocksdir.py passed, Duration: 3 s
        196/208 - p2p_node_network_limited.py passed, Duration: 11 s
        197/208 - feature_coinstatsindex.py passed, Duration: 18 s
        198/208 - feature_settings.py passed, Duration: 9 s
        199/208 - wallet_startup.py passed, Duration: 14 s
        200/208 - rpc_getdescriptorinfo.py passed, Duration: 3 s
        201/208 - rpc_addresses_deprecation.py passed, Duration: 6 s
        202/208 - feature_help.py passed, Duration: 1 s
        203/208 - rpc_help.py passed, Duration: 7 s
        204/208 - feature_shutdown.py passed, Duration: 4 s
        Remaining jobs: [p2p_permissions.py, feature_config_args.py, p2p_ibd_txrelay.py, feature_blockfilterindex_prune.py]
        205/208 - p2p_ibd_txrelay.py passed, Duration: 4 s
        Remaining jobs: [p2p_permissions.py, feature_config_args.py, feature_blockfilterindex_prune.py]
        206/208 - p2p_permissions.py passed, Duration: 33 s
        Remaining jobs: [feature_config_args.py, feature_blockfilterindex_prune.py]
        207/208 - feature_config_args.py passed, Duration: 35 s
        Remaining jobs: [feature_blockfilterindex_prune.py]
        208/208 - feature_blockfilterindex_prune.py passed, Duration: 12 s

        TEST                                               | STATUS    | DURATION

        example_test.py                                    | ✓ Passed  | 6 s
        feature_abortnode.py                               | ✓ Passed  | 35 s
        feature_anchors.py                                 | ✓ Passed  | 5 s
        feature_asmap.py                                   | ✓ Passed  | 11 s
        feature_assumevalid.py                             | ✓ Passed  | 14 s
        feature_bip68_sequence.py                          | ✓ Passed  | 69 s
        feature_block.py                                   | ✓ Passed  | 154 s
        feature_blockfilterindex_prune.py                  | ✓ Passed  | 12 s
        feature_blocksdir.py                               | ✓ Passed  | 3 s
        feature_cltv.py                                    | ✓ Passed  | 7 s
        feature_coinstatsindex.py                          | ✓ Passed  | 18 s
        feature_config_args.py                             | ✓ Passed  | 35 s
        feature_csv_activation.py                          | ✓ Passed  | 20 s
        feature_dersig.py                                  | ✓ Passed  | 9 s
        feature_fee_estimation.py                          | ✓ Passed  | 103 s
        feature_filelock.py                                | ✓ Passed  | 3 s
        feature_help.py                                    | ✓ Passed  | 1 s
        feature_includeconf.py                             | ✓ Passed  | 6 s
        feature_loadblock.py                               | ✓ Passed  | 7 s
        feature_logging.py                                 | ✓ Passed  | 11 s
        feature_maxuploadtarget.py                         | ✓ Passed  | 74 s
        feature_minchainwork.py                            | ✓ Passed  | 8 s
        feature_notifications.py                           | ✓ Passed  | 40 s
        feature_nulldummy.py --legacy-wallet               | ✓ Passed  | 3 s
        feature_proxy.py                                   | ✓ Passed  | 3 s
        feature_rbf.py                                     | ✓ Passed  | 23 s
        feature_reindex.py                                 | ✓ Passed  | 12 s
        feature_segwit.py --legacy-wallet                  | ✓ Passed  | 32 s
        feature_settings.py                                | ✓ Passed  | 9 s
        feature_shutdown.py                                | ✓ Passed  | 4 s
        feature_signet.py                                  | ✓ Passed  | 8 s
        feature_taproot.py                                 | ✓ Passed  | 104 s
        feature_uacomment.py                               | ✓ Passed  | 6 s
        feature_utxo_set_hash.py                           | ✓ Passed  | 4 s
        feature_versionbits_warning.py                     | ✓ Passed  | 6 s
        interface_bitcoin_cli.py                           | ✓ Passed  | 19 s
        interface_http.py                                  | ✓ Passed  | 6 s
        interface_rest.py                                  | ✓ Passed  | 12 s
        interface_rpc.py                                   | ✓ Passed  | 6 s
        mempool_accept.py                                  | ✓ Passed  | 12 s
        mempool_expiry.py                                  | ✓ Passed  | 5 s
        mempool_limit.py                                   | ✓ Passed  | 6 s
        mempool_package_onemore.py                         | ✓ Passed  | 59 s
        mempool_packages.py                                | ✓ Passed  | 61 s
        mempool_persist.py                                 | ✓ Passed  | 30 s
        mempool_reorg.py                                   | ✓ Passed  | 5 s
        mempool_resurrect.py                               | ✓ Passed  | 3 s
        mempool_spend_coinbase.py                          | ✓ Passed  | 2 s
        mempool_unbroadcast.py                             | ✓ Passed  | 17 s
        mempool_updatefromblock.py                         | ✓ Passed  | 376 s
        mining_basic.py                                    | ✓ Passed  | 11 s
        mining_getblocktemplate_longpoll.py                | ✓ Passed  | 69 s
        mining_prioritisetransaction.py                    | ✓ Passed  | 7 s
        p2p_add_connections.py                             | ✓ Passed  | 11 s
        p2p_addr_relay.py                                  | ✓ Passed  | 16 s
        p2p_addrv2_relay.py                                | ✓ Passed  | 18 s
        p2p_blockfilters.py                                | ✓ Passed  | 18 s
        p2p_blocksonly.py                                  | ✓ Passed  | 38 s
        p2p_compactblocks.py                               | ✓ Passed  | 28 s
        p2p_disconnect_ban.py                              | ✓ Passed  | 6 s
        p2p_dos_header_tree.py                             | ✓ Passed  | 6 s
        p2p_eviction.py                                    | ✓ Passed  | 8 s
        p2p_feefilter.py                                   | ✓ Passed  | 16 s
        p2p_filter.py                                      | ✓ Passed  | 9 s
        p2p_fingerprint.py                                 | ✓ Passed  | 3 s
        p2p_getaddr_caching.py                             | ✓ Passed  | 17 s
        p2p_getdata.py                                     | ✓ Passed  | 2 s
        p2p_ibd_txrelay.py                                 | ✓ Passed  | 4 s
        p2p_invalid_block.py                               | ✓ Passed  | 3 s
        p2p_invalid_locator.py                             | ✓ Passed  | 3 s
        p2p_invalid_messages.py                            | ✓ Passed  | 13 s
        p2p_invalid_tx.py                                  | ✓ Passed  | 8 s
        p2p_leak.py                                        | ✓ Passed  | 7 s
        p2p_leak_tx.py                                     | ✓ Passed  | 3 s
        p2p_message_capture.py                             | ✓ Passed  | 2 s
        p2p_nobloomfilter_messages.py                      | ✓ Passed  | 2 s
        p2p_node_network_limited.py                        | ✓ Passed  | 11 s
        p2p_permissions.py                                 | ✓ Passed  | 33 s
        p2p_ping.py                                        | ✓ Passed  | 6 s
        p2p_segwit.py                                      | ✓ Passed  | 95 s
        p2p_sendheaders.py                                 | ✓ Passed  | 16 s
        p2p_timeouts.py                                    | ✓ Passed  | 9 s
        p2p_tx_download.py                                 | ✓ Passed  | 52 s
        p2p_unrequested_blocks.py                          | ✓ Passed  | 9 s
        rpc_addresses_deprecation.py                       | ✓ Passed  | 6 s
        rpc_blockchain.py                                  | ✓ Passed  | 16 s
        rpc_createmultisig.py --legacy-wallet              | ✓ Passed  | 24 s
        rpc_decodescript.py                                | ✓ Passed  | 2 s
        rpc_deprecated.py                                  | ✓ Passed  | 3 s
        rpc_deriveaddresses.py                             | ✓ Passed  | 4 s
        rpc_deriveaddresses.py --usecli                    | ✓ Passed  | 4 s
        rpc_dumptxoutset.py                                | ✓ Passed  | 3 s
        rpc_estimatefee.py                                 | ✓ Passed  | 2 s
        rpc_fundrawtransaction.py --legacy-wallet          | ✓ Passed  | 100 s
        rpc_generate.py                                    | ✓ Passed  | 2 s
        rpc_generateblock.py                               | ✓ Passed  | 6 s
        rpc_getblockfilter.py                              | ✓ Passed  | 8 s
        rpc_getblockstats.py                               | ✓ Passed  | 3 s
        rpc_getchaintips.py                                | ✓ Passed  | 6 s
        rpc_getdescriptorinfo.py                           | ✓ Passed  | 3 s
        rpc_help.py                                        | ✓ Passed  | 7 s
        rpc_invalid_address_message.py                     | ✓ Passed  | 3 s
        rpc_invalidateblock.py                             | ✓ Passed  | 5 s
        rpc_misc.py                                        | ✓ Passed  | 8 s
        rpc_named_arguments.py                             | ✓ Passed  | 2 s
        rpc_net.py                                         | ✓ Passed  | 14 s
        rpc_packages.py                                    | ✓ Passed  | 4 s
        rpc_preciousblock.py                               | ✓ Passed  | 7 s
        rpc_psbt.py --legacy-wallet                        | ✓ Passed  | 43 s
        rpc_rawtransaction.py --legacy-wallet              | ✓ Passed  | 65 s
        rpc_scantxoutset.py                                | ✓ Passed  | 17 s
        rpc_setban.py                                      | ✓ Passed  | 6 s
        rpc_signer.py                                      | ✓ Passed  | 7 s
        rpc_signmessage.py                                 | ✓ Passed  | 3 s
        rpc_signrawtransaction.py --legacy-wallet          | ✓ Passed  | 18 s
        rpc_txoutproof.py                                  | ✓ Passed  | 4 s
        rpc_uptime.py                                      | ✓ Passed  | 2 s
        rpc_users.py                                       | ✓ Passed  | 11 s
        rpc_whitelist.py                                   | ✓ Passed  | 3 s
        tool_wallet.py --legacy-wallet                     | ✓ Passed  | 31 s
        wallet_abandonconflict.py --legacy-wallet          | ✓ Passed  | 20 s
        wallet_address_types.py --legacy-wallet            | ✓ Passed  | 48 s
        wallet_avoidreuse.py --legacy-wallet               | ✓ Passed  | 69 s
        wallet_backup.py --legacy-wallet                   | ✓ Passed  | 62 s
        wallet_balance.py --legacy-wallet                  | ✓ Passed  | 19 s
        wallet_basic.py --legacy-wallet                    | ✓ Passed  | 72 s
        wallet_bumpfee.py --legacy-wallet                  | ✓ Passed  | 94 s
        wallet_coinbase_category.py --legacy-wallet        | ✓ Passed  | 3 s
        wallet_create_tx.py --legacy-wallet                | ✓ Passed  | 61 s
        wallet_createwallet.py --legacy-wallet             | ✓ Passed  | 5 s
        wallet_createwallet.py --usecli                    | ✓ Passed  | 10 s
        wallet_disable.py --descriptors                    | ✓ Passed  | 1 s
        wallet_disable.py --legacy-wallet                  | ✓ Passed  | 3 s
        wallet_dump.py --legacy-wallet                     | ✓ Passed  | 39 s
        wallet_encryption.py --legacy-wallet               | ✓ Passed  | 7 s
        wallet_fallbackfee.py --legacy-wallet              | ✓ Passed  | 5 s
        wallet_groups.py --legacy-wallet                   | ✓ Passed  | 91 s
        wallet_hd.py --legacy-wallet                       | ✓ Passed  | 12 s
        wallet_implicitsegwit.py --legacy-wallet           | ✓ Passed  | 14 s
        wallet_import_rescan.py --legacy-wallet            | ✓ Passed  | 124 s
        wallet_import_with_label.py --legacy-wallet        | ✓ Passed  | 7 s
        wallet_importmulti.py --legacy-wallet              | ✓ Passed  | 18 s
        wallet_importprunedfunds.py --legacy-wallet        | ✓ Passed  | 9 s
        wallet_keypool.py --legacy-wallet                  | ✓ Passed  | 4 s
        wallet_keypool_topup.py --legacy-wallet            | ✓ Passed  | 80 s
        wallet_labels.py --legacy-wallet                   | ✓ Passed  | 13 s
        wallet_listreceivedby.py --legacy-wallet           | ✓ Passed  | 23 s
        wallet_listsinceblock.py --legacy-wallet           | ✓ Passed  | 13 s
        wallet_listtransactions.py --legacy-wallet         | ✓ Passed  | 65 s
        wallet_multiwallet.py --legacy-wallet              | ✓ Passed  | 63 s
        wallet_multiwallet.py --usecli                     | ✓ Passed  | 45 s
        wallet_orphanedreward.py                           | ✓ Passed  | 8 s
        wallet_reorgsrestore.py                            | ✓ Passed  | 15 s
        wallet_resendwallettransactions.py --legacy-wallet | ✓ Passed  | 6 s
        wallet_send.py --legacy-wallet                     | ✓ Passed  | 55 s
        wallet_startup.py                                  | ✓ Passed  | 14 s
        wallet_txn_clone.py                                | ✓ Passed  | 6 s
        wallet_txn_clone.py --mineblock                    | ✓ Passed  | 11 s
        wallet_txn_clone.py --segwit                       | ✓ Passed  | 6 s
        wallet_txn_doublespend.py --legacy-wallet          | ✓ Passed  | 5 s
        wallet_txn_doublespend.py --mineblock              | ✓ Passed  | 8 s
        wallet_watchonly.py --legacy-wallet                | ✓ Passed  | 4 s
        wallet_watchonly.py --usecli --legacy-wallet       | ✓ Passed  | 7 s
        feature_backwards_compatibility.py --descriptors   | ○ Skipped | 2 s
        feature_backwards_compatibility.py --legacy-wallet | ○ Skipped | 1 s
        feature_nulldummy.py --descriptors                 | ○ Skipped | 0 s
        interface_zmq.py                                   | ○ Skipped | 1 s
        mempool_compatibility.py                           | ○ Skipped | 0 s
        rpc_createmultisig.py --descriptors                | ○ Skipped | 0 s
        rpc_fundrawtransaction.py --descriptors            | ○ Skipped | 1 s
        rpc_psbt.py --descriptors                          | ○ Skipped | 0 s
        rpc_rawtransaction.py --descriptors                | ○ Skipped | 0 s
        rpc_signrawtransaction.py --descriptors            | ○ Skipped | 0 s
        tool_wallet.py --descriptors                       | ○ Skipped | 0 s
        wallet_abandonconflict.py --descriptors            | ○ Skipped | 0 s
        wallet_address_types.py --descriptors              | ○ Skipped | 0 s
        wallet_avoidreuse.py --descriptors                 | ○ Skipped | 0 s
        wallet_backup.py --descriptors                     | ○ Skipped | 1 s
        wallet_balance.py --descriptors                    | ○ Skipped | 0 s
        wallet_basic.py --descriptors                      | ○ Skipped | 0 s
        wallet_bumpfee.py --descriptors                    | ○ Skipped | 0 s
        wallet_coinbase_category.py --descriptors          | ○ Skipped | 0 s
        wallet_create_tx.py --descriptors                  | ○ Skipped | 0 s
        wallet_createwallet.py --descriptors               | ○ Skipped | 0 s
        wallet_descriptor.py --descriptors                 | ○ Skipped | 0 s
        wallet_encryption.py --descriptors                 | ○ Skipped | 0 s
        wallet_fallbackfee.py --descriptors                | ○ Skipped | 0 s
        wallet_groups.py --descriptors                     | ○ Skipped | 0 s
        wallet_hd.py --descriptors                         | ○ Skipped | 0 s
        wallet_importdescriptors.py --descriptors          | ○ Skipped | 1 s
        wallet_importprunedfunds.py --descriptors          | ○ Skipped | 0 s
        wallet_keypool.py --descriptors                    | ○ Skipped | 0 s
        wallet_keypool_topup.py --descriptors              | ○ Skipped | 0 s
        wallet_labels.py --descriptors                     | ○ Skipped | 0 s
        wallet_listdescriptors.py --descriptors            | ○ Skipped | 0 s
        wallet_listreceivedby.py --descriptors             | ○ Skipped | 0 s
        wallet_listsinceblock.py --descriptors             | ○ Skipped | 0 s
        wallet_listtransactions.py --descriptors           | ○ Skipped | 0 s
        wallet_multiwallet.py --descriptors                | ○ Skipped | 0 s
        wallet_resendwallettransactions.py --descriptors   | ○ Skipped | 0 s
        wallet_send.py --descriptors                       | ○ Skipped | 0 s
        wallet_signer.py --descriptors                     | ○ Skipped | 0 s
        wallet_taproot.py                                  | ○ Skipped | 0 s
        wallet_txn_doublespend.py --descriptors            | ○ Skipped | 1 s
        wallet_upgradewallet.py --legacy-wallet            | ○ Skipped | 1 s
        rpc_bind.py --ipv4                                 | ✖ Failed  | 3 s
        rpc_bind.py --ipv6                                 | ✖ Failed  | 4 s
        rpc_bind.py --nonloopback                          | ✖ Failed  | 6 s

        ALL                                                | ✖ Failed  | 3761 s (accumulated)
        Runtime: 963 s