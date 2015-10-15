#!/bin/env python

from DukePlotALot import *
from DukePlotALot2D import *
from plotlib import HistStorage,getColorList,getDictValue,HistStorageContainer
import matplotlib.pyplot as plt
from configobj import ConfigObj
try:
    from collections import OrderedDict
except ImportError:
    from ordered import OrderedDict

from rootpy.plotting.views import ScaleView
from rootpy.io import root_open
from rootpy.plotting import Graph

import style_class as sc

from object_plotting import *

import ROOT as r

masslist = [
     200,
     300,
     400,
     500,
     600,
     700,
     800,
     900,
     1000,
     1200,
     1400,
     1600,
     1800,
     2000,
]

thirteen_TeV_xs = {
     200:[585.35, 1.3373],
     300:[158.04, 1.360],
     400:[59.97, 1.3713],
     500:[27.612, 1.3752],
     600:[14.415, 1.3742],
     700:[8.1833, 1.3696],
     800:[4.9538, 1.3626],
     900:[3.1345, 1.3538],
     1000:[2.0611, 1.3435],
     1200:[0.96973, 1.3209],
     1400:[0.49332, 1.2964],
     1600:[0.26708, 1.2700],
     1800:[0.14995, 1.2473],
     2000:[0.08639, 1.2233],
     2500:[0.023951, 0.0],
     3000:[0.0071592, 0.0],
     3500:[0.002136, 0.0],
     4000:[0.00064163, 0.0],
     4500:[0.00018451, 0.0],
     5000:[5.1376e-05, 0.0],
     5500:[1.3505e-05, 0.0],
     6000:[3.3123e-06, 0.0],
     6500:[7.8732e-07, 0.0],
    }

eight_TeV_xs = {
     100:[2.71, 1.34],
     200:[3.06e-1, 1.38],
     300:[8.30e-2, 1.39],
     400:[2.90e-2, 1.39],
     500:[1.25e-2, 1.38],
     600:[6.19e-3, 1.37],
     700:[3.31e-3, 1.35],
     800:[1.90e-3, 1.33],
     900:[1.12e-3, 1.31],
     1000:[6.87e-4, 1.29],
     1100:[4.33e-4, 1.27],
     1200:[2.77e-4, 1.25],
     1300:[1.80e-4, 1.23],
     1400:[1.19e-4, 1.21],
     1500:[7.9e-5, 1.19],
     1600:[5.3e-5, 1.18 ],
     1700:[3.6e-5, 1.16],
     1800:[2.4e-5, 1.14],
     1900:[1.6e-5, 1.13],
     2000:[1.1e-5, 1.12],
    }

def main():
    ####################################################################
    # Individual cross section plots
    ####################################################################

    print("Now plotting: cross section comparison")

    x_vals =[]
    y_vals_8 = []
    y_vals_8_k = []
    y_vals_13 = []
    y_vals_13_k = []
    for item in masslist:
        x_vals.append(item)
        y_vals_8.append(eight_TeV_xs[item][0])
        y_vals_8_k.append(eight_TeV_xs[item][1])
        y_vals_13.append(thirteen_TeV_xs[item][0]/1000)
        y_vals_13_k.append(thirteen_TeV_xs[item][1])

    x_vals = np.array(x_vals)
    y_vals_8 = np.array(y_vals_8)
    y_vals_8_k = np.array(y_vals_8_k)
    y_vals_13 = np.array(y_vals_13)
    y_vals_13_k = np.array(y_vals_13_k)

    graph_8 = Graph(x_vals.shape[0])
    graph_8_k = Graph(x_vals.shape[0])
    graph_13 = Graph(x_vals.shape[0])
    graph_13_k = Graph(x_vals.shape[0])
    for i, (xx, y1, y2, y3, y4) in enumerate(zip(x_vals, y_vals_8, y_vals_8_k, y_vals_13, y_vals_13_k)):
        graph_8.SetPoint(i, xx, y1)
        graph_8.SetPointError(i, 0, 0, 0, 0)
        graph_8_k.SetPoint(i, xx, y2)
        graph_8_k.SetPointError(i, 0, 0, 0, 0)
        graph_13.SetPoint(i, xx, y3)
        graph_13.SetPointError(i, 0, 0, 0, 0)
        graph_13_k.SetPoint(i, xx, y4)
        graph_13_k.SetPointError(i, 0, 0, 0, 0)

    graph_8.SetTitle('LO xs (8 TeV)')
    graph_8.xaxis.SetTitle('$M$ (GeV)')
    graph_8.yaxis.SetTitle('xs $\cdot$ BR (pb)')

    graph_8_k.SetTitle('NLO k-factor (8 TeV)')
    graph_8_k.xaxis.SetTitle('$M_{\tilde{\nu}_{\tau}}$ (GeV)')
    graph_8_k.yaxis.SetTitle('k-factor')

    graph_13.SetTitle('LO xs (13 TeV)')
    graph_13.xaxis.SetTitle('$M_{\tilde{\nu}_{\tau}}$ (GeV)')
    graph_13.yaxis.SetTitle('xs $\cdot$ BR (pb)')

    graph_13_k.SetTitle('NLO k-factor (13 TeV)')
    graph_13_k.xaxis.SetTitle('$M_{\tilde{\nu}_{\tau}}$ (GeV)')
    graph_13_k.yaxis.SetTitle('k-factor')

    graph_8.SetLineColor('red')
    graph_8_k.SetLineColor('red')
    graph_8_k.SetLineStyle(2)
    graph_13.SetLineColor('blue')
    graph_13_k.SetLineColor('blue')
    graph_13_k.SetLineStyle(2)

    hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Linegraphs', cmsPositon = "upper right", legendPosition = 'lower left', lumi = 0, cms = 13)

    hist_style.Set_additional_text('Simulation')

    hist_style.Set_axis(logy = True, grid = True, xmin = 200, xmax = 2000, histaxis_ymin = 1.0, histaxis_ymax = 1.5)

    test = plotter(hist = [graph_8, graph_13], hist_axis = [graph_8_k, graph_13_k], style=hist_style)
    # test.Add_plot(plot = 'Ratio', pos = 1, height = 15, label = '')

    test.create_plot()

    test.SavePlot('plots/xs_comparison.pdf')

    return 42



main()
