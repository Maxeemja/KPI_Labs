/** 
 * A paragraph module.
 * @module paragraph
 */

import Sentence from './sentence.js';

/** Class representing a paragraph. */
export default class Paragraph {
	/**
	 * Crate single paragraph.
	 * @param {String} paragraph 
	 */
	constructor(paragraph) {
		this.paragraph = [];
		this.roll(paragraph);
	}

	roll(paragraphh) {
		try {
			paragraphh.match(/[^\.!\?]+[\.!\?]+/g).forEach((el) => {
				this.paragraph.push(new Sentence(el));
			});
		} catch (e) {
			console.error(`There must be at least one punctuation mark in the paragraph\nError in "${paragraphh}" paragraph;`);
		}

	}
}