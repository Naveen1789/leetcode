class AddToArrayFormInteger0989 {
    public List<Integer> addToArrayForm(int[] A, int K) {
        ArrayList<Integer> ans = new ArrayList<Integer>();

        int i = A.length - 1;
        int carry = 0;
        while (i >= 0 && K > 0){
            int sum = carry + A[i] + (K % 10);
            ans.add(0, sum % 10);
            carry = sum / 10;
            i--;
            K = K / 10;
        }

        while (i >= 0){
            int sum = carry + A[i];
            ans.add(0, sum % 10);
            carry = sum / 10;
            i--;
        }

        while (K > 0){
            int sum = carry + (K % 10);
            ans.add(0, sum % 10);
            carry = sum / 10;
            K = K / 10;
        }

        if (carry == 1){
            ans.add(0,1);
        }
        return ans;
    }
}
