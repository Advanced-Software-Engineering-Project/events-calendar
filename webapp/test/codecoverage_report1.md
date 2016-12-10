dyn-160-39-178-106:test shanqingtan$ istanbul cover /usr/local/lib/node_modules/mocha/bin/_mocha event_test.js


  Filter
    #render
      ✓ should return false when there is no event
      ✓ should return true when there has events
    #filterEventsByText
      ✓ should return true when event's title or group contains the text
      ✓ should return false when no event's title or group contains the text
    #filterEventByDate
      ✓ should return false when date range is set to alldate, today, tomorrow or next week but no event's date is in that range of time
      ✓ should return true when date range is set to alldate, today, tomorrow or next week and there has events whose date is in the range of next week


  6 passing (27ms)

=============================================================================
Writing coverage object [/Users/shanqingtan/GitHub/events-calendar/webapp/test/coverage/coverage.json]
Writing coverage reports at [/Users/shanqingtan/GitHub/events-calendar/webapp/test/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 100% ( 51/51 )
Branches     : 100% ( 10/10 )
Functions    : 100% ( 17/17 )
Lines        : 100% ( 51/51 )
================================================================================
