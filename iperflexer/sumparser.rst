The SumParser
=============

The sumparser parses sum-lines and stores the bandwidth sum. Unlike the `IperfParser` it uses the summed lines that iperf calculates. This means that if intervals and parallel threads were used and within one (or more) of those intervals one or more of the threads didn't report its value then the interval-sums will have fewer values than there were intervals (iperf will just skip summing an interval that didn't have all the threads reporting back). The ``IperfParser``, in contrast, will under-report the interval (unless the thread was actually dead) but it will at least give you a value. On the other hand, if all the sum-lines were there, then this would presumably be the more accurate method since we're taking what iperf itself reports.

.. '



The HumanExpressionSum Class
----------------------------

.. uml::

   HumanExpression <|-- HumanExpressionSum

.. module:: iperflexer.sumparser
.. autosummary::
   :toctree: api

   HumanExpression
   HumanExpression.thread_column   



CsvExpressionSum Class
----------------------

.. uml::

   CsvExpression <|-- CsvExpressionSum

.. autosummary::
   :toctree: api

   CsvExpressionSum
   CsvExpressionSum.thread_column   



The SumParser
-------------

.. uml::

   IperfParser <|-- SumParser
   SumParser: __call__(line)
   SumParser: last_line_bandwidth

.. autosummary::
   :toctree: api

   SumParser
   SumParser.__call__
   SumParser.pipe



Using the SumParser
-------------------

Checking The Call Output
------------------------

The ``__call__`` is the main way to use it. There are two ways to get the interval sums from the SumParser (and the IperfParser). One is to poll the returned value from the ``__call__`` to see if a value was returned.

::

    if in_documentation:
        data_folder = 'features/steps/samples/'
        data_path = os.path.join(data_folder, 'client_data.iperf')
        parser = SumParser()
        for line in open(data_path):
            bandwidth = parser(line)
            if bandwidth is not None:
                print(bandwidth)
    

::

    96.5
    94.4
    94.4
    93.3
    93.3
    94.4
    94.4
    94.4
    92.3
    94.4
    



.. warning:: the returned value is a float, not a string so it has to be cast to a string to be saved (don't do ``bandwidth + '\n'``).

.. '

Traversing the Values
---------------------

The original way to use it is to add all the lines and traverse the bandwidths afterwards. For the ``IperfParser`` this might be the safer way to use it if the data is being fed to it live while iperf is running, since it's adding up the threads, but for the ``SumParser`` I can't think of a down-side to either way (other than the warning about missing data for late threads noted at the top).

::

    if in_documentation:
        parser.reset()
    
        for line in open(data_path):
            parser(line)
        
        for bandwidth in parser.bandwidths:
            print(bandwidth)
    
    

::

    96.5
    94.4
    94.4
    93.3
    93.3
    94.4
    94.4
    94.4
    92.3
    94.4
    


           
The Last Line Bandwidth
-----------------------

When the `SumParser` matches a line that has an interval larger than what it is set to accept then it will set its ``last_line_bandwidth`` attribute to it, so once the whole iperf output has been consumed that attribute will have the final bandwidth value that iperf calculated for the entire session, assuming that the output is complete and this was the last line. If the line is missing it should be None.

Based on some empirical checking and some threads on the iperf discussion boards it looks like this is the most accurate value if there is a discrepancy between it and the added interval sums.

A Comparison to the Sums
~~~~~~~~~~~~~~~~~~~~~~~~

Here I'll compare what happens when you add the sum-lines up and take the mean versus using the ``last_line_bandwidth`` (iperf's calculated rate). ``parser.bandwidths`` is a generator of interval bandwidths and ``parser.intervals`` is a  dictionary that maps `interval:bandwidth`. Since the ``bandwidths`` attribute is a generator I can't take it's length so I'm using the length of the ``intervals`` instead.

.. '

::

    if in_documentation:
        parser.reset()
    
        for line in open(data_path):
            parser(line)
        
        calculated_average = sum(parser.bandwidths)/len(parser.intervals)
    



Now the outcome.

.. csv-table:: Calculated Sums-mean vs Iperf's Mean
   :header: Source, Bandwidth (Mbits/Second)

   Sum Lines, 94.18
   Iperf, 94.1


.. '

So... the calculated mean is higher... I don't really know what this means. My guess would be that this is a problem of loss of precision in converting everything into Mbits/second. Let's try an iperf file that used bits as the units.

Bit Sums
~~~~~~~~

First I'll set up the IperfParser and SumParser to convert to bits (which means no conversion in this case, since the source file was in bits). I'll also import the UnitConverter, a dict that has a sub-dict that returns the conversion factor when converting from one unit to another (it takes the form `unitconverter[<from units>][<to units>] = <conversion factor>`). The file that's going to be checked is :download:`client_p4_bits.iperf <features/steps/samples/client_p4_bits.iperf>` which is the output of the client-side output (the transmitter) when run with four parallel threads and the output format in bits.

.. '

::

    if in_documentation:
        #set up the unitconverter
        from unitconverter import UnitConverter
        converter = UnitConverter()
        data_path = os.path.join(data_folder, 'client_p4_bits.iperf')
    
        # rename the sum-parser used earlier to make it clearer
        sum_parser = parser
        
        #setup the parsers to use bits
        voodoo = IperfParser(units='bits')
        sum_parser.reset()
        sum_parser.units = 'bits'
    
        # load them up with the raw lines
        for line in open(data_path):
            sum_parser(line)
            voodoo(line)
    



Now we add the interval bandwidths together, convert the total from bits to Mbits and then take the mean. 

::

    if in_documentation:
        # convert the sums to Mbits and take the average
        total_bandwidth = sum(sum_parser.bandwidths) * converter['bits']['Mbits']
        calculated_average = total_bandwidth/len(sum_parser.intervals)
    
        # same for the re-added threads
        v_total = sum(voodoo.bandwidths) * converter['bits']['Mbits']
        v_average = v_total/len(voodoo.intervals)
    
        # now iperf's
        iperf_mean = sum_parser.last_line_bandwidth * converter['bits']['Mbits']
    



And here's what we get.

.. '

.. csv-table:: Bandwidth Comparison
   :header: Source, Mean Bandwidth (Mbits/Second)   

   Iperf, 93.592467
   Sum-Lines, 93.9524096
   Threads, 93.9524096


So in this case, since there were no threads with missing intervals the SumParser and the IperfParser came up with the same values but both were higher than iperf's calculated final value. It appears that there's more going on than just a round-off error.
