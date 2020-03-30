import networkx as nx
from create_and_migrate_db import mxGraph_Cells_Table_Class, Cell_Id_And_Capacity_Table_Class

def Generate_The_G_Object_Of_Graph_For_Networkx():
    G=nx.DiGraph()
    
    mxGraph_cells_object_list=mxGraph_Cells_Table_Class.query.filter().all()
    
    for mxGraph_cell_object in mxGraph_cells_object_list:
        cell_object_capacity_object=Cell_Id_And_Capacity_Table_Class.query.filter(Cell_Id_And_Capacity_Table_Class.cell_id==mxGraph_cell_object.cell_id).first()
        
        cell_object_source=mxGraph_cell_object.source
        cell_object_target=mxGraph_cell_object.target

        if cell_object_capacity_object.capacity is None:
            G.add_edge(cell_object_source,cell_object_target)
        else:
            G.add_edge(cell_object_source,cell_object_target,capacity=cell_object_capacity_object.capacity)
              
    return G