import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Navb from './components/Navb';
import PrivateRoute from './components/PrivateRoute';
import Splash from './components/Splash'
import { Games, PublicGames, GamePage, Create as CreateGame } from './components/games'
import { Questions, PublicQuestions, Create as CreateQuestion } from "./components/questions";
import { Host, Client } from "./components/play";

const App = () => {
  return (
    <div>
      <Router>
        <div>
          <Switch>
            <Route path="/login">
              <Splash />
            </Route>
            <Route path="/play/join/:token" component={Client} />
            <PrivateRoute path="/" component={LoggedIn} />
          </Switch>
        </div>
      </Router>
    </div>
  )
}

const LoggedIn = () => (
  <div>
    <Navb />
    <Switch>
      <Route exact path="/games" component={Games} />
      <Route path="/games/create" component={CreateGame} />
      <Route path="/games/:id" component={GamePage} />
      <Route path="/games/public" component={PublicGames} />

      <Route exact path="/questions" component={Questions} />
      <Route path="/questions/public" component={PublicQuestions} />
      <Route path="/questions/create" component={CreateQuestion} />

      <Route path="/play/host/:id" component={Host} />
      <Route exact path="/" component={Home} />
    </Switch>
  </div>
)

const Home = () => {
  return <h2>Home</h2>;
}

export default App;