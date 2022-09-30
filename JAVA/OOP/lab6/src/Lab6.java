/* Визначити ієрархію електроприладів.
Увімкнути деякі електроприлади в розетку.
Підрахувати споживану потужність. Провести сортування приладів у квартирі на основі потужності.
Знайти прилад у квартирі, що відповідає заданому діапазону електро-магнітного випромінювання.*/


import modules.Mobile;
import modules.Set;

public class Lab6 {
    public static void main(String[] args) {
        new Mobile(20, 20, true);
        new Mobile(10, 20, true);
        System.out.println(Set.getTotalPower());
        System.out.println(Set.getSortedByPower());
    }
}