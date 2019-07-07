class FirstUniqueCharacterInAString0387 {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> hMap = new HashMap<Character, Integer>();

        for (int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if (hMap.containsKey(c)) {
                hMap.put(c, hMap.get(c) + 1);
            }
            else {
                hMap.put(c, 1);
            }
        }

        for (int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if (hMap.get(c) == 1){
                return i;
            }
        }

        return -1;
    }
}
