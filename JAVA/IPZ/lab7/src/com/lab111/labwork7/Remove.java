package com.lab111.labwork7;
/**
 * Class for Removing items
 */
public class Remove implements Action{
    String s;
    public Remove(String s){
        this.s = s;
    }
    @Override
    public String Do() {
        return "Deleted: " + s;
    }
}
