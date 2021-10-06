package com.lab111.labwork5;

/**
 * relational table traversal interface
 * @author Hrytsiuk Max
 */
public interface Iterator {
    public void First();
    public void Next();
    public boolean IsDone();
    public String[] CurrentItem();
}
