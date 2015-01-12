Reconciling the Intervals and the Final
=======================================

The main reason for extracting the interval sums is so that you can perform time-series analysis. If you try and re-calculate the final bandwidths with these intervals, however, you will find that the values don't match. This is because iperf is both rounding the times and reserving the last transfer from the intervals (but adding it to the final sums). This is an exploration of how much of a difference it can make.

.. '

::

    # this package
    from iperflexer.iperfparser import IperfParser
    from iperflexer.sumparser import SumParser
    from iperflexer.unitconverter import UnitConverter
    from iperflexer.unitconverter import UnitNames as d_names
    from iperflexer.unitconverter import BinaryUnitNames as b_names
    from iperflexer.unitconverter import BinaryUnitconverter
    
    d_converter = UnitConverter()
    b_converter = BinaryUnitconverter()
    
    



The Data
--------

The iperf session was run over wifi with four threads, a buffer size of 128 Kilobytes and reporting at one second intervals. We'll use the :download:`server output <server_p4_128K.csv>` as the baseline and the :download:`client output <client_p4_128K.csv>` to reconcile the final sums and the interval sums.

.. '

::

    server_voodoo = IperfParser(units='bits', threads=4)
    server_sums = SumParser(units='bits', threads=4)
    client_voodoo = IperfParser(units='bits', threads=4)
    client_sums = SumParser(units='bits', threads=4)
    
    with open('server_p4_128K.csv') as reader:
        for line in reader:
            server_voodoo(line)
            server_sums(line)
            
    with open('client_p4_128K.csv') as reader:
        for line in reader:
            client_voodoo(line)
            client_sums(line)
    



Now we can compare the values for each different method.

::

    mbits = d_converter[d_names.bits][d_names.mbits]
    server_final = server_sums.last_line_bandwidth
    server_final_mbits = server_sums.last_line_bandwidth*mbits
    recalc = sum(server_voodoo.bandwidths)/float(len(server_voodoo.intervals)) * mbits
    client_final = client_sums.last_line_bandwidth * mbits
    client_recalc = sum(client_voodoo.bandwidths)/float(len(client_voodoo.intervals))
    client_recalc_mbits = client_recalc * mbits
    



.. csv-table:: Comparisons
   :header: Source, Value, Difference from Server Final

   Server Final,10.002708,0
   Server Recalculated,10.0002203279,0.00248767213115
   Client Final,10.08557,-0.082862
   Client Recalculated,10.1362346667,-0.133526666667


The link was obviously very bad. Let' see how much of a difference the case with the largest difference from the server's true bandwidth (re-calculated client data) was.

::

    proportion = (client_recalc - server_final)/float(server_final)
    print(proportion)
    

::

    0.0133490517435
    

