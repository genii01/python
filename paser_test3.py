import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--user", nargs = '?', action="store")          # extra value
parser.add_argument("--item", nargs = '?', action="store")          # extra value
parser.add_argument("--score", type=int, action="store")           # existence/nonexistence
args = parser.parse_args()
print(args.user)
print(args.item)
print(args.score)
