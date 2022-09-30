package com.lab111.labwork5;
/**
 * test class
 * @author Hrytsiuk Max
 */
public class Test {
    /**
     * test method
     * @param arr
     */
    public static void main(String[] arr){
        String[][] student=new String[4][3];//line: surname,faculty,group
        student[0][0]="Hrytsiuk";
        student[0][1]="FICT";
        student[0][2]="IO-02";
        student[1][0]="Ivanov";
        student[1][1]="IPSA";
        student[1][2]="KA-04";
        student[2][0]="Sidorov";
        student[2][1]="FMF";
        student[2][2]="FM-02";
        student[3][0]="Popov";
        student[3][1]="VPI";
        student[3][2]="VP-03";
        Students students=new Students(student);
        Iterator iteratorFromBegin=students.CreateIterator(1);
        iteratorFromBegin.First();
        Print(iteratorFromBegin.CurrentItem());
        iteratorFromBegin.Next();
        Print(iteratorFromBegin.CurrentItem());
        iteratorFromBegin.Next();
        Print(iteratorFromBegin.CurrentItem());
        iteratorFromBegin.Next();
        Print(iteratorFromBegin.CurrentItem());
        iteratorFromBegin.Next();
        Print(iteratorFromBegin.CurrentItem());
        /////////////////
        Iterator iteratorFromEnd=students.CreateIterator(2);
        iteratorFromEnd.First();
        Print(iteratorFromEnd.CurrentItem());
        iteratorFromEnd.Next();
        Print(iteratorFromEnd.CurrentItem());
        iteratorFromEnd.Next();
        Print(iteratorFromEnd.CurrentItem());
        iteratorFromEnd.Next();
        Print(iteratorFromEnd.CurrentItem());
    }
    /**
     * method for printing a relational table element
     * @param student - line of table
     */
    public static void Print(String[] student){
        try{
            for(int i=0;i<=2;i++){
                System.out.print(student[i]+" ");
            }
        }catch (NullPointerException e2){
        }
        System.out.println();
    }
}
