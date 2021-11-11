package com.lab111.labwork9;
/**
 * A concrete product, object of file
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class ObjectFile extends ProdObject {
    /**
     * Returns the string with the data of the object
     */
    @Override
    public String toString() {
        return "File object id" + getId();
    }
}
