import { roundStart } from '../app';
import { UI } from '../UI';

export const reset = () => {
	UI.cells.forEach((el) => {
		el.textContent = '';
    el.style.backgroundColor = ''; 
	});
  UI.info.textContent = 'Натисніть на клітинку щоб грати';
  roundStart();
};
