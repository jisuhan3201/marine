$(document).ready(function(){
    $("#nav-about").click(function() {
      $('html, body').animate ({
          scrollTop: $("#main-about").offset().top
      }, 500);
    });
    $("#nav-prod").click(function() {
        $('html, body').animate ({
            scrollTop: $("#main-prod").offset().top
        }, 500);
      });
    $("#nav-buy").click(function() {
        $('html, body').animate ({
            scrollTop: $("#main-buy").offset().top
        }, 500);
    });
    $("#nav-cooperation").click(function() {
        $('html, body').animate ({
            scrollTop: $("#main-cooperation").offset().top
        }, 500);
    });      
    $("#nav-contact").click(function() {
        $('html, body').animate ({
            scrollTop: $("#main-contact").offset().top
        }, 500);
    });      
});
  