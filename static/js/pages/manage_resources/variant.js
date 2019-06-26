/*
 *  Document   : tablesDatatables.js
 *  Author     : omsoftware
 *  Description: Custom javascript code used in Tables Datatables page
 */

// $("#variant").addClass("active");
load_variant_datatable()
$('input[type="search"]').attr('placeholder', 'Search here');
$('input[type="search"]').addClass('search');

function show_variant_modal(){
    $('#update-variant').hide();
    $('#save-variant').show();
    $(".error").remove();
    $('#myModal').modal('show');
};


function load_variant_datatable() {
    var table = $('#variant_datatable');
    var oTable = table.dataTable({
        "processing": true,
        "serverSide": true,
        "destroy": true,
        "ajax": "/manage_resources/variant-datatable/",
        "searching": true,
        "ordering": true,
        "paging": true,
        "columnDefs": [
            { orderable: false, targets: [ 2, 3 ] }
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


$("#save-variant").click(function(){
    flag = true
    $(".error").remove();
    variant_name = $('#variant-name').val()
    if (variant_name == ''){
        $('#variant-name').after('<span class="error" style="color:red">Please enter variant name</span>');
        flag = false;
    }
    if(!flag){
        return false
    }else{
        var formData = new FormData();
        formData.append("variant_name", $('#variant-name').val());
        $.ajax({
            type : 'POST',
            url : '/manage_resources/add-new-variant/',
            data : formData,
            cache: false, 
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    console.log('Data Submit');
                    bootbox.alert('<span class="center-block text-center">Variant Data Added Successfully</span>');
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


function change_variant_status(id){
    variant_status = $('#variant-status').is(':checked');
    bootbox.confirm({
        title: "Variant",
        message: "<span class='center-block text-center'><b>Do you want to change status of variant ?<b></span>",
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
                    url: '/manage_resources/change-variant-status/',
                    data: {'variant_status':variant_status, 'variant_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Variant status change successfully</span>",function(){
                                load_variant_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred for changing Variant status.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }else{
                load_variant_datatable();
             }
        }
    });
}


function edit_variant_data(id){
    $(".error").remove();
    $.ajax({
        type: "GET",
        url: '/manage_resources/show-variant-data/',
        data: {'variant_id': id},
        success: function(response) {
            if (response.success == "true") {
                $('#variant-name').val(response.variant_name);
                $('#hidden_variant_id').val(id);
            } else("#errorMessage")
        },
        error: function(response) {
            bootbox.alert('Error Occurred for changing Variant status.');
        },
        beforeSend: function() {
        },
        complete: function() {
            $('#update-variant').show();
            $('#save-variant').hide();
            $('#myModal').modal('show');
        }
    });
}


$('#update-variant').click(function(){
    $(".error").remove();
    variant_name = $('#variant-name').val()
    console.log('hello Ashish')
    if (variant_name == ''){
        $('#variant-name').after('<span class="error" style="color:red">Please enter variant -  name</span>');
        return false
    }else{
        var formData = new FormData();
        console.log($('#hidden_variant_id').val());
        formData.append('variant_id', $('#hidden_variant_id').val());
        formData.append("variant_name", $('#variant-name').val());
        $.ajax({
            type : 'POST',
            url : '/manage_resources/update-variant-data/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Variant Data Updated Successfully</span>',
                        function(){load_variant_datatable();}
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

function delete_variant_detail(id){
    bootbox.confirm({
        title: "Variant",
        message: "<span class='center-block text-center'><b>Do you want to delete selected variant ?<b></span>",
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
                    url: '/manage_resources/delete-variant-detail/',
                    data: {'variant_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Variant detail deleted successfully</span>",function(){
                                load_variant_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred while deleting Variant.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }else{
                load_variant_datatable();
             }
        }
    });
}