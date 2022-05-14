import { UI } from '../UI';
import { reset } from './reset';

export const newGame = () => {
	reset();
	UI.firstPlayerWins.textContent = '0';
	UI.secondPlayerWins.textContent = '0';
	UI.draws.textContent = '0';
};
