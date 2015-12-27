__author__ = 'huyansheng'

INTEGER,PLUS,EOF,MINUS,SPACE='INTEGER','PLUS','EOF','MINUS','SPACE'
class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value
    def __str__(self):
        return 'Token({type},{value})'.format(type=self.type,value=self.value)

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = text[self.pos]

    def error(self):
        raise Exception("Error parsing input")

    def advance(self):
        self.pos+=1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result+=self.current_char
            self.advance()
        return int(result)


    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue  # end here ,jump to the while  ; if is the break,jump out of the loop
            if self.current_char.isdigit():
                return Token(INTEGER,self.integer())
            if self.current_char == "+":
                self.advance()
                return Token(PLUS,"+")
            if self.current_char == "-":
                self.advance()
                return Token(MINUS,"-")
            self.error()
        return Token(EOF,None)


    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):   #the int+int
        self.current_token =self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        if op.type == MINUS:
            self.eat(MINUS)
        right = self.current_token
        self.eat(INTEGER)
        if op.type == PLUS:
            result = left.value+right.value
        if op.type == MINUS:
            result = left.value-right.value
        return result

def main():
    while True:
        try:
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()
