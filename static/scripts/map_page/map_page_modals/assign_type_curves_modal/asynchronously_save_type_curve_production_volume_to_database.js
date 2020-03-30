
$(function Asynchronously_Save_Type_Curve_Pad_Production_Volume_To_Database(){
	var frm = $('#type_curve_pad_production_volume_information_form');

	frm.submit(
		function(e){
			e.preventDefault();
			//alert('Saving Type Curve now');
			$.ajax({
				url: '/asynchronously_save_type_curve_production_volume_to_database',
				data: $('#type_curve_pad_production_volume_information_form').serialize(),
				type: 'POST',
				success: function(response){
					console.log(response);
					var save_check_mark=document.getElementById('type_curve_pad_production_volume_modal_save_check_mark')
					save_check_mark.style.display='inline';
					setTimeout(function(){
						save_check_mark.style.display='none';
					},2000);
				},
				error: function(error){
					console.log("There is an error with saving the type curve data to database.");
					alert('There is an error. Please contact application support');
				}
			});
	});
});
