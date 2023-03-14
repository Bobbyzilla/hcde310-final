function initMap() {
    var location = {lat: 47.655334, lng: -122.303520};
    var map = new google.maps.Map(document.getElementbyId("map"), {
        zoom: 4,
        center: location
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}