# Regression tests - Logs

Regression tests have been run by directly call test script : 

        test/functional/test_runner.py    

Here are the testing results :  

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