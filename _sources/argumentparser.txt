The Argument Parser
===================




The ArgumentParser provides the main user interface to the *IperfLexer*.

.. _argumentparser-arguments-class:

The Arguments Class
-------------------

This was originally called the `ArgumentParser` but re-named `Arguments` so as not to be confused with the python `ArgumentParser`. Its only real purpose is to separate the defining of the command-line arguments from the ``main`` module so that it can be documented a little better and possibly swapped out later for docopt without needing to clobber it entirely.

.. ifconfig:: repository != 'rtfd'

    .. uml::
    
       Arguments o-- argparse.ArgumentParser
       Arguments : Namespace parse_args()

.. currentmodule:: iperflexer.argumentparser       
.. autosummary::
   :toctree: api

   Arguments

Example Use::

   parser = Arguments()
   args = parser.parse_args()


.. _argumentparser-command-line-arguments:
   
Command Line Arguments
----------------------

This is a dump of the ``parseiperf --help`` output.




.. note:: The short-form of the `threads` argument is `p`, not `t` to match *iperf's* '--parallel' and avoid the *parseiperf's* '--tee'.

   


