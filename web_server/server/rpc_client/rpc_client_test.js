var client = require('./rpc_client');

//invoke add function
client.add(1, 2, function(response) {
  console.assert(response == 3);
})
