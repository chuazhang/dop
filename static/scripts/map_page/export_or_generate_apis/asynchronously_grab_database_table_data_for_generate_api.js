function getFormattedTime() {
    var today = new Date();
    return today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate() + "-" + today.getHours() + "-" + today.getMinutes() + "-" + today.getSeconds();
}
function downloadURI(uri, name) {
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    delete link;
  }
function generate_api(asset_type, format) {
    var id = "";
    if (asset_type == 'pad' || asset_type == 'cpf')
        id = document.getElementById('cell_id_of_' + asset_type + '_cell_selected').value;
    else if (asset_type == 'type_curve') {
        id = document.querySelectorAll('.type_curve_tablink.tab_selected')[0].textContent;
        if (id.length > 0) id = id[id.length - 1];
    }
    if (id.length <= 0) return;
    if (asset_type == 'pad' || asset_type == 'cpf')
        export_type = document.getElementById(asset_type + '_export_type').value;
    else
        export_type = format;
    if ((export_type == 'Excel') || (export_type == 'CSV')) {
        if (export_type == 'Excel') filename = getFormattedTime() + '.xlsx';
        else filename = getFormattedTime() + '.csv';
        parameters = asset_type + ',' + id + ',static/' + filename + ',' + export_type;
        $.ajax({
            url: '/asynchronously_grab_database_table_and_write_to_excel_file',
            data: parameters,
            type: 'POST',
            success: function(response){
                if (asset_type != 'type_curve') {
                    document.getElementById(asset_type + '_export_url').innerHTML = '<a href="' + window.location.origin + '/static/' + filename + '" target="_blank">' + filename + '</a>';
                } else {
                    if (export_type == 'Excel') {
                        var x = new XMLHttpRequest();
                        x.open("GET", window.location.origin + '/static/' + filename, true);
                        x.responseType = 'blob';
                        x.onload = function(e) { download(x.response, "type_curve.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" ); }
                        x.send();
                    } else if (export_type == 'CSV') {
                        $.ajax({
                            url: window.location.origin + '/static/' + filename, 
                            success: download.bind(true, "text/html", "type_curve.csv")
                        });
                    }
                }
                console.log("Success in exporting data to Excel file.");
            },
            error: function(error){
                console.log("Error!");
                alert('Error! Please contact application support.');
            }
        });
    } else if (export_type == 'JSON') {
        if (asset_type != 'type_curve')
            document.getElementById(asset_type + '_export_url').innerHTML = '<a href="EXPORT/JSON/' + id + '" target="_blank">' + window.location.origin + '/EXPORT/JSON/' + id + '</a>';
        else
            window.open('EXPORT/JSON/' + id);
    } else if (export_type == 'XML') {
        if (asset_type != 'type_curve')
            document.getElementById(asset_type + '_export_url').innerHTML = '<a href="EXPORT/XML/' + id + '" target="_blank">' + window.location.origin + '/EXPORT/XML/' + id + '</a>';
        else
            window.open('EXPORT/XML/' + id);
    }
}
$(document).ready(function () {
    $('#pad_export_type').on('change', function (e) { generate_api('pad', ''); });
    $('#cpf_export_type').on('change', function (e) { generate_api('cpf', ''); });
});