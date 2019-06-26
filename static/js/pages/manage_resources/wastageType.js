/*
 *  Document   : tablesDatatables.js
 *  Author     : omsoftware
 *  Description: Custom javascript code used in Tables Datatables page
 */
// $("#wastageType").addClass("active");
load_wastageType_datatable()
$('input[type="search"]').attr('placeholder', 'Search here');
$('input[type="search"]').addClass('search');


function show_wastageType_modal(){
    $('#update-wastageType').hide();
    $('#save-wastageType').show();
    $(".error").remove();
    $('#myModal').modal('show');
}

function load_wastageType_datatable() {
    var table = $('#wastageType_datatable');
    var oTable = table.dataTable({
        "processing": true,
        "serverSide": true,
        "destroy": true,
        "ajax": "/manage_resources/wastageType-datatable/",
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

$("#save-wastageType").click(function(){
    flag = true
    $(".error").remove();
    wastageType_name = $('#wastageType-name').val()
    description = $('#description').val()
    if (wastageType_name == ''){
        $('#wastageType-name').after('<span class="error" style="color:red">Please enter wastageType name</span>');
        flag = false;
    }
    if (description == ''){
        $('#description').after('<span class="error" style="color:red">Please enter description </span>');
        flag = false;
    }
    if(!flag){
        return false
    }else{
        var formData = new FormData();
        formData.append("wastageType_name", $('#wastageType-name').val());
        formData.append("description", $('#description').val());
        $.ajax({
            type : 'POST',
            url : '/manage_resources/add-new-wastageType/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">wastageType Data Added Successfully</span>');
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

function change_wastageType_status(id){
    wastageType_status = $('#wastageType-status').is(':checked');
    bootbox.confirm({
        title: "WastageType",
        message: "<span class='center-block text-center'><b>Do you want to change status of wastageType ?<b></span>",
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
                    url: '/manage_resources/change-wastageType-status/',
                    data: {'wastageType_status':wastageType_status, 'wastageType_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>wastageType status change successfully</span>",function(){
                                load_wastageType_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred for changing wastageType status.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }else{
                load_wastageType_datatable();
             }
        }
    });
}

function edit_wastageType_data(id){
    $(".error").remove();
    $.ajax({
        type: "GET",
        url: '/manage_resources/show-wastageType-data/',
        data: {'wastageType_id': id},
        success: function(response) {
            if (response.success == "true") {
                $('#wastageType-name').val(response.wastageType_name);
                $('#description').val(response.description);
                $('#hidden_wastageType_id').val(id);
            } else("#errorMessage")
        },
        error: function(response) {
            bootbox.alert('Error Occurred for changing wastageType status.');
        },
        beforeSend: function() {
        },
        complete: function() {
            $('#update-wastageType').show();
            $('#save-wastageType').hide();
            $('#myModal').modal('show');
        }
    });
}

$('#update-wastageType').click(function(){
    $(".error").remove();
    wastageType_name = $('#wastageType-name').val()
    description = $('#description').val()
    if (wastageType_name == ''){
        $('#wastageType-name').after('<span class="error" style="color:red">Please enter wastageType name</span>');
        return false
    }else{
        var formData = new FormData();
        formData.append('wastageType_id', $('#hidden_wastageType_id').val());
        formData.append("wastageType_name", $('#wastageType-name').val());
        formData.append("description", $('#description').val());
        $.ajax({
            type : 'POST',
            url : '/manage_resources/update-wastageType-data/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">wastageType Data Updated Successfully</span>',
                        function(){load_wastageType_datatable();}
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

function delete_wastageType_detail(id){
    bootbox.confirm({
        title: "wastageType",
        message: "<span class='center-block text-center'><b>Do you want to delete selected wastageType ?<b></span>",
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
                    url: '/manage_resources/delete-wastageType-detail/',
                    data: {'wastageType_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>wastageType detail deleted successfully</span>",function(){
                                load_wastageType_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred while deleting wastageType.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }else{
                load_wastageType_datatable();
             }
        }
    });
}