from unittest import TestCase
from types import StringType

from mock import patch

import nose.tools
from iperflexer.argumentparser import Arguments

raises = nose.tools.raises


class TestArguments(TestCase):
    def setUp(self):
        self.arguments = Arguments()
        return

    def set_and_run(self, arg=None, expected=None, default=False):
        self.arguments._parser = None
        if arg is not None and not default:
            options = ['takataka', "--" + arg]
            if type(expected) is StringType:
                 options += [expected]
        else:
            options = ['takataka']
        with patch('sys.argv', options ):
            args = self.arguments.parse_args()
            self.assertEqual(expected, getattr(args, arg))
        return
    
    def test_glob(self):
        glob = "*cow"
        self.set_and_run("glob", glob)
        return

    @raises(SystemExit)
    def test_error(self):
        glob = "*cow"
        self.set_and_run(arg=glob, expected=glob)
        return

    def test_units(self):
        units = "Mbits"
        flag = "units"
        self.set_and_run(flag, units)
        return

    def test_pdb(self):
        self.set_and_run('pudb', True)
        return

    def test_defaults(self):
        self.arguments._parser = None
        with patch('sys.argv', ['takataka']):
            args = self.arguments.parse_args()
            self.assertIsNone(args.glob)
            self.assertFalse(args.pudb)
            self.assertEqual("Mbits", args.units)
            #self.assertTrue(args.stdout)
        return

    def test_stdout(self):
        
        return
# end class TestArguments
