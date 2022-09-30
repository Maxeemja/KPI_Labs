package com.lab111.labwork7;
/**
 * class for editing
 */
public class Edit implements Action{
    String s;
    public Edit(String s){
        this.s = s;
    }
    @Override
    public String Do() {
        return "Edited: " + s;
    }
}
