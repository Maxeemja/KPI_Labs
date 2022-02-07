import { useFormik } from 'formik';
import { useState } from 'react';
import { Button, TextField } from '@mui/material';
import taskImg from '../../assets/lab1/task2.png'
export const Alg2 = () => {
	const [result, setResult] = useState();
	const formik = useFormik({
		initialValues: {
			a: '',
			b: '',
			c: '',
			d: ''
		},
		onSubmit: ({ a, b, c, d }) => {
			console.log(a);
			if (!a || !b || !c || !d) {
				formik.resetForm();
				return alert('Перевірте введені дані!');
			}

			if (a < 0 || b < 0 || c < 0 || d < 0) {
				formik.resetForm();
				return alert('а та b, а також c або d мають бути більшими за нуль');
			}
			formik.resetForm();
			setResult(
				((Math.sqrt(a) + b * b) / (Math.sqrt(b) - a * a) + Math.sqrt((a * b) / (c * d))).toFixed(3)
			);
		}
	});

	return (
		<div className='flex justify-between gap-10'>
			<div className=''>
				<p className='font-semibold mb-3'>Варіант завдання:</p>
				<img src={taskImg} alt='' />
			</div>

			<form className='flex gap-10' onSubmit={formik.handleSubmit}>
				<div className='flex flex-col gap-5'>
					<h2 className='text-center my-4 text-xl'>Задайте значення</h2>
					<TextField
						fullWidth
						id='a'
						name='a'
						label='a'
						type='number'
						value={formik.values.a}
						onChange={formik.handleChange}
					/>
					<TextField
						fullWidth
						id='b'
						name='b'
						label='b'
						type='number'
						value={formik.values.b}
						onChange={formik.handleChange}
					/>
					<TextField
						fullWidth
						id='c'
						name='c'
						label='c'
						type='number'
						value={formik.values.c}
						onChange={formik.handleChange}
					/>
					<TextField
						fullWidth
						id='d'
						name='d'
						label='d'
						type='number'
						value={formik.values.d}
						onChange={formik.handleChange}
					/>
				</div>
				<div className='flex flex-col justify-center items-center'>
					<p className='text-center font-bold mb-3'>{result}</p>
					<Button color='primary' variant='contained' fullWidth type='submit'>
						Результат!
					</Button>
				</div>
			</form>
			<div className='w-1/4'>
				<p>Блок-схема</p>
				{/* <img src={} alt='' /> */}
			</div>
		</div>
	);
};
