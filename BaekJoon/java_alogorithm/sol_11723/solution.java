package java_alogorithm.sol_11723;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class solution {
    public static void main(String[] args) throws Exception {
        List<Integer> bucket = new ArrayList<Integer>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            if (tmp.length == 1){
                operation(tmp[0], 0, bucket);
            }
            else{
                operation(tmp[0], Integer.parseInt(tmp[1]), bucket);
            }


        }

        System.out.println(bucket);
    }

    private static void operation(String operCommand, int n, List<Integer> bucket) {
        switch (operCommand) {
            case "add":
                add(n, bucket);
                break;
            case "remove":
                remove(n, bucket);
                break;
            case "check":
                check(n, bucket);
                break;
            case "toggle":
                toggle(n, bucket);
                break;
            case "all":
                all(n, bucket);
                break;
            case "empty":
                empty(n, bucket);
                break;
        }
    }

    private static void empty(int n, List<Integer> bucket) {
        bucket = new ArrayList<Integer>();
    }

    private static void all(int n, List<Integer> bucket) {
        bucket = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20));
    }

    private static void toggle(int n, List<Integer> bucket) {
        if(bucket.contains(n)){
            bucket.remove(Integer.valueOf(n));
        }
        else{
            bucket.add(n);
        }
    }

    private static void check(int n, List<Integer> bucket) {
        if(bucket.contains(n)){
            System.out.println(1);
        }
        else{
            System.out.println(0);
        }

    }

    private static void remove(int n, List<Integer> bucket) {
        if (bucket.contains(n)) {
            bucket.remove(Integer.valueOf(n));
        }
    }

    private static void add(int n, List<Integer> bucket) {
        if (!bucket.contains(n)) {
            bucket.add(n);
        }
    }
}
