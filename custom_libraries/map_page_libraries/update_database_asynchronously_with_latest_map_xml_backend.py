from bs4 import BeautifulSoup

from create_and_migrate_db import db, mxGraph_Cells_Table_Class,Cell_Id_And_Capacity_Table_Class

def Update_Database_Asynchronously_With_Latest_Map_XML_Backend(xml_data):
	soup = BeautifulSoup(xml_data, 'xml')
	list_of_all_cell_tags = soup.findAll('mxCell')
	list_of_cell_types=[]
	list_of_cell_ids=[]
	list_of_cell_asset_type=[]
	list_of_cell_source=[]
	list_of_cell_target=[]
	for cell_tag in list_of_all_cell_tags:
		if (cell_tag.get('vertex')) is not None:
			vertex_or_edge='vertex'
			cell_tag_id=cell_tag.get('id')
			asset_type=cell_tag.get('value')
			fake_source='FN_in_'+str(cell_tag_id)
			fake_target='FN_out_'+str(cell_tag_id)
		elif (cell_tag.get('edge')) is not None:
			vertex_or_edge='edge'
			cell_tag_id=cell_tag.get('id')
			asset_type=cell_tag.get('value')
			real_source=cell_tag.get('source')
			real_target=cell_tag.get('target')
			fake_source='FN_out_'+str(real_source)
			fake_target='FN_in_'+str(real_target)
		else:
			continue
		list_of_cell_types.append(vertex_or_edge)
		list_of_cell_ids.append(cell_tag_id)
		list_of_cell_asset_type.append(asset_type)
		list_of_cell_source.append(fake_source)
		list_of_cell_target.append(fake_target)

	list_of_lists_zip=zip(list_of_cell_ids,list_of_cell_asset_type,list_of_cell_types,list_of_cell_source,list_of_cell_target)
	Delete_Rows_Of_mxGraph_Tables_In_Database(db=db)
	Update_mxGraph_Tables_In_Database(db=db,list_of_lists_zip=list_of_lists_zip)
	#return christ

def Delete_Rows_Of_mxGraph_Tables_In_Database(db):
	mxGraph_Cells_Table_Class.query.delete()
	db.session.commit()

def Update_mxGraph_Tables_In_Database(db,list_of_lists_zip):
	for cell_id, asset_type, cell_type, cell_source, cell_target in list_of_lists_zip:
		cell_object_to_add=mxGraph_Cells_Table_Class(
			cell_id=cell_id,
			vertex_or_edge=cell_type,
			asset_type=asset_type,
			source=cell_source,
			target=cell_target
		)
		db.session.add(cell_object_to_add)
		#specific_cell_database_object=mxGraph_Cells_Table_Class.query.filter(mxGraph_Cells_Table_Class.cell_id==cell_id).first()
		db.session.commit()
		#updating or adding tuples in Cell_Id_And_Capacity_Table_Class
		specific_cell_id_and_capacity_table_object=Cell_Id_And_Capacity_Table_Class.query.filter(Cell_Id_And_Capacity_Table_Class.cell_id==cell_id).first()
		if specific_cell_id_and_capacity_table_object is None:
			cell_object_to_add=Cell_Id_And_Capacity_Table_Class(
				cell_id=cell_id)
			db.session.add(cell_object_to_add)
			db.session.commit()




	
