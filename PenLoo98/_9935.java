import java.util.*;
import java.io.*;

public class _9935{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputString = br.readLine();
        String bombString = br.readLine();
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < inputString.length(); i++){
            stack.push(inputString.charAt(i));
            if(stack.size() >= bombString.length()){
                boolean isEqual = true;
                for(int j = 0; j < bombString.length(); j++){
                    // 스택 안의 문자열이 폭발 문자열과 같은지 확인
                    if(stack.get(stack.size() - bombString.length() + j) != bombString.charAt(j)){
                        isEqual = false;
                        break;
                    }
                }
                // 폭발 문자열과 같다면 스택에서 제거
                if(isEqual){
                    for(int j = 0; j < bombString.length(); j++){
                        stack.pop();
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(char c : stack){
            sb.append(c);
        }
        System.out.println(sb.length() == 0 ? "FRULA" : sb.toString());
    }
}