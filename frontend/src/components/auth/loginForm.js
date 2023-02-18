import React from 'react';
import { Button, Form } from 'react-bootstrap'


const onSubmit = (e, handleSubmit) => {
	e.preventDefault();
	const username = e.target.elements.username.value;
	const password = e.target.elements.password.value;
	handleSubmit({username, password})
}

const LoginForm = props => {
	const { handleSubmit } = props
	return (
		<Form onSubmit={ e => onSubmit(e, handleSubmit)}>
				<Form.Control type="text" placeholder="username" name="username" />
				<Form.Control type="password" placeholder="password" name="password" />
				<Button type="submit">Login</Button>
		</Form>
	)
}

export default LoginForm;
