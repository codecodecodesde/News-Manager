import Base from './Base/Base';
import React from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter as Router  } from 'react-router-dom';

ReactDOM.render(<Router><Base /></Router>, document.getElementById('root'));
registerServiceWorker();