class Solution {
  public int canCompleteCircuit(int[] gas, int[] cost) {

    int sumOfGas = 0;
    int sumOfCost = 0;
    for (int g : gas) {
        sumOfGas += g;
    }

    for (int c : cost) {
        sumOfCost += c;
    }

    if (sumOfCost > sumOfGas){
        return -1;
    }

    int numberOfStations = gas.length;
    int fuelLeft = 0;
    int start = 0;
    for (int current = 0; current < numberOfStations; current++){
        fuelLeft = fuelLeft + gas[current] - cost[current];
        if (fuelLeft < 0) {
            start = current + 1;
            fuelLeft = 0;
        }
    }
    
    return start;
  }
    // public int canCompleteCircuit(int[] gas, int[] cost) {
    //
    //     int numberOfStations = gas.length;
    //
    //     for (int start = 0; start < numberOfStations; start++){
    //         int fuelLeft = 0;
    //         int currentStation = start;
    //         int numberOfStationsVisited = 0;
    //         while ((numberOfStationsVisited <= numberOfStations) && (fuelLeft + gas[currentStation] >= cost[currentStation])){
    //             fuelLeft = fuelLeft + gas[currentStation] - cost[currentStation];
    //             numberOfStationsVisited = numberOfStationsVisited + 1;
    //             currentStation = (currentStation + 1) % numberOfStations;
    //         }
    //
    //         if (numberOfStationsVisited >= numberOfStations){
    //             return start;
    //         }
    //
    //     }
    //
    //     return -1;
    // }
}
