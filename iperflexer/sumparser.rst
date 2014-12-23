The SumParser
=============

The sumparser parses sums and logs the bandwidth sum.

::

    BITS = 'bits'
    
    



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

.. autosummary::
   :toctree: api

   SumParser
   SumParser.__call__
   SumParser.pipe
   SumParser.last_line_bandwidth   

