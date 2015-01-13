from unittest import TestCase

from mock import MagicMock

from iperflexer.iperfexpressions import ParserKeys
from iperflexer import sumparser

HUMAN = "[SUM]  0.0- 1.0 sec   114 MBytes   957 Mbits/sec"
CSV = "20120720091543,192.168.20.62,0,192.168.20.50,5001,-1,0.0-1.0,786432,6291456"
CSV_SINGLE = "20121012155511,192.168.10.63,3453,192.168.10.50,5001,3,8.0-9.0,116801536,934412288"

HUMAN_OVERFLOW = "[SUM]  0.0- 1.0 sec   114 MBytes   12356432685 Mbits/sec"
CSV_SINGLE_OVERFLOW = "20120720091543,192.168.20.62,0,192.168.20.50,5001,-1,8.0-9.0,786432,147573952589676281856"

class TestSumParser(TestCase):
    def setUp(self):
        self.parser = sumparser.SumParser(maximum=1000, threads=4)
        return

    def test_bandwidth(self):
        return

    def test_human_regex(self):
        self.assertRegexpMatches(HUMAN, self.parser.regex[ParserKeys.human].pattern)
        return

    def test_csv_regex(self):
        self.assertRegexpMatches(CSV, self.parser.regex[ParserKeys.csv].pattern)
        return


    
if __name__ == "__main__":
    import pudb
    pudb.set_trace()
    parser = sumparser.SumParser(threads=1)
    parser(CSV_SINGLE)
