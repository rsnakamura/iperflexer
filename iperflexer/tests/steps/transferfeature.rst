Transfer Feature
================

.. literalinclude:: ../features/transfer.feature
   :language: gherkin

::

    data = """
    ------------------------------------------------------------
    Client connecting to tartarus, TCP port 5001
    TCP window size: 87040 Byte (default)
    ------------------------------------------------------------
    [  4] local 192.168.1.2 port 36821 connected with 192.168.1.3 port 5001
    [  3] local 192.168.1.2 port 36820 connected with 192.168.1.3 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  4]  0.0- 1.0 sec  6291456 Bytes  50331648 bits/sec
    [  3]  0.0- 1.0 sec  6291456 Bytes  50331648 bits/sec
    [SUM]  0.0- 1.0 sec  12582912 Bytes  100663296 bits/sec
    [  4]  1.0- 2.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  1.0- 2.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  1.0- 2.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  2.0- 3.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  2.0- 3.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  2.0- 3.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  3.0- 4.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  3.0- 4.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  3.0- 4.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  4.0- 5.0 sec  6291456 Bytes  50331648 bits/sec
    [  3]  4.0- 5.0 sec  6291456 Bytes  50331648 bits/sec
    [SUM]  4.0- 5.0 sec  12582912 Bytes  100663296 bits/sec
    [  4]  5.0- 6.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  5.0- 6.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  5.0- 6.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  6.0- 7.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  6.0- 7.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  6.0- 7.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  7.0- 8.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  7.0- 8.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  7.0- 8.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  8.0- 9.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  8.0- 9.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  8.0- 9.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  9.0-10.0 sec  6291456 Bytes  50331648 bits/sec
    [  4]  0.0-10.2 sec  59768832 Bytes  47007639 bits/sec
    [  3]  9.0-10.0 sec  6291456 Bytes  50331648 bits/sec
    [SUM]  9.0-10.0 sec  12582912 Bytes  100663296 bits/sec
    [  3]  0.0-10.2 sec  59768832 Bytes  47028560 bits/sec
    [SUM]  0.0-10.2 sec  119537664 Bytes  94015278 bits/sec
    """.splitlines()
    
    transfers = """12582912 
    11534336 
    11534336 
    11534336 
    12582912 
    11534336 
    11534336 
    11534336 
    11534336 
    12582912 
    """.splitlines()
    


Scenario: The IperfParser is generates transfers
------------------------------------------------

::

    @given("an IperfParser with all data loaded and set to bits")
    def bits_parser(context):
        context.parser = IperfParser(units='bits')
        for line in data:
            context.parser(line)
        return
    

::

    @when("the transfers are traversed")
    def traverse_transfers(context):
        context.expected = [int(value) for value in transfers]
        context.actual = [transfer for transfer in context.parser.transfers]
        return
    

::

    @then("the values from the data column have the sums")
    def assert_values(context):
        assert_that(context.expected,
                    contains(*context.actual))
        return
    



Example: missing sums
---------------------

::

    missing_sums = """
    ------------------------------------------------------------
    Client connecting to tartarus, TCP port 5001
    TCP window size: 87040 Byte (default)
    ------------------------------------------------------------
    [  4] local 192.168.1.2 port 36821 connected with 192.168.1.3 port 5001
    [  3] local 192.168.1.2 port 36820 connected with 192.168.1.3 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  4]  0.0- 1.0 sec  6291456 Bytes  50331648 bits/sec
    [  3]  0.0- 1.0 sec  6291456 Bytes  50331648 bits/sec
    [SUM]  0.0- 1.0 sec  12582912 Bytes  100663296 bits/sec
    [  4]  1.0- 2.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  1.0- 2.0 sec  5767168 Bytes  46137344 bits/sec
    [  4]  2.0- 3.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  2.0- 3.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  2.0- 3.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  3.0- 4.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  3.0- 4.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  3.0- 4.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  4.0- 5.0 sec  6291456 Bytes  50331648 bits/sec
    [  3]  4.0- 5.0 sec  6291456 Bytes  50331648 bits/sec
    [SUM]  4.0- 5.0 sec  12582912 Bytes  100663296 bits/sec
    [  4]  5.0- 6.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  5.0- 6.0 sec  5767168 Bytes  46137344 bits/sec
    [  4]  6.0- 7.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  6.0- 7.0 sec  5767168 Bytes  46137344 bits/sec
    [  4]  7.0- 8.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  7.0- 8.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  7.0- 8.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  8.0- 9.0 sec  5767168 Bytes  46137344 bits/sec
    [  3]  8.0- 9.0 sec  5767168 Bytes  46137344 bits/sec
    [SUM]  8.0- 9.0 sec  11534336 Bytes  92274688 bits/sec
    [  4]  9.0-10.0 sec  6291456 Bytes  50331648 bits/sec
    [  4]  0.0-10.2 sec  59768832 Bytes  47007639 bits/sec
    [  3]  9.0-10.0 sec  6291456 Bytes  50331648 bits/sec
    [SUM]  9.0-10.0 sec  12582912 Bytes  100663296 bits/sec
    [  3]  0.0-10.2 sec  59768832 Bytes  47028560 bits/sec
    [SUM]  0.0-10.2 sec  119537664 Bytes  94015278 bits/sec
    """.splitlines()
    
    missing_data = """12582912
    11534336 
    11534336 
    12582912 
    11534336 
    11534336 
    12582912 
    """.splitlines()
    

::

    @given("an IperfParser with missing data loaded and set to bits")
    def bits_parser(context):
        context.parser = IperfParser(units='bits')
        for line in missing_sums:
            context.parser(line)
        return
    




Example SumParser with all sums
-------------------------------

::

    @given("an SumParser with all data loaded and set to bits")
    def bits_parser(context):
        context.parser = SumParser(units='bits', threads=2)
        for line in data:
            context.parser(line)
        return
    




Example SumParser with missing sums
-----------------------------------

::

    @given("an SumParser with missing data loaded and set to bits")
    def bits_parser(context):
        context.parser = SumParser(units='bits', threads=2)
        for line in missing_sums:
            context.parser(line)
        return
    

::

    @then("the values from the data column have the fewer points")
    def assert_values(context):
        expected = [int(line) for line in missing_data]
        assert_that(expected,
                    contains(*context.actual))
        return
    



Scenario: Last Transfer
-----------------------

::

    @given("a SumParser loaded with data that has a last line")
    def load_sumparser(context):
        context.parser = SumParser(units='bits', threads=2)
        for line in missing_sums:
            context.parser(line)
        return
    

::

    @then("the transfer from the last line is saved as last_line_transfer")
    def last_line_transfer(context):
        expected = 119537664
        actual = context.parser.last_line_transfer
        assert_that(expected,
                    is_(equal_to(actual)))
        return
    

