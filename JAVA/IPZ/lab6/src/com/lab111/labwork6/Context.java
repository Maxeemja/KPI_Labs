package com.lab111.labwork6;
/**
 * Class Context
 */
public class Context {
    private Strategy strategy;
    public Context() {
    }
    /**
     * Set new strategy
     */
    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }
    /**
     * Do the strategy algorithm
     */
    public void sortByStrategy() {
        strategy.sort(new Object[5]);
    }
}

