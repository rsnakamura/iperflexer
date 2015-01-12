
# python standard library
import random

# third party
from behave import given, when, then
from hamcrest import assert_that, is_, equal_to

# this package
from iperflexer.unitconverter import IperfbinaryConverter, BinaryUnitNames


@given('an IperfbinaryConverter')
def iperfbinaryconverter(context):
    context.converter = IperfbinaryConverter()
    return


@when("the user converts from bytes to bits and back using iperf-units")
def bytes_to_bits(context):
    context.source = random.randrange(100)
    context.expected = context.source * 8
    context.outcome = context.source * context.converter[BinaryUnitNames.bytes][BinaryUnitNames.bits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.bytes]
    return


@when('the user converts from kibibytes to bits and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100)
    context.expected = context.source * 8 * (2**10)
    context.outcome = context.source * context.converter[BinaryUnitNames.iperf_kibibytes][BinaryUnitNames.bits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_kibibytes]
    return


@when('the user converts from bits to mebibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**20)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_mebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_mebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to gibibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**30)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_gibibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_gibibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to tebibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**40)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_tebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_tebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to pebibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**50)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_pebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_pebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to exbibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**60)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_exbibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_exbibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to zebibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**70)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_zebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_zebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to yobibytes and back using iperf-units')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**80)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_yobibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_yobibytes][BinaryUnitNames.bits]
    return
