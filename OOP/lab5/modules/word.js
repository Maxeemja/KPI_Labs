/**
 * Word module.
 * @module word
 */
import Letter from './letter.js';
const golosni = ["a", "e", "y", "u", "i", "o", "A", "E", "Y", "U", "I", "O"];
/** Class representing a single word in a sentence. */
export default class Word {
  /**
   * Create a word.
   * @param {String} word
   */
  constructor(word) {
    this.word = word.split('').map(el => {
      return new Letter(el);
    });
    this.amount = this.getAmount(word);
  }

  getAmount(word) {
    let counter = 0;
    for (let letter of word) {

      if (golosni.includes(letter)) {
        counter++;
      }
    }
    return counter;
  }
}