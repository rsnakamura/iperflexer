The Iperf Expressions
=====================
.. currentmodule:: iperflexer.iperfexpressions

This module holds a set of regular expressions to help with lexing the iperf input.



.. _iperfexpressions-expression-base:

The ExpressionBase
------------------

The ``ExpressionBase`` is an Abstract Base Class that provides a logger for children and requires that they implement an `expression` property. 

.. ifconfig:: repository != 'rtfd'

   .. uml::

      ExpressionBase -|> BaseClass
      ExpressionBase : String expression
      ExpressionBase : re.RegexObject regex

.. autosummary::
   :toctree: api

   ExpressionBase
   


The HumanExpression
-------------------

This is a concrete implementation of the :ref:`ExpressionBase <iperfexpressions-expression-base>`.

.. ifconfig:: repository != 'rtfd'

   .. uml::

      HumanExpression -|> ExpressionBase
      HumanExpression : String thread_column
      HumanExpression : String expression
      HumanExpression : re.RegexObject regex

.. autosummary::
   :toctree:

   HumanExpression

The `expression` is composed of parts from :ref:`Oatbran <oatbran-expressions>` so I will not re-define the base components. The following is an approximation of the expression (all the parts that are in all-capital letters are from oatbran):

.. math::

   threads &\gets `[' + OPTIONAL\_SPACES + INTEGER + `]'\\
   interval &\gets FLOAT + OPTIONAL\_SPACES + `-' + FLOAT + SPACES + `sec'\\    
   transfer &\gets REAL + SPACES + [`GKM'] + ? + `Bytes'\\    
   bandwidth &\gets REAL + SPACES + [`GKM'] + ? + (`bits'| `bytes') + `/sec'\\   
   expression  &\gets threads + SPACES + interval + SPACES + transfer + SPACES + bandwidth\\

   
