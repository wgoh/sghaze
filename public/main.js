
$(document).ready(function() {
	$.getJSON( "http://128.199.251.33:8000/", function( data  ) {
		var psiValue = data[0].psi;
      	$('.psi-value').text(psiValue);
    	var timestamp = moment.unix(data[0].timestamp).format("dddd, MMMM Do YYYY, ha");
        $('.timestamp').text(timestamp);

        var psiStatus = $('.psi-status');
        if (psiValue <= 50) {
        	psiStatus.text(" (good)");
        } else if (psiValue <= 100) {
			psiStatus.text(" (moderate)");
        } else if (psiValue <= 200) {
			psiStatus.text(" (unhealthy)");
        } else if (psiValue <= 300) {
			psiStatus.text(" (very unhealthy)");
        } else {
			psiStatus.text(" (hazardous)");
        }
	} );
});
