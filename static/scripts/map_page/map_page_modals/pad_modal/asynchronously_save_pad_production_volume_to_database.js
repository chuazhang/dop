
$(function Asynchronously_Save_Pad_Production_Volume_To_Database(){
	var frm = $('#pad_production_volume_information_form');

	frm.submit(
		function(e){
			e.preventDefault();
			$.ajax({
				url: '/asynchronously_save_pad_production_volume_to_database',
				data: $('#pad_production_volume_information_form').serialize(),
				type: 'POST',
				success: function(response){
					console.log(response);
					var save_check_mark=document.getElementById('pad_production_volume_modal_save_check_mark')
					save_check_mark.style.display='inline';
					setTimeout(function(){
						save_check_mark.style.display='none';
					},2000);
				},
				error: function(error){
					console.log("There is an error with saving the pad production volume data to database.");
					alert('There is an error. Please contact application support');
				}
			});
	});
});
