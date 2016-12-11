
var assert = require("assert");
/* istanbul ignore next */
var _ = require('underscore');
/* istanbul ignore next */
var moment = require('moment');
var events_none = [];
var events = require('./data.json');
var text = 'baptist';
function render(events) {
    if(events.length == 0) {
        return 'Sorry, none of the events matched your search!';
    }
    else {
        return true;
    }
}
function filterEventsByText(text, events) {

    var filteredEvents = _.filter(events, function(event) {
		return (
			(event.title.toLowerCase().indexOf(text.toLowerCase()) > -1)||
			(event.group.toLowerCase().indexOf(text.toLowerCase()) > -1)
		);
	});
    return render(filteredEvents);
}

function filterEventByDate(events, timerange) {
    var filteredEvents;
    switch (timerange) {
        case 'alldates':
			return render(events);

		case 'today':
			filteredEvents = _.filter(events, function(event) {
				return moment(event.datetime).isSame(moment(), 'day');
			});
			break;

		case 'tomorrow':
			filteredEvents = _.filter(events, function(event) {
				return moment(event.datetime).isSame(moment().add(1, 'days'), 'day');
			});
			break;

		case 'nextsevendays':
			var endTime = moment().startOf('day').add(7, 'days');
			break;
    }
    filteredEvents = filteredEvents || _.filter(events, function(event) {
		return moment(event.datetime).isBefore(endTime);
	});
	return render(filteredEvents);
}


describe('Filter', function(){
  describe('#render', function(){
      it("should return false when there is no event", function(){
          assert.equal('Sorry, none of the events matched your search!', render(events_none));
      });
      it("should return true when there has events", function(){
          assert.equal(true, render(events));
      });
  });
  describe('#filterEventsByText', function(){
    it("should return true when event's title or group contains the text", function(){
      assert.equal(true, filterEventsByText(text, events));
    });
    it("should return false when no event's title or group contains the text", function(){
      assert.equal('Sorry, none of the events matched your search!', filterEventsByText(text, events_none));
    });
  });
  describe('#filterEventByDate', function(){
    it("should return false when date range is set to alldate, today, tomorrow or next week but no event's date is in that range of time", function(){
      assert.equal('Sorry, none of the events matched your search!', filterEventByDate(events_none, 'alldates'));
      assert.equal('Sorry, none of the events matched your search!', filterEventByDate(events_none, 'today'));
      assert.equal('Sorry, none of the events matched your search!', filterEventByDate(events_none, 'tomorrow'));
      assert.equal('Sorry, none of the events matched your search!', filterEventByDate(events_none, 'nextsevendays'));
    }); 
    it("should return true when date range is set to alldate, today, tomorrow or next week and there has events whose date is in the range of next week", function(){
      assert.equal(true, filterEventByDate(events, 'alldates'));
      assert.equal(true, filterEventByDate(events, 'today'));
      assert.equal(true, filterEventByDate(events, 'tomorrow'));
      assert.equal(true, filterEventByDate(events, 'nextsevendays'));
    });
  });

});