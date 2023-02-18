import React from 'react';
import { connect } from "react-redux";
import { getPublicQuestions } from "../../actions/questions"
import { Button } from 'react-bootstrap'

const mapStateToProps = state => {
	return { questions: state.root.publicQuestions };
}

const connectedPublicQuestions = ( {questions, dispatch} ) => {
	const listItems = questions.map( (q) => (
		<li key={'q'+q.id}>{q.text}
			<ul>
				{
					q.answerOptions.map( (a) => (
						<li key={'a'+a.id}>{a.option} {a.isAnswer? "*" : ""}</li>
					))
				}
			</ul>
		</li>
	));

	return (
		<div>
			<h2>Public Questions</h2>
			<ul>
				{ listItems }
			</ul>
			<br />
			<Button onClick={ () => { dispatch(getPublicQuestions()) } }>Get Public Questions</Button>
		</div>
	);
};

const PublicQuestions = connect(mapStateToProps)(connectedPublicQuestions)

export default PublicQuestions;