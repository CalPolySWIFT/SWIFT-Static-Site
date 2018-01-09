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
        lat: 34.061297,
        lng: -117.819525,
        title: 'Address',
        infoWindow: {
            content: '<h5 class="title">SWIFT General Meeting Room: CBA 162 room 1001 @ Cal Poly Pomona</h5><p><span class="region">3801 W Temple Ave</span><br><span class="postal-code">Pomona, CA 91768</span><br><span class="country-name">United States</span></p>'
        }

    });
    map.addMarker({
        lat: 34.059670,
        lng: -117.819747,
        title: 'Address',
        infoWindow: {
            Content: '<h5 class="title">SWIFT Telecom Lab: CLA 98C 4-36 @ Cal Poly Pomona</h5><p><span class="region">3801 W Temple Ave</span><br><span class="postal-code">Pomona, CA 91768</span><br><span class="country-name">United States</span></p>'
        }
    });

});
