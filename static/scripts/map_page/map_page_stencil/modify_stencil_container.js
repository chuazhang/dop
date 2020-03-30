function Modify_Stencil_Container(tbContainer, container) {
    tbContainer.style.top = '110px';
    tbContainer.style.padding = '0px';
    tbContainer.style.width = '100px';
    tbContainer.style.background = "#EAEFF5";
    tbContainer.style.boxShadow = "5px 5px 5px grey";
    tbContainer.style.position = 'absolute';
    tbContainer.style.overflow = 'hidden';
    tbContainer.style.left = '0px';
    tbContainer.style.bottom = '0px';

    container.style.top = '70px';
    container.style.left = '104px';
    container.style.position = 'absolute';
	container.style.overflow = 'hidden';
	container.style.right = '0px';
	container.style.bottom = '0px';
	container.style.background = 'url("static/images/map_page/grid.gif")';
    container.addEventListener ("click", function() {
        if ($(".sidebar-item").hasClass('active')) {
            $('#hamburger_menu_business_submenu').hide();
            $('#hamburger_menu_analysis_submenu').hide();
            $('#hamburger_menu_workflow_submenu').hide();        
            document.getElementById('hamburger_menu_business_arrow').innerHTML = '&rtrif;';
            document.getElementById('hamburger_menu_analysis_arrow').innerHTML = '&rtrif;';
            document.getElementById('hamburger_menu_workflow_arrow').innerHTML = '&rtrif;';
            $(".button").toggleClass("active");
            $("main").toggleClass("move-to-left");
            $(".sidebar-item").toggleClass("active");
        }
    });
}