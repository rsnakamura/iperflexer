
#python standard library
import os

#this package
from iperfparser import IperfParser 
from iperfexpressions import HumanExpression, ParserKeys, CsvExpression
import oatbran as bran
from coroutine import coroutine


class HumanExpressionSum(HumanExpression):
    """
    Changes the thread-column regular expression to match SUMS if needed
    """
    def __init__(self, threads=4):
        """
        :param:

         - `threads`: number of parallel threads
        """
        super(HumanExpressionSum, self).__init__()
        self.threads = threads
        return

    @property
    def thread_column(self):
        """
        :return: expression to match the thread (sum) column
        """
        if self._thread_column is None:
            if self.threads > 1:
                thread = "SUM"
            else:
                thread = bran.OPTIONAL_SPACES + bran.INTEGER
            self._thread_column = bran.L_BRACKET + thread + bran.R_BRACKET
        return self._thread_column
# end class HumanExpressionSum


class CsvExpressionSum(CsvExpression):
    """
    Changes the thread column to look for -1 if needed
    """
    def __init__(self, threads=4):
        """
        :param:

         - `threads`: the number of parallel threads
        """
        super(CsvExpressionSum, self).__init__()
        self.threads = threads
        return

    @property
    def thread_column(self):
        """
        :return: the expression to match the thread (sum) column
        """
        if self._thread_column is None:
            if self.threads > 1:
                thread = "-1"
            else:
                thread = bran.INTEGER
            self._thread_column = bran.NAMED(ParserKeys.thread, thread)
        return self._thread_column
# end class CsvExpressionSum    


class SumParser(IperfParser):
    """
    The SumParser emits bandwidth sum lines
    """
    def __init__(self, *args, **kwargs):
        super(SumParser, self).__init__(*args, **kwargs)
        self.log_format = "({0}) {1} {2}/sec"
        self.last_line_bandwidth = None
        return

    @property
    def regex(self):
        """
        :return: a dictionary of compiled regular expressions
        """
        if self._regex is None:
            self._regex = {ParserKeys.human:HumanExpressionSum(threads=self.threads).regex,
                           ParserKeys.csv:CsvExpressionSum(threads=self.threads).regex}
        return self._regex

    def __call__(self, line):
        """
        The Main interface to add raw iperf lines to the parser
        
        :param:

         - `line`: a line of iperf output

        :return: bandwidth or None
        """
        match = self.search(line)
        assert type(match) == dict or match is None, "match: {0}".format(type(match)) 
        bandwidth = None
        if match is not None:
            bandwidth = self.bandwidth(match)
            if self.valid(match):                        
                self.intervals[float(match[ParserKeys.start])] = bandwidth
                self.logger.info(self.log_format.format(match[ParserKeys.start],
                                                        bandwidth,
                                                        self.units))
            else:
                # Assume it's the last line summary
                self.last_line_bandwidth = bandwidth
                return
        return bandwidth

    @coroutine
    def pipe(self, target):
        """
        A coroutine pipeline segment
                
        :warnings:

         - For bad connections with threads this might break (as the threads die)
         - Use for good connections or live data only (use `bandwidths` and completed data for greater fidelity)
         
        :parameters:

         - `target`: a target to send matched output to

        :send:

         - bandwidth converted to self.units as a float
        """
        while True:
            line = (yield)
            match = self.search(line)
            if match is not None and self.valid(match):
                # threads is a dict of interval:(thread_count, bandwidths)
                target.send(self.bandwidth(match))
        return
# end class SumParser


in_documentation = __name__ == '__builtin__'


if in_documentation:
    data_folder = 'features/steps/samples/'
    data_path = os.path.join(data_folder, 'client_data.iperf')
    parser = SumParser()
    for line in open(data_path):
        bandwidth = parser(line)
        if bandwidth is not None:
            print(bandwidth)


if in_documentation:
    parser.reset()

    for line in open(data_path):
        parser(line)
    
    for bandwidth in parser.bandwidths:
        print(bandwidth)



if in_documentation:
    parser.reset()

    for line in open(data_path):
        parser(line)
    
    calculated_average = sum(parser.bandwidths)/len(parser.intervals)


if in_documentation:
    print('   Sum Lines, {0}'.format(calculated_average))
    print("   Iperf, {0}".format(parser.last_line_bandwidth))


if in_documentation:
    #set up the unitconverter
    from unitconverter import UnitConverter
    converter = UnitConverter()
    data_path = os.path.join(data_folder, 'client_p4_bits.iperf')

    # rename the sum-parser used earlier to make it clearer
    sum_parser = parser
    
    #setup the parsers to use bits
    voodoo = IperfParser(units='bits')
    sum_parser.reset()
    sum_parser.units = 'bits'

    # load them up with the raw lines
    for line in open(data_path):
        sum_parser(line)
        voodoo(line)


if in_documentation:
    # convert the sums to Mbits and take the average
    total_bandwidth = sum(sum_parser.bandwidths) * converter['bits']['Mbits']
    calculated_average = total_bandwidth/len(sum_parser.intervals)

    # same for the re-added threads
    v_total = sum(voodoo.bandwidths) * converter['bits']['Mbits']
    v_average = v_total/len(voodoo.intervals)

    # now iperf's
    iperf_mean = sum_parser.last_line_bandwidth * converter['bits']['Mbits']


if in_documentation:
    print("   Iperf, {0}".format(iperf_mean))    
    print('   Sum-Lines, {0}'.format(calculated_average))
    print("   Threads, {0}".format(v_average))          
