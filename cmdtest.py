import sys

print(*[f'Arg. No. {i+1} => {arg}' for i, arg in enumerate(sys.argv[1:])], sep='\n')