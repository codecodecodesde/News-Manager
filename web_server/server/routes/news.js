var express = require('express');
var router = express.Router();

/* GET news page. */
router.get('/', function(req, res, next) {
  news=[{
    "source": "THe Wall Street Journal",
    "title": "Berkshire Hathaway Benefits From US Tax Plan",
    "description": "This is a description",
    "url":"https://www.cnn.com/2018/03/12/europe/theresa-may-russia-spy-poisoning-intl/index.html",
    "urlToImage": "https://cdn.cnn.com/cnnnext/dam/assets/180306171056-sergei-yulia-skripal-split-exlarge-169.jpg",
    "publishedAt": "...",
    "digest":"3RjuEomJo2601syZbU7OHA==\n",
    "reason": "recommand"
  },{
    "source": "lalalalalal",
    "title": "Berkshire Hathaway Benefits From US Tax Plan",
    "description": "lalalala",
    "url":"https://www.cnn.com/2018/03/12/europe/theresa-may-russia-spy-poisoning-intl/index.html",
    "urlToImage": "https://cdn.cnn.com/cnnnext/dam/assets/180306171056-sergei-yulia-skripal-split-exlarge-169.jpg",
    "publishedAt": "...",
    "digest":"3RjuEomJo2601syZbU7OHb==\n",
    "reason": "recommand"
  }];

  res.json(news);
});

module.exports = router;
