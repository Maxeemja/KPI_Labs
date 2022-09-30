package modules;

public class Word {
    private static final String vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ";

    final Letter[] letters;
    public int amount;

    public Word(Letter[] letters) {
        this.letters = letters;
        amount = this.getAmount(letters);
    }

    public int amount(){
        return this.amount;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (Letter letter : letters) {
            builder.append(letter);
        }
        return builder.toString();
    }

    public static Word toWord (String w) {
        Letter[] letters = new Letter[w.length()];
        for (int j = 0; j < letters.length; j++) {
            letters[j] = new Letter(w.charAt(j));
        }
        return new Word(letters);
    }

    public int getAmount(Letter[] letters) {
        int counter = 0;
        for(Letter letter : letters) {
            if (vowels.contains(letter.toString())) {
                counter++;
            }
        }
        return counter;
    }

}