class StrobogrammaticNumber0246 {
    public boolean isStrobogrammatic(String num) {
        HashMap<Character, Character> hMap = new HashMap<Character, Character>();

        hMap.put('0','0');
        hMap.put('1','1');
        hMap.put('6','9');
        hMap.put('8','8');
        hMap.put('9','6');

        int left = 0;
        int right = num.length() - 1;

        while (left <= right){
            if (hMap.containsKey(num.charAt(left)) && hMap.get(num.charAt(left)).equals(num.charAt(right))){
                left = left + 1;
                right = right - 1;
            }
            else{
                return false;
            }
        }
        return true;

    }
}
