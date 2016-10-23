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


$(document).ready(function(){
	// TEST JSON function
	var j = '[{"id": 1009214592509511,"datetime": "2016-02-25T19:00:00-0500","location": "Fairchild 700","group": "Columbia Bioinformatics","title": "Bioinformatics Student Research Panel","url": "https://www.facebook.com/events/563717810449699/"},{"id": 1009214592509511,"datetime": "2016-02-25T19:00:00-0500","location": "Fairchild 700","group": "Columbia Bioinformatics","title": "Bioinformatics Student Research Panel","url": "https://www.facebook.com/events/563717810449699/"},{"id": 1009214592509511,"datetime": "2016-02-25T19:00:00-0500","location": "Fairchild 700","group": "Columbia Bioinformatics","title": "Bioinformatics Student Research Panel","url": "https://www.facebook.com/events/563717810449699/"}]';
	var json = $.parseJSON(j);
    $(json).each(function (i, val){
    	$.each(val, function(k,v) {
    		console.log(k+" : "+ v);
    	});
    });
});
