function update_database_asynchronously_with_latest_map_xml(graph) {
	var encoder = new mxCodec();
	var node = encoder.encode(graph.getModel());
	var graph_xml_data=mxUtils.getPrettyXml(node);

	//jqeury for AJAX call
	xml_data=mxUtils.getXml(node);
	xml_data=(xml_data.toString());
	//alert(xml_data);
	//console.log(xml_data);
	$.ajax({
		url: '/update_database_asynchronously_with_latest_map_xml_page',
		data: xml_data,
		type: 'POST',
		success: function(response){
			console.log('Success in ajaxing latest map xml to database');
		},
		error: function(error){
			console.log("There is an error!");
			alert("There is an error!")
		}
	});
	//end of jquery for AJAX call
	//alert(graph_xml_data);
}