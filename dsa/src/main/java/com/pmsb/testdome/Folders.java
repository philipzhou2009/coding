/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.testdome;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import java.util.regex.*;

/**
 *
 * @author philip
 */
public class Folders {

    public static void run() {
        String xml =
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" +
                "<folder name=\"c\">" +
                    "<folder name=\"program files\">" +
                        "<folder name=\"uninstall    information\" />" +
                    "</folder>" +
                    "<folder name=\"users\" />" +
                "</folder>";

        Collection<String> names = folderNames(xml, 'u');
        for (String name : names) {
            System.out.println(name);
        }
    }

    public static Collection<String> folderNames0(String xml, char startingLetter) /*throws Exception*/ {
//        throw new UnsupportedOperationException("Waiting to be implemented.");

        List<String> result = new ArrayList<String>();

        int length = xml.length();
        int fromIdx = 0;
        int idx1 = 0, idx2 = 0;
        String sSub = "";
        while (true) {
            if (fromIdx >= length) {
                break;
            }

            idx1 = xml.indexOf("<folder name=", fromIdx);
            if (idx1 == -1) {
                break;
            }
            idx2 = xml.indexOf("\"", idx1 + 15);

            sSub = xml.substring(idx1 + 14, idx2);
            if (sSub.charAt(0) == startingLetter) {

                result.add(sSub);
            }

//            System.out.printf("idx1=%d, idx2=%d, %c, %c, %s\n", idx1, idx2, xml.charAt(idx1), xml.charAt(idx2), xml.substring(idx1 + 14, idx2));
            fromIdx = idx2 + 1;

        }

        return result;
    }

    public static Collection<String> folderNames(String xml, char startingLetter) {

        List<String> result = new ArrayList<String>();

        int length = xml.length();
        int fromIdx = 0;
        int idx1 = 0, idx2 = 0;
        String sSub = "";

        Pattern p = Pattern.compile("<folder\\s*name=\"[\\w\\s]*\"[\\s]*/*>");
        Matcher m = p.matcher(xml);
//        System.out.println("pattern: " + m.pattern());

        Pattern p1 = Pattern.compile("\"[\\w\\s]+\"");

        while (m.find()) {
            sSub = m.group();

//            System.out.println(m.start() + " " + sSub);

            Matcher m1 = p1.matcher(sSub);
            if (m1.find()) {
                sSub = m1.group();
//                System.out.println(m1.start() + " " + sSub);

                if (sSub.charAt(1) == startingLetter) {
                    result.add(sSub.substring(1, sSub.length() - 1));
                }

            }

        }

        return result;
    }
}
