import React from 'react';
import { Navbar, Nav, NavDropdown, Form } from 'react-bootstrap'
import { Link, NavLink } from 'react-router-dom'
import { Logout } from "./auth"

const Navb = () => (
	<Navbar bg="light" expand="lg">
	<Navbar.Brand as={Link} to='/'>Quiz-Py</Navbar.Brand>
	<Navbar.Toggle aria-controls="basic-navbar-nav" />
	<Navbar.Collapse id="basic-navbar-nav">
		<Nav className="mr-auto">
			<Nav.Link as={NavLink} to='/' exact>Home</Nav.Link>
			<NavDropdown title="Games" id="basic-nav-dropdown" as={NavLink} to='/games'>
				<NavDropdown.Item as={NavLink} to="/games" exact>My Games</NavDropdown.Item>
				<NavDropdown.Item as={NavLink} to="/games/public">Public Games</NavDropdown.Item>
				<NavDropdown.Divider />
				<NavDropdown.Item as={NavLink} to="/games/create">+ New Game</NavDropdown.Item>
			</NavDropdown>
			<NavDropdown title="Questions" id="basic-nav-dropdown" as={NavLink} to='/questions'>
				<NavDropdown.Item as={NavLink} to="/questions" exact>My Questions</NavDropdown.Item>
				<NavDropdown.Item as={NavLink} to="/questions/public">Public Questions</NavDropdown.Item>
				<NavDropdown.Divider />
				<NavDropdown.Item as={NavLink} to="/questions/create">+ New Question</NavDropdown.Item>
			</NavDropdown>
		</Nav>
		<Form inline>
			<Nav>
				<Nav.Link as={NavLink} to='/login'>Settings</Nav.Link>
				<Logout />
			</Nav>
		</Form>
	</Navbar.Collapse>
	</Navbar>
);

export default Navb;