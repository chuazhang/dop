// copy clipboard data from Excel or other to pad table
$(document).ready(function () {
    $('#Production_volume_table td input').on('paste', function (e) {
        $txt = $(this);
        setTimeout(function () {
            var data = null;
            if (navigator.userAgent.indexOf('MSIE')!==-1 || navigator.appVersion.indexOf('Trident/') > -1) {
                data = window.clipboardData.getData("Text");
                paste_data_to_pad(data, $txt, document.getElementById('Production_volume_table'));
            } else {
                navigator.clipboard.readText().then(function(data) {
                    paste_data_to_pad(data, $txt, document.getElementById('Production_volume_table'));
                })
            }
        }, 0);
    });
    $('#type_curve_Production_volume_table td input').on('paste', function (e) {
        $txt = $(this);
        setTimeout(function () {
            var data = null;
            if (navigator.userAgent.indexOf('MSIE')!==-1 || navigator.appVersion.indexOf('Trident/') > -1) {
                data = window.clipboardData.getData("Text");
                paste_data_to_pad(data, $txt, document.getElementById('type_curve_Production_volume_table'));
            } else {
                navigator.clipboard.readText().then(function(data) {
                    paste_data_to_pad(data, $txt, document.getElementById('type_curve_Production_volume_table'));
                })
            }
        }, 0);
    });
});

function paste_data_to_pad(data, $txt, table) {
    if (data == null) return;

    var curRowIndex = $txt.parent().parent().index();
    var curColIndex = $txt.parent().index(); 
    var totalRows = table.rows.length;
    var totalCols = table.rows[3].cells.length;
    var rows = data.split('\n');
    for (i = 0; i < rows.length; i++) {
        if ((rows[i] == null) || (rows[i].trim().length <= 0)) continue;
        var cells = rows[i].split(/\s+/);
        if (((i+curRowIndex) <= totalRows) && (cells.length > 0)) {
            for (j = 0; j < cells.length; j++) {
                if ((cells[j] == null) || (cells[j].trim().length <= 0)) continue;
                if ((j+curColIndex) <= totalCols) {
                    table.rows[i+curRowIndex].cells[j+curColIndex].children[0].value = cells[j];
                }
            }
        }
    }
}