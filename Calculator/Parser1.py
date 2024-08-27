from sly import Parser
from Lexer1 import Calclexer
import argparse

# Set up command-line argument parsing
apr = argparse.ArgumentParser()
apr.add_argument("filename", help="The file containing the expression")
apr.add_argument('-t', nargs='?', const=True, help="Show tokens")
args = apr.parse_args()

# Define the parser
class CalcParser(Parser):
    tokens = Calclexer.tokens
    literals = Calclexer.literals
    precedence = (('left', '+', '-'), ('left', '*', '/'))

    @_('expr')
    def L(self, p):
        return p.expr

    @_('L NEWLINE expr')
    def L(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('INTEGER')
    def expr(self, p):
        return p.INTEGER

    @_('ID')
    def expr(self, p):
        return p.ID

# Initialize lexer and parser
lexer = Calclexer()
parser = CalcParser()

# Read the input expression from the file
with open(args.filename) as f:
    expression = f.read()

# Show tokens if -t flag is set
if args.t:
    print("Tokens:")
    for token in lexer.tokenize(expression):
        print(f'type={token.type} value={token.value} lineno={token.lineno}')

# Parse the expression and print the result
print('\nResult:')
result = parser.parse(lexer.tokenize(expression))
print(result)
