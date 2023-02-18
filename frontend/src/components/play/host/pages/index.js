import React from 'react';
import * as state from '../../state';
import Registration from './registration';
import Question from './question';
import Leaderboard from './leaderboard';
import Finished from './finished';
import MakeTeams from './makeTeams';
import Hook from './hook';

const Page = (props) => {
	switch (props.currentState) {
		case state.STANDBY:
			return <div>Stand By</div>;
		case state.HOOK:
			return <Hook {...props} />;
		case state.REGISTRATION:
			return <Registration {...props} />;
		case state.MAKE_TEAMS:
			return <MakeTeams {...props} />;
		case state.QUESTION:
			return <Question {...props} />;
		case state.LEADERBOARD:
			return <Leaderboard {...props} />;
		case state.GAME_OVER:
			return <div>Game Over</div>;
		case state.FINISHED:
			return <Finished {...props} />;
		default:
			return <div>Default</div>;
	}
}

export default Page;