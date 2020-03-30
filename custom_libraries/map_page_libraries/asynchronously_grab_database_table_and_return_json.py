from flask import jsonify
from create_and_migrate_db import Pad_Forecasted_Volumes_Tables_Class, Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class, Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class, mxGraph_Cells_Table_Class

def Asynchronously_Grab_Database_Table_And_Return_JSON_Backend(id):
	database_objects = None
	if id.isdigit():
		specific_cell_database_object=mxGraph_Cells_Table_Class.query.filter(mxGraph_Cells_Table_Class.cell_id==id).first()
		if specific_cell_database_object is None:
			return ""
		asset_type=specific_cell_database_object.asset_type
		if asset_type == "Pad":
			database_objects=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.cell_id==id).all()
		elif asset_type == "CPF":
			database_objects=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.query.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.cell_id==id).all()
	else: # id is type curve type
		database_objects=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.query.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.type_curve_type==id).all()
	database_object_dictionary_list = []
	for database_object_record in database_objects:
		database_object_record_dictionary = {}
		if database_object_record:
			database_object_record_dictionary = dict(database_object_record.__dict__)
			database_object_record_dictionary.pop('_sa_instance_state',None)
		database_object_dictionary_list.append(database_object_record_dictionary)
	return jsonify(database_object_dictionary_list)
