from create_and_migrate_db import db, mxGraph_Cells_Table_Class,Cell_Id_And_Capacity_Table_Class,Pad_Forecasted_Volumes_Tables_Class, Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class,Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class

def Delete_All_Data_Related_To_Specific_Scenario(scenario_id):
    mxGraph_Cells_Table_Class.query.delete()
    Cell_Id_And_Capacity_Table_Class.query.delete()
    try:
        specific_cell_database_objects=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.scenario_id_forecast_belongs_to==scenario_id).delete()
    except:
        pass
    try:
        specific_cell_database_objects=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.query.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.scenario_id_forecast_belongs_to==scenario_id).delete()
    except:
        pass
    try:
        specific_cell_database_objects=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.query.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.scenario_id_forecast_belongs_to==scenario_id).delete()
    except:
        pass
    
    #removing all unassigned scenario id data
    try:
        specific_cell_database_objects=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.scenario_id_forecast_belongs_to=='error! there should always be a scenario number').delete()
    except:
        pass
    
    try:
        specific_cell_database_objects=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.query.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.scenario_id_forecast_belongs_to=='error! there should always be a scenario number').delete()
    except:
        pass

    db.session.commit()