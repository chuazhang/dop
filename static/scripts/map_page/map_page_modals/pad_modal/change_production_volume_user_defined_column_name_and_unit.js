
for (var i = 1; i <= 3; i++) {
	Listener_For_User_Defined_Title_And_Unit_Buttons(
		document.getElementById('user_defined_column_table_' + i), 
		document.getElementById('user_defined_column_label_' + i),
		document.getElementById('user_defined_column_pencil_' + i),
		document.getElementById('user_defined_column_' + i));
	Listener_For_User_Defined_Title_And_Unit_Buttons(
		document.getElementById('user_defined_column_table_unit_' + i), 
		document.getElementById('user_defined_column_label_unit_' + i),
		document.getElementById('user_defined_column_pencil_unit_' + i),
		document.getElementById('user_defined_column_unit_' + i));
}

function Listener_For_User_Defined_Title_And_Unit_Buttons(table, label, pencil, input) {
    if (label) {
		label.addEventListener('click',function (event) {
			table.style.display = 'none';
			input.style.display = 'block';
			input.value = label.textContent;
			input.focus();
		});
    }
    if (pencil) {
		pencil.addEventListener('click',function (event) {
			table.style.display = 'none';
			input.style.display = 'block';
			input.value = label.textContent;
			input.focus();
		});
    }
    if (input) {
		input.addEventListener('blur',function (event) {
			label.innerHTML = input.value;
			table.style.display = 'block';
			input.style.display = 'none';
		});
    }
}
