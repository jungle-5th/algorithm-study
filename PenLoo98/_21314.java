import java.io.*;

public class _21314 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputString = br.readLine();

        // 최대값은 K까지 자르면 된다.
        StringBuffer MaxSb = new StringBuffer();
        int mCount = 0;
        for (int i=0; i<inputString.length(); i++){
            while(i<inputString.length() && inputString.charAt(i) == 'M'){
                mCount++;
                i++;
            }
            if(i<inputString.length() && inputString.charAt(i) == 'K'){
                MaxSb.append("5").append("0".repeat(mCount));
                mCount = 0;
            }
            else{
                MaxSb.append("1".repeat(mCount));
                mCount = 0;
            }
        }
        System.out.println(MaxSb.toString());

        // 최소값은 M은 붙이고, K는 붙이지 않기.
        StringBuffer MinSb = new StringBuffer();
        mCount = 0;
        for (int i=0; i<inputString.length(); i++){
            if (inputString.charAt(i) == 'M'){
                // M->M
                if(i!=inputString.length()-1 && inputString.charAt(i+1) == 'M'){
                    mCount++;
                }
                // M->K
                else if(i!=inputString.length()-1 && inputString.charAt(i+1) == 'K'){
                    // 10^mCount
                    MinSb.append("1").append("0".repeat(mCount));
                    mCount = 0;
                }
                // M이 마지막인 경우
                else{
                    // 10^mCount
                    MinSb.append("1").append("0".repeat(mCount));
                    mCount = 0;
                }
            }
            else if (inputString.charAt(i) == 'K'){
                MinSb.append("5");
            }
        }
        System.out.println(MinSb.toString());
    }
}