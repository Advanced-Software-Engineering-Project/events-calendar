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
