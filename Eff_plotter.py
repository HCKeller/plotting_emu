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

    basedir="/disk1/erdweg/out/output2015_3_24_14_16/merged/"
    # lumi=19712

    # xs= ConfigObj("/disk1/erdweg/plotting/xs_Phys14.cfg")
    # bghists=HistStorage(xs,lumi,path=basedir,isData=True)

    bglist=OrderedDict()

    bglist["PU20bx25"]=['ZprimeToTauTau_M-1000_PU20bx25_PHYS14',
     'ZprimeToTauTau_M-5000_PU20bx25_PHYS14'
    ]
    bglist["AVE30BX50"]=['ZprimeToTauTau_M-1000_AVE30BX50_PHYS14',
     'ZprimeToTauTau_M-5000_AVE30BX50_PHYS14',
     ]
    bglist["PU40bx25"]=['ZprimeToTauTau_M-1000_PU40bx25_PHYS14',
     'ZprimeToTauTau_M-5000_PU40bx25_PHYS14',
    ]

    # bghists.addFileList(bglist)

    colorList={}
    colorList["PU20bx25"]="lightblue"
    colorList["AVE30BX50"]="lightgreen"
    colorList["PU40bx25"]="darkmagenta"

    hists=['HLT_Effs/eff_HLT_HLT_Mu40_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Mu40_v1_vs_pT(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_pT(Ele)',
     'HLT_Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_Nvtx',
    ]

    hists2D=['HLT_Effs/eff_HLT_HLT_Mu40_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_pT(Mu,Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_eta_vs_phi(Ele)',
     'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_pT(Mu,Ele)',
     'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_pT(Mu,Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_pT(Mu,Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_pT(Mu,Mu)',
     'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_eta_vs_phi(Mu)',
     'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_eta_vs_phi(Tau)',
     'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_pT(Mu,Tau)',
     'HLT_Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_eta_vs_phi(Ele)',
     'HLT_Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_eta_vs_phi(Ele)',
     'HLT_Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_pT(Ele,Ele)',
     'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_eta_vs_phi(Ele)',
     'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_eta_vs_phi(Tau)',
     'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_pT(Ele,Tau)',
    ]

    if True:
        for hist in hists:
            print("Now plotting: " + hist)
    
            histlist = []
            for item in bglist:
                tfile = root_open(basedir + bglist[item][1] + ".root", "READ")
                t_eff = Graph(tfile.Get(hist).CreateGraph())
                t_eff.SetLineColor(colorList[item])
                t_eff.SetTitle(item)
                if 'Nvtx' in hist:
                    t_eff.xaxis.SetTitle('$N_{vtx}$')
                if 'pT' in hist:
                    t_eff.xaxis.SetTitle('$p_{T}$ (GeV)')
                t_eff.yaxis.SetTitle('$\epsilon$')
                histlist.append(t_eff)
    
            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper right", legendPosition = 'lower middle', lumi = 1000, cms = 13)
    
            test = plotter(hist = [histlist[0], histlist[1], histlist[2]],style=hist_style)
    
            test.Set_axis(logy = False, grid = True)
    
            test._cms_text_x         = 0.12
            test._cms_text_y         = 0.91
    
            name=hist.replace("/","")
    
            test.make_plot('plots/%s.pdf'%(name))

    if True:
        for hist in hists2D:
            print("Now plotting: " + hist)
    
            histlist = []
            for item in bglist:
                tfile = root_open(basedir + bglist[item][1] + ".root", "READ")
                t_eff = tfile.Get(hist).CreateHistogram()
                # t_eff.SetLineColor(colorList[item])
                t_eff.SetTitle(item)
                # t_eff.xaxis.SetTitle(t_eff.GetXaxis().GetTitle())
                # t_eff.yaxis.SetTitle(t_eff.GetYaxis().GetTitle())
                histlist.append(t_eff)
    
            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "upper left", legendPosition = 'lower middle', lumi = 1000, cms = 13)

            hist_style.Set_additional_text('plot dummy')

            test = plotter2D(hist = histlist[0], style = hist_style)

            # test.Set_axis(xmin = -2.5, xmax = 2.5, ymin = 0, ymax = 3.1, zmin = 0, zmax = 1)

            name=hist.replace("/","")

            test.create_plot()

            test.save_plot('plots/%s.pdf'%(name))

    return 42



main()
