import React from 'react';
import { connect } from "react-redux";
import { Route, Redirect } from "react-router-dom";

const mapStateToProps = state => {
	return { isLoggedIn: state.root.user.isLoggedIn };
}

const ConnectedPrivateRoute = ( {component: Component, isLoggedIn, dispatch, ...rest} ) => {
	return (
	<Route {...rest} render={(props) => (
		isLoggedIn
		  ? <Component {...props} />
		  : <Redirect to='/login' />
	  )} />
	)
};

const PrivateRoute = connect(mapStateToProps)(ConnectedPrivateRoute)

export default PrivateRoute;