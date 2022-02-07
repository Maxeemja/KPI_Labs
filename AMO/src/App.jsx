import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Lab1 } from './pages/lab1/lab1';
import MainLinks from './components/MainLinks';
function App() {
	return (
		<BrowserRouter basename='/'>
			<div className='container my-8 mx-auto'>
				<p className='text-xl font-bold text-center'>АМО Лабораторні , Грицюк Максим ІО-02</p>
				<MainLinks />
				<Routes>
					<Route exact path='/lab1' element={<Lab1 />} />
					<Route path='/lab2' element={<div>laba2</div>} />
					<Route path='/lab3' element={<Lab1 />} />
					<Route path='/lab4' element={<Lab1 />} />
					<Route path='/lab5' element={<Lab1 />} />
				</Routes>
			</div>
		</BrowserRouter>
	);
}

export default App;
