import React, { useEffect } from 'react';
import { connect } from "react-redux";
import { useParams } from 'react-router-dom'
import { getGame } from "../../../actions/games"
import Game from "./game"

const mapStateToProps = state => {
	return { games: state.root.games };
}

const ConnectedGame = ( {games, dispatch}) => {
	let { id, numId=+id } = useParams()
	useEffect(() => {
		dispatch(getGame());
	}, [dispatch]);
	const game = games.filter(g => {
		return g.id === numId
	  })[0]
	if (game) {
		return (
			<div>
				<h2>{game.name}</h2>
				<Game game={game}></Game>
			</div>
		);
	}
	return <h2> No Games </h2>;
  }

const GamePage = connect(mapStateToProps)(ConnectedGame)

export default GamePage;