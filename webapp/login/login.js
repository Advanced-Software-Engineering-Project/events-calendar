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



function validateSignup(){
    if($('#password').val() != $('#confirm_password').val()) {
        $('#head').html('<p style="color:red;text-align:center">Passwords Don\'t Match</p>');
        return false
    } else {
        $('#head').html('<h2>Sign Up</h2>');
        return true
    }
}



// Prevent form submission
jQuery("form").submit(function(e){
    console.log('preventsubmit')
    e.preventDefault();
});

function new_account(){
    if (!validateSignup()) { return false }

    var obj ={};
    obj.firstname = $("#firstname").val();
    obj.lastname = $("#lastname").val();
    obj.email = $("#email").val();
    obj.password = $("#password").val();
    if (!obj.firstname || !obj.lastname || !obj.email || !obj.password) return false

    $.ajax({
        url: '/signup',
        method: 'POST',
        contentType: "application/json; charset=utf-8",
        //data: obj,
        data: JSON.stringify(obj),
        dataType : "json",
        success: function(response) {
                console.log(response.user_id);
                $.cookie('columbia_events_user_id', response.user_id);
                //Route to events page
                window.location.href = "../events/index.html";
            },
        error: function(response){
            $('#head').html('<p style="color:red;text-align:center">Email has been used</p>');
        }
    });
    return false
}

function login(){
    var obj ={};
    obj.exist_email = $("#exist_email").val();
    obj.exist_password = $("#exist_password").val();
    if (!obj.exist_email || !obj.exist_password ) return false
    $.ajax({
        url:  "/login",
        method: 'POST',
        contentType:"application/json; charset=utf-8",
        //data: obj,
        data: JSON.stringify(obj),
        dataType:"json",
        success: function(response) {
         console.log(response.user_id);
         $.cookie('columbia_events_user_id', response.user_id);
          //Route to events page
         window.location.href = "../events/index.html";
    
        },
        error:function(response){
            $('#warn').html('<p style="color:red;text-align:center">invalid user name or password</p>');
            
        }
    });
    return false
}