'use-strict';

window.events = [];
var Data = [];
var email;
var name;
$(function() {
	document.getElementById('all-events').style.background = "#a4defc";
	$('input[name="daterange1"]').daterangepicker();
	$('.favorites').click(function(){
            var Newdata = [];
            Data.forEach(function(element) {
                if(element.favorite === true) {
                    Newdata.push(element);
            }});
            render(Newdata);
            window.events = Newdata;
            $('#filterBar')[0].reset();
            document.getElementById('favorites').style.background = "#a4defc";
            document.getElementById('all-events').style.background = "transparent";
    });
    $('.all-events').click(function(){
            render(Data);
            window.events = Data;
            $('#filterBar')[0].reset();
            document.getElementById('all-events').style.background = "#a4defc";
            document.getElementById('favorites').style.background = "transparent";
    });

});



$.get(
	'/events',
	function(data) { 
		// Remove loading indicator
		$('.mdl-spinner').remove();

        data.events.forEach(function(element){
            element.rating = Math.round(element.rating);
            return;
        });
        window.events = data.events;
        Data = data.events;
        render(Data); 
        $(document).ready(function(){
            $("#user_name").text(data.name);
            $("#email").html('<p class="text-muted small" id = "email">'+data.email+'</p>');
        });
    }
);

function render(events){
    if(events.length === 0) {
        console.log(0);
        $("#eventlist").html('<p align="center">Sorry, none of the events matched your search!</p>');
        return;
    }
    else{
        $("#eventlist").html($("#eventTemplate").tmpl(events));
        $('.starrr').starrr();
        $('.starrr').on('starrr:change', function(e, value){
            var group_id = $(e).attr("currentTarget").id;
            $.ajax({
			 method: 'POST',
			 url: '/rate',
			 data: JSON.stringify({group_id: group_id, rate_value: value}),
			 contentType: "application/json; charset=utf-8",
		    });
        });
    }
}

function filterEventsByText() {
	var text = $('#search').val();
	var filteredEvents = _.filter(window.events, function(event) {
		return (
			(event.title.toLowerCase().indexOf(text.toLowerCase()) > -1)||
			(event.group.toLowerCase().indexOf(text.toLowerCase()) > -1)
		);
	});
	render(filteredEvents);
}

function filterEventByDate(e) {
	var timerange = e.target.selectedOptions[0].value;
	var filteredEvents;

	switch (timerange) {
		case 'alldates':
			render(window.events);
			return;

		case 'today':
			filteredEvents = _.filter(window.events, function(event) {
				return moment(event.datetime).isSame(moment(), 'day');
			});
			break;

		case 'tomorrow':
			filteredEvents = _.filter(window.events, function(event) {
				return moment(event.datetime).isSame(moment().add(1, 'days'), 'day');
			});
			break;

		case 'nextsevendays':
			var endTime = moment().startOf('day').add(7, 'days');
			break;

		//case 'customdate':
			//render(window.events);
			//return
	}

	filteredEvents = filteredEvents || _.filter(window.events, function(event) {
		return moment(event.datetime).isBefore(endTime);
	});

	render(filteredEvents);
}

function formatDate(datetime) {
	var time = new Date(datetime);
	return time.format();
}

function favor(favorite, id) {
	if (favorite) {
		return '<span class="glyphicon glyphicon-heart" onClick="setFavorite(false, ' + id + ')"></span>';
	} else {
		return '<span class="glyphicon glyphicon-heart-empty" onClick="setFavorite(true, ' + id + ')"></span>';
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
		});
	} else {
		$.ajax({
			method: 'DELETE',
			url: '/favorite',
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify({id: id}),
			success: favSuccess
		});
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

function logout() {
	$.ajax({
        method: 'POST',
		url:  "/logout",
		success: function(response) {
				window.location.href = "../login/index.html";
			}
	});
	return false;
}



document.getElementById('select-dates').addEventListener('change', function () {
    var style = this.value == "customdate" ? 'block' : 'none';
    document.getElementById('custom-date').style.display = style;
});