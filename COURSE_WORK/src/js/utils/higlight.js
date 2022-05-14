import { UI } from '../UI';

export const highlightName = (currentPlayer) => {
	if (currentPlayer === 'Хрестики') {
		UI.firstPlayerName.classList.add('highlighted');
		UI.secondPlayerName.classList.remove('highlighted');
	} else {
		UI.secondPlayerName.classList.add('highlighted');
		UI.firstPlayerName.classList.remove('highlighted');
	}
};
export const highlightCells = (arr) => {
  return arr.forEach(el => { 
    el.style.backgroundColor = 'violet' 
  });
}