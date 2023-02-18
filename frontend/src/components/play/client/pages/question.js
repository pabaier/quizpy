import React from 'react';
import { Button } from 'react-bootstrap'

const Question = ({data, sendMessage}) => {

	const onSubmit = e => {
		e.preventDefault();
		const answer = e.target.value;
		sendMessage(answer, 'answer');
	}

	const makeRows = () => {
		if(!data.answers) return;
		var key = 0;
		return data.answers.map(x => (
			<Button key={key++} onClick={onSubmit} value={x} block>{x}</Button>
		));
	}

	return (
		<div>
			{makeRows()}
		</div>
	)
}

export default Question;