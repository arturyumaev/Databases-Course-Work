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
    var sorting_type = document.querySelector('#sorting-button').innerText;
    
    // Categories options
    var clothing_types = options;

    // Get gender type
    var gender = '';

    // Проходимся по всем радио-баттонам и смотрим
    // какой из них активный, если нашли - получаем его название
    for (var i = 0, length = 3; i < length; i++) {
        if (document.querySelector('#gender-check-radio')[i].checked == true) {
            gender = document.querySelector('#gender-check-radio')[i].value;
        }
    }

    var queryString = '/collection?sort=' + sorting_type + '&gender=' + gender;
    if (clothing_types.length != 0) {
        for (let i = 0; i < clothing_types.length; i++) {
            queryString = queryString + '&cats=' + clothing_types[i];
        }
    } else {
        queryString += '&cats=None'
    }
    

    window.location.replace(queryString);
}

function add_to_cart(element) {
    var vendor = element.id.slice(12);
    
    var e = document.getElementById("size-" + vendor);
    var selectedSize = e.options[e.selectedIndex].value;
    if (selectedSize == 'Size') {
        selectedSize = '44';
    };

    console.log(vendor);
    console.log(selectedSize);

    var xhr = new XMLHttpRequest();
    var url = "/add_to_cart";
    var data = "vendor=" + vendor + "&size=" + selectedSize;
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // do something with response
            console.log(xhr.responseText);
        }
   };
   xhr.send(data);
};