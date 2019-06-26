/*
 *  Document   : login.js
 *  Author     : omsoftware
 *  Description: Custom javascript code used in Login page
 */


var Login = function () {

    // Function for switching form views (login, reminder and register forms)
    var switchView = function (viewHide, viewShow, viewHash) {
        viewHide.slideUp(250);
        viewShow.slideDown(250, function () {
            $('input').placeholder();
        });

        if (viewHash) {
            window.location = '#' + viewHash;
        } else {
            window.location = '#';
        }
    };

    return {
        init: function () {
            /* Switch Login, Reminder and Register form views */
            var formLogin = $('#form-login'),
                formReminder = $('#form-reminder'),
                formRegister = $('#form-register');
            formOtp = $('#form-otp');

            $('#link-register-login').click(function () {
                switchView(formLogin, formRegister, 'register');
            });

            $('#link-register').click(function () {
                switchView(formRegister, formLogin, '');
            });

            $('#link-reminder-login').click(function () {
                switchView(formLogin, formReminder, 'reminder');
            });

            $('#link-reminder').click(function () {
                switchView(formReminder, formLogin, '');
            });

            $('#otp-register').click(function () {
                switchView(formRegister, formOtp, '');
            });

            $('#resend-otp').click(function () {
                switchView(formOtp, formRegister, '');
            });


            // If the link includes the hashtag 'register', show the register form instead of login
            if (window.location.hash === '#register') {
                formLogin.hide();
                formRegister.show();
            }

            // If the link includes the hashtag 'reminder', show the reminder form instead of login
            if (window.location.hash === '#reminder') {
                formLogin.hide();
                formReminder.show();
            }

            /*
             *  Jquery Validation, Check out more examples and documentation at https://github.com/jzaefferer/jquery-validation
             */

            /* Login form - Initialize Validation */
            $('#form-login').validate({
                errorClass: 'help-block animation-slideDown', // You can change the animation class for a different entrance animation - check animations page
                errorElement: 'div',
                errorPlacement: function (error, e) {
                    e.parents('.form-group > div').append(error);
                },
                highlight: function (e) {
                    $(e).closest('.form-group').removeClass('has-success has-error').addClass('has-error');
                    $(e).closest('.help-block').remove();
                },
                success: function (e) {
                    e.closest('.form-group').removeClass('has-success has-error');
                    e.closest('.help-block').remove();
                },
                rules: {
                    'login-email': {
                        required: true,
                        email: true
                    },
                    'login-password': {
                        required: true,
                        minlength: 6
                    },
                    'mobile-number': {
                        required: true,
                        maxlength: 10
                    }
                },
                messages: {
                    'login-email': 'Please enter your account\'s email',
                    'login-password': {
                        required: 'Please provide your password',
                        minlength: 'Your password must be at least 6 characters long'
                    },
                    'mobile-number':{
                        required:'Please Enter Mobile Number',
                        maxlength:'Please Enter valid Mobile Number'
                    },
                }
            });

            /* Reminder form - Initialize Validation */
            $('#form-reminder').validate({
                errorClass: 'help-block animation-slideDown', // You can change the animation class for a different entrance animation - check animations page
                errorElement: 'div',
                errorPlacement: function (error, e) {
                    e.parents('.form-group > div').append(error);
                },
                highlight: function (e) {
                    $(e).closest('.form-group').removeClass('has-success has-error').addClass('has-error');
                    $(e).closest('.help-block').remove();
                },
                success: function (e) {
                    e.closest('.form-group').removeClass('has-success has-error');
                    e.closest('.help-block').remove();
                },
                rules: {
                    'reminder-email': {
                        required: true,
                        email: true
                    },
                    'reminder-mobile':{
                        required:true,
                        'mobile-number':true
                    },
                },
                messages: {
                    'reminder-email': 'Please enter your account number',
                    'reminder-mobile':'Please Enter your Registered Mobile Number',
                }
            });

            /* Register form - Initialize Validation */
            $('#form-register').validate({
                errorClass: 'help-block animation-slideDown', // You can change the animation class for a different entrance animation - check animations page
                errorElement: 'div',
                errorPlacement: function (error, e) {
                    e.parents('.form-group > div').append(error);
                },
                highlight: function (e) {
                    $(e).closest('.form-group').removeClass('has-success has-error').addClass('has-error');
                    $(e).closest('.help-block').remove();
                },
                success: function (e) {
                    if (e.closest('.form-group').find('.help-block').length === 2) {
                        e.closest('.help-block').remove();
                    } else {
                        e.closest('.form-group').removeClass('has-success has-error');
                        e.closest('.help-block').remove();
                    }
                },
                rules: {

                    'register-firstname': {
                        required: true,
                        minlength: 2
                    },

                    'register-lastname': {
                        required: true,
                        minlength: 2
                    },
                    'register-email': {
                        required: true,
                        email: true
                    },
                    'register-password': {
                        required: true,
                        minlength: 6
                    },
                    'register-password-verify': {
                        required: true,
                        equalTo: '#register-password'
                    },
                    'register-terms': {
                        required: true
                    }
                },
                messages: {
                    'register-firstname': {
                        required: 'Please enter your First Name',
                        minlength: 'Please enter valid name'
                    },
                    'register-lastname': {
                        required: 'Please enter your lastname',
                        minlength: 'Please enter your lastname'
                    },
                    'register-email': 'Please enter a valid email address',
                    'register-password': {
                        required: 'Please provide a password',
                        minlength: 'Your password must be at least 6 characters long'
                    },

                    'register-password-verify': {
                        required: 'Please provide a password',
                        minlength: 'Your password must be at least 6 characters long',
                        equalTo: 'Please enter the same password as above'
                    },
                    'register-terms': {
                        required: 'Please accept the terms!'
                    }
                }
            });
        }
    };
}();


$('#mobile-number').val(localStorage.username);
$('#login-password').val(localStorage.password);
if (localStorage.chkbx == 'true'){
    $('#login-remember-me').prop('checked', true);
}else{
    $('#login-remember-me').prop('checked', false);
}

$('#login-remember-me').click(function () {
    if ($('#login-remember-me').is(':checked')) {
        document.cookie = "login-remember-me=yes;domain="+document.location.origin+";path=/";
        // save username and password
        localStorage.username = $('#mobile-number').val();
        localStorage.password = $('#login-password').val();
        localStorage.chkbx = true;
    } else {
        document.cookie = "login-remember-me=no;domain="+document.location.origin+";path=/";
        localStorage.username = '';
        localStorage.password = '';
        localStorage.chkbx = false;
    }
});


function verifyMobileNumber() {

    // Function for switching form views (login, reminder and register forms)
    var switchView = function (viewHide, viewShow, viewHash) {
        viewHide.slideUp(250);
        viewShow.slideDown(250, function () {
            $('input').placeholder();
        });

        if (viewHash) {
            window.location = '#' + viewHash;
        } else {
            window.location = '#';
        }
    };

    contact = $('#verify-primary-contact').val();
    if (contact == '') {
        bootbox.alert('<span class="center-block text-center">Please Enter Mobile No</span>');
        return false
    } else {
        $.ajax({
            type: 'GET',
            url: '/account/verify-primary-contact/',
            data: {'contact': contact},
            success: function (response) {
                if (response.result == 'Success') {
                    $('#hidden-otp').val(response.otp);
                    $('#hidden-primary-contact').val(response.contact);
                    $('#otp').text(response.otp);

                    var formLogin = $('#form-login'),
                        formReminder = $('#form-reminder'),
                        formRegister = $('#form-register');
                    formOtp = $('#form-otp');

                    switchView(formRegister, formOtp, '');
                } else {
                    bootbox.alert('<span class="center-block text-center">' + response.message + '</span>');
                }
            },
            error: function (response) {
                bootbox.alert('error');
            },
            complete: function (response) {

            }
        });
    }
}

function verifyOTP() {
    entered_otp = $('#match-otp').val();
    if (entered_otp == '') {
        bootbox.alert('<span class="center-block text-center">Please Enter OTP</span>');
        return false
    } else if (entered_otp != $('#hidden-otp').val()) {
        bootbox.alert('<span class="center-block text-center">Enter OTP Does Not Match</span>');
        return false
    } else {
        $("#modal-Verification").modal('show');
    }
}

if ($("#login-error").val()){
    $('#modal-login-error').modal('show');
}