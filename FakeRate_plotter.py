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

def eff_rebinner(input_eff, rebinfac):
    all_hist = input_eff.GetCopyTotalHisto()
    pass_hist = input_eff.GetCopyPassedHisto()

    all_hist.Rebin(rebinfac)
    pass_hist.Rebin(rebinfac)

    output_eff = r.TEfficiency(pass_hist, all_hist)

    return output_eff

def eff_adder(input_1, input_2):
    all_hist = input_1.GetCopyTotalHisto()
    pass_hist = input_1.GetCopyPassedHisto()

    all_hist.Add(input_2.GetCopyTotalHisto())
    pass_hist.Add(input_2.GetCopyPassedHisto())

    output_eff = r.TEfficiency(pass_hist, all_hist)

    return output_eff

def project_x(input_eff, firstbin_x = 0, lastbin_x = -1):
    all_hist = input_eff.GetCopyTotalHisto()
    pass_hist = input_eff.GetCopyPassedHisto()

    all_hist_x = all_hist.ProjectionX('_px', firstbin_x, lastbin_x, 'e')
    pass_hist_x = pass_hist.ProjectionX('_px', firstbin_x, lastbin_x, 'e')

    output_eff = r.TEfficiency(pass_hist_x, all_hist_x)

    return output_eff

def project_y(input_eff, firstbin_y = 0, lastbin_y = -1):
    all_hist = input_eff.GetCopyTotalHisto()
    pass_hist = input_eff.GetCopyPassedHisto()

    all_hist_y = all_hist.ProjectionY('_py', firstbin_y, lastbin_y, 'e')
    pass_hist_y = pass_hist.ProjectionY('_py', firstbin_y, lastbin_y, 'e')

    output_eff = r.TEfficiency(pass_hist_y, all_hist_y)

    return output_eff

def main():

    basedir="/disk1/erdweg/out/output2015_8_3_16_34/merged/"

    colors = ['lime', 'deepskyblue', 'magenta', 'orangered', 'lightblue', 'gray']

    bglist=OrderedDict()

    bglist = ['QCD_Pt-15TTo7000-Flat_13TeV_P6']

    # bglist = ['QCD_Pt_5to10_13TeV_P8',
     # 'QCD_Pt_80to120_13TeV_P8',
     # 'QCD_Pt_120to170_13TeV_P8',
     # 'QCD_Pt_170to300_13TeV_P8',
     # 'QCD_Pt_300to470_13TeV_P8',
     # 'QCD_Pt_1000to1400_13TeV_P8',
     # 'QCD_Pt_1400to1800_13TeV_P8',
     # 'QCD_Pt_1800to2400_13TeV_P8',
     # 'QCD_Pt_2400to3200_13TeV_P8',
     # 'QCD_Pt_3200toInf_13TeV_P8',
    # ]

    hists2D=['JetFakeRate/eff_JetFakeRate_vs_pT_vs_eta'
    ]

    titles={
     'HLT_Effs/eff_HLT_HLT_Mu40_v1_vs_Nvtx':['HLT_Mu40_v1 efficiency','$N_{vtx}$','efficiency $\epsilon$']
    }

    yranges={
     'ID_Effs/eff_Muon_ID_vs_pT':[0.8,1.02],
    }

    for hist in hists2D:

        print("Now plotting: " + hist)

        hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower right', lumi = 0, cms = 13)

        hist_style.Set_additional_text('Simulation')

        name=hist.replace("/","")

        tfile = root_open(basedir + bglist[0] + ".root", "READ")
        t_eff = tfile.Get(hist)

        for i in range(1,len(bglist)-1):
            tfile = root_open(basedir + bglist[i] + ".root", "READ")
            t_eff = eff_adder(t_eff, tfile.Get(hist))

        ################################################################
        #
        # Projection along the xaxis:
        # Fake rate as a function of pT
        #
        ################################################################
        print('\t--> X-Projections')
        x_proj = project_x(t_eff)
        x_proj = Graph(x_proj.CreateGraph())
        x_proj.SetTitle('Combined')
        x_proj.SetColor(colors[0])
        x_proj.xaxis.SetTitle('$E_{T}$ (GeV)')
        x_proj.yaxis.SetTitle('Fake rate')

        x_proj_barrel = project_x(t_eff,1,15)
        x_proj_barrel = Graph(x_proj_barrel.CreateGraph())
        x_proj_barrel.SetTitle('Barrel')
        x_proj_barrel.SetColor(colors[1])

        x_proj_endcap = project_x(t_eff,16,-1)
        x_proj_endcap = Graph(x_proj_endcap.CreateGraph())
        x_proj_endcap.SetTitle('Endcap')
        x_proj_endcap.SetColor(colors[2])

        test = plotter(hist = [x_proj,x_proj_barrel,x_proj_endcap], style = hist_style)

        test.Set_axis(logy = True, xmin = 0, xmax = 1500, ymin = 1e-4, ymax = 1e0)

        test.create_plot()

        test.SavePlot('plots/%s_%s_x.pdf'%(bglist[0],name))

        ################################################################
        #
        # Projection along the yaxis:
        # Fake rate as a function of eta
        #
        ################################################################

        print('\t--> Y-Projections')
        y_proj = project_y(t_eff)
        y_proj = Graph(y_proj.CreateGraph())
        y_proj.SetTitle('Combined')
        y_proj.SetColor(colors[0])
        y_proj.xaxis.SetTitle('$|\eta|$')
        y_proj.yaxis.SetTitle('Fake rate')

        y_proj_100 = project_y(t_eff,1,10)
        y_proj_100 = Graph(y_proj_100.CreateGraph())
        y_proj_100.SetTitle('$E_{T} < 100\,$GeV')
        y_proj_100.SetColor(colors[1])

        y_proj_200 = project_y(t_eff,11,20)
        y_proj_200 = Graph(y_proj_200.CreateGraph())
        y_proj_200.SetTitle('$100\,$GeV$ < E_{T} < 200\,$GeV')
        y_proj_200.SetColor(colors[2])

        y_proj_500 = project_y(t_eff,21,50)
        y_proj_500 = Graph(y_proj_500.CreateGraph())
        y_proj_500.SetTitle('$200\,$GeV$ < E_{T} < 500\,$GeV')
        y_proj_500.SetColor(colors[3])

        y_proj_1000 = project_y(t_eff,51,100)
        y_proj_1000 = Graph(y_proj_1000.CreateGraph())
        y_proj_1000.SetTitle('$500\,$GeV$ < E_{T} < 1000\,$GeV')
        y_proj_1000.SetColor(colors[4])

        y_proj_inf = project_y(t_eff,101,-1)
        y_proj_inf = Graph(y_proj_inf.CreateGraph())
        y_proj_inf.SetTitle('$1000\,$GeV$ < E_{T}$')
        y_proj_inf.SetColor(colors[5])

        test = plotter(hist = [y_proj, y_proj_100, y_proj_200, y_proj_500, y_proj_1000, y_proj_inf], style = hist_style)

        test.Set_axis(logy = True, xmin = 0, xmax = 2.5, ymin = 1e-4, ymax = 1e0)

        test.create_plot()

        test.SavePlot('plots/%s_%s_y.pdf'%(bglist[0],name))

        ################################################################
        #
        # 2D Plot
        # Fake rate as a function of eta and pT
        #
        ################################################################

        print('\t--> 2D Plot')
        hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "outside left", legendPosition = 'lower middle', lumi = 0, cms = 13)

        hist_style.Set_additional_text('Simulation')

        t_eff = t_eff.CreateHistogram()
        t_eff.SetTitle(bglist[0])

        test = plotter2D(hist = t_eff, style = hist_style)

        test.Set_axis(xmin = 0, xmax = 1500, ymin = 0, ymax = 2.6, zmin = 0, zmax = 1)

        test.create_plot()

        test.save_plot('plots/%s_%s.pdf'%(bglist[0],name))

    return 42



main()
