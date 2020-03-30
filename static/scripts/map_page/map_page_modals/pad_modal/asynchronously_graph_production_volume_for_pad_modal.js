//alert('ola!');

function Asynchronously_Graph_Production_Volume_For_Pad_Modal(){

	var pad_modal_graph_tab_graph_div= document.getElementById("pad_modal_graph_tab_graph_div");
	pad_modal_graph_tab_graph_div.innerText= "Please wait while we generate the latest graph for you.. "

	$.ajax({
		url: '/asynchronously_graph_production_volume_for_pad_modal',
		data: $('#pad_production_volume_information_form').serialize(),
		type: 'POST',
		success: function(response){
			$("#pad_modal_graph_tab_graph_div").html(response);
			$("#pad_modal_graph_tab_graph_div").find("script").each(function(){
				eval($(this).text());
			});
			console.log('Success in generating graph for the pad modal!');
		},
		error: function(error){
			console.log("There is an error with saving the pad production volume data to database.");
			alert('There is an error. Please contact application support');
			}
		});
	};
