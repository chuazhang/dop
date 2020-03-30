from flask import request,session
from create_and_migrate_db import db, Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class

def Asynchronously_Save_Type_Curve_Production_Volume_To_Database_Backend():
	
	#return "Type Curve Pad production volume data has been saved to database"

	#loop to go through each row of row, grab corresponding data and save data in database
	list_of_rows=list(range(1,8)) 

	for row in list_of_rows:
		scenario_id_forecast_belongs_to=session.get('scenario_id','error! there should always be a scenario number')
		type_curve_type=request.form['type_curve_type']
		row_in_pad_modal=row
		forecasted_month=request.form['Type_Curve_'+str(row)+'_Forecasted_Month']
		produced_oil=request.form['Type_Curve_'+str(row)+'_Produced_Oil']
		produced_water=request.form['Type_Curve_'+str(row)+'_Produced_Water']
		injected_steam=request.form['Type_Curve_'+str(row)+'_Injected_Steam']
		produced_gas=request.form['Type_Curve_'+str(row)+'_Produced_Gas']
		user_defined_column_1_value=request.form['Type_Curve_'+str(row)+'_User_Defined_Column_1_Value']
		user_defined_column_2_value=request.form['Type_Curve_'+str(row)+'_User_Defined_Column_2_Value']
		user_defined_column_3_value=request.form['Type_Curve_'+str(row)+'_User_Defined_Column_3_Value']
		pad_specific_row_object=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.query\
			.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.scenario_id_forecast_belongs_to==scenario_id_forecast_belongs_to)\
			.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.type_curve_type==type_curve_type)\
			.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.row_in_pad_modal==row_in_pad_modal)\
			.first()
		if pad_specific_row_object is None:
			new_pad_specific_row_object_to_add=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class(
				scenario_id_forecast_belongs_to=scenario_id_forecast_belongs_to,
				type_curve_type=type_curve_type,
				row_in_pad_modal=row_in_pad_modal,
				forecasted_month=forecasted_month,
				produced_oil=produced_oil,
				produced_water=produced_water,
				injected_steam=injected_steam,
				produced_gas=produced_gas,
				user_defined_column_1_value=user_defined_column_1_value,
				user_defined_column_2_value=user_defined_column_2_value,
				user_defined_column_3_value=user_defined_column_3_value)
			db.session.add(new_pad_specific_row_object_to_add)
			db.session.commit()
		else:
			# using if condition and updating values in object insteading of deleting and adding values. This is done so that we can implement undo redo feature down the road
			pad_specific_row_object.scenario_id_forecast_belongs_to=scenario_id_forecast_belongs_to
			pad_specific_row_object.type_curve_type=type_curve_type
			pad_specific_row_object.row_in_pad_modal=row_in_pad_modal
			pad_specific_row_object.forecasted_month=forecasted_month
			pad_specific_row_object.produced_oil=produced_oil
			pad_specific_row_object.produced_water=produced_water
			pad_specific_row_object.injected_steam=injected_steam
			pad_specific_row_object.produced_gas=produced_gas
			pad_specific_row_object.user_defined_column_1_value=user_defined_column_1_value
			pad_specific_row_object.user_defined_column_2_value=user_defined_column_2_value
			pad_specific_row_object.user_defined_column_3_value=user_defined_column_3_value
			db.session.commit()

	return 'Type Curve data has been saved to database'
