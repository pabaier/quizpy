import React, { useEffect } from 'react';
import { connect } from "react-redux";
import { getQuestions } from "../../actions/questions"
import Question from "./question"
import { Container, Row, Col, CardDeck } from 'react-bootstrap';

const mapStateToProps = state => {
	return { questions: state.root.questions };
}

const ConnectedQuestions = ( {questions=[], dispatch} ) => {
	useEffect(() => {
		dispatch(getQuestions());
	}, [dispatch]);

	const listItems = questions.map( (q) => (
		<Col key={"cq" + q.id}>
			<Question question={q} />
		</Col>
	));

	return (
		<div>
			<h3>Questions</h3>
			<Container>
				<Row>
					<CardDeck>
						{listItems}
					</CardDeck>
				</Row>
			</Container>
		</div>
	);
};

const Questions = connect(mapStateToProps)(ConnectedQuestions)

export default Questions;