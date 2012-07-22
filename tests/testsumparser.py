from unittest import TestCase

from mock import MagicMock

from iperflexer.iperfexpressions import ParserKeys
from iperflexer import sumparser

HUMAN = "[SUM]  0.0- 1.0 sec   114 MBytes   957 Mbits/sec"
CSV = "20120720091543,192.168.20.62,0,192.168.20.50,5001,-1,0.0-1.0,786432,6291456"

class TestSumParser(TestCase):
    def setUp(self):
        self.parser = sumparser.SumParser()
        return

    def test_bandwidth(self):
        return

    def test_human_regex(self):
        self.assertRegexpMatches(HUMAN, self.parser.regex[ParserKeys.human].pattern)
        return

    def test_csv_regex(self):
        self.assertRegexpMatches(CSV, self.parser.regex[ParserKeys.csv].pattern)
        return

    def test_add(self):
        logger = MagicMock()

        parser = sumparser.SumParser()
        parser._logger = logger
        parser.add(HUMAN)
        logger.info.assert_called_with(parser.log_format.format(0.0, 957.0, "Mbits"))
        self.parser.reset()
        parser.add(CSV)
        logger.info.assert_called_with(parser.log_format.format(0.0, 6.291456, "Mbits"))
        return
        
