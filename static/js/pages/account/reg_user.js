function validate_reg_user_data(){
    flag = true
    var firstname =  $('#register-firstname').val();
    var name_regex  = /^[a-zA-Z]+$/;
    var pancard_regex = /^[A-Z]{5}\d{4}[A-Z]{1}/;
    var number_regex = /^[0-9]+$/;
    var ifsc_regex = /^[A-Z]{4}0[A-Z0-9a-z]{6}/;
    var email_regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    // var address_regex = /^[0-9a-zA-Z]+$/;
    $(".error").remove();


//    if (firstname.length == '' || !firstname.match(name_regex) ) {
//        $('#register-firstname').after('<span class="error" style="color:red">*required & contains alphabet</span>');
//    }

     if (firstname.length == '') {
         $('#register-firstname').after('<span class="error" style="color:red">This field is required</span>');
         flag = false
     }
     else if (!firstname.match(name_regex)){
         $('#register-firstname').after('<span class="error" style="color:red">This field is contains alphabet</span>');
         flag = false
     }


    if ($('#register-lastname').val() == '') {
        $('#register-lastname').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-lastname').val().match(name_regex)){
        $('#register-lastname').after('<span class="error" style="color:red">This field is contains alphabet</span>');
        flag = false
    }

    if ($('#register-company').val() == ''){
        $('#register-company').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-company').val().match(name_regex)){
        $('#register-company').after('<span class="error" style="color:red">This field is contains alphabet</span>');
        flag = false
    }

    if ($('#register-pancard').val() == ''){
        $('#register-pancard').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-pancard').val().match(pancard_regex)){
        $('#register-pancard').after('<span class="error" style="color:red">pattern - ( AAAAA1234A )</span>');
        flag = false
    }

    if ($('#register-pancard-image').val() == ''){
        $('#register-pancard-image').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }

    if ($('#register-benifieciency').val() == ''){
        $('#register-benifieciency').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-benifieciency').val().match(name_regex)){
        $('#register-benifieciency').after('<span class="error" style="color:red">This field is contains alphabet</span>');
        flag = false
    }

    if ($('#register-acc_number').val() == ''){
        $('#register-acc_number').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-acc_number').val().match(number_regex)){
        $('#register-acc_number').after('<span class="error" style="color:red">This field is contains number</span>');
        flag = false
    }

    if ($('#register-ifsc').val() == ''){
        $('#register-ifsc').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-ifsc').val().match(ifsc_regex)){
        $('#register-ifsc').after('<span class="error" style="color:red">pattern - ( AAAA0123456 )</span>');
        flag = false
    }

    if ($('#register-bankname').val() == ''){
        $('#register-bankname').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-bankname').val().match(name_regex)){
        $('#register-bankname').after('<span class="error" style="color:red">This field is contains alphabet</span>');
        flag = false
    }

    if ($('#register-phone').val() == ''){
        $('#register-phone').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-phone').val().match(number_regex)){
        $('#register-phone').after('<span class="error" style="color:red">This field is contains number</span>');
        flag = false
    }

    if ($('#register-altphone').val() == ''){
        $('#register-altphone').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-altphone').val().match(number_regex)){
        $('#register-altphone').after('<span class="error" style="color:red">This field is contains number</span>');
        flag = false
    }

    if ($('#register-email').val() == ''){
        $('#register-email').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-email').val().match(email_regex)){
        $('#register-email').after('<span class="error" style="color:red">This field is contains email</span>');
        flag = false
    }

    if ($('#register-password').val() == ''){
        $('#register-password').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    if ($('#confirm-password').val() == ''){
        $('#confirm-password').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    if ($('#register-address').val() == ''){
        $('#register-address').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }

    if ($('#state').val() == ''){
        $('#register-').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    if ($('#city').val() == ''){
        $('#city').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    if ($('#register-landmark').val() == ''){
        $('#register-landmark').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }

    if ($('#register-pin').val() == ''){
        $('#register-pin').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-pin').val().match(number_regex)){
        $('#register-pin').after('<span class="error" style="color:red">pattern - ( 123456 )</span>');
        flag = false
    }

    if ($('#register-town').val() == ''){
        $('#register-town').after('<span class="error" style="color:red">This field is required</span>');
        flag = false
    }
    else if (!$('#register-town').val().match(name_regex)){
        $('#register-town').after('<span class="error" style="color:red">This field is contains alphabet</span>');
        flag = false
    }
    if ($('#register-password').val() != $('#confirm-password').val()){
        $('#confirm-password').after('<span class="error" style="color:red">Password is not same</span>');
        flag = false
    }

    if (flag){
        return true
    }else{
        return false
    }
};


function save_registration_data(){
    if (validate_reg_user_data()){
        var formData = new FormData();
        formData.append("first_name", $('#register-firstname').val())
        formData.append("last_name", $('#register-lastname').val());
        formData.append("register-company", $('#register-company').val())
        formData.append("pan_card", $('#register-pancard').val())
        var input = document.getElementById('register-pancard-image');
        file = input.files[0];
        formData.append("pancard_image", file);
        formData.append("beneficiary_name", $('#register-benifieciency').val())
        formData.append("account_no", $('#register-acc_number').val())
        formData.append("ifsc_code", $('#register-ifsc').val())
        formData.append("bank_name", $('#register-bankname').val())
        formData.append("primary_contact", $('#register-phone').val())
        formData.append("alternate_contact", $('#register-altphone').val())
        formData.append("email", $('#register-email').val())
        formData.append("password", $('#register-password').val())
        formData.append("address", $('#register-address').val())
        formData.append("state", $('#state').val())
        formData.append("city", $('#city').val())
        formData.append("landmark", $('#register-landmark').val())
        formData.append("pincode", $('#register-pin').val())
        formData.append("town", $('#register-town').val())

        $.ajax({
            type : 'POST',
            url : '/account/add-new-reg-user/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    bootbox.alert('<span class="center-block text-center">User Registered Successfully</span>', function(){
                       window.location.href = '/account/index/';
                    });
                }else{
                    bootbox.alert('<span class="center-block text-center">'+response.message+'</span>');
                }
            },
            error : function(response){
                bootbox.alert('error');
            },
            complete : function(response){

            }
        });
    }else{
        return false
    }
}


$('#state').change(function(){
    state = $("#state").val();
    $('#city').html('').append('<option value="Select">Select City</option>').trigger("chosen:updated");
    if( state != 'Select'){
        $.ajax({
            type : 'GET',
            url : '/account/get-city-data/',
            data : {'state': state},
            success : function(response){
                $.each(response.city_data, function(index, value){
                    $('#city').append('<option value="'+value+'">'+value+'</option>').trigger("chosen:updated");
                });
            },
            error : function(response){
                bootbox.alert('error');
            },
            complete : function(response){

            }
        });
    }
});