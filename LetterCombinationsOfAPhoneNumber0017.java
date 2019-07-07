class LetterCombinationsOfAPhoneNumber0017 {
    public void findAllCombinations(String digits, String strSoFar, List<String> ans, HashMap<Integer, List<Character>> hMap) {

        if (digits == "" || digits.length() == 0){
            ans.add(strSoFar);
        }
        else{
            Character ch = digits.charAt(0);
            String remainingStr = digits.substring(1);
            List<Character> allPossibleCharacters = hMap.get(Character.getNumericValue(ch));
            for (Character c : allPossibleCharacters){
                String newStrSoFar = strSoFar + c;
                findAllCombinations(remainingStr, newStrSoFar, ans, hMap);
            }
        }
    }

    public List<String> letterCombinations(String digits) {
        if (digits == "" || digits.length() == 0){
            return new ArrayList<String>();
        }

        HashMap<Integer, List<Character>> hMap = new HashMap<Integer, List<Character>>();

        hMap.put(2, Arrays.asList('a', 'b', 'c'));
        hMap.put(3, Arrays.asList('d', 'e', 'f'));
        hMap.put(4, Arrays.asList('g', 'h', 'i'));
        hMap.put(5, Arrays.asList('j', 'k', 'l'));
        hMap.put(6, Arrays.asList('m', 'n', 'o'));
        hMap.put(7, Arrays.asList('p', 'q', 'r', 's'));
        hMap.put(8, Arrays.asList('t', 'u', 'v'));
        hMap.put(9, Arrays.asList('w', 'x', 'y', 'z'));

        List<String> ans = new ArrayList<String>();
        findAllCombinations(digits, "", ans, hMap);

        return ans;
    }
}
