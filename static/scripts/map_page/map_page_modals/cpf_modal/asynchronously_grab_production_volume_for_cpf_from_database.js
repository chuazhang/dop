function Asynchronously_Grab_Production_Volume_From_Database(id_of_double_clicked_cell) {
		//... ..- -- . ... ....
		//jqeury for AJAX call		
		$.ajax({
			url: '/asynchronously_grab_production_volume_from_database',
			data: id_of_double_clicked_cell,
			type: 'POST',
			success: function(response){
                // clear the table 
                var START_TR = 2; 
                for (var i = START_TR; i < $('#Production_volume_table tr').length; i++) { 
                    for (var j = 3; j <= 6; j++) { 
                        $('#Production_volume_table tr').eq(i).find('td').eq(j).find('input').val(''); 
                    } 
                } 
                document.getElementById('Pad_Name').value = ''; 
                // alert(JSON.stringify(response)); 
                for (var i = 0; i < response.length; i++) { 
                    //alert(response[i]); 
                    for (var key in response[i]) { 
                        // check if the property/key is defined in the object itself, not in parent 
                        //alert(id_of_double_clicked_cell == response[i]['cell_id']); 
                        if (response[i].hasOwnProperty(key) && id_of_double_clicked_cell == response[i]['cell_id']) { 
                            //alert(key); 
                            //alert(response[i][key]); 
                            if (key == 'forecasted_date') {  
                                $('#Production_volume_table tr').eq(i+START_TR).find('td').eq(2).find('input').val(response[i][key]);
                            } else if (key == 'injected_steam') { 
                                $('#Production_volume_table tr').eq(i+START_TR).find('td').eq(5).find('input').val(response[i][key]);
                            } else if (key == 'produced_gas') { 
                                $('#Production_volume_table tr').eq(i+START_TR).find('td').eq(6).find('input').val(response[i][key]);
                            } else if (key == 'produced_oil') { 
                                $('#Production_volume_table tr').eq(i+START_TR).find('td').eq(3).find('input').val(response[i][key]);
                            } else if (key == 'produced_water') { 
                                $('#Production_volume_table tr').eq(i+START_TR).find('td').eq(4).find('input').val(response[i][key]);
                            } else if (key == 'pad_name') { 
                                document.getElementById('Pad_Name').value = response[i][key]; 
                            } 
                        } 
                    }                
                }
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