// Usage:
// phantomjs groups_scraper.js


var fs = require('fs');
var page = require('webpage').create();

var images_dir = 'images/';
var save_images = true;

// Keyword for query of groups to fetch
var SEARCH_TERM = 'columbia';
// Total number of pages of groups to fetch
var MAX_PAGES = 20;

page.open("http://www.facebook.com/login.php", function(status) {

  if (status === "success") {

    page.onConsoleMessage = function(msg, lineNum, sourceId) {
      console.log('CONSOLE: ' + msg + ' (from line #' + lineNum + ' in "' + sourceId + '")');
    };

    page.evaluate(function() {
      document.getElementById("email").value = "";
      document.getElementById("pass").value = "";
      document.getElementById("loginbutton").click();
    });

    setTimeout(function() {
      page.evaluate(function() {
        console.log('At Homepage');
      });

      if (save_images) {
        page.render(images_dir + "home_page.png");
      }

     // Wait for page to render
     setTimeout(routeToSearch, 2000);

    }, 2000);

    function routeToSearch() {
      page.evaluate(function(SEARCH_TERM) {
        document.getElementsByClassName("_1frb")[0].value = SEARCH_TERM;
        document.getElementsByClassName("_42ft _4jy0 _4w98 _4jy3 _517h _51sy")[0].click();
        document.querySelector('button').click();
      }, SEARCH_TERM);

      setTimeout(function() {
        page.evaluate(function() {
          console.log('At Search Page');
        });

        if (save_images) {
          page.render(images_dir + "search_page.png");
        }

        // Wait for page to render
        setTimeout(routeToPages, 2000);
      }, 5000)
    }

    function routeToPages() {
      page.evaluate(function() {

        function eventFire(el, etype){
          if (el.fireEvent) {
            el.fireEvent('on' + etype);
          } else {
            var evObj = document.createEvent('Events');
            evObj.initEvent(etype, true, false);
            el.dispatchEvent(evObj);
          }
        }

        eventFire(document.querySelectorAll("._4xjz")[6], 'click');
      });

      setTimeout(function() {
        page.evaluate(function() {
          console.log('At Pages Page');
        });

        if (save_images) {
          page.render(images_dir + "pages_page.png");
        }

        // Wait for page to render
        setTimeout(scrollLoop, 2000);
      }, 5000)
    }

    var i = 1;
    function scrollLoop() {
      if (i === MAX_PAGES) {
        grabGroups();
      }
      page.evaluate(function() {
        window.document.body.scrollTop = document.body.scrollHeight;
      });

      i = i + 1;

      setTimeout(function() {
        page.evaluate(function() {
          console.log('Scrolling iteration...');
        });

        if (save_images) {
          page.render(images_dir + "pages_page_scroll_" + i + ".png");
        }

        // Wait for page to render
        setTimeout(scrollLoop, 2000);
      }, 5000)
    }

    function grabGroups() {
      var pages = page.evaluate(function() {
        var pages_els = document.querySelectorAll("._5und");
        var pages = [];

        for (var i = 0; i < pages_els.length; i++) {
          pages.push({
            group_id: JSON.parse(pages_els[i].getAttribute('data-bt')).id,
            group_name: pages_els[i].querySelector('._5d-5').innerHTML,
            group_url: pages_els[i].querySelector('a').href
          })
        }

        console.log(pages_els);
        console.log(pages_els.length);
        return JSON.stringify(pages)
      });

      writeResults(pages);
    }

    function writeResults(pages) {
      console.log(pages);
      console.log('Data saved in data/pages_data_2.json')
      var path = 'data/pages_data_2.json';
      fs.write(path, pages, 'w');

      phantom.exit();
    }

  }

});