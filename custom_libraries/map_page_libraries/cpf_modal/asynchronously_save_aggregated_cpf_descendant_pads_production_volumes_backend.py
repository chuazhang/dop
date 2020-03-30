from create_and_migrate_db import db, Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class

def Asynchronously_Save_Aggregated_CPF_Descendant_Pads_Production_Volumes_Backend(scenario_id,cpf_id,cpf_name,list_of_dates_in_aggregated_production_volume_for_cpf,aggregated_produced_oil_dict,aggregated_produced_water_dict,aggregated_injected_steam_dict,aggregated_produced_gas_dict,aggregated_user_defined_column_1_value_dict,aggregated_user_defined_column_2_value_dict,aggregated_user_defined_column_3_value_dict):
	
	row_in_cpf_modal=1
	
	for forecasted_date in list_of_dates_in_aggregated_production_volume_for_cpf:
		cpf_specific_row_object=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.query\
			.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.scenario_id_forecast_belongs_to==scenario_id)\
			.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.cell_id==cpf_id)\
			.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.row_in_cpf_modal==row_in_cpf_modal)\
			.first()
		
		if cpf_specific_row_object is None:
			new_cpf_specific_row_object_to_add=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class(
				scenario_id_forecast_belongs_to=scenario_id,
				cell_id=cpf_id,
				cpf_name=cpf_name,
				row_in_cpf_modal=row_in_cpf_modal,
				forecasted_date=forecasted_date,
				aggregated_produced_oil=aggregated_produced_oil_dict.get(forecasted_date,0),
				aggregated_produced_water=aggregated_produced_water_dict.get(forecasted_date,0),
				aggregated_injected_steam=aggregated_injected_steam_dict.get(forecasted_date,0),
				aggregated_produced_gas=aggregated_produced_gas_dict.get(forecasted_date,0),
				aggregated_user_defined_column_1_value=aggregated_user_defined_column_1_value_dict.get(forecasted_date,0),
				aggregated_user_defined_column_2_value=aggregated_user_defined_column_2_value_dict.get(forecasted_date,0),
				aggregated_user_defined_column_3_value=aggregated_user_defined_column_3_value_dict.get(forecasted_date,0))
			db.session.add(new_cpf_specific_row_object_to_add)
			db.session.commit()
		else:
			cpf_specific_row_object.scenario_id_forecast_belongs_to=scenario_id
			cpf_specific_row_object.cell_id=cpf_id
			cpf_specific_row_object.cpf_name=cpf_name
			cpf_specific_row_object.row_in_cpf_modal=row_in_cpf_modal
			cpf_specific_row_object.forecasted_date=forecasted_date
			cpf_specific_row_object.aggregated_produced_oil=aggregated_produced_oil_dict.get(forecasted_date,0)
			cpf_specific_row_object.aggregated_produced_water=aggregated_produced_water_dict.get(forecasted_date,0)
			cpf_specific_row_object.aggregated_injected_steam=aggregated_injected_steam_dict.get(forecasted_date,0)
			cpf_specific_row_object.aggregated_produced_gas=aggregated_produced_gas_dict.get(forecasted_date,0)
			cpf_specific_row_object.aggregated_user_defined_column_1_value=aggregated_user_defined_column_1_value_dict.get(forecasted_date,0)
			cpf_specific_row_object.aggregated_user_defined_column_2_value=aggregated_user_defined_column_2_value_dict.get(forecasted_date,0)
			cpf_specific_row_object.aggregated_user_defined_column_3_value=aggregated_user_defined_column_3_value_dict.get(forecasted_date,0)
			db.session.commit()
		row_in_cpf_modal+=1

	return 'cpf production volume data has been saved to database'