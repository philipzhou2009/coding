package codesignal;

import java.util.*;

public class MeanGroups {

    int[][] meanGroups(int[][] a) {

        int len = a.length;

        Map<Float, ArrayList<Integer>> m1 = new LinkedHashMap<>();

        for (int i = 0; i < len; i++) {

            int[] arrTmp = a[i];
            int arrLen = arrTmp.length;

            int sum = 0;
            for (int k : arrTmp) {
                sum += k;
            }

            float mean = (float) sum / arrLen;

            ArrayList<Integer> l = m1.get(mean);
            if (l == null) {
                l = new ArrayList<>();
                l.add(i);
                m1.put(mean, l);
            } else {
                l.add(i);
            }

        }

        System.out.println(m1);


        int[][] result = new int[m1.size()][];
        int i = 0;
        for (Map.Entry<Float, ArrayList<Integer>> entry : m1.entrySet()) {

            ArrayList<Integer> integerArrayList = entry.getValue();
            int[] ret = integerArrayList.stream().mapToInt(j -> j).toArray();

            result[i] = ret;
            i++;
        }

        System.out.println(Arrays.deepToString(result));

        return result;
    }
}
