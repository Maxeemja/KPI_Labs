package com.lab111.labwork9;
/**
 * A concrete product, request of a file
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class RequestFile extends ProdRequest {
    /**
     * Returns the string with the data of the object
     */
    @Override
    public String toString() {
        return "File request id" + getId();
    }
}
