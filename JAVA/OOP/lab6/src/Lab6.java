/* Визначити ієрархію електроприладів.
Увімкнути деякі електроприлади в розетку.
Підрахувати споживану потужність. Провести сортування приладів у квартирі на основі потужності.
Знайти прилад у квартирі, що відповідає заданому діапазону електро-магнітного випромінювання.*/


import modules.Laptop;
import modules.Mobile;
import modules.Set;
import modules.Tablet;

public class Lab6 {
    public static void main(String[] args) {
        new Mobile(20, 20, true);
        new Mobile(10, 20, true);
        new Mobile(10, 20, false);
        new Tablet(50, 40, true);
        new Laptop(70, 50, true);
        System.out.println("Full power consumption: " + Set.getTotalPower() + " watts");
        System.out.println("\nList of plugged devices sorted by power usage: \n" +  Set.getSortedByPower());
        System.out.println("\n" + Set.getFromRadRange(45, 50));
    }
}