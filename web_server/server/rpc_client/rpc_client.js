var jayson = require('jayson');

// create a client
var client = jayson.client.http({
  port: 4040,
  hostname: 'localhost'
});

// Test method.
function add(a, b, callback) {
  client.request('add', [a, b], function(err, response) {
    if (err) throw err;
    console.log(response.result);
    callback(response.result);
  });
}


// Get news summaries for a user.
function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser', [user_id, page_num], function(err, response) {
    if (err) throw err;
    console.log(response.result);
    callback(response.result);
  });
}


// Log a news click event for a user.
function logNewsClickForUser(user_id, news_id) {
  client.request('logNewsClickForUser', [user_id, news_id], function(err, response) {
      if (err) throw err;
      console.log(response);
  });
}


module.exports = {
  add : add,
  getNewsSummariesForUser : getNewsSummariesForUser,
  logNewsClickForUser : logNewsClickForUser
}
