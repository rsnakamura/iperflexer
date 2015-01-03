Binary Unit Converter
=====================

.. literalinclude:: ../binaryunitconverter.feature
   :language: gherkin




Scenario: User converts binary units
------------------------------------

Example: bytes to bits
~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    @given('a BinaryUnitConverter')
    def binaryunitconverter(context):
        context.converter = BinaryUnitConverter()
        return




.. code:: python

    @when("the user converts from bytes to bits and back")
    def bytes_to_bits(context):
        context.source = random.randrange(100)
        context.expected = context.source * 8
        context.outcome = context.source * context.converter[UnitNames.bytes][UnitNames.bits]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.bits][UnitNames.bytes]
        return




.. code:: python

    @then("the outcome is the correct conversion")
    def assert_bits(context):
        assert_that(context.outcome,
                    is_(equal_to(context.expected)))
        assert_that(context.reverse_outcome,
                    is_(equal_to(context.source)))
        return



Example: bits to bytes
~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to bytes')
    def step_implementation(context):
        context.bits = random.randrange(100)
        context.expected = context.bits/8.
        context.outcome = context.bits * context.converter[UnitNames.bits][UnitNames.bytes]
        return



Then the outcome is the correct conversion

Example: kibibytes to bits
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from kibibytes to bits and back')
    def step_implementation(context):
        context.source = random.randrange(100)
        context.expected = context.source * 8 * 1024
        context.outcome = context.source * context.converter[UnitNames.kibibytes][UnitNames.bits]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.bits][UnitNames.kibibytes]
        return



Example: bits to bits
~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to bits and back')
    def step_implementation(context):
        context.source = random.randrange(100)
        context.expected = context.source
        context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.bits]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.bits][UnitNames.bits]
        return



Example: bits to mebibits
~~~~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to mebibits and back')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (1024. * 1024)
        context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.mebibits]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.mebibits][UnitNames.bits]
        return



Example: bits to gibibits
~~~~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to gibibits and back')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (1024.**3)
        context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.gibibits]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.gibibits][UnitNames.bits]
        return



Example: bits to mebibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to mebibytes and back')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 1024.**2)
        context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.mebibytes]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.mebibytes][UnitNames.bits]
        return



Example: bits to gibibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to gibibytes and back')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 1024.**3)
        context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.gibibytes]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.gibibytes][UnitNames.bits]
        return



Example: bits to tebibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a BinaryUnitConverter


.. code:: python

    @when('the user converts from bits to tebibytes and back')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 1024.**4)
        context.outcome = context.source * context.converter[UnitNames.bits][UnitNames.tebibytes]
        context.reverse_outcome = context.outcome * context.converter[UnitNames.tebibytes][UnitNames.bits]
        return


