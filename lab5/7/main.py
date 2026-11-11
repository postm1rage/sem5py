import argparse


parser = argparse.ArgumentParser()
parser.add_argument("params", nargs="*")
args = parser.parse_args()

if args.params:
    for parameter in args.params:
        print(parameter)
else:
    print("no args")
