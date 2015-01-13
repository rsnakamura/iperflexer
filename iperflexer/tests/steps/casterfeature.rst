Casters
=======

This is an attempt to fix the casting of the extracted values from strings to ints or floats. While the easiest thing to do would be to cast everything to a float I decided that it seemed like a bad idea to force values that are ints to be floats. Then I found out that when Iperf in-fills 0's for missing intervals it sets them to 0.0, even if they are reporting bits and bytes, so the behavior has to handle this (python will raise an error if you try to cast something with a decimal point to an integer).

.. '

.. literalinclude:: ../features/caster.feature
   :language: gherkin

Scenario: The IperfParser is passed a line with an integer bandwidth
--------------------------------------------------------------------

::

    @given("an IperfParser set to bits and a thread of 1")
    def iperf_parser_bits(context):
        context.converter = UnitConverter()
        context.b_converter = BinaryUnitconverter()
        context.parser = IperfParser(units='bits')
        context.human_expression = HumanExpression()
        return
    

::

    @when("the IperfParser is called with a line with integer bandwidth")
    def integer_bandwidth(context):
        line = "[  3]  0.0- 1.0 sec  3014656 Bytes  24117248 bits/sec"
        match = context.human_expression.regex.search(line).groupdict()
        context.actual = context.parser.bandwidth(match)
        context.expected = 24117248
        return
    

::

    @then("the returned bandwidth is of type integer")
    def assert_integer(context):
        assert_that(context.actual,
                    is_(equal_to(context.expected)))
        assert_that(context.actual,
                    is_(instance_of(int)))
        return
    



Example: Float Bandwidth
~~~~~~~~~~~~~~~~~~~~~~~~

::

    @when("the IperfParser is called with a line with float bandwidth")
    def float_bandwidth(context):
        line = "[  4]  4.0- 5.0 sec   768 KBytes  6.29 Mbits/sec"
        match = context.human_expression.regex.search(line).groupdict()
        context.actual = context.parser.bandwidth(match)
        context.expected = 6.29 * context.converter[UnitNames.mbits][UnitNames.bits]
        return
    

::

    @then("the returned bandwidth is of type float")
    def assert_integer(context):
        assert_that(context.actual,
                    is_(equal_to(context.expected)))
        assert_that(context.actual,
                    is_(instance_of(float)))
        return
    




Example: Integer Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    @when("the IperfParser is called with a line with integer transfer")
    def integer_transfer(context):
        line = "[  4]  4.0- 5.0 sec   768 KBytes  6.29 Mbits/sec"
        match = context.human_expression.regex.search(line).groupdict()
        context.actual = context.parser.transfer(match)
        context.expected = 768 * \
          context.b_converter[BinaryUnitNames.kibibytes][BinaryUnitNames.bytes]
        return
    

::

    @then("the returned transfer is of type integer")
    def assert_integer_transfer(context):
        assert_that(context.actual,
                    is_(equal_to(context.expected)))
        assert_that(context.actual,
                    is_(instance_of(int)))
        return
    




Example: Float Transfer
~~~~~~~~~~~~~~~~~~~~~~~

::

    @when("the IperfParser is called with a line with float transfer")
    def integer_transfer(context):
        line = "[  3]  0.0-10.7 sec  3.50 MBytes  2.73 Mbits/sec"
        match = context.human_expression.regex.search(line).groupdict()
        context.actual = context.parser.transfer(match)
        context.expected = 3.50 * \
          context.b_converter[BinaryUnitNames.mebibytes][BinaryUnitNames.bytes]
        return
    

::

    @then("the returned transfer is of type float")
    def assert_integer_transfer(context):
        assert_that(context.actual,
                    is_(equal_to(context.expected)))
        assert_that(context.actual,
                    is_(instance_of(float)))
        return
    

