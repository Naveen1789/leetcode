class AddStrings0415 {
    public String addStrings(String num1, String num2) {

        int index1 = num1.length() - 1;
        int index2 = num2.length() - 1;
        StringBuilder ans = new StringBuilder();
        int carry = 0;
        while (index1 >= 0 && index2 >= 0){
            int sum = carry + num1.charAt(index1) + num2.charAt(index2) - 96;
            ans.insert(0, sum % 10);
            carry = sum / 10;

            index1--;
            index2--;
        }

        while (index1 >= 0){
            int sum = carry + num1.charAt(index1) - 48;
            ans.insert(0, sum % 10);
            carry = sum / 10;
            index1--;
        }

        while (index2 >= 0){
            int sum = carry + num2.charAt(index2) - 48;
            ans.insert(0, sum % 10);
            carry = sum / 10;
            index2--;
        }

        if (carry == 1){
            ans.insert(0, 1);
        }
        return ans.toString();
    }
}
