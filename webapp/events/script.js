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



// $.get(
//     "http://localhost:5000/eventss",
//     function(data) {
//         render(data.events);
//     });

$.get(
    "/events/" + getUserId(),
    function(data) {
        render(data.events);
    });

function getUserId() {
    var user_id = "";
    $.ajax({
        url:  "/get_userid",
        method: 'POST',
        contentType:"application/json; charset=utf-8",
        //data: obj,
        data: JSON.stringify(obj),
        dataType:"json",
        success: function(response) {
            user_id = resposne.user_id;
          console.log(response.user_id);
          $.cookie('columbia_events_user_id', response.user_id);
    
        },
        error:function(response){
        }
    });
    return user_id;
}

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

