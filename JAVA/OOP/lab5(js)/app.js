//відсортувати слова заданного тексту за зростанням кількості голосних у них

import Paragraph from './modules/paragraph.js';
import Sentence from './modules/sentence.js';
/** Class representing a text. */
class Text {
	/**
	 * Create main text.
	 * @param {String} text
	 */
	constructor(text) {
		this.text = text;
		this.resultedText = [];
		this.roll();
 		this.finalArray = this.getFinal(); 
		
	}

	roll() {
		this.text.replace(/[\n\r]/g, '\n ').split('\n').forEach((el) => {
			try {
				this.resultedText.push(new Paragraph(el));
			} catch (err) {
				console.log(err);
			}
		});
	}
	getFinal() {
		const final = [];
		this.resultedText.forEach(({paragraph}) => {
			paragraph.forEach(({pureSentence}) => {
				pureSentence.forEach((word) => {
					final.push(word);
				});
			});
		});
		return final.sort((prev, next) => prev.amount - next.amount);
	}
	printFinal() {
		let finalStr = '';
		this.finalArray.forEach(({word}) => {
			let str = '';
			word.forEach((letter) => {
				str += letter.letter;
			});
		finalStr += str + ' ';
		});
		console.log(finalStr);
	}
}



const input = new Text('FirstWord ipsum dolor sit, amet consectetur. Adipisicing elit. Nostrum aperiam placeat mollitia adipisci iusto eligendi, non nemo aspernatur sapiente possimus, quae, officiis cum dolores deleniti eius. Totam quo corporis iure?\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Nostrum aperiam placeat mollitia adipisci iusto eligendi, non nemo aspernatur sapiente possimus, quae, officiis cum dolores deleniti eius. Totam quo corporis iure?\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Nostrum aperiam placeat molliem ipsum dolor sit, amet consectetur adipisicing elit. Nostrum aperiam placeat mollitia adipisci iusto eligendi, non nemo aspernaturtia adipisci iusto eligendi, non nemo aspernatur sapiente possimus, quae, officiis cum dolores deleniti eius. Totam quo corporis iure?\nLor sapiente possimus, quae. LAST...');

input.printFinal();
console.log(input);


console.log(`%cInput: %c${input.text}`, 'color: red; font-weight: 700; font-size: 20px;', 'color: #f9f9f9');