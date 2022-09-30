package com.lab111.labwork6;
/**
 * Main class
 * @author Hrytsiuk Max
 *
 */
public class Test {
    public static void main(String[] args) {
        Context context = new Context();

        context.setStrategy(new SortOne());
        context.sortByStrategy();

        context.setStrategy(new SortTwo());
        context.sortByStrategy();
    }
}
