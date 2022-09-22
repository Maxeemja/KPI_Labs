import java.util.*;

public class Lab3 {
    //0210
    //StringBuilder
    //відсортувати слова за зростанням кількості голосних у них
    public static void main(String[] args) {
        String vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ";
        StringBuilder initStr = new StringBuilder("Ознайомлення з рядками та використання основних методів їх обробки в мові програмування Джава");

        Map<String, Integer> dict = new HashMap<>(); // основна хеш мапа для збереження каунтера голосних для кожного слова в реченні


        // основна операція по обрахунку к-ті голосних у кожному слові речення
        int counter = 0;
        for(int i = 0; i < initStr.length(); i++) {
            char currLetter = initStr.charAt(i);
            if (vowels.indexOf(currLetter) != -1) {
                counter++;
            }
            if (currLetter == ' ' || i == initStr.length() - 1) {
                int offset = String.join(" ", dict.keySet()).length();
                dict.put(initStr.substring(offset, i + 1).trim(), counter);
                counter = 0;
            }
        }

        // подальші махінації були проведені для сортування хешмапи за зростанням значень
        LinkedHashMap<String, Integer> sortedMap = new LinkedHashMap<>();
        ArrayList<Integer> list = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            list.add(entry.getValue());
        }
        Collections.sort(list);
        for (int num : list) {
            for (Map.Entry<String, Integer> entry : dict.entrySet()) {
                if (entry.getValue().equals(num)) {
                    sortedMap.put(entry.getKey(), num);
                }
            }
        }

        System.out.println(String.join(" ", sortedMap.keySet()));

    }
}
