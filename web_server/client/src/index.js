import React from 'react';
import ReactDOM from 'react-dom';
//import './index.css';
import App from './App/App';
import registerServiceWorker from './registerServiceWorker';

//TODO: remove later
import SignUpPage from './SignUp/SignUpPage';

ReactDOM.render(<SignUpPage />, document.getElementById('root'));
registerServiceWorker();
