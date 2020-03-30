	function Asynchronously_Grab_Production_Volume_From_Database(id_of_double_clicked_cell) {
		//alert(id_of_double_clicked_cell);
		//... ..- -- . ... ....
		//jqeury for AJAX call		
		$.ajax({
			url: '/asynchronously_grab_production_volume_from_database',
			data: id_of_double_clicked_cell,
			type: 'POST',
			success: function(response){
                // clear the table 
				table = document.getElementById('Production_volume_table'); 
				var input_nodes = table.getElementsByTagName('INPUT');
				for(var i = 0; i < input_nodes.length; ++i){
					if (input_nodes[i].id.indexOf('user_defined_column') == -1)
						input_nodes[i].value = '';
				}
                document.getElementById('Pad_Name').value = ''; 

                for (var i = 0; i < response.length; i++) { 
                    for (var key in response[i]) { 
                        if (response[i].hasOwnProperty(key) && id_of_double_clicked_cell == response[i]['cell_id']) { 
                            if (document.getElementById(response[i]['row_in_pad_modal'] + '_' + field_name_mapping_dictionary_defination[key]))
                                document.getElementById(response[i]['row_in_pad_modal'] + '_' + field_name_mapping_dictionary_defination[key]).value = response[i][key];
                            if (key == 'pad_name') document.getElementById('Pad_Name').value = response[i][key];
                        } 
                    }                
				}
				document.getElementById('load_type_curve').value = '';
				console.log("Success in ajaxing production volume to modal.");
				//call function which will place data in all input boxes for the modal
			},
			error: function(error){
				console.log("Error!");
				alert('Error! Please contact application support.');
			}
		});
		//end of jquery for AJAX call
	}
