$(document).ready(function () {
    $('#asset_summary_emulsion_radio').on('click', function (e) {
		openTabsInModal(e, 'asset_summary_tab', 'asset_summary_tablink', 'asset_summary_emulsion');
	});
    $('#asset_summary_steam_radio').on('click', function (e) {
		openTabsInModal(e, 'asset_summary_tab', 'asset_summary_tablink', 'asset_summary_steam');
	});

	$('#cpf_production_volume_tab_button').on('click', function (e) {
		openTabsInModal(e,'cpf_tab','cpf_tablink','CPF_Production_Volume_Tab');
	});
	$('#cpf_charts_tab_button').on('click', function (e) {
		openTabsInModal(e,'cpf_tab','cpf_tablink','CPF_Charts_Tab');
		Asynchronously_Graph_Production_Volume_For_CPF_Modal();
	});
	$('#cpf_capex_and_opex_tab_button').on('click', function (e) {
		openTabsInModal(e,'cpf_tab','cpf_tablink','CPF_CAPEX_and_OPEX');
	});
	$('#cpf_export_tab_button').on('click', function (e) {
		openTabsInModal(e,'cpf_tab','cpf_tablink','CPF_Export_Tab');
	});

	$('#pad_production_volume_tab_button').on('click', function (e) {
		openTabsInModal(e,'pad_tab','pad_tablink','Production_Volume_Tab');
	});
	$('#pad_charts_tab_button').on('click', function (e) {
		openTabsInModal(e,'pad_tab','pad_tablink','Charts_Tab');
		Asynchronously_Graph_Production_Volume_For_Pad_Modal();
	});
	$('#pad_outage_dates_tab_button').on('click', function (e) {
		openTabsInModal(e,'pad_tab','pad_tablink','Outage_Dates_Tab');
	});
	$('#pad_export_tab_button').on('click', function (e) {
		openTabsInModal(e,'pad_tab','pad_tablink','Export_Tab');
	});
});

function openTabsInModalFunc(curTab, tab, link, Tab_Name) {
	var i, x, tablinks;
	x = document.getElementsByClassName(tab);
	for (i = 0; i < x.length; i++) {
	  x[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName(link);
	for (i = 0; i < x.length; i++) {
    tablinks[i].style.backgroundColor = "F0F0F0";
    tablinks[i].style.color = "black";
	}
	document.getElementById(Tab_Name).style.display = "block";
	curTab.style.backgroundColor = "#005596";
	curTab.style.color = "white";
}

function openTabsInModal(evt, tab, link, Tab_Name) {
	openTabsInModalFunc(evt.currentTarget, tab, link, Tab_Name);
}