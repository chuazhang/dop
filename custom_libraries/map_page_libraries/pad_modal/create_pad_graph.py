import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as ply

#custom libraries
from custom_libraries.map_page_libraries.get_x_and_y_axis_data_for_graph import Get_X_And_Y_Axis_Data_For_Graph
 

def Create_Pad_Graph():
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Grab the x and y axis data
    dict_of_x_and_y_axis_data_for_graph=Get_X_And_Y_Axis_Data_For_Graph()

    forecasted_date_x_axis_data_list=dict_of_x_and_y_axis_data_for_graph['forecasted_date_x_axis_data_list']
    produced_oil_y_axis_data_list=dict_of_x_and_y_axis_data_for_graph['produced_oil_y_axis_data_list']
    produced_water_y_axis_data_list=dict_of_x_and_y_axis_data_for_graph['produced_water_y_axis_data_list']
    injected_steam_y_axis_data_list=dict_of_x_and_y_axis_data_for_graph['injected_steam_y_axis_data_list']
    produced_gas_y_axis_data_list=dict_of_x_and_y_axis_data_for_graph['produced_gas_y_axis_data_list']
    emulsion_y_axis_data_list=dict_of_x_and_y_axis_data_for_graph['emulsion_y_axis_data_list']
    actual_possible_maximum_throughput_emulsion_y_axis_data_list=dict_of_x_and_y_axis_data_for_graph['actual_possible_maximum_throughput_emulsion_y_axis_data_list']

    # Assigns 'None' if a value is empty
    produced_oil_y_axis_data_list=[(x if (x or x==0) else None) for x in produced_oil_y_axis_data_list]
    produced_water_y_axis_data_list=[(x if (x or x==0) else None) for x in produced_water_y_axis_data_list]
    injected_steam_y_axis_data_list=[(x if (x or x==0) else None) for x in  injected_steam_y_axis_data_list]
    produced_gas_y_axis_data_list=[(x if (x or x==0) else None) for x in  produced_gas_y_axis_data_list]
    emulsion_y_axis_data_list=[(x if (x or x==0) else None) for x in  emulsion_y_axis_data_list]
    actual_possible_maximum_throughput_emulsion_y_axis_data_list=[(x if (x or x==0) else None) for x in  actual_possible_maximum_throughput_emulsion_y_axis_data_list]
    
    # Add traces
    fig.add_trace(
        go.Scatter(x=forecasted_date_x_axis_data_list, y=produced_oil_y_axis_data_list, name="Bitumen [bbl/day]"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=forecasted_date_x_axis_data_list, y=produced_water_y_axis_data_list, name="Produced Water [m3/day]"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=forecasted_date_x_axis_data_list, y=injected_steam_y_axis_data_list, name="Injected Steam [m3/day]"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=forecasted_date_x_axis_data_list, y=produced_gas_y_axis_data_list, name="Produced Gas [m3/day]"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=forecasted_date_x_axis_data_list, y=emulsion_y_axis_data_list, name="Emulsion [m3/day]"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=forecasted_date_x_axis_data_list, y=actual_possible_maximum_throughput_emulsion_y_axis_data_list,\
            name="Actual Emulsion Capacity [m3/day]",\
                line = dict(color='orange', width=4, dash='dash')),\
                    secondary_y=True,
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>[bbl/day]</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>[m3/day]</b>", secondary_y=True)

    #horizontal legend and position it
    fig.update_layout(legend_orientation="h",
        legend=dict(x=-.1, y=1.3, font=dict(
            family="sans-serif",
            size=12,
            color="black"
        )))


    #save the figure
    pad_graph_div_data=ply.plot(fig, include_plotlyjs=False, output_type='div')
    return pad_graph_div_data
    #ply.plot(fig,filename="templates/home_page/map_page_modals/pad_modal/graphs/updated_graph.html",output_type="div", auto_open=False)