function Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes(id_of_double_clicked_cell) {
		//... ..- -- . ... ....
		//jqeury for AJAX call		
		
		$.ajax({
			url: '/asynchronously_aggegrate_all_cpf_descendant_pads_production_volumes',
			data: id_of_double_clicked_cell,
			type: 'POST',
			success: function(response){
				// the code below will go to "asynchronously_grab_production_volume_for_cpf_from_database" in future
                table = document.getElementById('cpf_modal_production_volume_table'); 
				var input_nodes = table.getElementsByTagName('INPUT');
				for(var i = 0; i < input_nodes.length; ++i){
					if (input_nodes[i].id.indexOf('user_defined_column') == -1)
						input_nodes[i].value = '';
				}
				document.getElementById('CPF_Name').value = '';
				

                for (var i = 0; i < response.length; i++) { 
                    for (var key in response[i]) { 
                        if (response[i].hasOwnProperty(key) && id_of_double_clicked_cell == response[i]['cell_id']) { 
                            if (document.getElementById('cpf_modal_' + response[i]['row_in_cpf_modal'] + '_' + field_name_mapping_dictionary_defination[key]))
                                document.getElementById('cpf_modal_' + response[i]['row_in_cpf_modal'] + '_' + field_name_mapping_dictionary_defination[key]).value = response[i][key];
                            if (key == 'cpf_name') document.getElementById('CPF_Name').value = response[i][key];
                        } 
                    }                
                }
    
				console.log("Success in aggregating all CPF descendant pads production volume to database.");
				//call function which will place data in all input boxes for the modal
			},
			error: function(error){
				console.log("Error!");
				alert('Error! Please contact application support.');
			}
		});
		//end of jquery for AJAX call
	}