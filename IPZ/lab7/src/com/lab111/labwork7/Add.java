package com.lab111.labwork7;
/**
 * class for adding
 */
public class Add implements Action{
    String s;
    public Add(String s){
        this.s = s;
    }
    @Override
    public String Do() {
        return "Added: " + s;
    }
}

