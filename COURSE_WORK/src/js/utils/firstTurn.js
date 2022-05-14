export function firstTurn () {
  const result = Math.floor(Math.random() * 2);
  return result === 0 ? 'Хрестики' : 'Нулики';
}