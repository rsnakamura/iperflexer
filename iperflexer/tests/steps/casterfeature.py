
# third-party
from behave import given, when, then
from hamcrest import assert_that, is_, equal_to, instance_of

# this package
from iperflexer.iperfparser import IperfParser
from iperflexer.iperfexpressions import HumanExpression
from iperflexer.unitconverter import UnitConverter, \
     UnitNames, BinaryUnitNames, BinaryUnitconverter


@given("an IperfParser set to bits and a thread of 1")
def iperf_parser_bits(context):
    context.converter = UnitConverter()
    context.b_converter = BinaryUnitconverter()
    context.parser = IperfParser(units='bits')
    context.human_expression = HumanExpression()
    return


@when("the IperfParser is called with a line with integer bandwidth")
def integer_bandwidth(context):
    line = "[  3]  0.0- 1.0 sec  3014656 Bytes  24117248 bits/sec"
    match = context.human_expression.regex.search(line).groupdict()
    context.actual = context.parser.bandwidth(match)
    context.expected = 24117248
    return


@then("the returned bandwidth is of type integer")
def assert_integer(context):
    assert_that(context.actual,
                is_(equal_to(context.expected)))
    assert_that(context.actual,
                is_(instance_of(int)))
    return


@when("the IperfParser is called with a line with float bandwidth")
def float_bandwidth(context):
    line = "[  4]  4.0- 5.0 sec   768 KBytes  6.29 Mbits/sec"
    match = context.human_expression.regex.search(line).groupdict()
    context.actual = context.parser.bandwidth(match)
    context.expected = 6.29 * context.converter[UnitNames.mbits][UnitNames.bits]
    return


@then("the returned bandwidth is of type float")
def assert_integer(context):
    assert_that(context.actual,
                is_(equal_to(context.expected)))
    assert_that(context.actual,
                is_(instance_of(float)))
    return


@when("the IperfParser is called with a line with integer transfer")
def integer_transfer(context):
    line = "[  4]  4.0- 5.0 sec   768 KBytes  6.29 Mbits/sec"
    match = context.human_expression.regex.search(line).groupdict()
    context.actual = context.parser.transfer(match)
    context.expected = 768 * \
      context.b_converter[BinaryUnitNames.kibibytes][BinaryUnitNames.bytes]
    return


@then("the returned transfer is of type integer")
def assert_integer_transfer(context):
    assert_that(context.actual,
                is_(equal_to(context.expected)))
    assert_that(context.actual,
                is_(instance_of(int)))
    return


@when("the IperfParser is called with a line with float transfer")
def integer_transfer(context):
    line = "[  3]  0.0-10.7 sec  3.50 MBytes  2.73 Mbits/sec"
    match = context.human_expression.regex.search(line).groupdict()
    context.actual = context.parser.transfer(match)
    context.expected = 3.50 * \
      context.b_converter[BinaryUnitNames.mebibytes][BinaryUnitNames.bytes]
    return


@then("the returned transfer is of type float")
def assert_integer_transfer(context):
    assert_that(context.actual,
                is_(equal_to(context.expected)))
    assert_that(context.actual,
                is_(instance_of(float)))
    return
