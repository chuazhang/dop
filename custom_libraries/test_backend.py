from custom_libraries.custom_networkx_libraries.generate_the_g_object_of_graph_for_networkx import Generate_The_G_Object_Of_Graph_For_Networkx
from custom_libraries.custom_networkx_libraries.translate_fn_to_cell_id import Translate_FN_To_Cell_ID
import networkx as nx

from flask import request
from create_and_migrate_db import db,mxGraph_Cells_Table_Class,Cell_Id_And_Capacity_Table_Class, All_Users_Information_Table_Class,Pad_Forecasted_Volumes_Tables_Class

#def Get_X_And_Y_Axis_Data_For_Graph():
def Test_Backend():
    #all the tuples for the specific pad is queries
    #id_of_double_clicked_cell=request.form['cell_id_of_pad_cell_selected']
    id_of_double_clicked_cell=2
    forecasted_date_y_axis_data_list=[]
    produced_oil_y_axis_data_list=[]
    produced_water_y_axis_data_list=[]
    injected_steam_y_axis_data_list=[]
    produced_gas_data_y_axis_data_list=[]
    specific_cell_database_objects=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.cell_id==id_of_double_clicked_cell).all()
    for specific_cell_db_object in specific_cell_database_objects:
        forecasted_date_y_axis_data_list.append(specific_cell_db_object.forecasted_date)
        produced_oil_y_axis_data_list.append(specific_cell_db_object.produced_oil)
        produced_water_y_axis_data_list.append(specific_cell_db_object.produced_water)
        injected_steam_y_axis_data_list.append(specific_cell_db_object.injected_steam)
        produced_gas_data_y_axis_data_list.append(specific_cell_db_object.produced_gas)
    dict_of_x_and_y_axis_data_for_graph={
        'forecasted_date_y_axis_data_list':forecasted_date_y_axis_data_list,
        'produced_oil_y_axis_data_list':produced_oil_y_axis_data_list,
        'produced_water_y_axis_data_list':produced_water_y_axis_data_list,
        'injected_steam_y_axis_data_list':injected_steam_y_axis_data_list,
        'produced_gas_data_y_axis_data_list':produced_gas_data_y_axis_data_list
        }
    return (dict_of_x_and_y_axis_data_for_graph)

def Test_Backend1():
    G=Generate_The_G_Object_Of_Graph_For_Networkx()
    G=nx.reverse(G)
    all_reachable_nodes_list=nx.descendants(G,'FN_in_3') #we will get list in FN format, not cell id
    all_reachable_nodes_cell_id_list=[]
    for node in all_reachable_nodes_list:
        node_cell_id=Translate_FN_To_Cell_ID(node)
        if node_cell_id not in all_reachable_nodes_cell_id_list:
            all_reachable_nodes_cell_id_list.append(node_cell_id)
    return str(all_reachable_nodes_cell_id_list)