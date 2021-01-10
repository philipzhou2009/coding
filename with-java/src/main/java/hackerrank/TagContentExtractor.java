package hackerrank;

import lombok.AllArgsConstructor;
import lombok.Data;

import javax.swing.text.html.HTML;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

@AllArgsConstructor
@Data
class TagItem {

    String tag;
    int start;
    int end;

    public String toString() {
        return tag + ", " + start + ", " + end;
    }
}

public class TagContentExtractor {

    private final static Logger myLogger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    static {
        myLogger.setLevel(Level.ALL);
    }

    String extractor(String input) {

        ArrayList<TagItem> items = new ArrayList<>();
        int i = 0;
        while (i < input.length()) {

            TagItem item = getTagItem(input, i);
            items.add(item);
            myLogger.info(item.toString());

            i = item.getEnd() + 1;
        }

//        myLogger.info(items);

        String result = "None";

        TagItem lastItem = items.get(0);
        i = 1;
        while (i < items.size()) {

            TagItem item = items.get(i);
            myLogger.info("item=" + item);

            if (item.getTag().equals("/" + lastItem.getTag())) {
                // find pair
                result = input.substring(lastItem.getEnd() + 1, item.getStart() - 1);
                myLogger.info(result);
//                break;
            }

            lastItem = item;
            i++;
        }

        return result;
    }

    private TagItem getTagItem(String input, int pos) {

        int idx1 = input.substring(pos).indexOf('<');
        int idx2 = input.substring(pos).indexOf('>');

        String tag = input.substring(pos).substring(idx1 + 1, idx2);

        return new TagItem(tag, idx1 + 1 + pos, idx2 + pos);
    }

}
