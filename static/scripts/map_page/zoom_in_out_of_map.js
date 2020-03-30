function Zoom_In_Out_Of_Map(graph) {

    var zoomPanListener = function(view, evt) {
        console.log('In Zoom Pan Listener');
        var tr = evt.getProperty('translate');
        var oldTr = evt.getProperty('previousTranslate');

        var sc = evt.getProperty('scale');
        var oldSc = evt.getProperty('previousScale');
        
        var s = view.scale;
    }; 

    // Zoom In and Out Handlers	
    graph.view.addListener(mxEvent.SCALE_AND_TRANSLATE, zoomPanListener);
    graph.view.addListener(mxEvent.TRANSLATE, zoomPanListener);
    graph.view.addListener(mxEvent.SCALE, zoomPanListener);

	document.getElementById('zoomIn').addEventListener("click", function(){
		graph.zoomIn();
	});
	document.getElementById('zoomOut').addEventListener("click", function(view, evt){
		graph.zoomOut();				
    });
}