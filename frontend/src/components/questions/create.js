import React, { useState } from 'react';
import { Button, Form, Col } from 'react-bootstrap'

const onSubmit = (e, key) => {
	e.preventDefault();
	const question = e.target.elements.question.value;
	const category = e.target.elements.category.value;
	// list of objects {'option': isAnswer(true/false)}
	var answerOptions = []
	for(var i=0; i < key; i++) {
		var text = e.target.elements[`answerOption-${i}`].value;
		var option = {};
		option[text] = answers[i] ;
		answerOptions.push(option);
	}
	console.log('submit', checked + " " + category + " " + question);
	console.log('answerOptions', answerOptions);
}

const checkChange = (e) => {
	checked = !checked
} 

var checked = false;
var answers = [false]

const Create = () => {

	const markAnswer = (e) => {
		var key = parseInt(e.target.id.split('-')[1])
		answers[key] = !answers[key];
		console.log('answers', answers);
	}

	const [key, setKey] = useState(1)
	const [answerOptions, setAnswerOptions] = useState([
		<Form.Row key={0}>
			<Col>
				<Form.Control type="text" placeholder="answer option" name="answerOption-0" />
			</Col>
			<Col>
				<Form.Check type="checkbox" label="Is Answer" id="isAnswer-0" onChange={markAnswer} />
			</Col>
		</Form.Row>
	]);

	const addAnswerOption = () => {
		setAnswerOptions([...answerOptions, 
			<Form.Row key={key}>
				<Col>
					<Form.Control type="text" placeholder="answer option" name={`answerOption-${key}`} />
				</Col>
				<Col>
					<Form.Check inline type="checkbox" label="Is Answer" id={`isAnswer-${key}`} onChange={markAnswer} />
				</Col>
			</Form.Row>
		]);
		setKey(key + 1);
		answers.push(false);
	}

	const removeAnswerOption = () => {
		if(key <= 0) return;
		var options = [...answerOptions];
		options.pop();
		setAnswerOptions([...options]);
		setKey(key-1);
	}


	return (
		<>
			<h3>Create Question</h3>

			<Form onSubmit={ e => onSubmit(e, key)}>
				<Form.Row>
					<Form.Control type="text" placeholder="question" name="question" />
				</Form.Row>
				<Form.Row>
					<Form.Control type="text" placeholder="category" name="category" />
				</Form.Row>
				<Form.Row>
					<Form.Check type="checkbox" label="Public" id="publicCheck" onChange={checkChange} />
				</Form.Row>
				{ answerOptions }
				<Form.Row>
					<Button variant="primary" onClick={addAnswerOption}>+</Button>
					<Button variant="danger" onClick={removeAnswerOption}>-</Button>
				</Form.Row>
				<Form.Row>
					<Button type="submit">Create Question</Button>
				</Form.Row>

			</Form>
		</>
	);
};

export default Create;