package com.lab111.labwork9;
/**
 * Abstract class for a request
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public abstract class ProdRequest {

    private int id;
    /**
     * @return the id
     */
    public int getId() {
        return id;
    }
    /**
     * @param id the id to set
     */
    public void setId(int id) {
        this.id = id;
    }
    public abstract String toString();
}
