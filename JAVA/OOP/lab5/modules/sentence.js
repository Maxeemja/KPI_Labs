/**
 * Sentence module.
 * @module sentence
 */

import Word from './word.js';
import Punctuation from './punctuation.js';

/** Class representing one sentence. */
export default class Sentence {
	/**
	 * Create a sentence.
	 * @param {String} sentence
	 */
	constructor(sentence) {
		this.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '.split('') + ['...'];
		this.sentence = [];
		this.roll(sentence);
		this.pureSentence = this.sentence.filter((value) => !(value instanceof Punctuation));
/* 		this.FinalArray = this.getFinalArray(); */
	}
	roll(sentence) {
		sentence.match(/[\w']+|[.,!?;_ ]/g).forEach((el) => {
			if (this.punctuation.includes(el)) {
				this.sentence.push(new Punctuation(el));
				return;
			}
			this.sentence.push(new Word(el));
		});
	}
/* 	getFinalArray(){
		const finalarr = [];
		this.pureSentence.forEach((word)=> {
			finalarr.push(word);
			return finalarr.sort((prev, next) => prev.amount - next.amount)
		});
	} */

}