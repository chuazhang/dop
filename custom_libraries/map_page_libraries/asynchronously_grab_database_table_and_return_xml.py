from create_and_migrate_db import Pad_Forecasted_Volumes_Tables_Class, Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class, Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class, mxGraph_Cells_Table_Class

def Asynchronously_Grab_Database_Table_And_Return_XML_Backend(id):
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
	xmlString = '<?xml version="1.0" encoding="utf-16"?><root>'
	for database_object_record in database_objects:
		database_object_record_dictionary = {}
		if database_object_record:
			database_object_record_dictionary = dict(database_object_record.__dict__)
			database_object_record_dictionary.pop('_sa_instance_state',None)
		for key in database_object_record_dictionary.keys():
			xmlString += "<"
			xmlString += str(key)
			xmlString += ">"
			xmlString += str(database_object_record_dictionary[key])
			xmlString += "</"
			xmlString += str(key)
			xmlString += ">"
	xmlString += "</root>"
	return xmlString
