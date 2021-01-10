package problem0925;

import java.util.ArrayList;

public class Solution01 {
    public boolean isLongPressedName(String name, String typed) {

        boolean result = true;

        ArrayList<int[]> nameList = getCharCounterArrayList(name);
        ArrayList<int[]> typedList = getCharCounterArrayList(typed);

        int nameListSize = nameList.size();
        int typedListSize = typedList.size();

        if (typedListSize != nameListSize) {
            return false;
        }

        for (int i = 0; i < nameListSize; i++) {
            int[] item1 = nameList.get(i);
            int[] item2 = typedList.get(i);

            if (item1[0] != item2[0] || item1[1] > item2[1]) {
                result = false;
                break;
            }
        }

        return result;
    }

    private ArrayList<int[]> getCharCounterArrayList(String s) {

        ArrayList<int[]> result = new ArrayList<>();
        char lastChar = 0;
        int counter = 0;
        for (char ch : s.toCharArray()) {
            if (ch == lastChar) {
                counter++;
            } else {
                if (lastChar == 0) {
                    counter++;
                } else {
//                    System.out.println("lastChar=" + lastChar + ",counter=" + counter);
                    int[] theOne = {lastChar, counter};
                    result.add(theOne);
                    counter = 1;
                }
                lastChar = ch;
            }
        }

//        System.out.println("lastChar=" + lastChar + ",counter=" + counter);
        int[] theOne = {lastChar, counter};
        result.add(theOne);

        return result;
    }
}
