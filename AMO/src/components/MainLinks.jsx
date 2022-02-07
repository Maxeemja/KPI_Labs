import { LabLink } from './LabLink';
const MainLabLinks = () => {
	return (
		<div className='flex justify-between my-8'>
			<LabLink to='/lab1' className="p-2">
				Лабораторна робота №1
			</LabLink>
			<LabLink to='/lab2' className="p-2">
				Лабораторна робота №2
			</LabLink>
			<LabLink to='/lab3' className="p-2">
				Лабораторна робота №3
			</LabLink>
			<LabLink to='/lab4' className="p-2">
				Лабораторна робота №4
			</LabLink>
			<LabLink to='/lab5' className="p-2">
				Лабораторна робота №5
			</LabLink>
		</div>
	);
};

export default MainLabLinks;
