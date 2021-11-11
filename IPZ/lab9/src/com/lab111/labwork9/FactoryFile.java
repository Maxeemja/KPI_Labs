
package com.lab111.labwork9;
/**
 * A concrete factory for a file
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class FactoryFile extends FactoryAPI {
    /**
     * Creates a new file object
     */
    @Override
    public ProdObject createProdObject() {
        return new ObjectFile();
    }
    /**
     * Creates a new file request
     */
    @Override
    public ProdRequest createProdRequest() {
        return new RequestFile();
    }
}
