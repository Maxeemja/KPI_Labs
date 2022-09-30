package com.lab111.labwork9;
/**
 * Main class that represents the work of Abstract Factory design pattern
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class Test {

    public static void main(String[] args) {
        //Creating new objects
        ProdObject o = FactoryAPI.factoryCreator("File").createProdObject();
        ProdRequest r = FactoryAPI.factoryCreator("DB").createProdRequest();
        o.setId(25);
        r.setId(12);
        System.out.println(o.toString());
        System.out.println(r.toString());
    }
}

