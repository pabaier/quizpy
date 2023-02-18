import React, { useState, useEffect } from 'react';

const Registration = ({data, pin}) => {
	const [players, setPlayers] = useState([]);

	useEffect(() => {
		if(data.name)
			setPlayers([...players, data.name])
	}, [data.name]);

	var printPlayers = () => {
		return players.map( (value, index) => (
			<li key={index}>{value}</li>
		))
	}

	return (
		<div>
			<h5>Game pin: {pin}</h5>
			<h1>Players</h1>
			<ul>
				{printPlayers()}
			</ul>
		</div>
	)
}

export default Registration;