__author__ = 'huyansheng'

INTEGER,PLUS,EOF,MINUS,SPACE,DIV,MULTI='INTEGER','PLUS','EOF','MINUS','SPACE',"DIV","MULTI"
class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value
    def __str__(self):
        return 'Token({type},{value})'.format(type=self.type,value=self.value)

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos]

    def error(self):
        raise Exception("Invalid Character")

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
            if self.current_char == "*":
                self.advance()
                return Token(MULTI,"*")
            if self.current_char == "/":
                self.advance()
                return Token(DIV,"/")
            if self.current_char == "+":
                self.advance()
                return Token(PLUS,"+")
            if self.current_char == "-":
                self.advance()
                return Token(MINUS,"-")
            self.error()
        return Token(EOF,None)

class Interpreter(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid Syntax")

    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        result = self.factor()
        while self.current_token.type in (DIV,MULTI):
            token = self.current_token
            if token.type == DIV:
                self.eat(DIV)
                result = result/self.factor()
            if token.type == MULTI:
                self.eat(MULTI)
                result = result*self.factor()
        return result

    def expr(self):
        final_result = self.term()
        while self.current_token.type in (PLUS,MINUS):
            token = self.current_token
            if token.type == MINUS:
                self.eat(MINUS)
                final_result = final_result-self.term()
            if token.type == PLUS:
                self.eat(PLUS)
                final_result = final_result+self.term()
        return final_result


def main():
    while True:
        try:
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        lexer =Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()
