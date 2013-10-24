The IperfParser
===============
.. currentmodule:: iperflexer.iperfparser

This is the class that performs the work if extracting the data-column.


.. autosummary::
   :toctree: api

   IperfParser

.. uml::

   IperfParser -|> BaseClass
   IperfParser : bandwidths
   IperfParser : regex
   IperfParser : intervals
   IperfParser : conversion
   IperfParser : filename(basename)
   IperfParser : reset()
   IperfParser : pipe(target)
   IperfParser : search(line)
   IperfParser : __call__(line)
   IperfParser : bandwidth(match)
   IperfParser : valid(match)

Properties
----------

bandwidths
~~~~~~~~~~

This is a generator of values from `IperfParser.intervals` in the sorted order of the keys (intervals). It is based on the premise that `IperfParser.intervals` is a dictionary whose keys are the start of the iperf sample intervals. e.g if the samples are reported at 1-second intervals then the keys are traversed :math:`0.0, 1.0,\ldots`.

.. note:: The name of the property suggests that the dictionary values are `bandwidths` but if this class is generalized to extract other columns then this will no longer be true and should be changed.
   
