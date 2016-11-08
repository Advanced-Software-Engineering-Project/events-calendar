'use-strict'

window.events = [];

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
    '/events',
    function(data) { render(data.events);}
);

function render(events){
    window.events = events;
    $("#eventlist").html($("#eventTemplate").tmpl(events));
}

function formatDate(datetime) {
    var time = new Date(datetime);
    return time.format();
}

function favor(favorite, id) {
    if (favorite) {
        return '<span class="glyphicon glyphicon-heart" onClick="setFavorite(false, ' + id + ')"></span>'
    } else {
        return '<span class="glyphicon glyphicon-heart-empty" onClick="setFavorite(true, ' + id + ')"></span>'
    }
}

function setFavorite(fav, id) {
    if (fav) {
        $.ajax({
            method: 'POST',
            url: '/favorite',
            data: JSON.stringify({id: id}),
            contentType: "application/json; charset=utf-8",
            success: favSuccess
        })
    } else {
        $.ajax({
            method: 'DELETE',
            url: '/favorite',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({id: id}),
            success: favSuccess
        })
    }

    function favSuccess() {
        // Flip the favorite flag for this event
        for (var i = 0; i < window.events.length; i++) {
            if (+window.events[i].id === +id) {
                window.events[i].favorite = !window.events[i].favorite;
            }
        }
        render(window.events);
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
        url:  "/logout",
        success: function(response) {
                window.location.href = "../login/index.html";
            }
    });
    return false
}

