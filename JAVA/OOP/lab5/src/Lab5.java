import modules.Word;
import java.util.*;
import java.util.stream.Collectors;


public class Lab5 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Введіть ваш текст: ");
        final StringBuilder initStr = new StringBuilder(sc.nextLine());
        sc.close();
        ArrayList<Word> list = new ArrayList<>(Collections.emptyList()); // основний ліст зі словами для збереження каунтера голосних для кожного слова в реченні

        //split по регулярочці для розбиття на слова  по символам '!', '.', '?' та пробілам
        for (String w : initStr.toString().split("[.?! ]\\s*")) {
            if(Objects.equals(w, "")) {
                continue;
            }
            Word word = Word.toWord(w);
            list.add(word);
        }
        String sortedWords = list.stream().sorted(Comparator.comparingInt(Word::amount)).map(Object::toString).collect( Collectors.joining(" "));;
        System.out.println(sortedWords);
    }
}
