import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', 
		help="display the square of a given number",
		type=int)
args = parser.parse_args() # returns data from the options specified
print(args.square**2)
