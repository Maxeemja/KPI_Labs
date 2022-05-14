export const handleTurn = (target, current) => {
	const cross = 'X';

	const nougth = 'O';

	target.textContent = current === 'Хрестики' ? cross : nougth;
};
