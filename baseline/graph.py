from sklearn.pipeline import *
from sklearn.naive_bayes import *
from sklearn.preprocessing import *
from sklearn.svm import *
from sklearn.decomposition import *
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.compose import *
from sklearn.feature_extraction.text import *
from sklearn.impute import *
from sklearn.ensemble import *
from sklearn.metrics import *
from sklearn.neural_network import *
from xgboost import *
import numpy as np
import pandas as pd
import inspect
import json
from types import FunctionType
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
import graphviz
dot = graphviz.Digraph(comment='First graph',strict=True)
function_names = []
function_input = {}
function_output = {}
function_source = {}
function_edges = {}

def extract_wrapped(decorated):
    closure = (c.cell_contents for c in decorated.__closure__)
    return next((c for c in closure if isinstance(c, FunctionType)), None)

def add_fuction_for_graph(connect = [], input_ = [] , output_ = []):
    def add_function(function):
        def to_add_node(*args,**kwargs):
            
            for index in range(len(connect)):
                if function.__name__ not in function_names:
                    function_names.append(function.__name__)
                    dot.node(function.__name__,function.__name__,tooltip = inspect.getsource(function))
                    function_input[function.__name__] = input_
                    function_output[function.__name__] = output_
                    function_source[function.__name__] = inspect.getsource(function)
                    function_edges[function.__name__] = []

                if connect[index] is not None and connect[index] in function_names:
                    label = []
                    for output__ in function_output[connect[index]]:
                        if output__ in input_[index]:
                            label.append(output__)
                    if len(label)>0:
                        dot.edge(connect[index],function.__name__,label = str(label))
                    else: 
                        dot.edge(connect[index],function.__name__)
                    function_edges[connect[index]].append((function.__name__,str(label)))
            result = function(*args,**kwargs)
            return [result,function.__name__]
        return to_add_node
    return add_function

def make_graph():
    dot.format = 'svg'
    print(dot.source)
    dot.render('Filename',view=True)

def make_commit():
    nodes = function_source
    edges = function_edges
    a_file = open("data.json", "w")
    json.dump(function_source, a_file)
    a_file.close()
    graph = nx.DiGraph()
    for key in nodes.keys():
        graph.add_node(key)
        
        
    for key in edges.keys():
        for item in edges[key]:
            graph.add_edge(key,item[0])
    # plt.subplot(121)
    # nx.draw_spring(graph, with_labels=True, font_weight='bold')
    G = graph
    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    node_x = []
    node_y = []
    node_text = [x for x in nodes.keys()]
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
    for x in nodes.keys():
        nodes[x] = "<br />".join(nodes[x].split("\n"))

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode="markers+text",
        hovertemplate='%{customdata}',
        text = node_text,
        textposition = "top center",
        customdata = [nodes[x] for x in nodes.keys()],
        name = "",
        marker=dict(
            color=["red"]*len(G.edges()),
            size=10,
            line_width=2))

    fig = go.Figure(data=[node_trace],
                layout=go.Layout(
                    title='<br>Network graph made with Plotly',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    indexOfedges = 0
    for key in edges.keys():
        for index in range(len(edges[key])):
            if(3*indexOfedges+1 > len(edge_x)):
                break
            fig.add_annotation(
            xref="x",
            yref="y",
            x=edge_x[3*indexOfedges+1],
            y=edge_y[3*indexOfedges+1],
            axref="x",
            ayref="y",
            ax=edge_x[3*indexOfedges],
            ay=edge_y[3*indexOfedges],
            arrowhead=2,
            startstandoff = 5,
            standoff = 10,
            
            )
            fig.add_annotation(
            xref="x",
            yref="y",
            x=(edge_x[3*indexOfedges+1]+edge_x[3*indexOfedges])/2,
            y=(edge_y[3*indexOfedges+1]+edge_y[3*indexOfedges])/2,
            axref="x",
            ayref="y",
            ax=(edge_x[3*indexOfedges+1]+edge_x[3*indexOfedges])/2,
            ay=(edge_y[3*indexOfedges+1]+edge_y[3*indexOfedges])/2,
            arrowhead=2,
            text = str(edges[key][index][1]),
            # textangle=math.degrees(math.atan((edge_y[3*indexOfedges+1]-edge_y[3*indexOfedges])/(edge_x[3*indexOfedges+1]-edge_x[3*indexOfedges])))
            )
            # print(math.degrees(math.atan((edge_y[3*indexOfedges+1]-edge_y[3*indexOfedges])/(edge_x[3*indexOfedges+1]-edge_x[3*indexOfedges]))))
            indexOfedges += 1
            

    fig.show()
