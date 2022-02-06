import { Button, getBreadcrumbsUtilityClass } from '@mui/material';
import TextField from '@mui/material/TextField';
import './alg1.scss';
import { useState } from 'react';
const Algorythm1 = () => {
	const initialState = {
		a: '',
		b: '',
		c: '',
		d: '',
		result: null,
		isResultCalculated: false
	};
	const [state, setState] = useState(initialState);
	const { a, b, c, d, result, isResultCalculated } = state;
	const res = (Math.sqrt(a) + b * b) / (Math.sqrt(b) - a * a) + Math.sqrt((a * b) / (c * d));

	const getResult = (e) => {
		e.preventDefault();
		setState({ ...initialState, result: res.toFixed(3), isResultCalculated: true });
	};
	return (
		<div className='task1'>
			<div className='column'>
				<img src='https://picsum.photos/200/300' alt='' />
			</div>
			<div className='column'>
				<form onSubmit={getResult}>
					<div className='row'>
						<TextField
							type='number'
							required
							margin='dense'
							id='outlined-basic'
							label='1ше число'
							value={a}
							onChange={(e) => setState({ ...state, isResultCalculated: false, a: e.target.value })}
							variant='outlined'
						/>
						<TextField
							type='number'
							required
							margin='dense'
							id='outlined-basic'
							label='2ге число'
							value={b}
							onChange={(e) => setState({ ...state, isResultCalculated: false, b: e.target.value })}
							variant='outlined'
						/>
					</div>
					<div className='row'>
						<TextField
							type='number'
							required
							margin='dense'
							id='outlined-basic'
							value={c}
							label='3тє число'
							onChange={(e) => setState({ ...state, isResultCalculated: false, c: e.target.value })}
							variant='outlined'
						/>
						<TextField
							type='number'
							required
							margin='dense'
							id='outlined-basic'
							label='4те число'
							value={d}
							onChange={(e) => setState({ ...state, isResultCalculated: false, d: e.target.value })}
							variant='outlined'
						/>
					</div>
					<div className='row'>
						{isResultCalculated ? <div className='result'>{result}</div> : null}
						<Button type='submit' variant='contained'>
							Результат!
						</Button>
					</div>
				</form>
			</div>
		</div>
	);
};
export default Algorythm1;
