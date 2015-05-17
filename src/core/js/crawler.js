//crawler namespace

var app = app || (function () {

    var page = new WebPage();
    var system = require('system');

    // check input
    var url = system.args[1] || "http://facebook.com";
    var tar = system.args[2] || "result.txt";

    console(url);
    console(tar);
    // handler for page events
    page.onError = function (msg, trace) {
        console.log(msg);
        trace.forEach(function (item) {
            console.log('  ', item.file, ':', item.line);
        });
    };


    page.onResourceReceived = function (resource) {
        if (resource.url == url) {
            status_code = resource.status;
        }
    };


    // crawler constructor
    var Crawler = function () {
        this.page = page;

    };

    // crawler methods contruction, callback
    Crawler.prototype.craw = function () {

        if (status == "fail" || status_code != 200) {
            console.log("Error: " + status_code + " for url: " + url);
            phantom.exit(1);
        }

        console.log("hello, world")

        this.page.injectJs('jquery-1.6.1.min.js');

    };

    Crawler.prototype.fire = funciton(_url)
    {
        this.page.open(_url || url, this.craw);
    }


    // crawler class constructor in this module
    return {

        crawler: Crawler()

    }

})();

var crawler = app.crawler;

crawler.fire();






