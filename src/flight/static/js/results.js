function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

vars = getUrlVars();
console.log(vars);

ip = null;

$.getJSON('http://ipinfo.io', function(data){
    ip=data["ip"];
});

$.ajax({
    url: "http://partners.api.skyscanner.net/apiservices/pricing/v1.0",
    beforeSend: function(request) {
        request.setRequestHeader({"Content-Type": "application/x-www-form-urlencoded",
                                 "X-Forwarded-For": ip,
                                 "Accept": "application/json"});
    },
    data: {"country": "UK",
               "currency": "GBP",
               "locale": "en-GB",
               "originplace": vars["q1"],
               "destinationplace": vars["q3"],
               "adults": vars["q5"],
               "locationSchema": "iata",
               "children": vars["q6"],
               "infants": vars["q7"],
               "cabinclass": vars["q8"],
               "outbounddate": vars["q2"],
               "apikey": "ha158486926168541326868639329158"},
    success: function(response) {
        console.log(response);
    },
    error: function(xhr) {
        console.log(xhr);
    }
});