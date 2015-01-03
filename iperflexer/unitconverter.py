
class UnitNames(object):
    """
    Unit Names is a namespace to hold units
    """
    __slots__ = ()
    bits = "bits"

    # base-10
    kbits = "K" + bits
    mbits = "M" + bits
    gbits = "G" + bits
    bytes = "Bytes"
    kbytes = "K" + bytes
    mbytes = "M" + bytes
    gbytes = "G" + bytes

    # base-2
    bibits = 'bi' + bits
    kibibits = "Ki" + bibits
    mebibits = 'Me' + bibits
    gibibits = "Gi" + bibits
    tebibits = "Te" + bibits
    bibytes = 'bi' + bytes
    kibibytes = "Ki" + bibytes
    mebibytes = "Me" + bibytes
    gibibytes = 'Gi' + bibytes
    tebibytes = 'Te' + bibytes
# end UnitNames

IDENTITY = 1
ONE = 1.0
KILO = 10**3
KIBI = 2**10
BYTE = 8
TO_BYTE = ONE/BYTE

class BaseConverter(dict):
    """
    A creator of unit-conversion dictionaries
    """
    def __init__(self, to_units, kilo_prefix):
        """
        base_converter constructor

        :param:

         - `to_units`: a list of the units to covert  to  (has to be half to-bits, half to-bytes)
         - `kilo_prefix`: kilo multiplier matching type of units
        """
        self.to_units = to_units
        self.kilo_prefix = kilo_prefix

        self._prefix_conversions = None
        self._bits_to_bytes = None
        self._bytes_to_bits = None

        # split the to_units list for later
        self.bit_conversions = self.byte_conversions = len(to_units)//2
        self.bit_units = to_units[:self.bit_conversions]
        self.byte_units = to_units[self.byte_conversions:]
        return

    @property
    def prefix_conversions(self):
        """
        List of lists of prefix conversions
        """
        if self._prefix_conversions is None:
            # start with list that assumes value has no prefix
            # this list is for 'bits' or 'bytes'
            # the values will be 1, 1/kilo, 1/mega, etc.
            start_list = [self.kilo_prefix**(-power)
                                         for power in xrange(self.bit_conversions)]
            self._prefix_conversions = self.conversions(conversion_factor=1,
                                                        start_list=start_list)
        return self._prefix_conversions

    @property
    def bits_to_bytes(self):
        """
        List of conversions for bits to bytes
        """
        if self._bits_to_bytes is None:
            self._bits_to_bytes = self.conversions(conversion_factor=TO_BYTE)
        return self._bits_to_bytes

    @property
    def bytes_to_bits(self):
        """
        list of conversions for bytes to bits
        """
        if self._bytes_to_bits is None:
            self._bytes_to_bits = self.conversions(conversion_factor=BYTE)
        return self._bytes_to_bits

    def conversions(self, conversion_factor, start_list=None):
        """
        Creates the converters

        :param:

         - `conversion_factor`: multiplier for values (8 or 1/8, or 1)
         - `start_list`: if given, use to start the conversion-list

        :return: list of conversion_lists
        """
        if start_list is None:
            # assume that prefix_conversions exists (not safe, but...)
            start_list = self.prefix_conversions[0]
        # start with byte_factor times the base conversions (1, 1/kilo, etc.)
        converter_list = [[conversion_factor * conversion
                           for conversion in start_list]]
        for previous in xrange(self.bit_conversions - 1):
            # 'pop' last item from previous list
            # and prepend one higher-power conversion
            next_conversions = ([self.kilo_prefix**(previous+1) * conversion_factor] +
                                converter_list[previous][:-1])
            converter_list.append(next_conversions)
        return converter_list

    def build_conversions(self):
        """
        builds the dictionary
        """
        # from bits to bytes
        for index, units in enumerate(self.bit_units):
            self[units] = dict(zip(self.to_units, self.prefix_conversions[index] +
                                   self.bits_to_bytes[index]))

        # from bytes to bits
        for index, units in enumerate(self.byte_units):
            self[units] = dict(zip(self.to_units, self.bytes_to_bits[index] +
                                   self.prefix_conversions[index]))
        return
# end class UnitConverter

decimal_to_units = [UnitNames.bits, UnitNames.kbits,UnitNames.mbits , UnitNames.gbits,
                UnitNames.bytes, UnitNames.kbytes, UnitNames.mbytes, UnitNames.gbytes]


class UnitConverter(BaseConverter):
    """
    The UnitConverter makes conversions based on a base-10 system
    """
    def __init__(self):
        super(UnitConverter, self).__init__(to_units=decimal_to_units,
                                            kilo_prefix=KILO)
        self.build_conversions()
        return
# end class UnitConverter

if __name__ == "__builtin__":
    converter = UnitConverter()
    bits = 10**6
    converted = bits * converter['bits']['Mbits']
    print(converted)

binary_to_units = [UnitNames.bits, UnitNames.kibibits,UnitNames.mebibits , UnitNames.gibibits, UnitNames.tebibits,
                UnitNames.bytes, UnitNames.kibibytes, UnitNames.mebibytes, UnitNames.gibibytes, UnitNames.tebibytes]

class BinaryUnitConverter(BaseConverter):
    """
    The BinaryUnitConverter is a conversion lookup table for binary data

    Usage::

       converted = old * UnitConverter[old units][new units]

    Use class UnitNames to get valid unit names
    """
    def __init__(self):
        super(BinaryUnitConverter, self).__init__(to_units=binary_to_units,
                                                  kilo_prefix=KIBI)
        self.build_conversions()
        return