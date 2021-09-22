package com.lab111.labwork4;

/**
 * @author Max Hrytsiuk
 *
 * Main class that draws an image by given coordinates
 *
 */
public class Test {

    public static void main(String [] args){
        Image i = new Image(new Coordinates(2,3), new Coordinates(5,10));
        i.printImage();
    }
}
