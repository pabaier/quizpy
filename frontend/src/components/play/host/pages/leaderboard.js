import React from 'react';
import Standings from '../../standings'

const Leaderboard = ({data}) => {
	return (
		<Standings data={data} title={'Standings'}></Standings>
	)
}

export default Leaderboard;