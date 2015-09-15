
$(document).ready(function() {
$.getJSON( "http://128.199.251.33:8000/", function( data  ) {
      $('.psi-value').text(data[0].psi);
        var timestamp = moment.unix(data[0].timestamp).format("dddd, MMMM Do YYYY, ha");
          $('.timestamp').text(timestamp);

} );
});
