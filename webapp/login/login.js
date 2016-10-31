$('.form').find('input, textarea').on('keyup blur focus', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

});

var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");
var exist_email = document.getElementById("exist_email");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

function new_account(){
    var obj ={};
    obj.firstname = $("#firstname").val();
    obj.lastname = $("#lastname").val();
    obj.email = $("#email").val();
    obj.password = $("#password").val();

    $.ajax({
        url: '/signup',
        method: 'POST',
        contentType: "application/json; charset=utf-8",
        //data: obj,
        data: JSON.stringify(obj),
        dataType : "json",
        success: function(response) {
            if(response !== "Signup Error"){
                console.log(response.user_id);
                $.cookie('columbia_events_user_id', response.user_id);
                //Route to events page
                window.location.href = "../events/index.html";
            }
            else{
                document.getElementById('signup').append('<span>Email address has been used</span>');
            }
        }
    });
    return false
}

function login(){
    var obj ={};
    obj.exist_email = $("#exist_email").val();
    obj.exist_password = $("#exist_password").val();

    $.ajax({
        url:  "/login",
        method: 'POST',
        contentType:"application/json; charset=utf-8",
        //data: obj,
        data: JSON.stringify(obj),
        dataType:"json",
        success: function(response) {
            if(response === "Login Error"){
                exist_email.setCustomValidity("Invalid email or password");
            }
            else{
                console.log(response.user_id);
                $.cookie('columbia_events_user_id', response.user_id);
                // Route to events page
                window.location.href = "../events/index.html";
            }
        }
    });
    return false
}