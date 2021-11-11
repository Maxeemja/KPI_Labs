
package com.lab111.labwork9;
/**
 * A concrete factory for DB
 *
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class FactoryDB extends FactoryAPI {
    /**
     * Creates a new DB object
     */
    @Override
    public ProdObject createProdObject() {
        return new ObjectDB();
    }
    /**
     * Creates a new DB request
     */
    @Override
    public ProdRequest createProdRequest() {
        return new RequestDB();
    }
}
