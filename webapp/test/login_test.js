
function validateSignup(obj){

    if (obj.password !== obj.confirm_password) {
        return "Passwords Don't match";
    } else {
        return true;
    }
}

function new_account(validate, obj){
    if (!validate) { return false; }
    if (!obj.firstname || !obj.lastname || !obj.email || !obj.password) {return false;}
    return true
}
var assert = require('assert');
describe('Signup', function(){
  describe('#validateSignup', function(){
    it('should return true when password equals confirm_password', function(){
      assert.equal(true, validateSignup({password:'123', confirm_password:'123'}));
    });
    it("should return passwords don't match when password doesn't equal to confirm_password", function(){
      assert.equal("Passwords Don't match", validateSignup({password:'123', confirm_password:'321'}));
    });
  });
  describe('#new_account', function(){
    it('should return false when validatesignup value is false', function(){
      assert.equal(false, new_account(false, {firstname:'a', lastname:'b', email:'123@columbia.edu', password:'123'}));
    });
    it('should return false when any value of firstname, lastname, email or comfirm_password is null', function(){
      assert.equal(new_account(true, {firstname: null , lastname:'b', email:'123@columbia.edu', password:'123'}), false);
      assert.equal(new_account(true, {firstname: 'a', lastname:null, email:'123@columbia.edu', password:'123'}), false);
      assert.equal(new_account(true, {firstname: 'a', lastname:'b', email:null, password:'123'}), false);
      assert.equal(new_account(true, {firstname: 'a', lastname:'b', email:'123@columbia.edu', password:null}), false);
    });
    it('should return true when validatesignup is true and all values of obj are not null', function(){
      assert.equal(true, new_account(true, {firstname: 'a', lastname:'b', email:'123@columbia.edu', password:'123'}));
    }); 
  });

});
