import React from 'react';
import ReactDOM from 'react-dom';
//import './index.css';
import App from './App/App';
import registerServiceWorker from './registerServiceWorker';

//TODO: remove later
import LoginPage from './Login/LoginPage';

ReactDOM.render(<LoginPage />, document.getElementById('root'));
registerServiceWorker();
