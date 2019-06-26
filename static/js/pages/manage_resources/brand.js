/*
 *  Document   : tablesDatatables.js
 *  Author     : omsoftware
 *  Description: Custom javascript code used in Tables Datatables page
 */

load_brand_datatable()
$('input[type="search"]').attr('placeholder', 'Search here');
$('input[type="search"]').addClass('search');


function show_brand_modal(){
    $('#update-brand').hide();
    $('#save-brand').show();
    $(".error").remove();
    $('#myModal').modal('show');
}

function load_brand_datatable() {
    var table = $('#brand_datatable');
    var oTable = table.dataTable({
        "processing": true,
        "serverSide": true,
        "destroy": true,
        "ajax": "/manage_resources/brand-datatable/",
        "searching": true,
        "ordering": true,
        "paging": true,
        "columnDefs": [
            { orderable: false, targets: [ 2, 3, 4 ] }
        ],

        // setup responsive extension: http://datatables.net/extensions/responsive/
        responsive: false,

        "order": [
            [0, 'asc']
        ],

        "lengthMenu": [
            // change per page values here
            [50,100,200],
            [50,100,200]
        ],
        // set the initial value
        "pageLength": 50,
    });
}

$("#save-brand").click(function(){
    flag = true
    $(".error").remove();
    brand_name = $('#brand-name').val()
    brand_image = $('#brand-image').val()
    if (brand_name == ''){
        $('#brand-name').after('<span class="error" style="color:red">Please enter brand name</span>');
        flag = false;
    }if(brand_image == ''){
        $('#brand-image').after('<span class="error" style="color:red">Please enter brand image</span>');
        flag = false;
    }
    if(!flag){
        return false
    }else{
        var formData = new FormData();
        formData.append("brand_name", $('#brand-name').val());
        var input = document.getElementById('brand-image');
        file = input.files[0];
        formData.append("brand_image", file);
        $.ajax({
            type : 'POST',
            url : '/manage_resources/add-new-brand/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Brand Data Added Successfully</span>');
                }
            },
            error : function(response){
                bootbox.alert('error');
            },
            complete : function(response){

            }
        });
    }
});

function change_brand_status(id){
    brand_status = $('#brand-status').is(':checked');
    bootbox.confirm({
        title: "Brand",
        message: "<span class='center-block text-center'><b>Do you want to change status of brand ?<b></span>",
        buttons: {
            cancel: {
                label: '<i class="fa fa-times" style="color:red"></i> Cancel'
            },
            confirm: {
                label: '<i class="fa fa-check"></i> Yes'
            }
        },
        callback: function (result) {
             if (result == true) {
                $.ajax({
                    type: "GET",
                    url: '/manage_resources/change-brand-status/',
                    data: {'brand_status':brand_status, 'brand_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Brand status change successfully</span>",function(){
                                load_brand_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred for changing Brand status.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }else{
                load_brand_datatable();
             }
        }
    });
}

function edit_brand_data(id){
    $(".error").remove();
    $.ajax({
        type: "GET",
        url: '/manage_resources/show-brand-data/',
        data: {'brand_id': id},
        success: function(response) {
            if (response.success == "true") {
                $('#brand-name').val(response.brand_name);
                $('#hidden_brand_id').val(id);
            } else("#errorMessage")
        },
        error: function(response) {
            bootbox.alert('Error Occurred for changing Brand status.');
        },
        beforeSend: function() {
        },
        complete: function() {
            $('#update-brand').show();
            $('#save-brand').hide();
            $('#myModal').modal('show');
        }
    });
}

$('#update-brand').click(function(){
    $(".error").remove();
    brand_name = $('#brand-name').val()
    brand_image = $('#brand-image').val()
    if (brand_name == ''){
        $('#brand-name').after('<span class="error" style="color:red">Please enter brand name</span>');
        return false
    }else{
        var formData = new FormData();
        formData.append('brand_id', $('#hidden_brand_id').val());
        formData.append("brand_name", $('#brand-name').val());
        if (brand_image != ''){
            var input = document.getElementById('brand-image');
            file = input.files[0];
            formData.append("brand_image", file);
        }
        $.ajax({
            type : 'POST',
            url : '/manage_resources/update-brand-data/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Brand Data Updated Successfully</span>',
                        function(){load_brand_datatable();}
                    );
                }
            },
            error : function(response){
                bootbox.alert('error');
            },
            complete : function(response){

            }
        });
    }
});

function delete_brand_detail(id){
    bootbox.confirm({
        title: "Brand",
        message: "<span class='center-block text-center'><b>Do you want to delete selected brand ?<b></span>",
        buttons: {
            cancel: {
                label: '<i class="fa fa-times" style="color:red"></i> Cancel'
            },
            confirm: {
                label: '<i class="fa fa-check"></i> Yes'
            }
        },
        callback: function (result) {
             if (result == true) {
                $.ajax({
                    type: "GET",
                    url: '/manage_resources/delete-brand-detail/',
                    data: {'brand_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Brand detail deleted successfully</span>",function(){
                                load_brand_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred while deleting Brand.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }else{
                load_brand_datatable();
             }
        }
    });
}