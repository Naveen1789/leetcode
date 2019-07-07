class StrobogrammaticNumberII0247 {
    ArrayList<String> ans ;
    HashMap<String, String> hMap;
    public List<String> findStrobogrammatic(int n) {
        ans = new ArrayList<String>();
        hMap = new HashMap<String, String>();

        hMap.put("0","0");
        hMap.put("1","1");
        hMap.put("6","9");
        hMap.put("8","8");
        hMap.put("9","6");

        findStrobogrammatic("", n);
        return ans;
    }

    public void findStrobogrammatic(String text, int length) {

        if (length == 0){
            ans.add(text);
            return;
        }

        else if(length == 1){
            if (text.equals("")){
                ans.add("0");
                ans.add("1");
                ans.add("8");
            }
            else {
                int lenOfText = text.length() / 2;
                ans.add(text.substring(0,lenOfText) + "0" + text.substring(lenOfText));
                ans.add(text.substring(0,lenOfText) + "1" + text.substring(lenOfText));
                ans.add(text.substring(0,lenOfText) + "8" + text.substring(lenOfText));
            }
        }
        else{
            for (Map.Entry<String,String> entry : hMap.entrySet()) {
                if(length <= 3 && entry.getKey().equals("0")){
                    continue;
                }
                String next = entry.getKey() + text + entry.getValue();
                findStrobogrammatic(next, length-2);
            }
        }
    }
}
