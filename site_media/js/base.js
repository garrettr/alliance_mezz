$(document).ready(function() {
    if($('#id_search').val() == "") {
        $('#id_search').val("Search");
    }
    $('#id_search').focus(function() {
       if ($(this).val() == "Search") {
          $(this).val("");
       } 
    });
    $('#id_search').blur(function() {
        if ($(this).val() == "") {
            $(this).val("Search");
        }
    });
});
