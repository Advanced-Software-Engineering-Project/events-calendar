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




app.get('/scrape', function(req, res){

  request(options, function(error, response, html){
    if(!error){
      var $ = cheerio.load(html);

      // Uncomment the hidden contents
      $('code')
        .contents()
        .filter(function(){
          if (this.nodeType === 8) {
            return true
          }
          return false
        })
        .replaceWith(function(){return this.data;});

      //console.debug(html);

      var events = [];

      $('._3u1').each(function(){ // ._gli._5und
        var data = $(this);
        var title = data.find('._42ef ._glj ._gll').text();
        var description = data.find('._glo').text();
        var date = data.find('._pac').text();

        var event = {
          title : title,
          description : description,
          date : date,
          url : null
        };

        events.push(event);

        console.log("event_xxx: ", event);
      });

    }

    // To write to the system we will use the built in 'fs' library.
    // In this example we will pass 3 parameters to the writeFile function
    // Parameter 1 :  output.json - this is what the created filename will be called
    // Parameter 2 :  JSON.stringify(json, null, 4) - the data to write, here we do an extra step by calling JSON.stringify to make our JSON easier to read
    // Parameter 3 :  callback function - a callback function to let us know the status of our function

    fs.writeFile('output.json', JSON.stringify(events, null, 4), function(err){

      console.log('File successfully written! - Check your project directory for the output.json file');

    });

    // Finally, we'll just send out a message to the browser reminding you that this app does not have a UI.
    res.send('Check your console!')

  });

});












app.listen('8081');
console.log('Magic happens on port 8081');
exports = module.exports = app;