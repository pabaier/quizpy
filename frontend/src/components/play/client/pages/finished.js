import React from 'react';
import { useHistory } from "react-router-dom";
import { Button } from 'react-bootstrap'

const displayFinalResult = (score, rank) => {
	return (
		<div>
			<h1>
				{rank}{placeSuffix(rank)} place{rank === 1 ? '!' : ''}<br />
			</h1>
			<h3>
				Final Score: {score}
			</h3>
		</div>
	)
}

const placeSuffix = (value) => {
	switch (value % 10) {
		case 1:
			return 'st'
		case 2:
			return 'nd'
		case 3:
			return 'rd'
		default:
			return 'th'
	}
}

const Finished = ({ data }) => {
	let history = useHistory();

	const finish = () => {
		history.push(`/`);
	}

	return (
		<div>
			{data.totalScore || data.totalScore >= 0 ? displayFinalResult(data.totalScore, data.rank) : ''}
			<Button size='sm' onClick={finish}>Done</Button>
		</div>
	)
}

export default Finished