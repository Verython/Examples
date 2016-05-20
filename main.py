from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser

def main(argv):
    input = FileStream(argv[1])
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()
    print tree.toStringTree()

if __name__ == '__main__':
    import sys
    main(sys.argv)
