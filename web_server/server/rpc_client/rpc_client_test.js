var client = require('./rpc_client');

//invoke add function
client.add(1, 2, function(response) {
  console.assert(response == 3);
})

// invoke "getNewsSummariesForUser"
client.getNewsSummariesForUser('test_user', 1, function(response) {
  console.assert(response != null);
})

// invokde "logNewsClickForUser"
client.logNewsClickForUser('test_user', 'nmuYSK3LFDb7SY727Ibonw==\n');
