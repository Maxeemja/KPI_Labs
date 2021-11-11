package com.lab111.labwork9;
/**
 * A concrete product, request of DB
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class RequestDB extends ProdRequest {
    /**
     * Returns the string with the data of the object
     */
    @Override
    public String toString() {
        return "DB request id" + getId();
    }
}
