import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static class Ed_Facility{
        String name;
        int est_date;
        int students_num;
        int rating;
        float cost_per_year;
        Ed_Facility(String name,int est_date,int students_num,int rating,float cost_per_year){ //конструктор класу
            this.name = name;
            this.est_date = est_date;
            this.students_num = students_num;
            this.rating = rating;
            this.cost_per_year = cost_per_year;
        }
        public static void  getInfo(Ed_Facility A){ // функція для відображення інформації про об'єкт
            System.out.println("Назва: " + A.name);
            System.out.println("Дата засну: " + A.est_date);
            System.out.println("Кількість студентів: " + A.students_num);
            System.out.println("Місце в рейтингу по Києву: " + A.rating);
            System.out.println("Середня ціна  навчання / рік: " + (int) A.cost_per_year + " гривень");
        }

        @Override // для перетворення інтових кодів у гарні рядки:)
        public String toString() {
            return name + "  " + est_date + "  " + students_num + " студентів";
        }

    }

    public static void main(String[] args) {
        Ed_Facility KNU = new Ed_Facility("KНУ імені Шевченка",1834,25000,1,35000);
        Ed_Facility KPI = new Ed_Facility("KПІ імені Сікорського",1898,40000,3,33000);
        Ed_Facility NaukMA = new Ed_Facility("Києво-Могилянська академія",1615,4500,2,40000);

        Ed_Facility[] universities = {KNU,KPI,NaukMA};
        System.out.println("Дата заснування у порядку зростання: ");
        Arrays.stream(universities).sorted(Comparator.comparingInt(o -> o.est_date)).forEach(System.out::println);
        System.out.println("______________________________________________________");
        System.out.println("Кількість студентів у порядку спадання: ");
        Arrays.stream(universities).sorted(Comparator.comparingInt(o -> -o.students_num)).forEach(System.out::println);

    }
}


