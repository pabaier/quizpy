import { SET_ACTIVE_GAME, DEACTIVATE_GAME} from "../constants/action-types";
import * as api from "./api"

const baseURL = process.env.REACT_APP_BASE_URL;

const handleError = (e) => {
	throw Error(e.statusText)
}

export function activateGame(gameId) {
	return function(dispatch, getState) {
		return new Promise((resolve, reject) => {
			api.getData(baseURL + `play/host/${gameId}/`, getState().root.user.access)
			.then(res => res.ok? res.json() : handleError(res))
			.then((data) => {
				dispatch(setActiveGame(data));
				resolve(data);
			})
			.catch(console.log);
		})
	}
}

function setActiveGame(payload){
	return { type: SET_ACTIVE_GAME, payload}
}

export function deactivateGame() {
	return { type: DEACTIVATE_GAME}
} 