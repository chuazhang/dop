from create_and_migrate_db import mxGraph_Cells_Table_Class
import networkx as nx
import matplotlib as mpl
#mpl.use('TkAgg')
mpl.use('Agg') #to remove error, might have to use TkAgg for Linux based systems
import matplotlib.pyplot as plt

def Asynchronously_Summarize_Asset_Connections_And_Save_To_SVG_Backend():
	cpf_list, hub_list, pad_list, steam_edge_list, emulsion_edge_list, edge_other_list = ([] for i in range(6))
	Get_List_For_CPF_Hub_And_Pad(cpf_list, hub_list, pad_list, steam_edge_list, emulsion_edge_list, edge_other_list)
	#print("CPF ", cpf_list, "Hub ", hub_list, "Pad ", pad_list, "Steam ", steam_edge_list, "Emulsion ",  emulsion_edge_list, "Other ", edge_other_list)

	orphan_list = []
	edge_list = steam_edge_list + emulsion_edge_list + edge_other_list
	Get_Orphan_List_From_Steam_Emulsion_And_Other(cpf_list, hub_list, pad_list, edge_list, orphan_list)
	#print("Orphan ", orphan_list)

	cpf_hub_dict, cpf_pad_dict, hub_pad_dict = ({} for i in range(3))
	Build_Dictionary_For_CPFHub_CPFPad_And_HubPad(cpf_list, hub_list, pad_list, edge_list, cpf_hub_dict, cpf_pad_dict, hub_pad_dict)
	#print("HUB_PAD_DICT", hub_pad_dict, "CPF_HUB_DICT", cpf_hub_dict, "CPF_PAD_DICT", cpf_pad_dict)

	totalRow = Calculate_Total_Rows(cpf_list, hub_list, orphan_list, cpf_hub_dict, hub_pad_dict, cpf_pad_dict)
	if (totalRow <= 0):
		return '||'
	rowHeight = 10.0 / totalRow if totalRow > 1 else 5.0 # 0.25
	#print('totalRow', totalRow, 'rowHeight', rowHeight)

	# add data into mxGraph and initial node positions
	G = nx.DiGraph(name="Asset Relationship Diagram")
	G.add_edges_from([[(GetPrefix(edge[0], cpf_list, hub_list, pad_list) + str(edge[0])), \
        (GetPrefix(edge[1], cpf_list, hub_list, pad_list) + str(edge[1]))] for edge in edge_list])
	orphan_list_with_prefix = [(GetPrefix(orphan, cpf_list, hub_list, pad_list) + str(orphan)) for orphan in orphan_list]
	# fake_list are the extent vertexes, if we just draw needed nodes sometimes the extent is wrongly calculated and labels are cropped 
	fake_list = ['extent_fake_1', 'extent_fake_2', 'extent_fake_3', 'extent_fake_4'] 
	G.add_nodes_from(fake_list + orphan_list_with_prefix)
	pos = nx.spring_layout(G)
	
	Set_Positions_For_Edge_Vertexes_And_Orphan_Nodes(pos, cpf_list, hub_list, pad_list, orphan_list, cpf_hub_dict, cpf_pad_dict, hub_pad_dict, fake_list, rowHeight)

	node_label_pos = {}
	for curPos in pos:
		node_label_pos[curPos] = [pos[curPos][0] + 0.55, pos[curPos][1]]
	node_list = [("CPF " + str(cpf)) for cpf in cpf_list] + [("Hub " + str(hub)) for hub in hub_list] + [("Pad " + str(pad)) for pad in pad_list] + orphan_list_with_prefix
	node_labels = {}
	for i, curPos in enumerate(pos):
		node_labels[curPos] = curPos if curPos.find('extent_fake_') else ""

	# initialize the drawing height
	fig = plt.gcf()
	plt.figure(figsize=(10.0, totalRow * 0.25))
	fig.clf()

	data = Generate_Emulsion_SVG_From_Nodes_And_Edges(G, pos, cpf_list, hub_list, pad_list, fake_list, emulsion_edge_list, node_list, node_label_pos, node_labels, totalRow * 0.25)
	data += '|';
	data += Generate_Steam_SVG_From_Nodes_And_Edges(G, pos, cpf_list, hub_list, pad_list, fake_list, steam_edge_list, node_list, node_label_pos, node_labels, totalRow * 0.25)
	data += '|';
	data += str(totalRow);
	plt.close('all')
	return data

def GetPrefix(node, cpf_list, hub_list, pad_list):
	if node in cpf_list:
		return "CPF "
	elif node in hub_list:
		return "Hub "
	elif node in pad_list:
		return "Pad "
	return ""

def Get_List_For_CPF_Hub_And_Pad(cpf_list, hub_list, pad_list, steam_edge_list, emulsion_edge_list, edge_other_list):
	mxGraph_cells_object_list=mxGraph_Cells_Table_Class.query.filter().all()

	# build cpf_list, hub_list, pad_list, steam_edge_list, emulsion_edge_list, and edge_other_list
	for mxGraph_cell_object in mxGraph_cells_object_list:		
		source_str = str.replace(str.replace(mxGraph_cell_object.source, 'FN_in_', ''), 'FN_out_', '')
		source_id = (int)(source_str if (source_str and (source_str != 'None')) else -1)
		target_str = str.replace(str.replace(mxGraph_cell_object.target, 'FN_in_', ''), 'FN_out_', '')
		target_id = (int)(target_str if (target_str and (target_str != 'None')) else -1)
		if mxGraph_cell_object.vertex_or_edge.strip() == "vertex":
			if mxGraph_cell_object.asset_type.strip() == "CPF":
				cpf_list.append((int)(mxGraph_cell_object.cell_id))
			elif mxGraph_cell_object.asset_type.strip() == "Hub":
				hub_list.append((int)(mxGraph_cell_object.cell_id))
			elif mxGraph_cell_object.asset_type.strip() == "Pad":
				pad_list.append((int)(mxGraph_cell_object.cell_id))
		elif mxGraph_cell_object.vertex_or_edge.strip() == "edge":
			if (source_id in cpf_list and target_id in hub_list) or (source_id in hub_list and target_id in pad_list) or (source_id in cpf_list and target_id in pad_list):
				steam_edge_list.append([source_id, target_id])
			elif (source_id in hub_list and target_id in cpf_list) or (source_id in pad_list and target_id in hub_list) or (source_id in pad_list and target_id in cpf_list) or (source_id in cpf_list and target_id in cpf_list):
				emulsion_edge_list.append([source_id, target_id])
			else:
				edge_other_list.append([source_id, target_id])

def Get_Orphan_List_From_Steam_Emulsion_And_Other(cpf_list, hub_list, pad_list, edge_list, orphan_list):
	for cpf in cpf_list:
		cpfIsOrphan = True
		for edge in edge_list:
			if cpf == edge[0] or cpf == edge[1]:
				cpfIsOrphan = False
				continue
		if cpfIsOrphan:
			orphan_list.append(cpf)
	for hub in hub_list:
		hubIsOrphan = True
		for edge in edge_list:
			if hub == edge[0] or hub == edge[1]:
				hubIsOrphan = False
				continue
		if hubIsOrphan:
			orphan_list.append(hub)
	for pad in pad_list:
		padIsOrphan = True
		for edge in edge_list:
			if pad == edge[0] or pad == edge[1]:
				padIsOrphan = False
				continue
		if padIsOrphan:
			orphan_list.append(pad)

def Build_Dictionary_For_CPFHub_CPFPad_And_HubPad(cpf_list, hub_list, pad_list, edge_list, cpf_hub_dict, cpf_pad_dict, hub_pad_dict):
	for hub in hub_list:
		hub_pad_distinct_set = set()
		for edge in edge_list:
			if hub == edge[0] or hub == edge[1]:
				not_hub = edge[1] if hub == edge[0] else edge[0]
				if not_hub in pad_list:
					hub_pad_distinct_set.add(not_hub)
		hub_pad_dict[hub] = hub_pad_distinct_set
	for cpf in cpf_list:
		cpf_hub_distinct_set = set()
		for edge in edge_list:
			if cpf == edge[0] or cpf == edge[1]:
				not_cpf = edge[1] if cpf == edge[0] else edge[0]
				if not_cpf in hub_list:
					cpf_hub_distinct_set.add(not_cpf)
		cpf_hub_dict[cpf] = cpf_hub_distinct_set
	for cpf in cpf_list:
		cpf_pad_distinct_set = set()
		for edge in edge_list:
			if cpf == edge[0] or cpf == edge[1]:
				not_cpf = edge[1] if cpf == edge[0] else edge[0]
				if not_cpf in pad_list:
					cpf_pad_distinct_set.add(not_cpf)
		cpf_pad_dict[cpf] = cpf_pad_distinct_set

def Calculate_Total_Rows(cpf_list, hub_list, orphan_list, cpf_hub_dict, hub_pad_dict, cpf_pad_dict):
	totalRow = 0
	# calculate start from CPF
	for cpf in cpf_list:
		if cpf_hub_dict and (cpf in cpf_hub_dict):
			for cpf_hub in cpf_hub_dict[cpf]:
				if hub_pad_dict and (cpf_hub in hub_pad_dict):
					totalRow += len(hub_pad_dict[cpf_hub])
				else: # hub has no pad
					totalRow += 1
		if cpf_pad_dict and (cpf in cpf_pad_dict):
			totalRow += len(cpf_pad_dict[cpf])
	# if hub started alone without CPF, we also need to add new row
	for hub in hub_list:
		findCpf = False
		for cpf_hub in cpf_hub_dict:
			if hub in cpf_hub_dict[cpf_hub]:
				findCpf = True
				continue
		if findCpf == False:
			if hub_pad_dict and (hub in hub_pad_dict):
				totalRow += len(hub_pad_dict[hub])
			else: # hub has no pad but has connection to another hub
				totalRow += 1
	# add orphan list to row
	totalRow += len(orphan_list)
	return totalRow

def Set_Positions_For_Edge_Vertexes_And_Orphan_Nodes(pos, cpf_list, hub_list, pad_list, orphan_list, cpf_hub_dict, cpf_pad_dict, hub_pad_dict, fake_list, rowHeight):
	rowNum = 1
	for cpf in cpf_list:
		pos['CPF ' + str(cpf)] = [-5, 5 - rowNum * rowHeight]
		#print("CPF ", cpf, -5, 5 - rowNum * rowHeight)
		if cpf_hub_dict and (cpf in cpf_hub_dict):
			for cpf_hub in cpf_hub_dict[cpf]:
				pos['Hub ' + str(cpf_hub)] = [0, 5 - rowNum * rowHeight]
				#print('Hub ', str(cpf_hub), 0, 5 - rowNum * rowHeight)
				if hub_pad_dict and (cpf_hub in hub_pad_dict):
					for hub_pad in hub_pad_dict[cpf_hub]:
						pos['Pad ' + str(hub_pad)] = [5, 5 - rowNum * rowHeight]
						#print('Pad ', str(hub_pad), 5, 5 - rowNum * rowHeight)
						rowNum += 1
				else: # if hub has no pad, we also need to move to next row
					rowNum += 1
		if cpf_pad_dict and (cpf in cpf_pad_dict):
			for cpf_pad in cpf_pad_dict[cpf]:
				pos['Pad ' + str(cpf_pad)] = [5, 5 - rowNum * rowHeight]
				#print('Pad ', str(cpf_pad), 5, 5 - rowNum * rowHeight)
				rowNum += 1
	for hub in hub_list:
		findCpf = False
		for cpf_hub in cpf_hub_dict:
			if hub in cpf_hub_dict[cpf_hub]:
				findCpf = True
				continue
		if findCpf == False:
			pos['Hub ' + str(hub)] = [0, 5 - rowNum * rowHeight]
			#print('Hub ', str(hub), 0, 5 - rowNum * rowHeight)
			if hub_pad_dict and (hub in hub_pad_dict):
				for hub_pad in hub_pad_dict[hub]:
					pos['Pad ' + str(hub_pad)] = [5, 5 - rowNum * rowHeight]
					#print('Pad ', str(hub_pad), 5, 5 - rowNum * rowHeight)
					rowNum += 1
			else:
				rowNum += 1
	for orphan in orphan_list:
		orphanType = GetPrefix(orphan, cpf_list, hub_list, pad_list)
		if orphanType == "CPF ":
			pos[orphanType + str(orphan)] = [-5, 5 - rowNum * rowHeight]
		elif orphanType == "Hub ":
			pos[orphanType + str(orphan)] = [0, 5 - rowNum * rowHeight]
		else:
			pos[orphanType + str(orphan)] = [5, 5 - rowNum * rowHeight]
		rowNum += 1
	# add extent vertexes position to fake list
	pos[fake_list[0]] = [-4.6, 5]
	pos[fake_list[1]] = [5.4, 5]
	pos[fake_list[2]] = [-4.6, -5]
	pos[fake_list[3]] = [5.4, -5]

def Generate_Steam_SVG_From_Nodes_And_Edges(G, pos, cpf_list, hub_list, pad_list, fake_list, steam_edge_list, node_list, node_label_pos, node_labels, height):
	# draw edges, STEAM and EMULSION texts, nodes,  
	#nx.draw_networkx_edges(G, pos, edgelist=steam_edge_list, node_size=30, edge_color='#005596', width=0.2, arrowstyle='->') #, connectionstyle='arc3,rad=0.4')
	steam_label_list = {}
	for edge in steam_edge_list:
		#print((GetPrefix(edge[0], cpf_list, hub_list, pad_list) + str(edge[0])),(GetPrefix(edge[1], cpf_list, hub_list, pad_list) + str(edge[1])), "STEAM")        
		steam_label_list[((GetPrefix(edge[0], cpf_list, hub_list, pad_list) + str(edge[0])),(GetPrefix(edge[1], cpf_list, hub_list, pad_list) + str(edge[1])))] = "STEAM" 
	nx.draw_networkx_edges(G, pos, edgelist=steam_label_list, node_size=30, edge_color='#005596', width=0.2, arrowstyle='->') #, connectionstyle='arc3,rad=0.4')
	#nx.draw_networkx_edge_labels(G, pos, edge_labels=steam_label_list, label_pos=0.7, font_size=3, font_color='red', alpha=0.5, rotate=False)
	nx.draw_networkx_nodes(G, pos, nodelist=fake_list, node_size=1, node_shape='>', alpha=0.0)
	nx.draw_networkx_nodes(G, pos, nodelist=node_list, node_size=30, node_shape='s', alpha=1.0)
	nx.draw_networkx_labels(G, node_label_pos, labels=node_labels, node_size=30, font_size=6, font_color='#8B0000', font_weight='normal')

	# generate SVG file
	fig = plt.gcf()
	plt.axis('off')
	fileName = "static/asset_summary_steam.svg"
	plt.figure(figsize=(10.0, height))
	fig.savefig(fileName, bbox_inches='tight', pad_inches=0, dpi=100)
	fig.clf()

	# return SVG file content
	with open('static/asset_summary_steam.svg', 'r') as file:
		return file.read().replace('\n', '')
	return ""

def Generate_Emulsion_SVG_From_Nodes_And_Edges(G, pos, cpf_list, hub_list, pad_list, fake_list, emulsion_edge_list, node_list, node_label_pos, node_labels, height):	
	emulsion_label_list = {}
	for edge in emulsion_edge_list:
		#print((GetPrefix(edge[0], cpf_list, hub_list, pad_list) + str(edge[0])),(GetPrefix(edge[1], cpf_list, hub_list, pad_list) + str(edge[1])), "EMULSION")        
		emulsion_label_list[((GetPrefix(edge[0], cpf_list, hub_list, pad_list) + str(edge[0])),(GetPrefix(edge[1], cpf_list, hub_list, pad_list) + str(edge[1])))] = "EMULSION" 
	#nx.draw_networkx_edge_labels(G, pos, edge_labels=emulsion_label_list, label_pos=0.7, font_size=3, font_color='blue', alpha=0.5, rotate=False)
	nx.draw_networkx_edges(G, pos, edgelist=emulsion_label_list, node_size=30, edge_color='#00FF00', width=0.2, arrowstyle='->') #, connectionstyle='arc3,rad=0.4')
	nx.draw_networkx_nodes(G, pos, nodelist=fake_list, node_size=1, node_shape='>', alpha=0.0)
	nx.draw_networkx_nodes(G, pos, nodelist=node_list, node_size=30, node_shape='s', alpha=1.0)
	nx.draw_networkx_labels(G, node_label_pos, labels=node_labels, node_size=30, font_size=6, font_color='#8B0000', font_weight='normal')

	# generate SVG file
	fig = plt.gcf()
	plt.axis('off')
	fileName = "static/asset_summary_emulsion.svg"
	plt.figure(figsize=(10.0, height))
	fig.savefig(fileName, bbox_inches='tight', pad_inches=0, dpi=100)
	fig.clf()

	# return SVG file content
	with open('static/asset_summary_emulsion.svg', 'r') as file:
		return file.read().replace('\n', '')
	return ""
	