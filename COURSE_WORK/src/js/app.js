import '../scss/reset.scss';
import '../scss/style.scss';
import { UI } from './UI';
import { firstTurn } from './utils/firstTurn';
import { handleTurn } from './utils/handleTurn';
import { checkGrid } from './utils/checkGrid';
import { highlightName } from './utils/higlight';
import { reset } from './utils/reset';
import { newGame } from './utils/newGame';
import { roundEnded } from './utils/roundEnded';

UI.firstPlayerName.textContent = 'Гравець 1';
UI.secondPlayerName.textContent = 'Гравець 2';
UI.resetButton.addEventListener('click', reset);
UI.newGameButton.addEventListener('click', newGame);
export const roundStart = () => {
	const init = firstTurn();
	let currentTurn = init;
	UI.currentTurnMessage.textContent = `${init} починають`;
	highlightName(currentTurn);
	UI.gridContainer.addEventListener('click', fillCell);
	function fillCell(event) {
		if (!event.target.textContent && event.target.id) {
			handleTurn(event.target, currentTurn);
			if (checkGrid().length) {
				UI.gridContainer.removeEventListener('click', fillCell);
				return roundEnded(checkGrid(), currentTurn);
			}
			currentTurn = currentTurn === 'Хрестики' ? 'Нулики' : 'Хрестики';
			UI.currentTurnMessage.textContent = `${currentTurn} ходять!`;
			highlightName(currentTurn);
		}
	}
};
roundStart();