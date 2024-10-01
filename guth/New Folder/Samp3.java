
import java.util.*;
public class Samp {
    public static void main(String[] args) {
        String name1 = "pao";
        String name2 = "cjayi";
        System.out.print(name1.compareTo(name2));
        /*Integer in[] = {1,2,3};
        Double dou[] = {1.1,2.1,3.1};
        String st[] = {"abc","def","ghi"};
        Generic<Integer> inn1 = new Generic<Integer>(in);
        Generic<Double> inn2 = new Generic<Double>(dou);
        Generic<String> inn3 = new Generic<String>(st);
        for (int var : inn1.get()) {
            System.out.println(var);
        }
        for (double var : inn2.get()) {
            System.out.println(var);
        }
        for (String var : inn3.get()) {
            System.out.println(var);
        }*/
    }       
}

class Generic<T>{
    public T ar[];
    public  Generic(T[] ar){
        this.ar = ar;
    }
    public T[] get(){
        return ar;
    }
    public void set(T[] inp){
        this.ar = inp;
    }
}
