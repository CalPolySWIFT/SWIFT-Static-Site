var map;
jQuery(document).ready(function(){

    map = new GMaps({
        div: '#map',
        lat: 34.0569172,
        lng: -117.8217494,
    });
    map.addMarker({
        lat: 34.0569172,
        lng: -117.8217494,
        title: 'Address',      
        infoWindow: {
            content: '<h5 class="title">Cal Poly Pomona</h5><p><span class="region">3801 W Temple Ave</span><br><span class="postal-code">Pomona, CA 91768</span><br><span class="country-name">United States</span></p>'
        }
        
    });
    map.addMarker({
        lat: 34.0597805,
        lng: -117.8196481,
        title: 'Address',
        infoWindow: {
            content: '<h5 class="title">SWIFT General Meeting Room: CBA 162 room 1001 @ Cal Poly Pomona</h5><p><span class="region">3801 W Temple Ave</span><br><span class="postal-code">Pomona, CA 91768</span><br><span class="country-name">United States</span></p>'
        }

    });

});
