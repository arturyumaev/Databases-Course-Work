function myFunction(sort_on) {
    document.querySelector("#sorting-button").textContent=sort_on;
}

var options = [];
$( '.dropdown-menu-category a' ).on( 'click', function( event ) {

   var $target = $( event.currentTarget ),
       val = $target.attr( 'data-value' ),
       $inp = $target.find( 'input' ),
       idx;

   if ( ( idx = options.indexOf( val ) ) > -1 ) {
      options.splice( idx, 1 );
      setTimeout( function() { $inp.prop( 'checked', false ) }, 0);
   } else {
      options.push( val );
      setTimeout( function() { $inp.prop( 'checked', true ) }, 0);
   }

   $( event.target ).blur();
      
   // console.log( options );
   return false;
});

function send_filter_results () {
    // Sorting type
    var soring_type = document.querySelector('#sorting-button').innerText;
    
    // Categories options
    var clothing_types = options;

    // Get gender type
    var gender = '';

    for (var i = 0, length = 3; i < length; i++) {
        if (document.querySelector('#gender-check-radio')[i].checked == true) {
            gender = document.querySelector('#gender-check-radio')[i].value;
        }
    }

    console.log('Results');
    console.log(soring_type);
    console.log(clothing_types);
    console.log(gender);
}