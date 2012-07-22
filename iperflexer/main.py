# python
import sys
import os

# iperflexer
from argumentparser import Arguments
from iperfparser import IperfParser
from unitconverter import UnitNames
from finder import find

class ArgumentError(Exception):
    """
    """
# end class ArgumentError

UNITS = {'bits': UnitNames.bits,
         'kbits': UnitNames.kbits,
         'mbits': UnitNames.mbits,
         'gbits': UnitNames.gbits,         
         'bytes': UnitNames.bytes,
         'kbytes': UnitNames.kbytes,
         'mbytes': UnitNames.mbytes,
         'gbytes': UnitNames.gbytes}

WRITEABLE = 'w'
ADD_NEWLINE = "{0}\n"

def enable_debugging():
    try:
        import pudb
        pudb.set_trace()
    except ImportError:
        raise ArgumentError("`pudb` argument given but unable to import `pudb`")

def pipe(args):
    """
    Reads input from standard in and sends output to standard out.
    """
    units = UNITS[args.units.lower()]
    parser = IperfParser(units=units)
    for line in sys.stdin:
        parser.add(line)
    for bandwidth in parser.bandwidths:
        sys.stdout.write(ADD_NEWLINE.format(bandwidth))
    return

def analyze(args):
    """
    Reads data from files and outputs to files
    """
    units = UNITS[args.units.lower()]
    parser = IperfParser(units=units)
    for name in find(args.glob):
        basename, _ = os.path.splitext(name)
        new_name = basename + "_{0}.csv".format(units)
        for line in open(name):
            parser.add(line)

        with open(new_name, WRITEABLE) as output:
            for line in parser.bandwidths:
                output.write(ADD_NEWLINE.format(line))
        parser.reset()

def main():
    args = Arguments().parse_args()
    if args.pudb:
        enable_debugging()
    if args.glob is None:
        pipe(args)
    else:
        analyze(args)
    return

if __name__ == "__main__":
    main()
