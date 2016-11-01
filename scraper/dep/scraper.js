var express = require('express');
var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app     = express();



var options = {
  url: 'https://www.facebook.com/search/pages/?q=columbia%20university',
  headers: {
    'User-Agent': 'request',
    'dnt': 1,
    'accept-language': 'en-US,en;q=0.8,fr;q=0.6',
    'upgrade-insecure-requests': 1,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'cache-control': 'max-age=0',
    'authority': 'www.facebook.com',
    'cookie': 'datr=BDkcV-_7haIIZuILU78LRnRZ; lu=gA_fuLGahnhyh5T1RNNto-NQ; sb=HDkcV5s1DOEUEczamFuEXyGO; _ga=GA1.2.1585845431.1474032856; c_user=1084380721; xs=36%3AnyontbA6y-SPIQ%3A2%3A1461467421%3A6482; fr=0Lo9YceHsP4DsufUw.AWWIsGvEyhRZHCXCujYI8lWTmew.BXHDkd.5j.FgE.0.0.BYDNqE.AWVrtTZW; csm=2; s=Aa5kCyc1qRdxOObx.BXb_GY; p=-2; act=1477238930381%2F7; presence=EDvF3EtimeF1477238933EuserFA21084380721A2EstateFDt2F_5b_5dElm2FnullEuct2F1477237355BEtrFA2loadA2EtwF202900783EatF1477238932826G477238933241CEchFDp_5f1084380721F3CC'
  }
};


var events = [];
var done = 0;

var pages_urls = JSON.parse(fs.readFileSync('columbia_pages_urls.json', 'utf8'));

app.get('/scrape', function(req, res){

  for (var i = 0; i < 1; i++) { // pages_urls.length - 400
    console.log('getting events for', pages_urls[i]);
    getEvents(pages_urls[i]);
  }

});

function getEvents(url){

  options.url = url;

  request(options, function(error, response, html){
    if(!error){
      var $ = cheerio.load(html);

      // Uncomment the hidden contents
      $('code')
        .contents()
        .filter(function(){
          if (this.nodeType === 8) {
            console.log('uncommenting comment');
            return true
          }
          return false
        })
        .replaceWith(function(){return this.data;});

      // console.log(html);
      // savePage(html);
      console.log('found the events div? ', $('._3j40').length);

      $('._4dmd._4eok').each(function(){  // (Event div)
        var data = $(this);
        console.log(data.text());
        var title = data.find('._4dmk').find('a').text();
        var date = data.find('._5x8v').text();
        var date_location = data.find('.fsm.fwn.fcg').text();

        var event = {
          title: title,
          date: date,
          date_location: date_location
        };

        events.push(event);

        console.log("event_found_xxx: ", event);
      });

      done = done + 1;
      console.log(done, pages_urls.length)
      if (done === 1) { //pages_urls.length - 1) {
        saveEvents();
      }

    }

  });
}

function saveEvents() {
  fs.appendFile('events.json', JSON.stringify(events, null, 4), function(err){
    console.log('Appended events to events.json');
  });
}

function savePage(html) {
  fs.appendFile('events_page.html', html, function(err){
    console.log('Wrote events_page.html');
  });
}





app.listen('8082');
console.log('Scraping on port 8082');
exports = module.exports = app;