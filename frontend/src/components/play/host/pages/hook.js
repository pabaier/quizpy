import React from 'react';

const Hook = ({data}) => {

	const h1 = () => {return data.h1 ? <h1>{data.h1}</h1> : ''}
	const h3 = () => {return data.h3 ? <h3>{data.h3}</h3> : ''}
	const h5 = () => {return data.h5 ? <h5>{data.h5}</h5> : ''}
	const p = () => {return data.p ? <p>{data.p}</p> : ''}


	return (
		<div>
			{h1()}
			{h3()}
			{h5()}
			{p()}
		</div>
	)
}

export default Hook;