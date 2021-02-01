package codesignal;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MeanGroupsTest {

    @Test
    void meanGroups() {

        int[][] a = {{3, 3, 4, 2},
                {4, 4},
                {4, 0, 3, 3},
                {2, 3},
                {3, 3, 3}
        };

        int[][] actual = new MeanGroups().meanGroups(a);


    }

    @Test
    void case2() {

        int[][] a = {{-2, 4, 7, -6, 2, -5, 3},
                {-1, 0, 0, 0},
                {2, 2, -6, 17, 9, -22, 30, -16, 0, -1, -11, 6, 0, -4},
                {3, 3, -8, -2, 3},
        };

        int[][] actual = new MeanGroups().meanGroups(a);


    }
}