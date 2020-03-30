function ModifyEdgeStyle(source, target, style, value) {
    style = "";
    value = "";
    if (source == null || target == null || source.value == null || target.value == null) {
        style = "strokeColor=#C05046;labelBackgroundColor=#FFFFFF;fontFamily=Tahoma;strokeWidth=3;";
        value = "Not Connected";
    } else if ((source.value.indexOf('CPF') >= 0 && target.value.indexOf('Hub') >= 0) || (source.value.indexOf('CPF') >= 0 && target.value.indexOf('Pad') >= 0) || (source.value.indexOf('Hub') >= 0 && target.value.indexOf('Pad') >= 0)) {
        style = "strokeColor=#4BACC6;labelBackgroundColor=#FFFFFF;fontFamily=Tahoma;strokeWidth=3;";
        value = "Steam";
    } else if ((source.value.indexOf('Hub') >= 0 && target.value.indexOf('CPF') >= 0) || (source.value.indexOf('Pad') >= 0 && target.value.indexOf('Hub') >= 0) || (source.value.indexOf('Pad') >= 0 && target.value.indexOf('CPF') >= 0)) {
        style = "strokeColor=#9DBB61;labelBackgroundColor=#FFFFFF;fontFamily=Tahoma;strokeWidth=3;";
        value = "Emulsion";
    } else if (source.value.indexOf('CPF') >= 0 && target.value.indexOf('CPF') >= 0) {
        style = "strokeColor=#9DBB61;labelBackgroundColor=#FFFFFF;fontFamily=Tahoma;strokeWidth=3;";
        value = "Emulsion";
    }
    return [style, value];
}
function Update_Edge_Label_After_Connection_With_Another_Node_And_Edge_Color_Accordingly(graph) {
    mxConnectionHandler.prototype.connectImage = new mxImage('static/images/map_page/connector.gif', 16, 16);
    mxConnectionHandlerInsertEdge = mxConnectionHandler.prototype.insertEdge;
    mxConnectionHandler.prototype.insertEdge = function(parent, id, value, source, target, style)
    {
        style = graph.getStylesheet().getDefaultEdgeStyle();
        style[mxConstants.STYLE_CURVED] = '1';
        var values = ModifyEdgeStyle(source, target, style, value);
        style = values[0]; value = values[1];
        return mxConnectionHandlerInsertEdge.apply(this, arguments);
    };
    mxEdgeHandlerConnect = mxEdgeHandler.prototype.connect;
    mxEdgeHandler.prototype.connect = function(	edge, terminal, isSource, isClone, me ) {
        mxEdgeHandlerConnect.apply(this, arguments);
        var values = ModifyEdgeStyle(edge.source, edge.target, edge.style, edge.value);
        edge.style = values[0]; edge.value = values[1];
        graph.refresh(edge);
    }
    mxEdgeHandlerChangeTerminalPoint = mxEdgeHandler.prototype.changeTerminalPoint;
    mxEdgeHandler.prototype.changeTerminalPoint = function(	edge, point, isSource, isClone, me ) {
        mxEdgeHandlerChangeTerminalPoint.apply(this, arguments);
        var values = ModifyEdgeStyle(edge.source, edge.target, edge.style, edge.value);
        edge.style = values[0]; edge.value = values[1];
        graph.refresh(edge);
    }
};