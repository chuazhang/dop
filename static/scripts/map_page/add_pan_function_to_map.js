function Add_Pan_Function_To_Map(graph) {
    graph.setPanning(true);
    mxPanningHandler.prototype.isPanningTrigger = function(me) {
        var evt = me.getEvent();
        return true;
    };
    graph.panningHandler.ignoreCell = false;
    graph.panningHandler.addListener(mxEvent.PAN_START, function() { 
        graph.container.style.cursor = 'move';
    });
    graph.panningHandler.addListener(mxEvent.PAN_END, function() { 
        graph.container.style.cursor = 'default'; 
    });
}