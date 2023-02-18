import React from 'react';
import { connect } from "react-redux";
import { postLogIn } from "../../actions/auth";
import LoginForm from "./loginForm";
import { useHistory } from "react-router-dom";

const mapStateToProps = state => {
	return { isLoggedIn: state.root.user.isLoggedIn };
}

const ConnectedLogin = ( {isLoggedIn, dispatch} ) => {
	let history = useHistory();

	const loginSubmit = creds => {
		dispatch(postLogIn({
			creds,
			loginSuccess
		}));
	}

	const loginSuccess = () => {
		history.push("/");
	}

	return (
		<div>
			<h2>Login</h2>
			<br />
			<LoginForm handleSubmit={loginSubmit} />
		</div>
	);
};

const Login = connect(mapStateToProps)(ConnectedLogin)

export default Login;