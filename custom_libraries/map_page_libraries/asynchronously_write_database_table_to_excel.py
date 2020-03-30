import xlsxwriter
import csv
from create_and_migrate_db import Pad_Forecasted_Volumes_Tables_Class, Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class, Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class

def Asynchronously_Grab_Database_Table_And_Write_To_Excel_File_Backend(params):
	parameters=params.split(',')
	if parameters[0] == "pad":
		database_objects=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.cell_id==int(parameters[1])).all()
	elif parameters[0] == "cpf":
		database_objects=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.query.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.cell_id==int(parameters[1])).all()
	elif parameters[0] == "type_curve":
		database_objects=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.query.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.type_curve_type==parameters[1]).all()
	else:
		return 'Database data failed save in Excel file'
	if (parameters[3] == "Excel"):
		Write_Database_Table_To_Xlsx(database_objects, parameters[2]) 
	elif (parameters[3] == "CSV"):
		Write_Database_Table_To_CSV(database_objects, parameters[2]) 
	return 'Database data successfully saved in Excel file'

def Write_Database_Table_To_Xlsx(database_objects, filename):
	workbook = xlsxwriter.Workbook(filename)
	worksheet = workbook.add_worksheet()
	row = 0
	for database_object_record in database_objects:
		database_object_record_dictionary = {}
		if database_object_record:
			database_object_record_dictionary = dict(database_object_record.__dict__)
			database_object_record_dictionary.pop('_sa_instance_state',None)
			if (row == 0):
				col = 0
				for cells in database_object_record_dictionary:
					worksheet.write(row, col, cells)
					col += 1
				row += 1
			col = 0
			for cells in database_object_record_dictionary:
				worksheet.write(row, col, database_object_record_dictionary[cells])
				col += 1
			row += 1
	workbook.close()

def Write_Database_Table_To_CSV(database_objects, filename):
	with open(filename, 'w', newline='') as file:
		writer = csv.writer(file)
		row = 0
		for database_object_record in database_objects:
			database_object_record_dictionary = {}
			if database_object_record:
				database_object_record_dictionary = dict(database_object_record.__dict__)
				database_object_record_dictionary.pop('_sa_instance_state',None)
				if (row == 0):
					writer.writerow(database_object_record_dictionary)
				writer.writerow(database_object_record_dictionary.values())
				row += 1
