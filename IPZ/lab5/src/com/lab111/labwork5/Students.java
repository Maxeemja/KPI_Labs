package com.lab111.labwork5;
/**
 * 	relational table creation class
 *  with information about students
 *  and creating iterators for direct and
 *  backtrack this table
 * @author Hrytsiuk
 */
public class Students implements RelativeTable{
    /**
     * Relative table- array
     */
    private String[][] students;
    /**
     * relational table constructor
     * @param students - two-dimensional array with student information
     */
    Students(String[][] students){
        this.students=new String[students.length][students[0].length];
        for(int i=0;i<=students.length-1;i++){
            this.students[i]=students[i];
        }
    }
    /**
     * a class for creating an iterator of the required type depending on the passed parameter typeOfIterator
     * @param typeOfIterator - type of iterator
     */
    public Iterator CreateIterator(int typeOfIterator){
        Iterator iterator;
        if(typeOfIterator==1){
            iterator=new RoundsFromStart(this.students);
        }else
            iterator=new RoundsFromEnd(this.students);
        return iterator;
    }
}