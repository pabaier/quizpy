import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { REGISTRATION } from '../state';
import Page from './pages';

const Client = () => {
	let { token } = useParams()
	const [state, setState] = useState(REGISTRATION);
	const [data, setData] = useState({});
	const [ws, setWs] = useState(null);

	useEffect(() => {
		if (!ws) {
			setWs(new WebSocket(process.env.REACT_APP_WS_BASE_URL + `ws/join/${token}/`))
		}

		return function cleanup() {
			if (ws) {
				ws.close();
			}
		}
	}, [ws, token]);

	const sendMessage = (data, type) => {
		try {
			ws.send(JSON.stringify({
				'data': data,
				'type': type,
			}));
		} catch (error) {
			console.log(error);
		}
	}

	if (!ws) {
		return (<div></div>)
	}

	ws.onmessage = e => {
		const receivedData = JSON.parse(e.data);
		setState(receivedData.state);
		setData({ ...receivedData.data });
	}

	ws.onclose = () => {
		console.log('disconnected')
		// automatically try to reconnect on connection loss
	}

	const packageData = {
		currentState: state,
		data,
		sendMessage,
	}

	return (
		<div>
			<Page {...packageData}></Page>
		</div>
	);
};

export default Client;