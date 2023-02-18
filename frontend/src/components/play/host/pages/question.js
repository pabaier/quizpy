import React from 'react';
import { Button } from 'react-bootstrap'

const Question = ({data}) => {

	const makeRows = () => {
		if(!data.answers) return;
		var key = 0;
		return data.answers.map(x => (
			<Button key={key++} value={x} block disabled>{x}</Button>
		));
	}

	return (
		<div>
			<h3>{data.text ? data.text : ''}</h3>
			{makeRows()}
		</div>
	)
}

export default Question;