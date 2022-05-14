import { UI } from '../UI';
import { highlightCells } from './higlight';
export const checkGrid = () => {
	let combo = [];
	const rows = [[...UI.cells].slice(0, 3), [...UI.cells].slice(3, 6), [...UI.cells].slice(6)];
	const column1 = [[...UI.cells].filter((el) => ['0', '3', '6'].includes(el.id))];
	const column2 = [[...UI.cells].filter((el) => ['1', '4', '7'].includes(el.id))];
	const column3 = [[...UI.cells].filter((el) => ['2', '5', '8'].includes(el.id))];
	const columns = [...column1, ...column2, ...column3];
	const diagonals = [
		[...UI.cells].filter((el) => ['0', '4', '8'].includes(el.id)),
		[...UI.cells].filter((el) => ['2', '4', '6'].includes(el.id))
	];

	rows.forEach((row) => {
		if (row.every((el) => el.textContent === 'O') || row.every((el) => el.textContent === 'X')) {
			combo.push('РЯДОК');
			return highlightCells(row);
		}
	});
	columns.forEach((column) => {
		if (
			column.every((el) => el.textContent === 'O') ||
			column.every((el) => el.textContent === 'X')
		) {
			combo.push('СТОВПЕЦЬ');
			return highlightCells(column);
		}
	});
	diagonals.forEach((diagonal) => {
		if (
			diagonal.every((el) => el.textContent === 'O') ||
			diagonal.every((el) => el.textContent === 'X')
		) {
			combo.push('ДІАГОНАЛЬ');
			return highlightCells(diagonal);
		}
	});
	if ([...UI.cells].every((el) => el.textContent !== '' && combo.length === 0)) {
		return 'DRAW';
	}
	return combo;
};
