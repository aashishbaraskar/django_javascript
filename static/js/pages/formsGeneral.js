/*
 *  Document   : formsGeneral.js
 *  Author     : omsoftware
 *  Description: Custom javascript code used in Forms General page
 */

var FormsGeneral = function() {

    return {
        init: function() {
            /* Toggle .form-bordered class on block's form */
            $('.toggle-bordered').click(function() {
                $(this)
                    .parents('.block')
                    .find('form')
                    .toggleClass('form-bordered');
            });
        }
    };
}();