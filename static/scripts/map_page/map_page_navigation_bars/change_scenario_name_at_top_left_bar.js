$(document).ready(function () {
    $('#scenario_name_label').on('click', function (e) {
		change_scenario_name();
    });
    $('#scenario_name_pencil').on('click', function (e) {
		change_scenario_name();
    });
    $('#scenario_name_input').on('blur', function (e) {
		scenario_input_change_to_label();
    });
    $('#base_scenario_name_label').on('click', function (e) {
        document.getElementById('BaseCaseModal').style.display='block';
    });
    $('#select_scenario_name').on('change', function (e) {
		document.getElementById('base_scenario_name_label').innerHTML = document.getElementById("select_scenario_name").value;
    });
});

function change_scenario_name() {
	document.getElementById('scenario_name_label').style.display = 'none';
	document.getElementById('scenario_name_pencil').style.display = 'none';
	document.getElementById('scenario_name_input').style.display = 'block';
	document.getElementById('scenario_name_input').value = document.getElementById('scenario_name_label').textContent;
	document.getElementById('scenario_name_input').focus();
}

function scenario_input_change_to_label() {
	document.getElementById('scenario_name_label').innerHTML = document.getElementById('scenario_name_input').value;
	document.getElementById('scenario_name_label').style.display = 'block';
	document.getElementById('scenario_name_pencil').style.display = 'block';
	document.getElementById('scenario_name_input').style.display = 'none';
}
