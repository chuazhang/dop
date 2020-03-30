import networkx as nx

from custom_libraries.custom_networkx_libraries.generate_the_g_object_of_graph_for_networkx import Generate_The_G_Object_Of_Graph_For_Networkx
from create_and_migrate_db import db,mxGraph_Cells_Table_Class, Cell_Id_And_Capacity_Table_Class

def Asynchronously_Graph_Theory_Maximum_Flow_In_Emulsion_Line_Backend(id_of_double_clicked_cell):
	G=Generate_The_G_Object_Of_Graph_For_Networkx()


	cpf_objects=mxGraph_Cells_Table_Class.query.filter(mxGraph_Cells_Table_Class.asset_type=='CPF').all()

	for cpf_object in cpf_objects:
		CPF_source='FN_out_'+str(cpf_object.cell_id)
		G.add_edge(CPF_source,'Master_CPF')
		#Master_CPF is the fake CPF that connects with all CPFs in the graph
		#this is necessary to allow us to find maximum flow when CPFs are interconnected

	specific_cell_objects=Cell_Id_And_Capacity_Table_Class.query.filter().all()

	for specific_cell_object in specific_cell_objects:
		specific_cell='FN_out_'+str(specific_cell_object.cell_id)
		try:
			flow_value, flow_dict = nx.maximum_flow(G,specific_cell,'Master_CPF')
			specific_cell_object.actual_possible_maximum_throughput=flow_value
			db.session.commit()
		except:
			continue #don't use 'pass', as pass willl make the loop stop, whereas 'continue' makes it go to the next iteration
	
	double_clicked_cell_object=Cell_Id_And_Capacity_Table_Class.query.filter(Cell_Id_And_Capacity_Table_Class.cell_id==id_of_double_clicked_cell).first()

	return str(double_clicked_cell_object.actual_possible_maximum_throughput)

