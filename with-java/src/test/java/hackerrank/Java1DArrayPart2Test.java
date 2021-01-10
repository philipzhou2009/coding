package hackerrank;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

@AllArgsConstructor
@Data
class ParamStrut {
    int[] game;
    int leap;
    boolean result;
}


class Java1DArrayPart2Test {

    @Test
    public void canWin() {

        ArrayList<ParamStrut> cases = new ArrayList<>();
        cases.add(new ParamStrut(new int[]{0, 0, 0, 0, 0}, 3, true));
        cases.add(new ParamStrut(new int[]{0, 0, 0, 1, 1, 1}, 5, true));
        cases.add(new ParamStrut(new int[]{0, 0, 1, 1, 1, 0}, 3, false));
        cases.add(new ParamStrut(new int[]{0, 1, 0}, 1, false));
        cases.add(new ParamStrut(new int[]{0, 0, 0, 0, 1, 0, 1}, 3, true));

        cases.forEach(x -> {
            boolean actual = Java1DArrayPart2.canWin(x.getLeap(), x.getGame());
            assertEquals(x.isResult(), actual);
            System.out.println("=================");
        });

    }
}