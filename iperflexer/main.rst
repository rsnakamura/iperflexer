The Main Module
===============


Argument Error
--------------

::

    class ArgumentError(Exception):
        """
        An error to raise if something is wrong with the arguments
        """
    # end class ArgumentError
    

::

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
    



Enable Debugging
----------------

::

    def enable_debugging():
        try:
            import pudb
            pudb.set_trace()
        except ImportError as error:
            print(error)
            raise ArgumentError("`pudb` argument given but unable to import `pudb`")
    



Pipe Function
-------------


::

    def pipe(args, infile=None, outfile=None):
        """
        Reads input from standard in and sends output to standard out.
        """
        if infile is None:
            infile = sys.stdin
        if outfile is None:
            outfile = sys.stdout
        try:
            units = UNITS[args.units.lower()]
        except KeyError:
            raise ArgumentError("Unknown Units: {0}".format(args.units))
            return
    
        if args.voodoo and not args.lastlinebandwidth:
            parser = IperfParser(units=units,
                                 maximum=args.maximum,
                                 threads=args.threads)
        else:
            parser = SumParser(units=units, maximum=args.maximum,
                               threads=args.threads)
        for line in infile:
            parser(line)
            if args.tee:
                sys.stderr.write(line)
    
        if args.lastlinebandwidth:
            # this will only work with the SumParser
            outfile.write(ADD_NEWLINE.format(parser.last_line_bandwidth))
        else:
            for bandwidth in parser.bandwidths:
                outfile.write(ADD_NEWLINE.format(bandwidth))
        parser.reset()
        return
    



Find Files Function
-------------------



Main
----

::

    def main():
        args = Arguments().parse_args()
        if args.pudb:
            enable_debugging()
        if args.glob is None:
            pipe(args)
        else:
            find_files(args)
        return
    

