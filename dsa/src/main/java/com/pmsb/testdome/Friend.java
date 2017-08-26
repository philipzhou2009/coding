/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.testdome;

import java.util.*;

/**
 *
 * @author philip
 */
import java.util.ArrayList;
import java.util.HashMap;

import java.util.Collection;
import java.util.ArrayList;

public class Friend {

    private Collection<Friend> friends;
    private String email;
//    private Collection<Friend> excludes = new ArrayList<Friend>();

    public Friend(String email) {
        this.email = email;
        this.friends = new ArrayList<Friend>();
    }

    public String getEmail() {
        return email;
    }

    public Collection<Friend> getFriends() {
        return friends;
    }

    public void addFriendship(Friend friend) {
        friends.add(friend);
        friend.getFriends().add(this);

//        Collections.sort(friends, new Comparator<Friend>() {
//            public int compare(Friend lhs, Friend rhs) {
//                // -1 - less than, 1 - greater than, 0 - equal, all inversed for descending
//                return lhs.email.compareTo(rhs.email);
//            }
//        });
//Collections.sort(friends, (a, b) -> b.getEmail().compareTo(a.getEmail()));
        ((ArrayList) friends).sort(Comparator.comparing(Friend::getEmail));
    }

    public boolean canBeConnected(Friend friend) {
        Collection<Friend> excludes = new ArrayList<>();
        boolean found = help(friend, excludes);
        return found;
    }

    public boolean help(Friend target, Collection<Friend> excludes) {

        boolean found = false;

        // no direct conn
        excludes.add(this);

        for (Friend x : friends) {
            if (x.email.equals(target.email)) {
                return true;
            }

            if (!excludes.contains(x)) {
                found = x.help(target, excludes);

                if (found) {
                    return true;
                }
            }
        }

        return found;
    }

    public static void main(String[] args) {
        Friend a = new Friend("A");
        Friend b = new Friend("B");
        Friend c = new Friend("C");

        a.addFriendship(b);
        b.addFriendship(c);

        System.out.println(a.canBeConnected(c));
    }
}

class Runner {

    private HashMap<Integer, Resource> resources = new HashMap<Integer, Resource>();

    public Iterable<Resource> getResources() {
        return this.resources.values();
    }

    public Resource acquireResource(int id) {
        Resource w = this.resources.getOrDefault(id, null);
        if (w == null) {
            w = new Resource(id);
            this.resources.put(id, w);
        }

        return w;
    }

    public void releaseResource(int id) {
        Resource w = this.resources.getOrDefault(id, null);
        if (w == null) {
            throw new IllegalArgumentException();
        }

        w.dispose();
        resources.remove(id);
//resources.get(id)
        w = null;
    }

    public class Resource {

        private ArrayList<String> tasks = new ArrayList<String>();

        private int id;

        public int getId() {
            return this.id;
        }

        public Iterable<String> getTasks() {
            return this.tasks;
        }

        public Resource(int id) {
            this.id = id;
        }

        public void performTask(String task) {
            if (this.tasks == null) {
                throw new IllegalStateException(this.getClass().getName());
            }

            this.tasks.add(task);
        }

        public void dispose() {
            this.tasks = null;
        }
    }

    public static void main(String[] args) {
        Runner d = new Runner();

        d.acquireResource(1).performTask("Task11");
        d.acquireResource(2).performTask("Task21");
        System.out.println(String.join(", ", d.acquireResource(2).getTasks()));
        d.releaseResource(2);
        d.acquireResource(1).performTask("Task12");
        System.out.println(String.join(", ", d.acquireResource(1).getTasks()));
        d.releaseResource(1);
    }
}

class JavaApplication2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        func1();
    }

    public static void func1() {
//        System.out.println("");
//        Utils.OutputResult("func1", 0);
        debug("func1");

    }

    public static void func2() {

    }

    public static void func3() {

    }

    public static void func4() {

    }

    public static void func5() {

    }

    public static void func6() {

    }

    public static void func7() {

    }

    public static void func8() {

    }

    public static void func9() {

    }

    public static void debug(String s) {
        System.out.println("debug:" + s);
    }
}

class DriverExam {

    public static void executeExercise(IExercise exercise) {
//        throw new UnsupportedOperationException("Waiting to be implemented.");
        try {
            exercise.start();
            exercise.execute();
        } catch (Exception e) {
            exercise.markNegativePoints();
        } finally {
            exercise.end();
        }
    }

    public static void main(String[] args) {
        DriverExam.executeExercise(new Exercise());
    }
}

class Exercise implements IExercise {

    public void start() {
        System.out.println("Start");
    }

    public void execute() {
        System.out.println("Execute");
    }

    public void markNegativePoints() {
        System.out.println("MarkNegativePoints");
    }

    public void end() {
        System.out.println("End");
    }
}

interface IExercise {

    void start() throws Exception;

    void execute();

    void markNegativePoints();

    void end();
}
