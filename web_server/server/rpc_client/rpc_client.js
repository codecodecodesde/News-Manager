var jayson = require('jayson');

var client = jayson.client.http({
  port: 4040,
  hostname: 'localhost'
});

function add(a, b, callback) {
  client.request('add', [a, b], function(err, error, response) {
    if(err) throw err;
    console.log(response);
    callback(response);
  });
}

function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser', [user_id, page_num], function(err, response){
    if(err) throw err;
    console.log(response);
    callback(response.result);
  });
}

function logNewsClickForUser(user_id, news_id) {
  client.request('logNewsClickForUser', [user_id, news_id], function(err, response) {
    if (err) throw err;
    console.log(response);
  });
}

module.exports = {
  add: add,
  getNewsSummariesForUser : getNewsSummariesForUser,
  logNewsClickForUser : logNewsClickForUser
}
