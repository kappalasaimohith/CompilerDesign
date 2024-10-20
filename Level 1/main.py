import argparse
from Tiny_C_Lexer import lex

lexer = lex()

parser = argparse.ArgumentParser()
parser.usage = "tinyCC [options] file"
parser.add_argument("-i", nargs=1, help="input program file")
parser.add_argument('-tokens', action='store_true', help="Show tokens in file.toks (or out.toks)")

args = parser.parse_args()

expr = ''
with open(args.i[0], "r") as f:
    expr = f.read()

if args.tokens:
    with open(f'{args.i[0]}.toks', "w") as f:
        for token in lexer.tokenize(expr):
            f.write(f'type={token.type} value={token.value} lineno={token.lineno}\n')
