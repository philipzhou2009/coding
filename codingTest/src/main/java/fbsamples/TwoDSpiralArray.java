package fbsamples;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class TwoDSpiralArray {

    int[][] spiral(int n) {

        int[][] result = new int[n][n];

        int total = n * n;


//        4*(n-1)

        for (int i = 1; i <= total; i++) {

            int j = (i-1) % (n-1);

            int x;
            int y;
            if (j==0) {

                x = i-1;
                y = 0;
            }

            if (j==1)
            {
                x= i;
//                y=
            }

        }

        return null;
    }
}
