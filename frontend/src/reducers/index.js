import { LOG_IN, LOG_OUT, SET_QUESTIONS, SET_PUBLIC_QUESTIONS, SET_GAMES, SET_ACTIVE_GAME, DEACTIVATE_GAME } from "../constants/action-types";
import { combineReducers } from "redux";

const initialState = {
	user: {
		isLoggedIn: false,
		access: '',
		refresh: '',
	},
	questions: [],
	publicQuestions: [],
	games: [],
	activeGame: null
};

const rootReducer = combineReducers({
	root: appReducer,
})

function appReducer(state = initialState, action) {
	switch (action.type) {
		case LOG_IN:
			return Object.assign({}, state, {
				user: {
					...state.user,
					isLoggedIn: true,
					...action.payload
				}
			})
		case LOG_OUT:
			return Object.assign({}, state, {
				user: {
					...state.user,
					isLoggedIn: false,
					access: '',
					refresh: '',
				}
			})
		case SET_QUESTIONS:
			return Object.assign({}, state, {
				questions: action.payload.results
			})
		case SET_PUBLIC_QUESTIONS:
			return Object.assign({}, state, {
				publicQuestions: action.payload.results
			})
		case SET_GAMES:
			return Object.assign({}, state, {
				games: action.payload.results
			})
		case SET_ACTIVE_GAME:
			return Object.assign({}, state, {
				activeGame: action.payload
			})
		case DEACTIVATE_GAME:
			return Object.assign({}, state, {
				activeGame: null
			})
		default:
			return state;
	}
  }

export default rootReducer;

// function rootReducer(state = initialState, action) {
// 	if (action.type === ADD_ARTICLE) {
// 		return Object.assign({}, state, {
// 			articles: state.articles.concat(action.payload)
// 		});
// 	}
// 	return state;
// };

// function login(state = false, action) {
// 	switch (action.type) {
// 		case LOG_IN:
// 			console.log('*******', state);
// 			return !state;
// 	}
// }

// const rootReducer = (state = initialState, action) => {
// 	console.log('*******', state);
// 	return {
// 		isLoggedIn: login(state.user.isLoggedIn, action),
// 	}
// };