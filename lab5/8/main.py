import argparse


parser = argparse.ArgumentParser()
parser.add_argument("params", nargs="*")
args = parser.parse_args()

if not args.params:
    print("NO PARAMS")
else:
    try:
        numbers = [int(parameter) for parameter in args.params]
    except Exception as error:
        print(type(error).__name__)
    else:
        if len(numbers) == 1:
            print("TOO FEW PARAMS")
        elif len(numbers) > 2:
            print("TOO MANY PARAMS")
        else:
            print(sum(numbers))
