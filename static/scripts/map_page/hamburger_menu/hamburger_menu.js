$(document).ready(function () {
    function make_submenu_arrow_point_to_right() {
        document.getElementById('hamburger_menu_business_arrow').innerHTML = '&rtrif;';
        document.getElementById('hamburger_menu_analysis_arrow').innerHTML = '&rtrif;';
        document.getElementById('hamburger_menu_workflow_arrow').innerHTML = '&rtrif;';
    }

    function turn_off_hamburger_and_all_submenus() {
        $('#hamburger_menu_business_submenu').hide();
        $('#hamburger_menu_analysis_submenu').hide();
        $('#hamburger_menu_workflow_submenu').hide();
        make_submenu_arrow_point_to_right();        
        toggleSidebar();
    }

    function toggleSidebar() {
        $(".button").toggleClass("active");
        $("main").toggleClass("move-to-left");
        $(".sidebar-item").toggleClass("active");
    }
    
    $(".button").on("click tap", function() {
        $('#hamburger_menu_business_submenu').hide();
        $('#hamburger_menu_analysis_submenu').hide();
        $('#hamburger_menu_workflow_submenu').hide();        
        make_submenu_arrow_point_to_right();        
        toggleSidebar();
    });

    $('#hamburger_menu_business').on('click', function (e) {
        $('#hamburger_menu_business_submenu').toggle();
        make_submenu_arrow_point_to_right();        
        if ($('#hamburger_menu_business_submenu').is(':visible'))
            document.getElementById('hamburger_menu_business_arrow').innerHTML = '&dtrif;';
        $('#hamburger_menu_analysis_submenu').hide();
        $('#hamburger_menu_workflow_submenu').hide();        
    });
    $('#hamburger_business_save_scenario').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
        document.getElementById('SaveScenarioModal').style.display='block'; 
    });
    $('#hamburger_business_load_case').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
        document.getElementById('BaseCaseModal').style.display='block';
    });
    $('#hamburger_business_import_data').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
    });
    $('#hamburger_business_track_history').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
        document.getElementById('ChangeHistoryModal').style.display='block'; 
    });
    $('#hamburger_business_asset_summary').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
        Summarize_Asset_Connections();
    });
    $('#hamburger_business_type_curve').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
        document.getElementById('AssignTypeCurvesModal').style.display='block';
    });
    
    $('#hamburger_menu_analysis').on('click', function (e) {
        $('#hamburger_menu_business_submenu').hide();
        $('#hamburger_menu_analysis_submenu').toggle();
        make_submenu_arrow_point_to_right();        
        if ($('#hamburger_menu_analysis_submenu').is(':visible')) 
            document.getElementById('hamburger_menu_analysis_arrow').innerHTML = '&dtrif;';
        $('#hamburger_menu_workflow_submenu').hide();        
    });
    $('#hamburger_analysis_run_economics').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
    });

    $('#hamburger_menu_workflow').on('click', function (e) {
        $('#hamburger_menu_business_submenu').hide();
        $('#hamburger_menu_analysis_submenu').hide();
        $('#hamburger_menu_workflow_submenu').toggle();        
        make_submenu_arrow_point_to_right();        
        if ($('#hamburger_menu_workflow_submenu').is(':visible'))
            document.getElementById('hamburger_menu_workflow_arrow').innerHTML = '&dtrif;';
    });
    $('#hamburger_workflow_user_management').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
    });
    $('#hamburger_workflow_work_assignment').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
    });
    
    $('#hamburger_menu_profile').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
		document.getElementById('LogOutModal').style.display='block';
    });

    $('#hamburger_menu_invite').on('click', function (e) {
        turn_off_hamburger_and_all_submenus();
        document.getElementById('InviteUserModal').style.display='block';
    });
});
