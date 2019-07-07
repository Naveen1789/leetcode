class DIStringMatch0942 {

    public int[] diStringMatch(String S) {
        int N = S.length();
        int lo = 0, hi = N;
        int[] ans = new int[N + 1];
        for (int i = 0; i < N; ++i) {
            if (S.charAt(i) == 'I')
                ans[i] = lo++;
            else
                ans[i] = hi--;
        }

        ans[N] = lo;
        return ans;
    }

//     public int[] diStringMatch(String S) {

//         int low = 0;
//         int high = S.length();

//         int[] ans = new int[high+1];

//         if (S.charAt(0) == 'D'){
//             ans[0] = high;
//             high = high - 1;
//         }
//         else {
//             ans[0] = 0;
//             low = low + 1;
//         }


//         int i = 0;
//         while (i < S.length() - 1){
//             if (S.charAt(i) == 'I'){
//                 if (S.charAt(i+1) == 'I'){
//                     ans[i+1] = low;
//                     low = low + 1;
//                 }
//                 else{
//                     ans[i+1] = high;
//                     high = high - 1;
//                 }
//             }
//             else{
//                 if (S.charAt(i+1) == 'D'){
//                     ans[i+1] = high;
//                     high = high - 1;
//                 }
//                 else {
//                     ans[i+1] = low;
//                     low = low + 1;
//                 }
//             }
//             i = i + 1;
//         }
//         ans[S.length()] = high;
//         return ans;
//     }
}
