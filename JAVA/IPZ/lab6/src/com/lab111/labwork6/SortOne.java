package com.lab111.labwork6;
/**
 * Class SortOne extends interface Strategy
 */
public class SortOne implements Strategy {
    @Override
    public void sort(Object[] mas) {
        System.out.println("It was sorted in straight order");
    }
}
