package hackerrank;

import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Java1DArrayPart2 {

    private final static Logger myLogger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    static {
        myLogger.setLevel(Level.ALL);
    }

    public static boolean canWin(int leap, int[] game) {
        ArrayList<Integer> footprints = new ArrayList<>();
        footprints.add(0);
        return recur(leap, game, 0, footprints);
    }

    private static boolean recur(int leap, int[] game, int pos, ArrayList<Integer> footprints) {

        myLogger.info("pos=" + pos + ",footprints=" + footprints);

        int gameLength = game.length;

        boolean tmp1 = false;
        int nextPos = pos + 1;
        if (nextPos >= gameLength) {
            tmp1 = true;
        } else if (game[nextPos] == 0 && !footprints.contains(nextPos)) {
            footprints.add(nextPos);
            tmp1 = recur(leap, game, nextPos, footprints);
        }

        boolean tmp2 = false;
        nextPos = pos + leap;
        if (nextPos >= gameLength) {
            return true;
        } else if (game[nextPos] == 0 && !footprints.contains(nextPos)) {
            footprints.add(nextPos);
            tmp2 = recur(leap, game, nextPos, footprints);
        }

        boolean tmp0 = false;
        nextPos = pos - 1;
        if (nextPos > 0 && game[nextPos] == 0 && !footprints.contains(nextPos)) {
            footprints.add(nextPos);
            tmp0 = recur(leap, game, nextPos, footprints);
        }

        return tmp0 || tmp1 || tmp2;
    }

}
