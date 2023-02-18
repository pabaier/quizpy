import React from 'react';
import Standings from '../../standings'

const Finished = ({data}) => {

	return (
		<Standings data={data} title={'Final Results'}></Standings>
	)
}

export default Finished;