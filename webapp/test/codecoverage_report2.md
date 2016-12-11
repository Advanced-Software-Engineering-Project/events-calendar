dyn-160-39-178-106:test shanqingtan$ istanbul cover /usr/local/lib/node_modules/mocha/bin/_mocha login_test.js


  Signup
    #validateSignup
      ✓ should return true when password equals confirm_password
      ✓ should return passwords don't match when password doesn't equal to confirm_password
    #new_account
      ✓ should return false when validatesignup value is false
      ✓ should return false when any value of firstname, lastname, email or comfirm_password is null
      ✓ should return true when validatesignup is true and all values of obj are not null


  5 passing (7ms)

=============================================================================
Writing coverage object [/Users/shanqingtan/GitHub/events-calendar/webapp/test/coverage/coverage.json]
Writing coverage reports at [/Users/shanqingtan/GitHub/events-calendar/webapp/test/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 100% ( 27/27 )
Branches     : 100% ( 10/10 )
Functions    : 100% ( 10/10 )
Lines        : 100% ( 25/25 )
================================================================================

