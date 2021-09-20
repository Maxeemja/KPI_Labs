package com.lab111.labwork2;
/** Class #1
 * @author Maxym Vlasov
 * @version 1.0
 */
abstract class Cl1 implements If1 {
    /**Method for this class*/
    @Override
    public void meth1() {
        System.out.println("Cl1.meth1()");
    }
    /**Inherited method*/
    public void meth3() {
        System.out.println("Cl1.meth3()");
    }
}
package com.lab111.labwork2;
/** Class #2
 * @author Maxym Vlasov
 * @version 1.0
 */
public class Cl2 extends Cl3 implements If2 {
    /**Method for this class*/
    @Override
    public void meth2() {
        System.out.println("Cl2.meth2()");
    }
}
package com.lab111.labwork2;
/** Class #3
 * @author Maxym Vlasov
 * @version 1.0
 */
public class Cl3 implements If3 {

    /**Method for this class*/
    @Override
    public void meth3() {
        System.out.println("Cl3.meth3()");
    }
    /**Inherited method*/
    @Override
    public void meth2() {
        System.out.println("Cl3.meth2()");
    }

    /**Inherited method*/
    @Override
    public void meth1() {
        System.out.println("Cl3.meth1()");
    }
}
package com.lab111.labwork2;
/** Interface #1
 * @version 1.0
 *
 * @author Maxym Vlasov
 */
public interface If1 extends If2 {
    /**Method for execution*/
    public void meth1();
}
package com.lab111.labwork2;
/** Interface #2
 *
 * @author Maxym Vlasov
 * @version 1.0
 */
public interface If2 {
    /**Method for execution*/
    public void meth2();
}
package com.lab111.labwork2;
/** Interface #3
 * @author Maxym Vlasov
 * @version 1.0
 */
public interface If3 extends If1 {
    /**Method for execution*/
    public void meth3();
}
