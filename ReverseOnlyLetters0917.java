class ReverseOnlyLetters0917 {
    public String reverseOnlyLetters(String S) {
        char[] charArray = S.toCharArray();

        int left = 0;
        int right = charArray.length - 1;

        while (left < right){
            while (left < right && !Character.isLetter(charArray[left])){
                left = left + 1;
            }

            while (right > left && !Character.isLetter(charArray[right])){
                right = right - 1;
            }

            if (left < right){
                char temp = charArray[left];
                charArray[left] = charArray[right];
                charArray[right] = temp;
            }
            left = left + 1;
            right = right - 1;
        }

        return new String(charArray);
    }
}
