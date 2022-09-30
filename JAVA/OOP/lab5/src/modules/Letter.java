package modules;

public class Letter {
    final char letter;

    public Letter(char letter) {
        this.letter = letter;
    }

    @Override
    public String toString() {
        return String.valueOf(letter);
    }
}