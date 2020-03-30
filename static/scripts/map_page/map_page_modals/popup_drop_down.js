$(document).ready(function () {
    $('#type_curve_export_drop_down').on('mouseover', function () {
        document.getElementById("type_curve_export_drop_down_div").style.display = 'block';
    });
    $('#type_curve_export_drop_down_wrapper').on('mouseleave', function () {
        document.getElementById("type_curve_export_drop_down_div").style.display = 'none';
    });
    $('#type_curve_export_drop_down_excel').on('click', function () {
        document.getElementById("type_curve_export_drop_down_div").style.display = 'none';
        generate_api('type_curve', 'Excel');
    });
    $('#type_curve_export_drop_down_csv').on('click', function () {
        document.getElementById("type_curve_export_drop_down_div").style.display = 'none';
        generate_api('type_curve', 'CSV');
    });
    $('#type_curve_export_drop_down_json').on('click', function () {
        document.getElementById("type_curve_export_drop_down_div").style.display = 'none';
        generate_api('type_curve', 'JSON');
    });
    $('#type_curve_export_drop_down_xml').on('click', function () {
        document.getElementById("type_curve_export_drop_down_div").style.display = 'none';
        generate_api('type_curve', 'XML');
    });
});
  