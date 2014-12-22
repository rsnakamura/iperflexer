The Iperf Lexer (Read Me)
=========================


This is a program to extract bandwidths from `iperf <http://sourceforge.net/projects/iperf/>`_ output. To install it you can use pip.

::

   pip install iperflexer

It requires ``numpy`` to run. If not already installed you can use a package manager or pip.

::

   pip install numpy

It is meant to be used with files with data-reporting intervals shorter than the total run-time (e.g. 1 second intervals). Once installed it creates a command-line command named ``parseiperf``.

Running It
----------

The original idea behind it was to use it as part of a pipeline so you can pipe iperf output to it directly ::

  iperf -c 192.168.10.5 -i 1 -P 4 | parseiperf

Which will then send the total bandwith for each interval to standard-output (it does this so that it can then be piped to another command such as one that calculates statistics). You can also ``cat`` an existing file to it::

  cat test.iperf | parseiperf

The Command-Line Options
------------------------

You can get a list of the options using the help option.

.. code:: bash

   parseiperf -h

::

    usage: parseiperf [-h] [-g GLOB] [-u UNITS] [-s] [-v] [--pudb] [--pdb] [-t]
    
                      [-p THREADS] [-m MAXIMUM]
    
    optional arguments:
      -h, --help            show this help message and exit
      -g GLOB, --glob GLOB  A file-glob to match input file names. (default=Non
    e)
      -u UNITS, --units UNITS
                            Output units per second
                            [bits,Bytes,KBits,KBytes,Mbits,MBytes,Gbits,GBytes]
    
                            (default=Mbits)
      -s, --save            If glob is provided, save to a file instead of send
    ing
                            to stdout. (default=False)
      -v, --voodoo          Add threads yourself instead of using 'sum' lines.
                            (default=False)
      --pudb                Enable pudb (if installed). (default=False)
      --pdb                 Enable pdb (default=False)
      -t, --tee             Send lines standard error as they come in.
                            (default=False)
      -p THREADS, --threads THREADS
                            Specify thread count (default=4)
      -m MAXIMUM, --maximum MAXIMUM
                            Maximum allowed bandwidth (default=1000000)
    
    
    



Glob
~~~~

Although I said above that you pipe input to the ``parseiperf`` command you can also use a file-glob to pass in file-names to it. It descends into all sub-directories to look for matches so you need to make sure the glob is restrictive enough to not match unexpected files and you also need to surround it with quotation marks (so that the shell's interface doesn't expand the glob before passing it to the command). The output for all the files will be concatenated and output to standard output.

::

   parseiperf -g "*.iperf"

Units
~~~~~

The ``--units`` tells the `iperflexer` what units the bandwidths should use. One of the primary reasons for this code was to allow the iperf raw-data to be output in bits per second and then converted later to the more human-readable Megabits per second. The names for the units is meant to match the iperf headers (so megabits-per-second is `Mbits`).

Saves
~~~~~

As noted above, the default behavior is to send output to standard output, concatenating the values for multiple data-files, but if you passed in a file-name-glob you can use the ``--save`` option and it will save the output for each input file to a separate file. The output-file-names will be the input-file-names with `.csv` appended to them.

VooDoo
~~~~~~

The ``--voodoo`` flag will tell ``iperflexer`` to re-add the individual threads (otherwise it uses the summed-values that iperf provides).

Debugging
~~~~~~~~~

The ``--pudb`` and ``--pdb`` options will start the chosen debugger before running the command.

Tee
~~~

The ``--tee`` option tells the command to send the output to standard error and standard output. This way if you use it in the originally intended way (piping to another command) you can still see what happened.

Threads
~~~~~~~

Since the ``voodoo-parser`` re-adds the threads it needs to know how many of them there are, so if you use it, pass in the ``--threads`` option to change it from the default of 4 if you need to. I could have made it infer-them, but I wanted to be able to work with data where the connection was bad and the threads sometimes died and this seemed to be the safest way to do it. It doesn't really matter if all the threads finish their reporting, it's mostly for the bad connections.

.. note:: If you only use one thread (likely meaning you didn't use iperf's ``--parallel`` option) it will still parse the output but you have to explicitly tell it that there's one thread (``-p 1``) or it won't work (even if you don't use the voodoo-parser).

.. '

Maximum
~~~~~~~

Sometimes when the bandwidth gets really small iperf seems to react by generating an unbelievably large number. When the ``iperflexer`` sees a bandwidth that's larger than what's set as the ``--maximum`` (default is :math:`10^6`) it will report the value as 0.

Building the Documentation
--------------------------

I try to keep an updated build of the documentation on the web at `bitbucket <http://rallion.bitbucket.org/commands/iperf_lexer/index.html>`_ and `pypi <https://pythonhosted.org/iperflexer/>`_ but these instructions should help if you want to build them yourself.

The code was written in a literate programming style using `Pweave <http://mpastell.com/pweave/>`_ so next to each python file you will also find a restructured-text file used for the documentation -- the python package is also the `sphinx <http://sphinx-doc.org/>`_ source for the documentation. If you want to edit or re-generate a file you need pweave::

  pip install pweave

Note that pweave has changed since I started using it, requiring Python 3 style ``print`` functions instead of the older python ``print`` statements so if you install it now some of the files may raise an error when weaving (generating the rst files). I don't *think* they will since I'm using stdout and stderr directly, not printing, but buyer beware.

Pweave itself requires matplotlib if you want to generate the rst files (it's meant to facilitate `reproducible research <http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1003285>`_ and it has some conveniences for creating plots with matplotlib). So if you want to create the rst files you need to install it::

   pip install matplotlib

Matplotlib itself requires numpy and they can take a long time to build. If you're not into building them just for this and you have a package manager it's probably better to use it. For debian-based systems::

   sudo apt-get install python-matplotlib


Since it's a sphinx repository you'll of course need sphinx::

   pip install sphinx

I'm using the `alabaster <https://github.com/bitprophet/alabaster>`_ sphinx theme so you need that too::

   pip install alabaster   

At the moment I'm using ``sphinxcontrib-plantuml`` for the UML diagrams. This prevents it from working or Read the Docs so I might remove them eventually, but for now if you want them you'll need both plantuml and the sphinx extension::

   apt-get install plantuml
   apt-get install graphviz
   pip install sphinxcontrib-plantuml   

I think that's everything. If it is, then when you're next to the `Makefile` you can build the (html) documentation with::

   make html

And it will output the html files to ``build/html``. I also `rsync` the html files to a folder where my apache server can see it so if you build it before I remember to get rid of that in the Makefile you will likely see an error but that shouldn't affect the built documentation (although if just by coincidence you have the exact same file structure as me it might clobber something (sorry)).