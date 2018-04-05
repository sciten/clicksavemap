// get cookie
// needed for django session
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


// used to place markers from the database (used as an interface between the database and then map api)
// the lat and lng are parameteres received in JSON
function placeOurMarker(lat, lng, address_details = null) {
    // create google friendly object for location
    let location = { lat: parseFloat(lat), lng: parseFloat(lng) };

    return placeGoogleMarker(location, address_details);
}