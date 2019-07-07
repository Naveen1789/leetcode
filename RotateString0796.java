class RotateString0796 {
    public boolean rotateString(String A, String B) {
        if (A.length() != B.length()) {
            return false;
        }
        return ((A + A).indexOf(B) == -1) ? false : true;

    }
}
