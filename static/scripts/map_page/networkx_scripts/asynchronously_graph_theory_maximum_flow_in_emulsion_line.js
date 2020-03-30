function Asynchronously_Graph_Theory_Maximum_Flow_In_Emulsion_Line(id_of_double_clicked_cell) {
	//alert(id_of_double_clicked_cell);
	//jqeury for AJAX call		
	$.ajax({
		url: '/asynchronously_graph_theory_maximum_flow',
		data: id_of_double_clicked_cell,
		type: 'POST',
		success: function(response){
			console.log("Maximum flow has been found.")
			//console.log(response)
			//var graph_analysis_span=document.getElementById('graph_theory_analysis_span');
			//graph_analysis_span.style.display="inline";
			//document.getElementById('actual_possible_maximum_throughput_span').innerText=response;
			//setTimeout(function(){
				//graph_analysis_span.style.display='none';
			//},2000);
		},
		error: function(error){
			console.log("Error with finding maximum flow.");
			alert('Error! Please contact application support.');
		}
	});
	//end of jquery for AJAX call
}
