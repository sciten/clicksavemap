function initAddresses() {
    url_to_call = _site_url + "/all_addresses";

    fetch(url_to_call, { credentials: "same-origin" }) // Call the fetch function passing the url of the API as a parameter
        .then((resp) => resp.json())
        .then(function (data) {
            let status = data.status;
            if (status == "ok") {
                // empty the text list
                $("ul#addresses").empty();

                // we got addresses
                let addresses = data.result;
                // parse addresses and place marker
                addresses.map(function (address) {
                    placeOurMarker(address.lat, address.lng, address.address);
                    placeAddressTextUnder(address.address);
                });


            } else {
                alert("Problems on fetching the addresses from the database! Msg: " + data.message);
            }

        })
        .catch(function () {
            alert("Error on getting the data");
        });
}


function saveAddressDb(latLng, address) {

    // prepare the form data
    var data = JSON.stringify({
        lat: latLng.lat(),
        lng: latLng.lng(),
        address: address
    });

    url_to_call = _site_url + "/save_address";

    fetch(url_to_call,
        {
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            credentials: "same-origin",
            method: "POST",
            body: data
        })
        .then((resp) => resp.json())
        .then(function (data) {
            let status = data.status;

            if (status == "ok") {
                // refresh the text link under the map
                initAddresses();
            } else {
                alert("Problems on saving the address to the database! Msg: " + data.message);
            }
        });

    
}


