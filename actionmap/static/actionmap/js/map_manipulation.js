var map, geocoder, infowindow;
var map_center = { lat: 47.0736852, lng: 15.3717504 };

// initialize the map
function initMap() {
    infowindow = new google.maps.InfoWindow();
    geocoder = new google.maps.Geocoder();
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: map_center
    });

    map.addListener('click', function (event) {
        processNewPosition(event.latLng);
        placeGoogleMarker(event.latLng);
    });

    initAddresses();
}

// used to append the location to the bottom list
function placeAddressTextUnder(address_details) {
    $("ul#addresses").append("<li>" + address_details + "</li>");
}


// place the marker on the map
function placeGoogleMarker(location, details) {
    details = details || 0;
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });

    if (details) {
        google.maps.event.addListener(marker, 'click', function () {
            infowindow.setContent('<div><strong>' + details + '</strong><br>');
            infowindow.open(map, this);
        });
    }
}

// this is ASYNC
// we will save only AFTER we receive a response from google
function processNewPosition(latLng) {
    var address;

    geocoder.geocode({
        latLng: latLng
    }, function (responses) {
        if (responses && responses.length > 0) {
            address = responses[0].formatted_address;
        } else {
            address = "Unknown";
        }

        // call the API to save the address in database
        saveAddressDb(latLng, address);
        
    });
}