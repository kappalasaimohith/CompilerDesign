from sly import Lexer

class lex(Lexer):
    # Define literals and tokens
    literals = {'=', '{', '}', '(', ')','+','-','/', '*', ';', ','}
    tokens = { 'INT', 'ID', 'PRINT', 'INTEGER' }
    
    # Define token patterns
    INTEGER = r'[0-9]+'
    ID = r'[a-zA-Z][a-zA-Z0-9_]*'
    
    # Keyword definitions
    ID['int'] = 'INT'
    ID['print'] = 'PRINT'
    
    # Ignore whitespace and tabs
    ignore = ' \t '
    
    # Handle newlines
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    
    # Handle errors
    def error(self, t):
        print("ERROR:")
        print(f'Line {self.lineno}: Bad character {t.value[0]!r}')
        self.index += 1
