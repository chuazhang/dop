function Modify_Stencil_Arrow(tbContainer, container) {
    // Add label to tbContainer
    var stencil_label = document.createElement("Label");
    stencil_label.style.color = "white";
    stencil_label.style.background = "#005596";
    stencil_label.style.position = 'absolute';
    stencil_label.style.top = '70px';
    stencil_label.style.left = '0px';
    stencil_label.style.width = '100px';
    stencil_label.style.padding = "6px";
    stencil_label.style.font="bold 25px arial,serif";
    stencil_label.innerHTML = "Stencil";
    document.body.appendChild(stencil_label);

    var left_panel_arrow = document.createElement('button');
    left_panel_arrow.style.position = 'absolute';
    left_panel_arrow.style.top = '70px';
    left_panel_arrow.style.left = '101px';
    left_panel_arrow.style.border = '0px';
    left_panel_arrow.style.margin = '0px';
    left_panel_arrow.style.padding = '0px';
    left_panel_arrow.style.width = '20px';
    left_panel_arrow.style.height = '40px';
    left_panel_arrow.style.border = '1px solid black';
    left_panel_arrow.style.outline = 0;
    left_panel_arrow.style.webkitBoxShadow = 'none';
    left_panel_arrow.style.background = 'white';
    left_panel_arrow.style.boxShadow = 'none';
    left_panel_arrow.style.borderRadius = '0px';
    left_panel_arrow.innerHTML = "&#9664;";
    left_panel_arrow.title = "Collapse / Expand left side menu";
    left_panel_arrow.addEventListener ("click", function() {
        if (tbContainer.style.display == null || tbContainer.style.display == "none") {
            tbContainer.style.display = "block";
            container.style.left = '104px';
            left_panel_arrow.innerHTML = "&#9664;";
            left_panel_arrow.style.left = '101px';
            stencil_label.style.display = 'block';
        } else {
            tbContainer.style.display = "none";
            container.style.left = '0px';
            left_panel_arrow.innerHTML = "&#9654;";
            left_panel_arrow.style.left = '0px';
            stencil_label.style.display = 'none';
        }
    });
    document.body.appendChild(left_panel_arrow);
}