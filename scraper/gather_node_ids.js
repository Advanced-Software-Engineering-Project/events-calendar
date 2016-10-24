var express = require('express');
var fs = require('fs');
var request = require('request');
var app     = express();


var pages_urls = JSON.parse(fs.readFileSync('columbia_pages_urls.json', 'utf8'));

var options = {
  url: '',
  headers: {
    'User-Agent': 'request',
    'dnt': 1,
    'accept-language': 'en-US,en;q=0.8,fr;q=0.6',
    'upgrade-insecure-requests': 1,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'cache-control': 'max-age=0',
    'authority': 'www.facebook.com',
    'cookie': 'datr=BDkcV-_7haIIZuILU78LRnRZ; lu=gA_fuLGahnhyh5T1RNNto-NQ; sb=HDkcV5s1DOEUEczamFuEXyGO; _ga=GA1.2.1585845431.1474032856; p=-2; act=1477249606821%2F14; c_user=1084380721; xs=36%3AnyontbA6y-SPIQ%3A2%3A1461467421%3A6482; fr=0Lo9YceHsP4DsufUw.AWUaKua3gZoC29OIZt6THMaYFyo.BXHDkd.5j.FgE.0.0.BYDRLk.AWUqBjai; csm=2; s=Aa5kCyc1qRdxOObx.BXb_GY; presence=EDvF3EtimeF1477253253EuserFA21084380721A2EstateFDt2F_5b_5dElm2FnullEuct2F1477237355BEtrFA2loadA2EtwF491848628EatF1477253252995G477253253025CEchFDp_5f1084380721F3CC'
  }
};

var pages_with_ids = [];
var done = 0;
for (var i = 0; i < pages_urls.length; i++) {

  (function(i) {
    var page_url_copied = pages_urls[i];
    options.url = 'https://graph.facebook.com/v2.8/?access_token=EAACEdEose0cBAImQxWV7neXsmyuJhkZARuuWk2pg2b3HDylBEE5hX4kZA8iZCOr5mVGi5cJeldCcL1ypYA9k0TzSZBAkDrDBPLQHUbEJZBTZAKCZC0AOo4mxi3JdCkEQDZCV6LKfLVzrTVjN71r8fpZAfHLkk0Fdxd8uSFcxXYG3f3QZDZD&debug=all&format=json&id=' + page_url_copied + 'method=get&pretty=0&suppress_http_code=1';

    request(options, function (error, response, data) {
      if (!error) {
        console.log(data);
        var node_id = JSON.parse(data).id;

        console.log(node_id);
        var page_data = {
          url: page_url_copied,
          node_id: node_id
        };
        pages_with_ids.push(page_data);

        done = done + 1;
        console.log(done, pages_urls.length)
        if (done === pages_urls.length - 1) {
          savePageData();
        }

      }

    });
  })(i)

}


function savePageData() {
  fs.writeFile('pages_with_ids.json', JSON.stringify(pages_with_ids, null, 4), function(err){
    console.log('Saved pages_with_ids to pages_with_ids.json');
  });
}