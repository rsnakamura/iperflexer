Iperf Binary Unit Converter
===========================

.. literalinclude:: ../iperfbinaryconverter.feature
   :language: gherkin



Scenario: User converts binary units
------------------------------------

Example: bytes to bits
~~~~~~~~~~~~~~~~~~~~~~

::

    @given('an IperfbinaryConverter')
    def iperfbinaryconverter(context):
        context.converter = IperfbinaryConverter()
        return
    

::

    @when("the user converts from bytes to bits and back using iperf-units")
    def bytes_to_bits(context):
        context.source = random.randrange(100)
        context.expected = context.source * 8
        context.outcome = context.source * context.converter[BinaryUnitNames.iperf_bytes][BinaryUnitNames.bits]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_bytes]
        return
    



Then the outcome is the correct conversion

Example: kibibytes to bits
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from kibibytes to bits and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100)
        context.expected = context.source * 8 * (2**10)
        context.outcome = context.source * context.converter[BinaryUnitNames.iperf_kibibytes][BinaryUnitNames.bits]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_kibibytes]
        return
    



Then the outcome is the correct conversion

Example: bits to bits
~~~~~~~~~~~~~~~~~~~~~

   #. Given a IperfbinaryConverter
   #. When the user converts from bits to bits and back using 
   #. Then the outcome is the correct conversion

Example: bits to mebibits
~~~~~~~~~~~~~~~~~~~~~~~~~

   #. Given a IperfbinaryConverter
   #. When the user converts from bits to mebibits and back using 
   #. Then the outcome is the correct conversion

Example: bits to gibibits
~~~~~~~~~~~~~~~~~~~~~~~~~

   #. Given an IperfbinaryConverter
   #. When the user converts from bits to gibibits and back
   #. Then the outcome is the correct conversion

Example: bits to mebibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to mebibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**20)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_mebibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_mebibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion

Example: bits to gibibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to gibibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**30)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_gibibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_gibibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion

Example: bits to tebibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to tebibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**40)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_tebibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_tebibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion

.. Example: bits to pebibits
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. Given a IperfbinaryConverter
.. 
.. <<name='bits_to_pebibits', wrap=False>>=
.. @when('the user converts from bits to pebibits and back')
.. def step_implementation(context):
..     context.source = random.randrange(100000)
..     context.expected = context.source / (2.**50)
..     context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.pebibits]
..     context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.pebibits][BinaryUnitNames.bits]
..     return
.. 
.. 
.. Then the outcome is the correct conversion
.. 
Example: bits to pebibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to pebibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**50)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_pebibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_pebibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion

.. Example: bits to exbibits
.. ~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. Given a IperfbinaryConverter
.. 
.. <<name='bits_to_exbibits', wrap=False>>=
.. @when('the user converts from bits to exbibits and back')
.. def step_implementation(context):
..     context.source = random.randrange(100000)
..     context.expected = context.source / (2.**60)
..     context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.exbibits]
..     context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.exbibits][BinaryUnitNames.bits]
..     return
.. 
.. 
.. Then the outcome is the correct conversion
.. 
Example: bits to exbibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to exbibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**60)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_exbibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_exbibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion

.. Example: bits to zebibits
.. ~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. Given a IperfbinaryConverter
.. 
.. <<name='bits_to_zebibits', wrap=False>>=
.. @when('the user converts from bits to zebibits and back')
.. def step_implementation(context):
..     context.source = random.randrange(100000)
..     context.expected = context.source / (2.**70)
..     context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.zebibits]
..     context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.zebibits][BinaryUnitNames.bits]
..     return
.. 
.. 
.. Then the outcome is the correct conversion
.. 
Example: bits to zebibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to zebibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**70)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_zebibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_zebibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion

.. Example: bits to yobibits
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. Given a IperfbinaryConverter
.. 
.. <<name='bits_to_yobibits', wrap=False>>=
.. @when('the user converts from bits to yobibits and back')
.. def step_implementation(context):
..     context.source = random.randrange(100000)
..     context.expected = context.source / (2.**80)
..     context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.yobibits]
..     context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.yobibits][BinaryUnitNames.bits]
..     return
.. 
.. 
.. Then the outcome is the correct conversion
.. 
Example: bits to yobibytes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a IperfbinaryConverter

::

    @when('the user converts from bits to yobibytes and back using iperf-units')
    def step_implementation(context):
        context.source = random.randrange(100000)
        context.expected = context.source / (8 * 2.**80)
        context.outcome = context.source * context.converter[BinaryUnitNames.bits][BinaryUnitNames.iperf_yobibytes]
        context.reverse_outcome = context.outcome * context.converter[BinaryUnitNames.iperf_yobibytes][BinaryUnitNames.bits]
        return
    



Then the outcome is the correct conversion
