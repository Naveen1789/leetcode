class DecodeString0394 {
    public String decodeString(String s) {
        char[] chrArr = s.toCharArray();
        Stack st = new Stack();

        for (int i = 0; i < chrArr.length; i++) {
            char c = chrArr[i];
            if (Character.isDigit(c)){
                int k = c - '0';
                int j = i+1;
                while(j < chrArr.length && Character.isDigit(chrArr[j])){
                    k = k * 10 + (chrArr[j] - '0');
                    j++;
                }
                st.push(Integer.toString(k));
                i = j-1;
            }
            else if (c == '['){
                st.push("[");
            }
            else if(c == ']'){
                // Build the substring
                StringBuilder subStr = new StringBuilder();
                while (!st.peek().equals("[")){
                    // System.out.println("Popping " + st.peek() + " from stack");
                    subStr.insert(0,st.pop());
                }
                // remove '['
                st.pop();

                // Get the number of times to repeat the substr
                // System.out.println("Popping " + st.peek() + " from stack");
                int numOfRep = Integer.parseInt(st.pop().toString());
                StringBuilder repSubStr = new StringBuilder();
                while(numOfRep > 0){
                    repSubStr.append(subStr.toString());
                    numOfRep--;
                }
                st.push(repSubStr.toString());

            }

            else {
                // System.out.println("Pushing " + c + " to stack");
                st.push(Character.toString(c));
            }


        }

        StringBuilder ans = new StringBuilder();
        while (!st.empty()){
            ans.insert(0, st.pop());
        }
        return ans.toString();
    }
}
