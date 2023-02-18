import React from 'react';
import { connect } from "react-redux";
import { logOut } from "../../actions/auth";
import { useHistory } from "react-router-dom";
import { Button } from 'react-bootstrap'

const ConnectedLogout = ( {dispatch} ) => {
	let history = useHistory();

	const logoutSubmit = () => {
		dispatch(logOut()).then(() => {
			logoutSuccess();
		});
	}

	const logoutSuccess = () => {
		history.push("/");
	}

	return (
		<Button className="btn-sm" variant="outline-success" onClick={() => logoutSubmit()}>Logout</Button>
	);
};

const Logout = connect()(ConnectedLogout)

export default Logout;