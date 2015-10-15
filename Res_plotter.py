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

def main():

    basedir="/disk1/erdweg/Skimming/"
    # lumi=19712

    # xs= ConfigObj("/disk1/erdweg/plotting/xs_Phys14.cfg")
    # bghists=HistStorage(xs,lumi,path=basedir,isData=True)

    bglist=OrderedDict()

    bglist["RPV"]=['RPV_test_13TeV'
     ]

    colorList={}
    colorList["RPV"]="lightblue"

    hists2D=['Effs/eff_HLT_HLT_Mu40_v1_vs_eta_vs_phi(Mu)',
     # 'Effs/eff_HLT_HLT_Mu40_v1_vs_pT(Mu)',
     # 'Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Mu17_TkMu8_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_pT(Ele)',
     # 'Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_Nvtx',
     # 'Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_Nvtx',
    ]

    if True:
        for hist in hists2D:
            print("Now plotting: " + hist)

            tfile = root_open(basedir + bglist["RPV"][0] + ".root", "READ")
            t_eff = tfile.Get(hist).CreateHistogram()
            # t_eff.SetLineColor(colorList[item])
            t_eff.SetTitle(item)
            # t_eff.xaxis.SetTitle(t_eff.GetXaxis().GetTitle())
            # t_eff.yaxis.SetTitle(t_eff.GetYaxis().GetTitle())
    
            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "upper left", legendPosition = 'lower middle', lumi = 1000, cms = 13)

            hist_style.Set_additional_text('plot dummy')

            test = plotter2D(hist = histlist[0], style = hist_style)
    
            test.Add_y_projection(20)
            test.Add_x_projection(20)

            test.Set_axis(xmin = -2.5, xmax = 2.5, ymin = 0, ymax = 3.1, zmin = 0, zmax = 1)

            name=hist.replace("/","")

            test.create_plot()

            #test.show_fig()

            ret_hist = test.Get_x_projection_hist()

            plot_gauss_fit(test.Get_x_projection_axis(), ret_hist, xmin = -2.1, xmax = 2.1)

            test.save_plot('plots/%s.pdf'%(name))

    return 42



main()
