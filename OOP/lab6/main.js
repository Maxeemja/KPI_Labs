/* Визначити ієрархію електроприладів. 
Увімкнути деякі електроприлади в розетку. 
Підрахувати споживану потужність. Провести сортування приладів у квартирі на основі потужності. 
Знайти прилад у квартирі, що відповідає заданому діапазону електро-магнітного випромінювання.*/

import {
	Set, Phone, Tablet, Laptop
} from './modules/modules.js';
	
	new Phone(10, 10, true);
	new Tablet(20, 70, true);
	new Phone(30, 40, true);
	new Tablet(50, 60, false);
	new Laptop(80, 90, true);
	new Laptop(30, 100, false);

	const style = 'color: pink; font-weight: 700; font-size: 21px;';
	console.log('%cPowered on devices:', style, Set.setOfDevices);
	console.log('%cFull power consumption:', style, Set.getTotalPower());
	console.log('%cSorted per power:', style, Set.sortPower());
	console.log('%cDevices included in the specified EM radiation interval:', style, Set.sortRad(20, 80));