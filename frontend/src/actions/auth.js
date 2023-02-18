import { LOG_IN, LOG_OUT } from "../constants/action-types";
import * as api from './api';

const baseURL = process.env.REACT_APP_BASE_URL;

export function logIn(payload) {
	return { type: LOG_IN, payload}
}

export function logOut(payload) {
	return function (dispatch) {
		return new Promise((resolve, reject) => {
			dispatch( {type: LOG_OUT, payload} )
			resolve();
		})
}}

const handleError = (e) => {
	throw Error(e.statusText)
}

export function postLogIn(payload) {
	return function(dispatch, getState) {
		api.postData(baseURL + 'auth/jwt-token/', payload.creds)
		.then(res => res.ok? res.json() : handleError(res))
		.then((data) => {
			dispatch(logIn(data));
			payload.loginSuccess()
		})
		.catch(console.log);
	}
};