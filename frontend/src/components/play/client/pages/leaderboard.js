import React from 'react';

const displayTotalScore = (score, rank, team) => {
	return (
		<div>
			You are in {rank}{placeSuffix(rank)} place{rank === 1 ? '!' : ''}<br />
			{team ? <span>Team: {team}<br /></span> : ''}
			Total Score: {score}
		</div>
	)
}

const displayRoundScore = (result) => {
	return (
		<div>
			Last Round:<br />
			<div style={{ paddingLeft: '100px' }}>
				Answer: {result.answer}<br />
				Correct: {result.correct ? "Yes!" : "No"}<br />
				Score: {result.score}<br />
				Time: {result.time}
			</div>
		</div>
	);
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

const Leaderboard = ({ data }) => {

	return (
		<div>
			<h5>{data.totalScore || data.totalScore >= 0 ? displayTotalScore(data.totalScore, data.rank, data.team) : ''}</h5>
			<h5>{data.roundResult ? displayRoundScore(data.roundResult) : ''}</h5>
		</div>
	)
}

export default Leaderboard