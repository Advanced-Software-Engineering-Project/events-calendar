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
        "http://localhost:5000/eventss",
        function(data) {
            render(data.events);
        });

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
        console.log(favorite);
    }
    else {
        return '<span class="glyphicon glyphicon-heart-empty"></span>'
        console.log(favorite);
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

