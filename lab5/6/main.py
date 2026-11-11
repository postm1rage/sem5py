import sys


args = sys.argv[1:]
sort_requested = "--sort" in args
parameters = [argument for argument in args if argument != "--sort"]
pairs = [parameter.split("=", 1) for parameter in parameters]

if sort_requested:
    pairs.sort(key=lambda pair: pair[0])

for key, value in pairs:
    print(f"Key: {key} Value: {value}")
