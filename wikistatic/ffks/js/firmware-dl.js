(function($) {
    "use strict";

    // Of course we need a dirty hack for this...
    // Because web technology is awesome!
    // http://stackoverflow.com/a/6246260/1592377
    $(".vendor + label").mousedown(function(e){
        var self        = $(this);
        var radioButton = $("#" + $(this).attr("for"));

        if(radioButton.is(":checked")) {
            var uncheck = function() {
                setTimeout(function() { radioButton.removeAttr("checked"); }, 0);
            };

            var unbind = function() {
                self.unbind("mouseup", up);
            };

            var up = function() {
                uncheck();
                unbind();
            };

            self.bind("mouseup", up);
            self.one("mouseout", unbind);
        }
    });
})(jQuery);
