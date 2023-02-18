import React from 'react';
import { ListGroup } from 'react-bootstrap';

const Answers = ( {answers} ) => {
	let i = 0;
	const listItems = answers.map( (a) => {
		i = i + 1;
		if(i>3){i=0}
		return (
			<ListGroup.Item
				key={'a'+a.id}
				variant={i%4===0 ? 'warning' : i%3===0 ? 'info' : i%2===0 ? 'secondary' : null}
			>
				{a.option} {a.isAnswer? "*" : ""}
			</ListGroup.Item>
		)
	});

	return (
		<ListGroup>
			{ listItems }
		</ListGroup>
	);
}

export default Answers
