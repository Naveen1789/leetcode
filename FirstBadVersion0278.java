/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class FirstBadVersion0278 extends VersionControl {
    public int firstBadVersion(int n) {
        System.out.println(n);

        int l = 1;
        int r = n;

        while (l < r){
            int m = l + ((r - l) / 2);
            if (isBadVersion(m)){
                r = m;
            }
            else{
                l = m + 1;
            }

        }

        return l;
    }
}
