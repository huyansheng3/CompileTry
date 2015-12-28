package me.compiler.learning;

/**
 * Created with IntelliJ IDEA.
 * User: huyansheng
 * Date: 15-12-27
 * Time: 下午10:52
 * To change this template use File | Settings | File Templates.
 */
public class Token {
    public Type type;
    public String value;
    public Token(){

    }
    public Token(Type type,String value){
        this.type = type;
        this.value = value;
    }
    @Override
    public String toString() {
        return "Token("+type+","+value+")";
    }
}
