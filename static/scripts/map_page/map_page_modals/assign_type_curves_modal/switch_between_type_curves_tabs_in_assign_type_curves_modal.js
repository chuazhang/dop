$(document).ready(function () {
    $('#type_curve_tab_a_button').on('click', function (e) {
		Switch_Between_Type_Curves('A');
	});
    $('#type_curve_tab_b_button').on('click', function (e) {
		Switch_Between_Type_Curves('B');
	});
    $('#type_curve_tab_c_button').on('click', function (e) {
		Switch_Between_Type_Curves('C');
	});
    $('#type_curve_tab_d_button').on('click', function (e) {
		Switch_Between_Type_Curves('D');
	});
});

function Switch_Between_Type_Curves(type_curve) {
    $.ajax({
        url: '/asynchronously_grab_type_curve_production_volume_from_database',
        data: type_curve,
        type: 'POST',
        success: function(response){
            table = document.getElementById('type_curve_Production_volume_table'); 
            var input_nodes = table.getElementsByTagName('INPUT');
            for(var i = 0; i < input_nodes.length; ++i){
                if ((input_nodes[i].id.indexOf('_Forecasted_Month') == -1) && (input_nodes[i].id.indexOf('user_defined_column') == -1))
                    input_nodes[i].value = '';
            }
            document.getElementById('type_curve_type').value=type_curve;

            for (var i = 0; i < response.length; i++) { 
                for (var key in response[i]) { 
                    if (response[i].hasOwnProperty(key)) { 
                        if (document.getElementById('Type_Curve_' + response[i]['row_in_pad_modal'] + '_' + field_name_mapping_dictionary_defination[key]))
                            document.getElementById('Type_Curve_' + response[i]['row_in_pad_modal'] + '_' + field_name_mapping_dictionary_defination[key]).value = response[i][key];
                    } 
                }                
            }
        },
        error: function(error){
            console.log("Error!");
            alert('Error! Please contact application support.');
        }
    });

    // change selected type curve button to be active
    var i, tablinks;
    tablinks = document.getElementsByClassName('type_curve_tablink');
    for (i = 0; i < tablinks.length; i++) {
        if (tablinks[i].innerHTML == ('Type Curve ' + type_curve)) {
            tablinks[i].classList.add('tab_selected');
        } else {
            tablinks[i].classList.remove('tab_selected');
        }
    }
    document.getElementById('type_curve_type').value = type_curve;
}