import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;

class SortCharactersByFrequency0451 {

  public String frequencySort(String s){
        Integer[] map = new Integer[256];
        Arrays.fill(map,new Integer(0));

        char[] chArr = s.toCharArray();
        for(char c : chArr){
            map[c] = map[c] + 1;
        }

        ArrayList<Integer> countList = new ArrayList<Integer>(Arrays.asList(map));

        StringBuilder ans = new StringBuilder();
        while (true){
            int max = Collections.max(countList);
            if (max <= 0){
                break;
            }
            int indexOfMax = countList.indexOf(max);

            while (max > 0){
                ans.append((char)indexOfMax);
                max--;
            }
            countList.set(indexOfMax, 0);
        }

        return ans.toString();
  }

}
