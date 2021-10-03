import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")          # extra value
parser.add_argument("-f", "--fast", dest="fast", action="store_true")           # existence/nonexistence
args = parser.parse_args()

if args.decimal == '1':
    print("decimal is 1")

if args.fast:
    print("-f option is used")
