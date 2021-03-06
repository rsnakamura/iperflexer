from unittest import TestCase

from mock import MagicMock, patch 

import iperflexer

PUDB = MagicMock()

SAMPLE = """
------------------------------------------------------------
Client connecting to 192.168.20.50, TCP port 5001
TCP window size: 16.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.20.62 port 33593 connected with 192.168.20.50 port 5001
[  4] local 192.168.20.62 port 33594 connected with 192.168.20.50 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0- 1.0 sec  1.00 MBytes  8.39 Mbits/sec
[  4]  0.0- 1.0 sec   896 KBytes  7.34 Mbits/sec
[SUM]  0.0- 1.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  1.0- 2.0 sec   640 KBytes  5.24 Mbits/sec
[  4]  1.0- 2.0 sec   512 KBytes  4.19 Mbits/sec
[SUM]  1.0- 2.0 sec  1.12 MBytes  9.44 Mbits/sec
[  3]  2.0- 3.0 sec   512 KBytes  4.19 Mbits/sec
[  4]  2.0- 3.0 sec   512 KBytes  4.19 Mbits/sec
[SUM]  2.0- 3.0 sec  1.00 MBytes  8.39 Mbits/sec
[  4]  3.0- 4.0 sec   384 KBytes  3.15 Mbits/sec
[  3]  3.0- 4.0 sec   384 KBytes  3.15 Mbits/sec
[SUM]  3.0- 4.0 sec   768 KBytes  6.29 Mbits/sec
[  3]  4.0- 5.0 sec   512 KBytes  4.19 Mbits/sec
[  4]  4.0- 5.0 sec   768 KBytes  6.29 Mbits/sec
[SUM]  4.0- 5.0 sec  1.25 MBytes  10.5 Mbits/sec
[  4]  5.0- 6.0 sec   384 KBytes  3.15 Mbits/sec
[  3]  5.0- 6.0 sec   384 KBytes  3.15 Mbits/sec
[SUM]  5.0- 6.0 sec   768 KBytes  6.29 Mbits/sec
[  3]  6.0- 7.0 sec  0.00 Bytes  0.00 bits/sec
[  3]  7.0- 8.0 sec  0.00 Bytes  0.00 bits/sec
[  3]  8.0- 9.0 sec  0.00 Bytes  0.00 bits/sec
[  3]  9.0-10.0 sec  0.00 Bytes  0.00 bits/sec
[  3]  0.0-10.7 sec  3.50 MBytes  2.73 Mbits/sec
[  4]  6.0- 7.0 sec   256 KBytes  2.10 Mbits/sec
[SUM]  6.0- 7.0 sec   256 KBytes  2.10 Mbits/sec
[  4]  7.0- 8.0 sec  0.00 Bytes  0.00 bits/sec
[SUM]  7.0- 8.0 sec  0.00 Bytes  0.00 bits/sec
[  4]  8.0- 9.0 sec  0.00 Bytes  0.00 bits/sec
[SUM]  8.0- 9.0 sec  0.00 Bytes  0.00 bits/sec
[  4]  9.0-10.0 sec  0.00 Bytes  0.00 bits/sec
[SUM]  9.0-10.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 10.0-11.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 11.0-12.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 12.0-13.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 13.0-14.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 14.0-15.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 15.0-16.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 16.0-17.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 17.0-18.0 sec  0.00 Bytes  0.00 bits/sec
[  4] 18.0-19.0 sec  0.00 Bytes  0.00 bits/sec
[  4]  0.0-19.3 sec  3.75 MBytes  1.63 Mbits/sec
""".split()


STDOUT = MagicMock()


class TestMain(TestCase):
    def create_patch(self, name):
        patcher = patch(name)
        thing = patcher.start()
        self.addCleanup(patcher.stop)
        return thing

    @patch("sys.argv", ['takataka'])
    @patch('sys.stdin', SAMPLE)
    @patch('sys.stdout.write', STDOUT)
    def test_pipe(self):
        iperflexer.main.main()
        #STDOUT.assert_called_with('0.0')
        
    @patch("sys.argv", ['takataka', '-g', '*perf'])
    @patch('sys.stdout.write', STDOUT)
    def test_analyze(self):
        from iperflexer import main
        finder = MagicMock()
        finder.return_value= ["i.perf"]
        main.find = finder
        opener = MagicMock()
        opener.return_value = SAMPLE
        with patch('__builtin__.open', opener):
            main.main()
        finder.assert_called_with('*perf')
        return
# end class TestMain
