import sys
import importlib
#from . import *
def main(argv):
    name = argv[1][ :-3]
    print(name)
    so = importlib.import_module(name)
    sol = so.Solution()
    print(getattr(sol, name)(argv[2: ]))
if __name__ == "__main__":
    main(sys.argv)