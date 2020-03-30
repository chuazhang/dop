import re
def Translate_FN_To_Cell_ID(fn_id_or_out_str):
    cell_id=re.findall('\d+', fn_id_or_out_str )
    cell_id=cell_id[0] #switching from list to str
    cell_id=int(cell_id) #switching from str to int
    return cell_id
