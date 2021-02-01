package codesignal;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CountPairsWithSumTest {

    @Test
    void countPairsWithSum() {

        int actual = new CountPairsWithSum().countPairsWithSum(8, new int[]{2, 3, 6, 2, 8});
        assertEquals(1, actual);

    }

    @Test
    void case2() {
        int actual = new CountPairsWithSum().countPairsWithSum(11, new int[]{10, 9, 4, 0, 8, 1, 7, 6, 10, 5});
        assertEquals(3, actual);
    }
}