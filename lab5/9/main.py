import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true")
parser.add_argument("params", nargs="*")
args = parser.parse_args()

pairs = [parameter.split("=", 1) for parameter in args.params]

if args.sort:
    pairs.sort(key=lambda pair: pair[0])

for key, value in pairs:
    print(f"Key: {key} Value: {value}")
