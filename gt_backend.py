from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask_bcrypt import Bcrypt #for password hashing
from os import urandom

#CUSTOM LIBRARIES

#Log In Page Libraries
from custom_libraries.log_in_page_libraries.log_in_page_backend import Log_In_Page_Backend

#Map Page Libraries
from custom_libraries.map_page_libraries.update_database_asynchronously_with_latest_map_xml_backend import Update_Database_Asynchronously_With_Latest_Map_XML_Backend
from custom_libraries.map_page_libraries.pad_modal.asynchronously_save_pad_production_volume_to_database_backend import Asynchronously_Save_Pad_Production_Volume_To_Database_Backend
from custom_libraries.map_page_libraries.assign_type_curves_modal.asynchronously_save_type_curve_production_volume_to_database_backend import Asynchronously_Save_Type_Curve_Production_Volume_To_Database_Backend
from custom_libraries.map_page_libraries.cpf_modal.asynchronously_aggegrate_all_cpf_descendant_pads_production_volumes import Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes_Backend
from custom_libraries.map_page_libraries.edges_modals.asynchronously_save_constraints_to_database_backend import Asynchronously_Save_Constraints_To_Database_Backend
from custom_libraries.map_page_libraries.edges_modals.asynchronously_grab_gathering_line_data_from_database_backend import Asynchronously_Grab_Gathering_Line_Data_From_Database_Backend
from custom_libraries.custom_networkx_libraries.asynchronously_graph_theory_maximum_flow_in_emulsion_line_backend import Asynchronously_Graph_Theory_Maximum_Flow_In_Emulsion_Line_Backend
from custom_libraries.map_page_libraries.pad_modal.create_pad_graph import Create_Pad_Graph
from custom_libraries.map_page_libraries.cpf_modal.create_cpf_graph import Create_CPF_Graph

from custom_libraries.map_page_libraries.asynchronously_summarize_asset_connections_and_save_to_svg_backend import Asynchronously_Summarize_Asset_Connections_And_Save_To_SVG_Backend
from custom_libraries.map_page_libraries.asynchronously_write_database_table_to_excel import Asynchronously_Grab_Database_Table_And_Write_To_Excel_File_Backend
from custom_libraries.map_page_libraries.asynchronously_grab_database_table_and_return_json import Asynchronously_Grab_Database_Table_And_Return_JSON_Backend
from custom_libraries.map_page_libraries.asynchronously_grab_database_table_and_return_xml import Asynchronously_Grab_Database_Table_And_Return_XML_Backend
from custom_libraries.map_page_libraries.asynchronously_send_email_through_smtp import Asynchronously_Send_Email_Through_SMTP

#Test Library
from custom_libraries.test_backend import Test_Backend

#ADMIN LIBRARIES
from custom_libraries.admin_libraries.admin_dashboard_backend import Admin_Dashboard_Backend
from custom_libraries.admin_libraries.add_new_user_backend import Add_New_User_Backend
from custom_libraries.admin_libraries.list_all_users_backend import List_All_Users_Backend

#database libraries
from flask_sqlalchemy import SQLAlchemy #for database ORM
from config import Config
from create_and_migrate_db import db,mxGraph_Cells_Table_Class,Cell_Id_And_Capacity_Table_Class, All_Users_Information_Table_Class,Pad_Forecasted_Volumes_Tables_Class, Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class, Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class
from custom_libraries.custom_database_functionality_libraries.delete_all_data_related_to_specific_scenario import Delete_All_Data_Related_To_Specific_Scenario

app=Flask(__name__)
app.secret_key = urandom(12)
bcrypt = Bcrypt(app) #for password hashing
app.config.from_object(Config)
db=SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def Log_In_Page():
	return Log_In_Page_Backend(bcrypt=bcrypt)

@app.route('/home_page', methods=['GET','POST'])
def Home_Page():
	logged_in_user=session.get('user_name','') 
	is_the_user_logged_in=session.get('logged_in',False)
	session['scenario_id'] = '5325x' #this will be automatically generated for each scenario
	
	if (logged_in_user!='') and (is_the_user_logged_in==True):
		logged_in_user_object=All_Users_Information_Table_Class.query.filter(All_Users_Information_Table_Class.user_name==logged_in_user).first()
		Delete_All_Data_Related_To_Specific_Scenario(scenario_id=session.get('scenario_id','error! there should always be a scenario number'))
		list_of_rows=list(range(1,8))
		return render_template('home_page/map_page.html', list_of_rows=list_of_rows, logged_in_user_object=logged_in_user_object)	
	else:
		return redirect(url_for('Log_In_Page'))
	
@app.route('/log_out', methods=['GET','POST'])
def Log_Out():
	session['logged_in'] = False
	return redirect(url_for('Home_Page'))

@app.route('/admin_page', methods=['GET','POST'])
def Admin_Page():
	return Admin_Dashboard_Backend()

@app.route('/admin_page/add_new_user', methods=['GET','POST'])
def Add_New_User():
	return Add_New_User_Backend(bcrypt=bcrypt)

@app.route('/admin_page/list_all_users', methods=['GET','POST'])
def List_All_Users():
	return List_All_Users_Backend()


#START OF AJAX CALLS FUNCTIONS
@app.route('/update_database_asynchronously_with_latest_map_xml_page', methods=['POST'])
def Update_Database_Asynchronously_With_Latest_Map_XML():
	xml_data=request.get_data()
	Update_Database_Asynchronously_With_Latest_Map_XML_Backend(xml_data)
	return 'done!'

@app.route('/asynchronously_save_pad_production_volume_to_database', methods=['POST'])
def Asynchronously_Save_Pad_Production_Volume_To_Database():
	success_message=Asynchronously_Save_Pad_Production_Volume_To_Database_Backend()
	return success_message

@app.route('/asynchronously_grab_production_volume_from_database', methods=['POST'])
def Asynchronously_Grab_Production_Volume_From_Database():
	id_of_double_clicked_cell=request.get_data()
	id_of_double_clicked_cell=int(id_of_double_clicked_cell)
	#all the tuples for the specific pad is queried
	specific_cell_database_objects=Pad_Forecasted_Volumes_Tables_Class.query.filter(Pad_Forecasted_Volumes_Tables_Class.cell_id==id_of_double_clicked_cell).all()
	ary = []
	for cell in specific_cell_database_objects:
		dictret = {}
		if cell:
			dictret = dict(cell.__dict__)
			dictret.pop('_sa_instance_state',None)
			#print(dictret)
		ary.append(dictret)
	return jsonify(ary)

@app.route('/asynchronously_grab_database_table_and_write_to_excel_file', methods=['POST'])
def Asynchronously_Grab_Database_Table_And_Write_To_Excel_File():
	return Asynchronously_Grab_Database_Table_And_Write_To_Excel_File_Backend(request.get_data().decode("utf-8"))

@app.route('/EXPORT/JSON/<id>', methods=['GET','POST'])
def Asynchronously_Grab_Database_Table_And_Return_JSON(id):
	return Asynchronously_Grab_Database_Table_And_Return_JSON_Backend(id)

@app.route('/EXPORT/XML/<id>', methods=['GET','POST'])
def Asynchronously_Grab_Database_Table_And_Return_XML(id):
	return Asynchronously_Grab_Database_Table_And_Return_XML_Backend(id)

@app.route('/asynchronously_save_constraints_to_database', methods=['POST'])
def Asynchronously_Save_Constraints_To_Database():
	Asynchronously_Save_Constraints_To_Database_Backend()
	return 'Asset constraints data has been saved to database'

@app.route('/asynchronously_grab_gathering_line_data_from_database', methods=['POST'])
def Asynchronously_Grab_Gathering_Line_Data_From_Database():
	specific_cell_database_object_capacity=Asynchronously_Grab_Gathering_Line_Data_From_Database_Backend()
	return specific_cell_database_object_capacity

@app.route('/asynchronously_save_type_curve_production_volume_to_database', methods=['POST'])
def Asynchronously_Save_Type_Curve_Production_Volume_To_Database():
	success_message=Asynchronously_Save_Type_Curve_Production_Volume_To_Database_Backend()
	return success_message

@app.route('/asynchronously_grab_type_curve_production_volume_from_database', methods=['POST'])
def Asynchronously_Grab_Type_Curve_Production_Volume_From_Database():
	type_curve_type=request.get_data()
	type_curve_type=type_curve_type.decode("utf-8")
	database_object_records_for_selected_type_curve=Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.query.filter(Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class.type_curve_type==type_curve_type).all()
	database_object_dictionary_list = []
	for database_object_record in database_object_records_for_selected_type_curve:
		database_object_record_dictionary = {}
		if database_object_record:
			database_object_record_dictionary = dict(database_object_record.__dict__)
			database_object_record_dictionary.pop('_sa_instance_state',None)
		database_object_dictionary_list.append(database_object_record_dictionary)
	return jsonify(database_object_dictionary_list)

@app.route('/asynchronously_aggegrate_all_cpf_descendant_pads_production_volumes', methods=['POST'])
def Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes():
	cell_id_of_cpf_cell_selected=request.get_data()
	success_message=Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes_Backend(cell_id_of_cpf_cell_selected)
	#return success_message
	#THE CODE BELOW SHOULD BE IN asynchronously_grab_aggregated_cpf_data_from_database
	cell_id_of_cpf_cell_selected=cell_id_of_cpf_cell_selected.decode("utf-8") 
	cell_id_of_cpf_cell_selected=int(cell_id_of_cpf_cell_selected)
	database_object_records_for_selected_cpf=Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.query.filter(Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class.cell_id==cell_id_of_cpf_cell_selected).all()
	database_object_dictionary_list = []
	for database_object_record in database_object_records_for_selected_cpf:
		database_object_record_dictionary = {}
		if database_object_record:
			database_object_record_dictionary = dict(database_object_record.__dict__)
			database_object_record_dictionary.pop('_sa_instance_state',None)
		database_object_dictionary_list.append(database_object_record_dictionary)
	return jsonify(database_object_dictionary_list)


@app.route('/asynchronously_graph_production_volume_for_pad_modal', methods=['POST'])
def Asynchronously_Graph_Production_Volume_For_Pad_Modal():
	graph_div_data=Create_Pad_Graph()
	return graph_div_data

@app.route('/asynchronously_graph_production_volume_for_cpf_modal', methods=['POST'])
def Asynchronously_Graph_Production_Volume_For_CPF_Modal():
	graph_div_data=Create_CPF_Graph()
	return graph_div_data

@app.route('/asynchronously_graph_theory_maximum_flow', methods=['POST'])
def Asynchronously_Graph_Theory_Maximum_Flow():
	id_of_double_clicked_cell=request.get_data()
	id_of_double_clicked_cell=id_of_double_clicked_cell.decode("utf-8") 
	actual_possible_maximum_flow=Asynchronously_Graph_Theory_Maximum_Flow_In_Emulsion_Line_Backend(id_of_double_clicked_cell)
	return actual_possible_maximum_flow

@app.route('/asynchronously_summarize_asset_connections_and_save_to_svg', methods=['POST'])
def Asynchronously_Summarize_Asset_Connections_And_Save_To_SVG():
	return Asynchronously_Summarize_Asset_Connections_And_Save_To_SVG_Backend()

@app.route('/invite_user_send_email', methods=['POST'])
def Asynchronously_Send_Email():
	return Asynchronously_Send_Email_Through_SMTP(app, request.get_data().decode("utf-8"))

#END OF AJAX CALL FUNCTIONS

#test route to see if functions work
@app.route('/test', methods=['GET','POST'])
def Test():
	#id_of_double_clicked_cell=request.form['cell_id_of_pad_cell_selected']
	#return str(id_of_double_clicked_cell)
	a=Asynchronously_Aggegrate_All_CPF_Descendant_Pads_Production_Volumes_Backend()
	return a


# no cache is stored
# very useful in development ..
# .. as well as in production ..
# .. when new updates are made 
@app.after_request
def add_header(r):
	r.headers["Pragma"]="no-cache"
	r.headers["Expires"]="0"
	r.headers["Cache-Control"]="public, max-age=0"
	return r

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0', port=8080)
	#debug will be set to True once problem with Werkzeug is fixed