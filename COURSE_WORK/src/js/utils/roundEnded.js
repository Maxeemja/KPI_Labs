import { UI } from '../UI';
export const roundEnded = (result, side) => {
	if (result !== 'DRAW') {
		UI.currentTurnMessage.textContent = `${side} виграли!`;
		if (side === 'Хрестики') {
			UI.firstPlayerWins.textContent = +UI.firstPlayerWins.textContent + 1;
		} else {
			UI.secondPlayerWins.textContent = +UI.secondPlayerWins.textContent + 1;
		}
	} else {
		UI.currentTurnMessage.textContent = `Ніхто не виграв...`;
		UI.draws.textContent = +UI.draws.textContent + 1;
	}
	UI.info.textContent = result !== 'DRAW' ? `${result.join(' + ')} combo` : 'НІЧИЯ';
};
