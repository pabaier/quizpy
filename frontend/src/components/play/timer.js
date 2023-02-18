import React, {useState, useEffect} from 'react';

const Timer = ({time, sendMessage, startTime}) => {
	// use one state variable for all variables so when any values change the timer only renders once
	const [vars, setVars] = useState({'timeLeft': time, 'startTime': startTime})

	const calculateTimeLeft = () => {
		// when the clock hits 0, tell the host to grab the next state
		if(vars.timeLeft < 1)
			stop()
		// re-renders the timer with the new time but not after it stops
		else
			setVars({...vars, 'timeLeft': vars.timeLeft - 1});
	}

	useEffect(() => {
		// startTime indicates if the page was rendered from the host or re-rendered internally
		// if the timer is re-rendered internally, startTime will not change because it is set when
		// the component renders in the host
		// 
		// if the startTime changed that means this is a new render from the host, so reset the local state
		// to the new state values
		if(startTime !== vars.startTime) {
			setVars({'timeLeft': time, 'startTime': startTime});
		}
		// if the startTime did not change, then this is an internal render so start the timer
		else {
			const timer = setTimeout(() => {
				calculateTimeLeft();
			}, 1000);
			return () => {clearTimeout(timer);};
		}
	  });

	const stop = () => {
		sendMessage('stop');
	}

	return (
		<div>
			<div>{vars.timeLeft}</div>
		</div>
	)
}

export default Timer;