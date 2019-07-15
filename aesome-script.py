# PYTHON_ARGCOMPLETE_OK
import argcomplete
from argcomplete.completers import EnvironCompleter
import argparse
# https://argcomplete.readthedocs.io/en/latest/

parser = argparse.ArgumentParser()
parser.add_argument("--env-var1").completer = EnvironCompleter
# parser.add_argument("--env-var2").completer = EnvironCompleter
argcomplete.autocomplete(parser)