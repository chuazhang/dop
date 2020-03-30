Listener_For_Add_Remove_User_Defined_Buttons(document.getElementById('add_user_defined_column_image'), 
    document.getElementById('remove_user_defined_column_image'),
    document.getElementById('Production_volume_table'), document.getElementById('PadModal'));

function Listener_For_Add_Remove_User_Defined_Buttons(elem_add, elem_remove, tab, modal) {
    if (elem_add) {
        elem_add.addEventListener('click',function (event) {
            elem_remove.style.display = 'block';
            var colCount = 0; // table row cell index start from 0 so colCount need to minus one and we are turn on next 
            for (var i = 0; i < tab.rows[0].cells.length; i++) {
                if (window.getComputedStyle(tab.rows[0].cells[i]).display !== "none")
                    colCount++;
            }
            for (var i = 0; i < tab.rows.length; i++) {
                tab.rows[i].cells[colCount - 1].style.display = 'table-cell';
            }
            if (colCount >= (tab.rows[0].cells.length - 1)) {
                elem_add.style.display = 'none';
            } 
        });
    }
    if (elem_remove) {
        elem_remove.addEventListener('click',function (event) {
            elem_add.style.display = 'block';
            var colCount = -1; // table row cell index start from 0 so colCount need to minus one and we are turn off current
            for (var i = 0; i < tab.rows[0].cells.length; i++) {
                if (window.getComputedStyle(tab.rows[0].cells[i]).display !== "none")
                    colCount++;
            }
            for (var i = 0; i < tab.rows.length; i++) {
                tab.rows[i].cells[colCount - 1].style.display = 'none';
            }
            if (colCount <= (tab.rows[0].cells.length - 3)) {
                elem_remove.style.display = 'none';
            } 
        });
    }
}
