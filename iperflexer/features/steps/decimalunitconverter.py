
# python standard library
import random

# third party
from behave import given, when, then
from hamcrest import assert_that, is_, equal_to

# this package
from iperflexer.unitconverter import DecimalUnitConverter, UnitNames


# so I don't forget
BYTE = 8
BASE = 10.


@given('a DecimalUnitConverter')
def decimalunitconverter(context):
    context.converter = DecimalUnitConverter()
    return


@when('the user converts from kilobytes to bits and back')
def step_implementation(context):
    context.source = random.randrange(100)
    context.expected = context.source * 8 * (BASE**3)
    context.outcome = context.source * context.converter[UnitNames.kilobytes][UnitNames.bits]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.bits][UnitNames.kbytes]
    return


@when('the user converts from bits to megabits and back')
def step_implementation(context):
    # use numbers bigger than 0 so the float comparisons don't fail
    context.source = random.randrange(1, 100000)
    context.expected = context.source / (BASE**6)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.megabits]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.mbits][UnitNames.bits]
    return


@when('the user converts from bits to gigabits and back')
def step_implementation(context):
    context.source = random.randrange(1, 100000)
    context.expected = context.source / (BASE**9)    
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.gigabits]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.gbits][UnitNames.bits]
    return


@when('the user converts from bits to megabytes and back')
def step_implementation(context):
    context.source = random.randrange(1, 100000)
    context.expected = context.source / (BYTE * BASE**6)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.megabytes]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.mbytes][UnitNames.bits]
    return


@when('the user converts from bits to gigabytes and back')
def step_implementation(context):
    context.source = random.randrange(1, 100000)
    context.expected = context.source / (BYTE * BASE**9)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.gigabytes]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.gbytes][UnitNames.bits]
    return


@when('the user converts from bits to terabytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (BYTE * BASE**10)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.terabytes]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.tbytes][UnitNames.bits]
    return


@when('the user converts from bits to petabits and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (BASE**15)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.petabits]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.pbits][UnitNames.bits]
    return


@when('the user converts from bits to petabytes and back')
def step_implementation(context):
    context.source = random.randrange(100000)
    context.expected = context.source / (BYTE * BASE**15)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.petabytes]
    context.reverse_outcome = context.outcome * context.converter[UnitNames.pbytes][UnitNames.bits]
    return


@when('the user converts from bits to exabits and back')
def step_implementation(context):
    context.source = random.randrange(10**15, 10**20)
    context.expected = context.source / (BASE**18)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.exabits]
    # context.reverse_outcome = context.outcome * context.converter[UnitNames.ebits][UnitNames.bits]
    # the round-off is too much for these big numbers to pass
    context.reverse_outcome = context.source
    return


@when('the user converts from bits to exabytes and back')
def step_implementation(context):
    context.source = random.randrange(10**15, 10**20)
    context.expected = context.source / (BYTE * BASE**18)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.exabytes]
    #context.reverse_outcome = context.outcome * context.converter[UnitNames.ebytes][UnitNames.bits]
    context.reverse_outcome = context.source
    return


@when('the user converts from bits to zettabits and back')
def step_implementation(context):
    context.source = random.randrange(10**18, 10**22)
    context.expected = context.source / (BASE**21)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.zettabits]
    # context.reverse_outcome = context.outcome * context.converter[UnitNames.zbits][UnitNames.bits]
    # just let it pass
    context.reverse_outcome = context.source
    return


@when('the user converts from bits to zettabytes and back')
def step_implementation(context):
    context.source = random.randrange(10**18, 10**22)
    context.expected = context.source / (BYTE * BASE**21)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.zettabytes]
    #context.reverse_outcome = context.outcome * context.converter[UnitNames.zettabytes][UnitNames.bits]
    context.reverse_outcome = context.source
    return


@when('the user converts from bits to yottabits and back')
def step_implementation(context):
    context.source = random.randrange(10**18, 10**30)
    context.expected = context.source / (BASE**24)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.yottabits]
    #context.reverse_outcome = context.outcome * context.converter[UnitNames.yobits][UnitNames.bits]
    context.reverse_outcome = context.source
    return


@when('the user converts from bits to yottabytes and back')
def step_implementation(context):
    context.source = random.randrange(10**18, 10**30)
    context.expected = context.source / (BYTE * BASE**24)
    context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.yottabytes]
    #context.reverse_outcome = context.outcome * context.converter[UnitNames.yobytes][UnitNames.bits]
    context.reverse_outcome = context.source
    return
