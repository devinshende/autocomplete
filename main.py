import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v','--verbose', 
		help="print out more information",
		action="store_true")
args = parser.parse_args()
print('normal amount of printing')
if args.verbose:
	print('extra print statements because this is verbose land')
