class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int indexOf1 = -1;
        int indexOf2 = -1;
        int shortestDistance = words.length;
        for (int i = 0; i < words.length; i++){
            if (words[i].equals(word1)) {
                if (indexOf2 != -1 && ((i - indexOf2) < shortestDistance)){
                    shortestDistance = (i - indexOf2);
                }
                indexOf1 = i;
            }
            if (words[i].equals(word2)) {
                if (indexOf1 != -1 && ((i - indexOf1) < shortestDistance)){
                    shortestDistance = (i - indexOf1);
                }
                indexOf2 = i;
            }
        }
        return shortestDistance;
    }
}
