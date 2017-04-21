function initMap() {

    var styledMapType = new google.maps.StyledMapType(
        [
            { "elementType": "geometry", "stylers": [ { "color": "#212121" } ] },
            { "elementType": "labels.icon", "stylers": [ { "visibility": "off" } ] },
            { "elementType": "labels.text.fill", "stylers": [ { "color": "#757575" } ] },
            { "elementType": "labels.text.stroke", "stylers": [ { "color": "#212121" } ] },
            { "featureType": "administrative", "elementType": "geometry", "stylers": [ { "color": "#757575" } ] },
            { "featureType": "administrative.country", "elementType": "labels.text.fill", "stylers": [ { "color": "#9e9e9e" } ] },
            { "featureType": "administrative.land_parcel", "stylers": [ { "visibility": "off" } ] },
            { "featureType": "administrative.locality", "elementType": "labels.text.fill", "stylers": [ { "color": "#bdbdbd" } ] },
            { "featureType": "poi", "elementType": "labels.text.fill", "stylers": [ { "color": "#757575" } ] },
            { "featureType": "poi.park", "elementType": "geometry", "stylers": [ { "color": "#181818" } ] },
            { "featureType": "poi.park", "elementType": "labels.text.fill", "stylers": [ { "color": "#616161" } ] },
            { "featureType": "poi.park", "elementType": "labels.text.stroke", "stylers": [ { "color": "#1b1b1b" } ] },
            { "featureType": "road", "elementType": "geometry.fill", "stylers": [ { "color": "#2c2c2c" } ] },
            { "featureType": "road", "elementType": "labels.text.fill", "stylers": [ { "color": "#8a8a8a" } ] },
            { "featureType": "road.arterial", "elementType": "geometry", "stylers": [ { "color": "#373737" } ] },
            { "featureType": "road.highway", "elementType": "geometry", "stylers": [ { "color": "#3c3c3c" } ] },
            { "featureType": "road.highway.controlled_access", "elementType": "geometry", "stylers": [ { "color": "#4e4e4e" } ] },
            { "featureType": "road.local", "elementType": "labels.text.fill", "stylers": [ { "color": "#616161" } ] },
            { "featureType": "transit", "elementType": "labels.text.fill", "stylers": [ { "color": "#757575" } ] },
            { "featureType": "water", "elementType": "geometry", "stylers": [ { "color": "#000000" } ] },
            { "featureType": "water", "elementType": "labels.text.fill", "stylers": [ { "color": "#3d3d3d" } ] }
        ],
        {name: 'Dark Map'}
    );

    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 52.2297, lng: 21.0122},
        zoom: 16,
        mapTypeControlOptions: {
            mapTypeIds: ['styled_map']
        }
    });

    map.mapTypes.set('styled_map', styledMapType);
    map.setMapTypeId('styled_map');

    infoWindow = new google.maps.InfoWindow;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            var marker = new google.maps.Marker({
                position: pos,
                map: map
            });

            map.setCenter(pos);
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    }
    else {
        handleLocationError(false, infoWindow, map.getCenter());
    }
    }

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}