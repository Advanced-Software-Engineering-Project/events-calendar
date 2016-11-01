var fs = require('fs');
var page = require('webpage').create();



page.open("http://www.facebook.com/login.php", function(status) {

  if (status === "success") {

    page.onConsoleMessage = function(msg, lineNum, sourceId) {
      console.log('CONSOLE: ' + msg + ' (from line #' + lineNum + ' in "' + sourceId + '")');
    };

    page.evaluate(function() {
      document.getElementById("email").value = "ionox0@gmail.com";
      document.getElementById("pass").value = "";
      document.getElementById("loginbutton").click();
    });

    setTimeout(function() {
      page.evaluate(function() {
        console.log('At Homepage');
      });
      page.render("home_page.png");

      routeToSearch();
    }, 2000);

    function routeToSearch() {
      page.evaluate(function() {
        document.getElementsByClassName("_1frb")[0].value = "columbia";
        document.getElementsByClassName("_42ft _4jy0 _4w98 _4jy3 _517h _51sy")[0].click();
        document.querySelector('button').click();
      });

      setTimeout(function() {
        page.evaluate(function() {
          console.log('At Search Page');
        });
        page.render("search_page.png");

        routeToPages();
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
        page.render("pages_page.png");

        scrollLoop();
      }, 5000)
    }

    var i = 1;
    function scrollLoop() {
      if (i === 10) {
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
        page.render("pages_page_scroll_" + i + ".png");

        scrollLoop();
      }, 5000)
    }

    function grabGroups() {
      var pages = page.evaluate(function() {
        var pages_els = document.querySelectorAll("._5und");
        var pages = [];
        var i = 0;

        for (var i = 0; i < pages_els.length; i++) {
          pages.push({
            group_id: JSON.parse(pages_els[i].getAttribute('data-bt')).id,
            group: pages_els[i].querySelector('._5d-5').innerHTML,
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
      var path = 'pages_data.json';
      fs.write(path, pages, 'w');

      phantom.exit();
    }

  }

});