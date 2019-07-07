class MeetingRoomsII0253 {
    public int minMeetingRooms(int[][] intervals) {

        if (intervals == null || intervals.length == 0){
            return 0;
        }

        Integer[] startTimes = new Integer[intervals.length];
        Integer[] endTimes = new Integer[intervals.length];

        for(int i = 0; i < intervals.length; i++){
            startTimes[i] = intervals[i][0];
            endTimes[i] = intervals[i][1];
        }

        Arrays.sort(startTimes, new Comparator<Integer>() {
           public int compare(Integer a, Integer b){
               return a - b;
           }
        });

        Arrays.sort(endTimes, new Comparator<Integer>() {
           public int compare(Integer a, Integer b){
               return a - b;
           }
        });

        int stPtr = 0;
        int endPtr = 0;
        int numOfRoomsReq = 0;
        while (stPtr < intervals.length){
            if (startTimes[stPtr] >= endTimes[endPtr]){
                numOfRoomsReq--;
                endPtr++;
            }
            numOfRoomsReq++;
            stPtr++;
        }

        return numOfRoomsReq;
    }
}
