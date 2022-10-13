import java.util.Arrays;
import java.util.Comparator;

public class Lab4 {
    public static class EdFacility {
        private final String name;
        private final int est_date;
        private final int studentsNum;
        private final int rating;
        private final float costPerYear;

        EdFacility(String name, int est_date, int studentsNum, int rating, float costPerYear){ //конструктор класу
            this.name = name;
            this.est_date = est_date;
            this.studentsNum = studentsNum;
            this.rating = rating;
            this.costPerYear = costPerYear;
        }

        public String getInfo() {
            return "Назва: " + name +  "\nРік заснування: " + est_date + "\nК-ть студентів: " + studentsNum + "\nМісце в рейтингу по Україні: " + rating + "\nВартість за рік навчання: " + costPerYear;
        }

        public int est_date() {
            return this.est_date;
        }

        public int studentsNum() {
            return this.studentsNum;
        }

        @Override // для перетворення інтових кодів у гарні рядки:)
        public String toString() {
            return name + "  " + est_date + "  " + studentsNum + " студентів";
        }

    }

    public static void main(String[] args) {
        EdFacility knu = new EdFacility("KНУ імені Шевченка",1834,32000,1,35000);
        EdFacility kpi = new EdFacility("KПІ імені Сікорського",1898,40000,3,33000);
        EdFacility naukma = new EdFacility("Києво-Могилянська академія",1615,4500,2,40000);
        /*НаУКМА*/
        EdFacility[] universities = {knu,kpi,naukma};
        System.out.println("Дата заснування у порядку зростання: ");
        Arrays.stream(universities).sorted(Comparator.comparingInt(EdFacility::est_date)).forEach(System.out::println);
        System.out.println("______________________________________________________");
        System.out.println("Кількість студентів у порядку спадання: ");
        Arrays.stream(universities).sorted(Comparator.comparingInt(EdFacility::studentsNum).reversed()).forEach(System.out::println);
        System.out.println("______________________________________________________");
        System.out.println(kpi.getInfo());
    }
}


