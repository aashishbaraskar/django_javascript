
load_unit_datatable()
$('input[type="search"]').attr('placeholder', 'Search here');
$('input[type="search"]').addClass('search');

function show_unit_modal(){
    $('#update-unit').hide();
    $('#save-unit').show();
    $(".error").remove();
    $('#myModal').modal('show');
}

function load_unit_datatable() {
    var table = $('#unit_datatable');
    var oTable = table.dataTable({
        "processing": true,
        "serverSide": true,
        "destroy": true,
        "ajax": "/manage_resources/unit-datatable/",
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

$("#save-unit").click(function(){
    flag = true
    $(".error").remove();
    unit_name = $('#unit-name').val()
    base_unit = $('#base-unit').val()

    if (unit_name == '') {
        $('#unit-name').after('<span class="error" style="color:red">Please enter Unit name</span>');
        flag = false;
    }if (base_unit == ''){
        $('#base-unit').after('<span class="error" style="color:red">Please enter Base Unit </span>');
        flag = false;
    }
    if(!flag){
        return false
    }else{
        var formData = new FormData();
        formData.append("unit_name", $('#unit-name').val());
        formData.append("base_unit", $('#base-unit').val());

        $.ajax({
            type : 'POST',
            url : '/manage_resources/add-new-unit/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Unit Data Added Successfully</span>');
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

function change_unit_status(id) {
    unit_status = $('#unit-status').is(':checked');
    bootbox.confirm({
        title: "Unit",
        message: "<span class='center-block text-center'><b>Do you want to change status of units ?<b></span>",
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
                    url: '/manage_resources/change-unit-status/',
                    data: {'unit_status': unit_status, 'unit_id': id},
                    success: function (response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Unit status change successfully</span>", function () {
                                load_unit_datatable();
                            });
                        } else ("#errorMessage")
                    },
                    error: function (response) {
                        bootbox.alert('Error Occurred for changing Category status.');
                    },
                    beforeSend: function () {
                    },
                    complete: function () {
                    }
                });
            }
        }
    });
}

function edit_unit_data(id){
    $(".error").remove();
    $.ajax({
        type: "GET",
        url: '/manage_resources/show-unit-data/',
        data: {'unit_id': id},
        success: function(response) {
            if (response.success == "true") {
                $('#unit-name').val(response.unit_name);
                $('base-unit').val(response.base_unit);
                $('#hidden_unit_id').val(id);
            } else("#errorMessage")
        },
        error: function(response) {
            bootbox.alert('Error Occurred for changing unit status.');
        },
        beforeSend: function() {
        },
        complete: function() {
            $('#update-unit').show();
            $('#save-unit').hide();
            $('#myModal').modal('show');
        }
    });
}

$('#update-unit').click(function(){
    flag=true
    $(".error").remove();
    unit_name = $('#unit-name').val()
    base_unit = $('#base-unit').val()
    if (unit_name == '') {
        $('#unit-name').after('<span class="error" style="color:red">Please enter Unit name</span>');
        flag= false;
    }
    if (base_unit == ''){
        $('#base-unit').after('<span class="error" style="color:red">Please enter base unit</span>');
        flag=false;
    }
    if(!flag) {
        return false
    }
    else{
        var formData = new FormData();
        formData.append('unit_id', $('#hidden_unit_id').val());
        formData.append("unit_name", $('#unit-name').val());
        formData.append("base_unit", $('#base-unit').val());

        $.ajax({
            type : 'POST',
            url : '/manage_resources/update-unit-data/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Unit Data Updated Successfully</span>',
                        function(){load_unit_datatable();}
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

function delete_unit_detail(id){
    bootbox.confirm({
        title: "Unit",
        message: "<span class='center-block text-center'><b>Do you want to delete selected Unit?<b></span>",
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
                    url: '/manage_resources/delete-unit-detail/',
                    data: {'unit_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Unit detail deleted successfully</span>",function(){
                                load_unit_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred while deleting unit.');
                    },
                    beforeSend: function() {
                    },
                    complete: function() {
                    }
                });
             }
        }
    });
}

