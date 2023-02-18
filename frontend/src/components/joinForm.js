import React from 'react';
import { Button, Col, Form } from 'react-bootstrap'
import { useHistory } from "react-router-dom";

const JoinForm = props => {
	let history = useHistory();
	
	const onSubmit = (e) => {
		e.preventDefault();
		const gameToken = e.target.elements.gameToken.value;
		history.push(`/play/join/${gameToken}`);
	}

	return (
		<Form onSubmit={ e => onSubmit(e)}>
			<Form.Row >
					<Col>
						<Form.Control type="text" name="gameToken" placeholder="Enter Game ID" />
					</Col>
					<Col>
						<Button className="show-grid text-left" type="submit">Join Game</Button>
					</Col>
			</Form.Row>
		</Form>
	)
}

export default JoinForm;
