package com.lab111.labwork9;
/**
 * A concrete product, object of DB
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class ObjectDB extends ProdObject{
    /**
     * Returns the string with the data of the object
     */
    @Override
    public String toString() {
        return "DB object id" + getId();
    }
}
