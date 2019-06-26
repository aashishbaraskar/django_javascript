/*
 *  Document   : tablesDatatables.js
 *  Author     : omsoftware
 *  Description: Custom javascript code used in Tables Datatables page
 */


$(document).ready(function() {
    $('#brand_datatable').DataTable();
    $('input[type="search"]').attr('placeholder', 'Search here');
    $('input[type="search"]').addClass('searchh');

} );



var TablesDatatables = function() {
    return {
        init: function() {
            /* Initialize Bootstrap Datatables Integration */
            App.datatables();

            /* Initialize Datatables */
            $('#subcategory_datatable').dataTable({
                ajax: "/manage_resources/subcategory-datatable/",
                columnDefs: [ { orderable: false, targets: [ 1, 2, 3, 4 ] } ],
                pageLength: 10,
                lengthMenu: [[10, 20, 30, -1], [10, 20, 30, 'All']]
            });

            /* Add placeholder attribute to the search input */
            $('.dataTables_filter input').attr('placeholder', 'Search here');
        }
    };
}();

//$( document ).ready(function() {
//    intializeTable();
//});
//
//function intializeTable(){
//    alert('Hi')
//    var table = $('#brand_datatable');
//    var oTable = table.dataTable({
//        "processing": true,
//        "destroy": true,
//        "serverSide": true,
//        "ajax": "/manage_resources/brand_datatable/",
//        "searching": true,
//        "ordering": true,
//        "paging": true,
//        "columnDefs": [
//            {"targets": 2, "orderable": false},
//            {"targets": 3, "orderable": false},
//            {"targets": 4, "orderable": false},
//        ],
//        buttons: [
//            { extend: 'print', className: 'btn dark btn-outline' },
//            { extend: 'copy', className: 'btn red btn-outline' },
//            { extend: 'pdf', className: 'btn green btn-outline' },
//            { extend: 'excel', className: 'btn yellow btn-outline ' },
//            { extend: 'csv', className: 'btn purple btn-outline ' },
//            { extend: 'colvis', className: 'btn dark btn-outline', text: 'Columns'}
//        ],
//        // setup responsive extension: http://datatables.net/extensions/responsive/
//        responsive: false,
//
//        //"ordering": false, disable column ordering
//        //"paging": false, disable pagination
//
//        "order": [
//            [0, 'asc']
//        ],
//
//        "lengthMenu": [
//            // change per page values here
//            [10,20,50,100],
//            [10,20,50,100],
//        ],
//        // set the initial value
//        "pageLength": 10,
//    });
//    // handle datatable custom tools
//    $('#billing_table_tools > li > a.tool-action').on('click', function() {
//        var action = $(this).attr('data-action');
//        oTable.DataTable().button(action).trigger();
//    });
//}

function save_subcategory(){
    var formData = new FormData();
    formData.append("sub_cat_name", $('#subcategory-name').val());
    formData.append("sub_cat_description", $('#Subcategory-description').val());
    formData.append("category_fk", $('#category-fk').val());

    var input = document.getElementById('subcategory-Image');
    file = input.files[0];
    formData.append("sub_cat_image", file);

    $.ajax({
        type : 'POST',
        url : '/manage_resources/add-new-subcategory/',
        data : formData,
        cache: false,
        processData: false,
        contentType: false,
        success : function(response){
            if(response.success == 'true'){
                $('#myModal').modal('hide');
                alert('Subcategory Data Added Successfully!');
            }
        },
        error : function(response){
            alert('error');
        },
        complete : function(response){

        }
    });
}