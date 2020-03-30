from flask import request

#database libraries
from create_and_migrate_db import Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class, Cell_Id_And_Capacity_Table_Class

def Get_CPF_X_And_Y_Axis_Data_For_Graph():
    #all the tuples for the specific pad is queries
    id_of_double_clicked_cell=request.form['cell_id_of_cpf_cell_selected']
    forecasted_date_x_axis_data_list=[]
    produced_oil_y_axis_data_list=[]
    produced_water_y_axis_data_list=[]
    injected_steam_y_axis_data_list=[]
    produced_gas_y_axis_data_list=[]
    emulsion_y_axis_data_list=[]
    actual_possible_maximum_throughput_emulsion_y_axis_data_list=[]
    specific_cell_database_objects=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.query.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.cell_id==id_of_double_clicked_cell).all()
    specific_cell_capacity_object=Cell_Id_And_Capacity_Table_Class.query.filter(Cell_Id_And_Capacity_Table_Class.cell_id==id_of_double_clicked_cell).first()
    for specific_cell_db_object in specific_cell_database_objects:
        forecasted_date_x_axis_data_list.append(specific_cell_db_object.forecasted_date)
        produced_oil_y_axis_data_list.append(specific_cell_db_object.aggregated_produced_oil)
        produced_water_y_axis_data_list.append(specific_cell_db_object.aggregated_produced_water)
        injected_steam_y_axis_data_list.append(specific_cell_db_object.aggregated_injected_steam)
        produced_gas_y_axis_data_list.append(specific_cell_db_object.aggregated_produced_gas)
        actual_possible_maximum_throughput_emulsion_y_axis_data_list.append(specific_cell_capacity_object.actual_possible_maximum_throughput)
        
        #generating emulsion data 
        produced_oil_for_this_date=specific_cell_db_object.aggregated_produced_oil
        produced_water_for_this_date=specific_cell_db_object.aggregated_produced_water
        if produced_oil_for_this_date=="":
            produced_oil_for_this_date=None
        else:
            #converting from bbl/day to m3/day
            produced_oil_for_this_date=round(0.158987*produced_oil_for_this_date,0)
        if produced_water_for_this_date=="":
            produced_water_for_this_date=None 
        emulsion_y_axis_data_for_this_date= Sum_Args_With_None(produced_oil_for_this_date,produced_water_for_this_date)
        emulsion_y_axis_data_list.append(emulsion_y_axis_data_for_this_date)

    dict_of_x_and_y_axis_data_for_graph={
        'forecasted_date_x_axis_data_list':forecasted_date_x_axis_data_list,
        'produced_oil_y_axis_data_list':produced_oil_y_axis_data_list,
        'produced_water_y_axis_data_list':produced_water_y_axis_data_list,
        'injected_steam_y_axis_data_list':injected_steam_y_axis_data_list,
        'produced_gas_y_axis_data_list':produced_gas_y_axis_data_list,
        'emulsion_y_axis_data_list':emulsion_y_axis_data_list,
        'actual_possible_maximum_throughput_emulsion_y_axis_data_list':actual_possible_maximum_throughput_emulsion_y_axis_data_list
        }
    return (dict_of_x_and_y_axis_data_for_graph)

#this helps sum args with None in it 
def Sum_Args_With_None(*args):
    args = [a for a in args if not a is None]
    return sum(args) if args else None 