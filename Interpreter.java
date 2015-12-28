package me.compiler.learning;

import java.util.Scanner;

/**
 * Created with IntelliJ IDEA.
 * User: huyansheng
 * Date: 15-12-27
 * Time: 下午2:57
 * To change this template use File | Settings | File Templates.
 */
enum Type{
    PLUS("PLUS"),MINUS("MINUS"),SPACE("SPACE"),MULTI("MULTI"),DIV("DIV"),INTEGER("INTEGER"),EOF("EOF");
    private String type;
    private Type(String type){      //枚举构造函数只能为私有
        this.type = type;
    }
    @Override
    public String toString() {
        return "type : "+this.type;    //To change body of overridden methods use File | Settings | File Templates.
    }
}
public class Interpreter {
    private char[] text;
    private int pos=0;
    private Token current_token=null;
    private char current_char;
    public Interpreter(char[] text){
        this.text = text;
        this.current_char = text[pos];
    }
    public void advance(){
        pos+=1;
        if (pos> this.text.length-1){
            this.current_char ='\0';
        }
        else {
            this.current_char = this.text[pos];
        }
    }
    public void skip_whitespace(){
        while ( this.current_char == '\0'){
            advance();
        }
    }
    public String setInt(){
        String result="";
        while (Character.isDigit(this.current_char)){
            result+=this.current_char;
            advance();
        }
        return result;
    }
    public Token get_next_token(){
        Token token = new Token();
        while (this.current_char != '\0'){
            if (Character.isSpaceChar(this.current_char)){
                skip_whitespace();
                continue;
            }
            if (Character.isDigit(this.current_char)){

                token = new Token(Type.INTEGER,setInt());
                return token;
            }
            if (this.current_char == '+'){
                advance();
                return token =  new Token(Type.PLUS,"+");

            }
            if (this.current_char== '-'){
                advance();
                return token = new Token(Type.MINUS,"-");

            }
        }
        return token;
    }

    public void eat(Type type){
        if (this.current_token.type == type){
            this.current_token = get_next_token();
        }
        else {
        System.err.println("error");
        }
    }

    public int expr(){
        int result=0;
        this.current_token = get_next_token();
        Token left = this.current_token;
        this.eat(Type.INTEGER);
        Token op =this.current_token;
        if(op.type == Type.MINUS){
            this.eat(Type.MINUS);
        }
        if (op.type == Type.PLUS){
            this.eat(Type.PLUS);
        }
        Token right = this.current_token;
        this.eat(Type.INTEGER);
        if(op.type == Type.MINUS){
            result = Integer.parseInt(left.value)-Integer.parseInt(right.value);
        }
        if (op.type == Type.PLUS){
            result = Integer.parseInt(left.value)+Integer.parseInt(right.value);
        }
        return result;
    }

    public static void main(String[] args){
        while (true){
            Scanner sc = new Scanner(System.in);
            System.out.println("请输入算数表达式:");
            String text = sc.nextLine();
            Interpreter interpreter = new Interpreter(text.toCharArray());
            System.out.println(interpreter.expr());
        }
    }
}
