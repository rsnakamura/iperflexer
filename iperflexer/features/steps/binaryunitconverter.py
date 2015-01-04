
# python standard library
import random

# third party
from behave import given, when, then
from hamcrest import assert_that, is_, close_to

# this package
from iperflexer.unitconverter import BinaryUnitconverter, BinaryUnitNames


BYTE = 8
BASE = 2
DELTA = 0.0001


@given('a BinaryUnitconverter')
def binaryunitconverter(context):
    context.converter = BinaryUnitconverter()
    return


@when("the user converts from bytes to bits and back")
def bytes_to_bits(context):
    context.source = random.randrange(100)
    context.expected = context.source * BYTE
    context.outcome = context.source * context.converter[BinaryUnitNames.bytes][BinaryUnitNames.bits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.bytes]
    return


@then("the outcome is the correct conversion")
def assert_bits(context):
    assert_that(context.outcome,
                is_(close_to(value=context.expected,
                             delta=DELTA)))
    assert_that(context.reverse_outcome,
                is_(close_to(value=context.source,
                             delta=DELTA)))
    return


@when('the user converts from bits to bytes')
def step_implementation(context):
    context.bits = random.randrange(100)
    context.expected = context.bits/8.
    context.outcome = context.bits * context.converter[BinaryUnitNames.bits][BinaryUnitNames.bytes]
    return


@when('the user converts from kibibytes to bits and back')
def step_implementation(context):
    context.source = random.randrange(100)
    context.expected = context.source * 8 * (2**10)
    context.outcome = context.source * context.converter[BinaryUnitNames.kibibytes][BinaryUnitNames.bits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.kibibytes]
    return


@when('the user converts from bits to bits and back')
def step_implementation(context):
    context.source = random.randrange(100)
    context.expected = context.source
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.bits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to mebibits and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (2.**20)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.mebibits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.mebibits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to gibibits and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (2.**30)    
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.gibibits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.gibibits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to mebibytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**20)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.mebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.mebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to gibibytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**30)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.gibibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.gibibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to tebibytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**40)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.tebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.tebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to pebibits and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (2.**50)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.pebibits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.pebibits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to pebibytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**50)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.pebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.pebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to exbibits and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (2.**60)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.exbibits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.exbibits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to exbibytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**60)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.exbibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.exbibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to zebibits and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (2.**70)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.zebibits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.zebibits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to zebibytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (8 * 2.**70)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.zebibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.zebibytes][BinaryUnitNames.bits]
    return


@when('the user converts from bits to yobibits and back')
def step_implementation(context):
    # the inputs need to be much larger to effectively test this
    context.source = random.randrange(10**10, 10**30)
    context.expected = context.source / (2.**80)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.yobibits]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.yobibits][BinaryUnitNames.bits]
    return


@when('the user converts from bits to yobibytes and back')
def step_implementation(context):
    context.source = random.randrange(10**20, 10**30)
    context.expected = context.source / (8 * 2.**80)
    context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.yobibytes]
    context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.yobibytes][BinaryUnitNames.bits]
    return
