
$(function Asynchronously_Save_Constraints_To_Database(){
	var frm = $('#emulsion_line_constraints_information_form');

	frm.submit(
		function(e){
			e.preventDefault();
			$.ajax({
				url: '/asynchronously_save_constraints_to_database',
				data: $('#emulsion_line_constraints_information_form').serialize(),
				type: 'POST',
				success: function(response){
					console.log(response);
					var save_check_mark=document.getElementById('emulsion_line_modal_save_check_mark')
					save_check_mark.style.display='inline';
					var cell_id_of_emulsion_line_cell_selected=document.getElementById('cell_id_of_emulsion_line_cell_selected').value;
					Asynchronously_Graph_Theory_Maximum_Flow_In_Emulsion_Line(cell_id_of_emulsion_line_cell_selected);
					setTimeout(function(){
						save_check_mark.style.display='none';
					},2000);
				},
				error: function(error){
					console.log("There is an error with saving the constraints to database.");
					alert('There is an error. Please contact application support');
				}
			});
	});
});

