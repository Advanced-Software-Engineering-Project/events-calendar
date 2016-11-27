'use-strict'

window.events = [];

$(function() {
	$('input[name="daterange1"]').daterangepicker();
	$('.my-favorites').click(function(){
		var $this = $(this);
		$this.toggleClass('my-favorites');
		if($this.hasClass('my-favorites')){
			$this.text('My Favorites');
			$this.value('my-favorites');         
		} else {
			$this.text('All Events');
			$this.value('all-events');
		}
	});
});
var dummy;


$.get(
	'/events',
	function(data) { 
        window.events = data.events;
        render(data.events); 
    }
);

function render(events){
	$("#eventlist").html($("#eventTemplate").tmpl(events));
    $('.starrr').starrr(); 
    $('.starrr').on('starrr:change', function(e, value){
        var group_id = $(e).currentTarget.id;
        $.ajax({
			method: 'POST',
			url: '/rate',
			data: JSON.stringify({group_id: group_id, rate_value: value}),
			contentType: "application/json; charset=utf-8",
		})
})
}

function filterEventsByText() {
	var text = $('#search').val();
	var filteredEvents = _.filter(window.events, function(event) {
		return (event.title.toLowerCase().indexOf(text.toLowerCase()) > -1)
	})
	$("#eventlist").html($("#eventTemplate").tmpl(filteredEvents));
}

function filterEventByDate(e) {
	var timerange = e.target.selectedOptions[0].value;

	switch (timerange) {
		case 'alldates':
			render(window.events);
			return

		case 'today':
			var endTime = moment().startOf('day').add(1, 'days');
			break;

		case 'tomorrow':
			var endTime = moment().startOf('day').add(2, 'days');
			break;

		case 'nextsevendays':
			var endTime = moment().startOf('day').add(7, 'days');
			break;

		case 'customdate':
			render(window.events);
			return
	}

	var filteredEvents = _.filter(window.events, function(event) {
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



function logout() {
	$.ajax({
        method: 'POST',
		url:  "/logout",
		success: function(response) {
				window.location.href = "../login/index.html";
			}
	});
	return false
}



document.getElementById('select-dates').addEventListener('change', function () {
    var style = this.value == "customdate" ? 'block' : 'none';
    document.getElementById('custom-date').style.display = style;
});