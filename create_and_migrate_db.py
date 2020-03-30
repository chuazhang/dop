#.. these functions:
#.. python create_and_migrate_db.py db init  <-to create database originally
#.. python create_and_migrate_db.py db migrate <- to update the original database with new schemas
#.. python create_and_migrate_db.py db upgrate <- to push the update onto the original database
#.. if copying this for another web app, don't forget to copy the "if __name__:" part at the end

#reference: https://www.youtube.com/watch?v=BAOfjPuVby0

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager=Manager(app)

manager.add_command('db',MigrateCommand)

#<DATABASE STARTS HERE:>
class mxGraph_Cells_Table_Class(db.Model):
	__tablename__='mxGraph_cells_table'
	cell_id=db.Column(db.Integer,primary_key=True)
	vertex_or_edge=db.Column(db.String(100))
	asset_type=db.Column(db.String(100))
	source=db.Column(db.String(100))
	target=db.Column(db.String(100))

#this table is needed as the mxGraph table gets wiped clean and remade everytime we add a new cell
class Cell_Id_And_Capacity_Table_Class(db.Model):
	__tablename__='cell_id_and_capacity_table'
	cell_id=db.Column(db.Integer,primary_key=True)
	capacity=db.Column(db.Integer)
	actual_possible_maximum_throughput=db.Column(db.Integer)

class All_Users_Information_Table_Class(db.Model):
	__tablename__='user_information_table'
	user_unique_id=db.Column(db.String,primary_key=True)
	user_name=db.Column(db.String,unique=True)
	hashed_password=db.Column(db.String)

class Pad_Forecasted_Volumes_Tables_Class(db.Model):
	__tablename__='pad_forecasted_volumes_table'
	unique_id=db.Column(db.Integer,primary_key=True)
	scenario_id_forecast_belongs_to=db.Column(db.String(200))
	cell_id=db.Column(db.Integer)
	pad_name=db.Column(db.String(50))
	row_in_pad_modal=db.Column(db.Integer)
	forecasted_date=db.Column(db.String(50))
	produced_oil=db.Column(db.Integer)
	produced_water=db.Column(db.Integer)
	injected_steam=db.Column(db.Integer)
	produced_gas=db.Column(db.Integer)
	user_defined_column_1_value=db.Column(db.Integer)
	user_defined_column_2_value=db.Column(db.Integer)
	user_defined_column_3_value=db.Column(db.Integer)

class Aggregated_CPF_Descendant_Pads_Production_Volumes_Tables_Class(db.Model):
	__tablename__='aggregated_cpf_descendant_pads_production_volumes_table'
	unique_id=db.Column(db.Integer,primary_key=True)
	scenario_id_forecast_belongs_to=db.Column(db.String(200))
	cell_id=db.Column(db.Integer)
	cpf_name=db.Column(db.String(50))
	row_in_cpf_modal=db.Column(db.Integer)
	forecasted_date=db.Column(db.String(50))
	aggregated_produced_oil=db.Column(db.Integer)
	aggregated_produced_water=db.Column(db.Integer)
	aggregated_injected_steam=db.Column(db.Integer)
	aggregated_produced_gas=db.Column(db.Integer)
	aggregated_user_defined_column_1_value=db.Column(db.Integer)
	aggregated_user_defined_column_2_value=db.Column(db.Integer)
	aggregated_user_defined_column_3_value=db.Column(db.Integer)

class Pad_Forecasted_Type_Curves_Volumes_For_Specific_Scenario_Tables_Class(db.Model):
	__tablename__='pad_forecasted_type_curves_volumes_for_specific_scenario_table'
	unique_id=db.Column(db.Integer,primary_key=True)
	scenario_id_forecast_belongs_to=db.Column(db.String(200))
	type_curve_type=db.Column(db.String(50))
	row_in_pad_modal=db.Column(db.Integer)
	forecasted_month=db.Column(db.String(50))
	produced_oil=db.Column(db.Integer)
	produced_water=db.Column(db.Integer)
	injected_steam=db.Column(db.Integer)
	produced_gas=db.Column(db.Integer)
	user_defined_column_1_value=db.Column(db.Integer)
	user_defined_column_2_value=db.Column(db.Integer)
	user_defined_column_3_value=db.Column(db.Integer)
#<END OF DATABASE>

if __name__=='__main__':
	manager.run()