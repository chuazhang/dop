function Asynchronously_Graph_Production_Volume_For_CPF_Modal(){

	var cpf_modal_graph_tab_graph_div= document.getElementById("cpf_modal_graph_tab_graph_div");
	cpf_modal_graph_tab_graph_div.innerText= "Please wait while we generate the latest graph for you.. "

	$.ajax({
		url: '/asynchronously_graph_production_volume_for_cpf_modal',
		data: $('#cpf_modal_production_volume_information_form').serialize(),
		type: 'POST',
		success: function(response){
			$("#cpf_modal_graph_tab_graph_div").html(response);
			$("#cpf_modal_graph_tab_graph_div").find("script").each(function(){
				eval($(this).text());
			});
			console.log('Success in generating graph for the cpf modal!');
		},
		error: function(error){
			console.log("There is an error with saving the cpf production volume data to database.");
			alert('There is an error. Please contact application support');
			}
		});
	};
