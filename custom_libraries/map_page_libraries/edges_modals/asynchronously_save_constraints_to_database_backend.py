from flask import request
from create_and_migrate_db import db, Cell_Id_And_Capacity_Table_Class

def Asynchronously_Save_Constraints_To_Database_Backend():
	cell_id_of_cell_selected=request.form['cell_id_of_emulsion_line_cell_selected']
	line_capacity_value=request.form['line_capacity']
	specific_cell_database_object=Cell_Id_And_Capacity_Table_Class.query.filter(Cell_Id_And_Capacity_Table_Class.cell_id==cell_id_of_cell_selected).first()
	if specific_cell_database_object is None:
		new_cell_id_capacity_tuple_to_add=Cell_Id_And_Capacity_Table_Class(cell_id=cell_id_of_cell_selected,capacity=line_capacity_value)
		db.session.add(new_cell_id_capacity_tuple_to_add)
		db.session.commit()
	else:
		specific_cell_database_object.capacity=line_capacity_value
		db.session.commit()