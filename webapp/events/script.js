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
    var json = $.getJSON('eventdata.json');
    $(json).each(function (i, val){
    	$.each(val, function(k,v) {
    		console.log(k+" : "+ v);
    	});
    });
});
