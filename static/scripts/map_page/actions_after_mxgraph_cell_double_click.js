// Installs a handler for double click events in the graph
// that shows the pop up window
function actions_after_mxgraph_cell_double_click (sender,evt,graph) 
	{
		try 
			{
			var cell = evt.getProperty('cell');
			var id_of_double_clicked_cell=cell.id;
			var asset_type_of_double_clicked_cell=cell.value;
			
			//alert(id_of_double_clicked_cell);
			//most of the time, we will be using the cell id input box in the modals (since we are serializing the form), but sometimes we might need to use this
			document.getElementById('cell_id_of_cell_selected').value=id_of_double_clicked_cell;
			

			if (asset_type_of_double_clicked_cell=='Pad') {
				//alert('pad selected!');
				document.getElementById('cell_id_of_pad_cell_selected').value=id_of_double_clicked_cell; // this is needed for modals to work..
				// as the modals are based on cell id store modal values to respective tuple in database
				// ... ..- -- . ... ....
				document.getElementById('PadModal').style.display='block';
				openTabsInModalFunc(document.getElementById('pad_production_volume_tab_button'),'pad_tab','pad_tablink','Production_Volume_Tab');
				Asynchronously_Grab_Production_Volume_From_Database(id_of_double_clicked_cell);
			} else if (asset_type_of_double_clicked_cell=='CPF') {
				document.getElementById('cell_id_of_cpf_cell_selected').value=id_of_double_clicked_cell; // this is needed for modals to work..
				// as the modals are based on cell id store modal values to respective tuple in database
				// ... ..- -- . ... ....
				document.getElementById('CPFModal').style.display='block';
				openTabsInModalFunc(document.getElementById('cpf_production_volume_tab_button'),'cpf_tab','cpf_tablink','CPF_Production_Volume_Tab');
				Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes(id_of_double_clicked_cell);
				//Asynchronously_Grab_Production_Volume_From_Database(id_of_double_clicked_cell);
			} else {
				//alert(id_of_double_clicked_cell);
				document.getElementById('cell_id_of_emulsion_line_cell_selected').value=id_of_double_clicked_cell; // this is needed for modals to work..
				// as the modals are based on cell id store modal values to respective tuple in database
				// ... ..- -- . ... ....
				document.getElementById('EmulsionLineModal').style.display='block';
				Asynchronously_Grab_Gathering_Line_Data_From_Database(id_of_double_clicked_cell);
			}
			
			// changes the label of the cell to:
			//graph.model.setValue(cell, id_of_double_clicked_cell);
			
			//alert(id_of_double_clicked_cell);

			evt.consume();
			}
		
		catch (err) 
			{
			//pass - as doubleclicked on blank space in graph
			}
	};


function Asynchronously_Grab_Gathering_Line_Data_From_Database(id_of_double_clicked_cell) {
	//alert(id_of_double_clicked_cell);
	//... ..- -- . ... ....
	//jqeury for AJAX call		
	$.ajax({
		url: '/asynchronously_grab_gathering_line_data_from_database',
		data: id_of_double_clicked_cell,
		type: 'POST',
		success: function(response){
			document.getElementById('line_capacity').value=response;
			console.log("Success in ajaxing gathering line data to modal.");
		},
		error: function(error){
			console.log("Error!");
			alert('Error! Please contact application support.');
		}
	});
	//end of jquery for AJAX call
}

