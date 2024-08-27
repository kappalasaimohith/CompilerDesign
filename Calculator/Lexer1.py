from sly import Lexer

class Calclexer(Lexer):
    literals = { '+', '-', '*', '/', '(', ')' }
    ignore = ' '
    
    tokens = [ 'INTEGER', 'NEWLINE', 'ID' ]
    
    INTEGER = r'[0-9]+'
    NEWLINE = r'\n'
    
    def INTEGER(self, token):
        token.value = int(token.value)
        return token
    
    ID = r'[a-z]+'
    
    def ID(self, token):
        token.value = int(input(f"Enter the value of {token.value}: "))
        return token
