package com.lab111.labwork5;
/**
 * class bypass table in the opposite direction
 * @author Hrytsiuk
 */
public class RoundsFromEnd implements Iterator{
    private int position;
    String[][] students;
    /**
     * iterator creation constructor
     * reverse table traversal
     * @param students - array with information about students
     */
    RoundsFromEnd(String[][] students){
        this.students=new String[students.length][students[0].length];
        for(int i=0;i<=students.length-1;i++){
            this.students[i]=students[i];
        }
    }
    /**
     * setting the current position to the last element of the table
     */
    public void First(){
        this.position=this.students.length-1;
    }
    /**
     * setting the current position to the next element of the table
     */
    public void Next(){
        this.position--;
    }
    /**
     * checking for the presence of an element with
     * given position in the table
     */
    public boolean IsDone(){
        if (position==-1){
            return true;
        }
        else return false;
    }
    /**
     * method to return a table item
     * with catching errors missing
     * in the table of elements
     */
    public String[] CurrentItem(){
        try{
            if (this.IsDone()){
                throw new NullPointerException();
            }
            return this.students[position];
        }catch (NullPointerException e1){
            System.out.println("Iterator out of bounds");
        }

        return null;
    }
}