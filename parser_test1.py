import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--decimal", dest="decimal", action="store")          # extra value
parser.add_argument("--fast", dest="fast", action="store_true")           # existence/nonexistence
args = parser.parse_args()

print(args.decimal)
print(args.fast)
