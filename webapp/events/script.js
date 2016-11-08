$(function() {
    $('input[name="daterange"]').daterangepicker();
    $('input[name="timerange"]').daterangepicker({
        timePicker: true,
        timePickerIncrement: 30,
        locale: {
            format: 'h:mm A'
        }
    });
});
var dummy;



$.get(
     "/eventss",
     function(data) {
         render(data.events);
     });


//function getUserId() {
//    $.ajax({
//        url:  "/get_userid",
//        contentType:"application/json; charset=utf-8",
//        dataType:"json",
//        success: function(response) {
//            user_id = response.user_id;
//            console.log(response.user_id);
//            console.log("success")
//            return response.user_id;
//          // $.cookie('columbia_events_user_id', response.user_id);
//    
//        },
//        error:function(response){
//            console.log("error")
//        }
//    });
//    return false
//}


//$.get(
//    'events/' + getUserId(), // TODO: not sure how to do ths
//    function(data) { render(data.events);}
//);

function render(events){
    $("#eventTemplate").tmpl(events).appendTo("#eventlist");
}

function formatDate(datetime) {
    var time = new Date(datetime);
    return time.format();
}

function favor(favorite, id) {
    var id = this.id;
    if(favorite === 1) {
        return '<span class="glyphicon glyphicon-heart"></span>'

    }
    else {
        return '<span class="glyphicon glyphicon-heart-empty"></span>'

    }
}

function eventRating(rating, id) {
    var id = this.id;
    var minus = 5 - rating;
    var stars = '';
    while(rating > 0) {
        stars += '<span class="glyphicon glyphicon-star"></span>';
        rating -=1;
        console.log(rating);
    }
    while(minus > 0) {
        stars += '<span class="glyphicon glyphicon-star-empty"></span>';
        minus -=1;
    }
    return stars
}

function logout() {
    $.ajax({
        url:  "/logout"
        // TODO: redirect to root.
        
    });
    return false
}

