
load_category_datatable()
$('input[type="search"]').attr('placeholder', 'Search here');
$('input[type="search"]').addClass('search');

function show_category_modal(){
    $('#update-category').hide();
    $('#save-category').show();
    $(".error").remove();
    $('#myModal').modal('show');
}

function load_category_datatable() {
    var table = $('#category_datatable');
    var oTable = table.dataTable({
        "processing": true,
        "serverSide": true,
        "destroy": true,
        "ajax": "/manage_resources/category-datatable/",
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

$("#save-category").click(function(){
    flag = true
    $(".error").remove();
    category_name = $('#category-name').val()
    category_description = $('#category-description').val()
    category_image = $('#category-image').val()
    if (category_name == '') {
        $('#category-name').after('<span class="error" style="color:red">Please enter category name</span>');
        flag = false;
    }if (category_description == ''){
        $('#category-description').after('<span class="error" style="color:red">Please enter category Description</span>');
        flag = false;
    }if(category_image == ''){
        $('#category-image').after('<span class="error" style="color:red">Please enter Category image</span>');
        flag = false;
    }
    if(!flag){
        return false
    }else{
        var formData = new FormData();
        formData.append("category_name", $('#category-name').val());
        formData.append("category_description", $('#category-description').val());

        var input = document.getElementById('category-image');
        file = input.files[0];
        formData.append("category_image", file);
        $.ajax({
            type : 'POST',
            url : '/manage_resources/add-new-category/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Category Data Added Successfully</span>');
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

function change_category_status(id) {
    category_status = $('#category-status').is(':checked');
    bootbox.confirm({
        title: "Category",
        message: "<span class='center-block text-center'><b>Do you want to change status of Category ?<b></span>",
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
                    url: '/manage_resources/change-category-status/',
                    data: {'brand_status': category_status, 'category_id': id},
                    success: function (response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Category status change successfully</span>", function () {
                                load_category_datatable();
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

function edit_category_data(id){
    $(".error").remove();
    $.ajax({
        type: "GET",
        url: '/manage_resources/show-category-data/',
        data: {'category_id': id},
        success: function(response) {
            if (response.success == "true") {
                $('#category-name').val(response.category_name);
                $('#hidden_category_id').val(id);
                $('#category-description').val(response.category_description)
            } else("#errorMessage")
        },
        error: function(response) {
            bootbox.alert('Error Occurred for changing Category status.');
        },
        beforeSend: function() {
        },
        complete: function() {
            $('#update-category').show();
            $('#save-category').hide();
            $('#myModal').modal('show');
        }
    });
}

$('#update-category').click(function(){
    flag=true
    $(".error").remove();
    category_name = $('#category-name').val()
    category_description = $('#category-description').val()
    category_image = $('#category-image').val()
    if (category_name == '') {
        $('#category-name').after('<span class="error" style="color:red">Please enter category name</span>');
        flag= false;
    }
    if (category_description == ''){
        $('#category-description').after('<span class="error" style="color:red">Please enter category Description</span>');
        flag=false;
    }
    if(!flag) {
        return false
    }
    else{
        var formData = new FormData();
        formData.append('category_id', $('#hidden_category_id').val());
        formData.append("category_name", $('#category-name').val());
        formData.append("category_description", $('#category-description').val());
        if (category_image != ''){
            var input = document.getElementById('category-image');
            file = input.files[0];
            formData.append("category_image", file);
        }
        $.ajax({
            type : 'POST',
            url : '/manage_resources/update-category-data/',
            data : formData,
            cache: false,
            processData: false,
            contentType: false,
            success : function(response){
                if(response.success == 'true'){
                    $('#myModal').modal('hide');
                    bootbox.alert('<span class="center-block text-center">Category Data Updated Successfully</span>',
                        function(){load_category_datatable();}
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

function delete_category_detail(id){
    bootbox.confirm({
        title: "Category",
        message: "<span class='center-block text-center'><b>Do you want to delete selected Category ?<b></span>",
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
                    url: '/manage_resources/delete-category-detail/',
                    data: {'category_id': id},
                    success: function(response) {
                        if (response.success == "true") {
                            bootbox.alert("<span class='center-block text-center'>Category detail deleted successfully</span>",function(){
                                load_category_datatable();
                            });
                        } else("#errorMessage")
                    },
                    error: function(response) {
                        bootbox.alert('Error Occurred while deleting Category.');
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

