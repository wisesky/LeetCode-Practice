import sys
import importlib
import argparse
def main(argv):
    #print(argv)
    # s1 cmd argv parser 
    #moduleName = argv[1] 必须事先指定参数类型,无法对所有Solution统一
    #parser = argparse.ArgumentParser(description='Solution Time ')
    #parser.add_argument('p1', type=int)
    # s2 input
    moduleName = input('Type in the module Name : ')
    if moduleName.endswith('.py'):
        moduleName = moduleName[ :-3]
    so = importlib.import_module(moduleName).Solution()
    func = getattr(so, moduleName)
    #p1 = input('params1 = ')
    #p2 = input('params2 = ')
    #r = func(p1, p2)
    print(func())
    return 


if __name__ == "__main__":
    main(sys.argv)
