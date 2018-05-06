import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.min.js';

import React from 'react';
import App from '../App/App';
import LoginPage from '../Login/LoginPage';
import SignUpPage from '../SignUp/SignUpPage';
import Auth from '../Auth/Auth';
import { BrowserRouter as Router, Route, Link, withRouter  } from 'react-router-dom';

import './Base.css';

const logout = (history) => {
  Auth.deauthenticateUser();
  history.push('/login');
};

const Base = withRouter(({ history }) => (
    <div>
      <nav className="nav-bar indigo lighten-1">
        <div className="nav-wrapper">
          <ul id="nav-mobile" className="right">
            {Auth.isUserAuthenticated() ?
              (<div>
                <li>{Auth.getEmail()}</li>
                <li><a onClick={()=>{history.push('/login');}}>Log out</a></li>
              </div>)
              :
              (<div>
                <li><Link to="/login">Log in</Link></li>
                <li><Link to="/signup">Sign up</Link></li>
              </div>)
            }
          </ul>
        </div>
      </nav>
      <br/>
      <Route exact path="/" render={() => (Auth.isUserAuthenticated() ?
        (<App />) : (<LoginPage />))}/>
      <Route exact path="/login" component={LoginPage} />
      <Route exact path="/signup" component={SignUpPage} />
    </div>
));

export default Base;
