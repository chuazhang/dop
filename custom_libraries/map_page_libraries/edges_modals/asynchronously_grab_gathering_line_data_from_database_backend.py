from flask import request
from create_and_migrate_db import Cell_Id_And_Capacity_Table_Class

def Asynchronously_Grab_Gathering_Line_Data_From_Database_Backend():
    id_of_double_clicked_cell=request.get_data()
    id_of_double_clicked_cell=int(id_of_double_clicked_cell)
    specific_cell_database_object=Cell_Id_And_Capacity_Table_Class.query.filter(Cell_Id_And_Capacity_Table_Class.cell_id==id_of_double_clicked_cell).first()
    if specific_cell_database_object is None:
        specific_cell_database_object_capacity=""
    else:
        specific_cell_database_object_capacity=specific_cell_database_object.capacity
    return str(specific_cell_database_object_capacity)