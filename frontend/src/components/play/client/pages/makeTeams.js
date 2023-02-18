import React from 'react';

const MakeTeams = ({data}) => {

	return (
		<div>
			{
				data.team?
					<div>
						<center>
							Team
							<br/>
							<h1>{data.team}</h1>
						</center>
					</div>
				: ''
			}
		</div>
	)
}

export default MakeTeams;