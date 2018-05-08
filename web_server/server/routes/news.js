var express = require('express');
var rpc_client = require('../rpc_client/rpc_client');
var router = express.Router();


/* GET news summary list. */
router.get('/userId=:userId&pageNum=:pageNum', function(req, res, next) {
  var user_id = req.params['userId'];
  var page_num = req.params['pageNum'];

  rpc_client.getNewsSummariesForUser(user_id, page_num, function(response) {
    res.json(response);
  });
});


/* Log news click event. */
router.post('/userId=:userId&newsId=:newsId', function(req, res, next) {
  console.log('Logging news click...');
  var user_id = req.params['userId'];
  var news_id = req.params['newsId'];
  
  rpc_client.logNewsClickForUser(user_id, news_id);
  res.status(200);
});


module.exports = router;
