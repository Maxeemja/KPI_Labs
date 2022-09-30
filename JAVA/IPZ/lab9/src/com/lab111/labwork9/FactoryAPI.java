package com.lab111.labwork9;
/**
 * Method for creating a factory of a special type
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public abstract class FactoryAPI {

    public static FactoryAPI factoryCreator(String factoryType){
        if(factoryType == "File")
            return new FactoryFile();
        return new FactoryDB();
    }
    public abstract ProdObject createProdObject();
    public abstract ProdRequest createProdRequest();
}
