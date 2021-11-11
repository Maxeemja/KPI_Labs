package com.lab111.labwork6;
/**
 * Class SortTwo extends interface Strategy
 */
public class SortTwo implements Strategy {
    @Override
    public void sort(Object[] mas) {
        System.out.println("It was sorted in reverse order");
    }
}
