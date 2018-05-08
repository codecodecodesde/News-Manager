var auth = require('./routes/auth');
var bodyParser = require('body-parser');
var cors = require('cors');
var express = require('express');
var passport = require('passport');
var path = require('path');

var index = require('./routes/index');
var news = require('./routes/news');

var app = express();

app.use(bodyParser.json());

var config = require('./config/config.json');

require('./models/main.js').connect(config.mongoDbUri);

var authChecker = require('./auth/auth_checker');

// load passport strategies.
app.use(passport.initialize());
passport.use('local-signup', require('./auth/signup_local_strategy'));
passport.use('local-login', require('./auth/login_local_strategy'));

// view engine setup
app.set('views', path.join(__dirname, '../client/build'));
app.set('view engine', 'jade');
app.use('/static', express.static(path.join(__dirname, '../client/build/static')));

// TODO: remove this after development is done
app.use(cors());

app.use('/', index);
app.use('/auth', auth);
app.use('/news', authChecker);
app.use('/news', news);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});

module.exports = app;
