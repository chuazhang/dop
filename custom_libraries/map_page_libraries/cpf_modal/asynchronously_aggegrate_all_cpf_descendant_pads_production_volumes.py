from flask import request, session
import networkx as nx
from datetime import datetime as dt
from dateutil.relativedelta import *

#Custom Libraries
from custom_libraries.custom_networkx_libraries.generate_the_g_object_of_graph_for_networkx import Generate_The_G_Object_Of_Graph_For_Networkx
from custom_libraries.custom_networkx_libraries.translate_fn_to_cell_id import Translate_FN_To_Cell_ID
from custom_libraries.map_page_libraries.cpf_modal.asynchronously_save_aggregated_cpf_descendant_pads_production_volumes_backend import Asynchronously_Save_Aggregated_CPF_Descendant_Pads_Production_Volumes_Backend

from create_and_migrate_db import db,mxGraph_Cells_Table_Class,Cell_Id_And_Capacity_Table_Class, All_Users_Information_Table_Class,Pad_Forecasted_Volumes_Tables_Class


def Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes_Backend(cell_id_of_cpf_cell_selected):
    id_of_double_clicked_cell=cell_id_of_cpf_cell_selected
    id_of_double_clicked_cell=id_of_double_clicked_cell.decode("utf-8") 
    id_of_double_clicked_cell=int(id_of_double_clicked_cell)
    cell_id=id_of_double_clicked_cell
    #print(type(id_of_double_clicked_cell))
    #print(id_of_double_clicked_cell)
    cpf_name='' #will need to grab this somehow
    scenario_id=session.get('scenario_id','error! there should always be a scenario number')
    #scenario_id='5325x'
    fn_id_of_double_clicked_cell='FN_in_'+str(id_of_double_clicked_cell) #we can all it FN_in or FN_out, it doesn't matter
    
    G=Generate_The_G_Object_Of_Graph_For_Networkx()

    set_of_all_steam_line_descendant_nodes_for_the_cpf=nx.descendants(G.reverse(), fn_id_of_double_clicked_cell) #reserved the graph to give us steam line
    #print(str(set_of_all_steam_line_descendant_nodes_for_the_cpf))
    set_of_all_descendant_steam_line_PAD_nodes_for_the_cpf=Get_Set_Of_Pad_Nodes_From_Descendant_Nodes_Set(set_of_all_descendant_nodes_for_the_cpf=set_of_all_steam_line_descendant_nodes_for_the_cpf)
    #this will need to be changed later, but for now assume
    set_of_all_descendant_emulsion_line_PAD_nodes_for_the_cpf=set_of_all_descendant_steam_line_PAD_nodes_for_the_cpf
    
    #first find the earliest date amongst all dates
    try:
        earliest_date_in_string=Compare_Nodes_And_Get_The_Earliest_Date(scenario_id,set_of_all_descendant_emulsion_line_PAD_nodes_for_the_cpf)
    except:
        earliest_date_in_string=dt.today().strftime("%m/%d/%Y") #this is if there are no production volume data saved for any nodes    
    forecasted_date=earliest_date_in_string
    aggregated_produced_oil_dict={}
    aggregated_produced_water_dict={}
    aggregated_injected_steam_dict={}
    aggregated_produced_gas_dict={}
    aggregated_user_defined_column_1_value_dict={}
    aggregated_user_defined_column_2_value_dict={}
    aggregated_user_defined_column_3_value_dict={}

    number_of_months_in_aggegregated_production_volume_for_cpf=7
    list_of_rows_in_aggregated_production_volume_for_cpf=range(number_of_months_in_aggegregated_production_volume_for_cpf)
    list_of_dates_in_aggregated_production_volume_for_cpf=[]

    for row in list_of_rows_in_aggregated_production_volume_for_cpf:
        list_of_dates_in_aggregated_production_volume_for_cpf.append(forecasted_date)
        date_in_dt_object=dt.strptime(forecasted_date, "%m/%d/%Y")
        next_date_in_dt_object=date_in_dt_object+relativedelta(months=1)
        next_date_in_dt_object_in_string=next_date_in_dt_object.strftime("%m/%d/%Y")
        forecasted_date=next_date_in_dt_object_in_string

    #print(str(set_of_all_descendant_emulsion_line_PAD_nodes_for_the_cpf))

    for forecasted_date in list_of_dates_in_aggregated_production_volume_for_cpf:

        aggregated_oil_so_far_for_this_forecasted_date=0 #to reset the value for each new forecasted date
        aggregated_produced_water_so_far_for_this_forecasted_date=0
        aggregated_injected_steam_so_far_for_this_forecasted_date=0
        aggregated_produced_gas_so_far_for_this_forecasted_date=0
        aggregated_user_defined_column_1_value_so_far_for_this_forecasted_date=0
        aggregated_user_defined_column_2_value_so_far_for_this_forecasted_date=0
        aggregated_user_defined_column_3_value_so_far_for_this_forecasted_date=0


        for pad_node_id in set_of_all_descendant_emulsion_line_PAD_nodes_for_the_cpf:
            tuple_object_for_specific_descendant_node=Pad_Forecasted_Volumes_Tables_Class.query\
                .filter(Pad_Forecasted_Volumes_Tables_Class.scenario_id_forecast_belongs_to==scenario_id)\
                .filter(Pad_Forecasted_Volumes_Tables_Class.cell_id==pad_node_id)\
                .filter(Pad_Forecasted_Volumes_Tables_Class.forecasted_date==forecasted_date)\
                .first()

            # CHECK VALUES IF IT EXISTS, AND IF IT DOESN'T  GIVE ZERO 
            # THIS BLOCK CAN GO TO A SEPERATE FUNCTION LATER

            if tuple_object_for_specific_descendant_node is None: #this means there is no tuple for particule forecasted date in the node (cell)
                pass
            else:
                new_node_produced_oil_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.produced_oil or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_oil_so_far_for_this_forecasted_date += new_node_produced_oil_value_for_the_forecasted_date
                new_node_produced_water_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.produced_water or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_produced_water_so_far_for_this_forecasted_date += new_node_produced_water_value_for_the_forecasted_date
                new_node_injected_steam_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.injected_steam or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_injected_steam_so_far_for_this_forecasted_date += new_node_injected_steam_value_for_the_forecasted_date
                new_node_produced_gas_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.produced_gas or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_produced_gas_so_far_for_this_forecasted_date += new_node_produced_gas_value_for_the_forecasted_date
                new_node_user_defined_column_1_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.user_defined_column_1_value or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_user_defined_column_1_value_so_far_for_this_forecasted_date += new_node_user_defined_column_1_value_for_the_forecasted_date
                new_node_user_defined_column_2_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.user_defined_column_2_value or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_user_defined_column_2_value_so_far_for_this_forecasted_date += new_node_user_defined_column_2_value_for_the_forecasted_date
                new_node_user_defined_column_3_value_for_the_forecasted_date = int(tuple_object_for_specific_descendant_node.user_defined_column_3_value or 0) # 'or 0' is used to parse empty string, using this means empty strings will show as 0
                aggregated_user_defined_column_3_value_so_far_for_this_forecasted_date += new_node_user_defined_column_3_value_for_the_forecasted_date
            
            aggregated_produced_oil_dict[forecasted_date] = aggregated_oil_so_far_for_this_forecasted_date
            aggregated_produced_water_dict[forecasted_date] = aggregated_produced_water_so_far_for_this_forecasted_date
            aggregated_injected_steam_dict[forecasted_date] = aggregated_injected_steam_so_far_for_this_forecasted_date
            aggregated_produced_gas_dict[forecasted_date] = aggregated_produced_gas_so_far_for_this_forecasted_date
            aggregated_user_defined_column_1_value_dict[forecasted_date] = aggregated_user_defined_column_1_value_so_far_for_this_forecasted_date
            aggregated_user_defined_column_2_value_dict[forecasted_date] = aggregated_user_defined_column_2_value_so_far_for_this_forecasted_date
            aggregated_user_defined_column_3_value_dict[forecasted_date] = aggregated_user_defined_column_3_value_so_far_for_this_forecasted_date
            #END OF CHECK VALUES IF IT EXISTS, AND IF IT DOESN'T  GIVE ZERO
    
    #print(aggregated_produced_oil_dict)
            

    message=Asynchronously_Save_Aggregated_CPF_Descendant_Pads_Production_Volumes_Backend(scenario_id=scenario_id,\
        cpf_id=id_of_double_clicked_cell,\
            cpf_name=cpf_name,\
            list_of_dates_in_aggregated_production_volume_for_cpf=list_of_dates_in_aggregated_production_volume_for_cpf,\
        aggregated_produced_oil_dict=aggregated_produced_oil_dict,\
            aggregated_produced_water_dict=aggregated_produced_water_dict,\
            aggregated_injected_steam_dict=aggregated_injected_steam_dict,\
            aggregated_produced_gas_dict=aggregated_produced_gas_dict,\
                aggregated_user_defined_column_1_value_dict=aggregated_user_defined_column_1_value_dict,\
                    aggregated_user_defined_column_2_value_dict=aggregated_user_defined_column_2_value_dict,\
                        aggregated_user_defined_column_3_value_dict=aggregated_user_defined_column_3_value_dict
        )
    return message

    
def Get_Set_Of_Pad_Nodes_From_Descendant_Nodes_Set(set_of_all_descendant_nodes_for_the_cpf):
    set_of_all_descendant_PAD_nodes_for_the_cpf=set() 
    for fn_node in set_of_all_descendant_nodes_for_the_cpf:
        cell_id_of_decendent_node=Translate_FN_To_Cell_ID(fn_node)
        #print(type(cell_id_of_decendent_node))
        #print(str(cell_id_of_decendent_node))
        specific_node_information_object=mxGraph_Cells_Table_Class.query.filter(mxGraph_Cells_Table_Class.cell_id==cell_id_of_decendent_node).first()
        if specific_node_information_object.asset_type=='Pad':
            set_of_all_descendant_PAD_nodes_for_the_cpf.add(cell_id_of_decendent_node)
    
    return set_of_all_descendant_PAD_nodes_for_the_cpf

def Compare_Nodes_And_Get_The_Earliest_Date(scenario_id,set_of_all_descendant_emulsion_line_PAD_nodes_for_the_cpf):
    cell_id_and_first_date_dictionary={}
    list_of_dates=[]
    for pad_node_id in set_of_all_descendant_emulsion_line_PAD_nodes_for_the_cpf:
        try:
            specific_cell_first_row_database_object=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.cell_id==pad_node_id)\
                .filter(Pad_Forecasted_Volumes_Tables_Class.scenario_id_forecast_belongs_to==scenario_id)\
                .filter(Pad_Forecasted_Volumes_Tables_Class.row_in_pad_modal==1).first()
            cell_id_and_first_date_dictionary[specific_cell_first_row_database_object.cell_id]=specific_cell_first_row_database_object.forecasted_date
            date_in_dt_object=dt.strptime(specific_cell_first_row_database_object.forecasted_date, "%m/%d/%Y")
            list_of_dates.append(date_in_dt_object) #captial Y for four digit year
            earliest_date=min(list_of_dates)
            earliest_date_in_string=earliest_date.strftime("%m/%d/%Y")
        except:
            pass
    return earliest_date_in_string
