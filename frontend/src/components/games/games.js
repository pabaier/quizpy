import React, { useEffect } from 'react';
import { connect } from "react-redux";
import { getGames } from "../../actions/games"
import { ListGroup, Button, Container, Row, Col, Dropdown, SplitButton } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { useHistory } from "react-router-dom";

const mapStateToProps = state => {
	return { games: state.root.games };
}

const ConnectedGames = ( {games=[], dispatch} ) => {
	useEffect(() => {
		dispatch(getGames());
	}, [dispatch]);

	let history = useHistory();

	const navigateToGame = (gameId, teamNumber) => {
		history.push({
			pathname: `/play/host/${gameId}`,
			teamNumber
		})
	}

	const dropdown = (gameId) => {
			let a = [<Dropdown.Item disabled={true} key={1}>Select Number of Teams</Dropdown.Item>]
			for(let i = 2; i<=20; i++ ) {
				a.push(
					<Dropdown.Item name="time" key={i} onSelect = { () => navigateToGame(gameId, i)}>{i}</Dropdown.Item>
				)
			}
			return a
	}

	const listItems = games.map( (g, index) => {

		return (
		<ListGroup.Item key={'g'+g.id}
			variant={index%2===0 ? 'light' : null}
		>
			<Link to={`/games/${g.id}`}>
				{g.name} - {g.questions.length} questions
			</Link>
				<Container>
					<Row>
						<Col>
								<SplitButton variant="outline-info" title='Team Game' drop={'down'} onClick={() => navigateToGame(g.id, 2)}>
									{dropdown(g.id)}
								</SplitButton>
						</Col>
						<Col>
								<Button  variant="outline-warning"	 onClick={() => navigateToGame(g.id, 0) } >
									play individual
								</Button>
						</Col>
					</Row>
				</Container>
		</ListGroup.Item>)
	});

	return (
		<div>
			<h2>Games</h2>
			<ListGroup defaultActiveKey="#link1">
					{listItems}
			</ListGroup>
		</div>
	);
};

const Games = connect(mapStateToProps)(ConnectedGames)

export default Games;