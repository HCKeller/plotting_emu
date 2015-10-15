#!/bin/env python

from DukePlotALot import *
from plotlib import HistStorage,getColorList,getDictValue,HistStorageContainer
import matplotlib.pyplot as plt
from configobj import ConfigObj
try:
    from collections import OrderedDict
except ImportError:
    from ordered import OrderedDict

from rootpy.plotting.views import ScaleView

from object_plotting import *

def main():

    basedir="/disk1/erdweg/out/output2015_2_13_15_47/merged//"
    lumi=1000

    xs= ConfigObj("/disk1/erdweg/plotting/xs_Phys14.cfg")
    bghists=HistStorage(xs,lumi,path=basedir)
    # bghists.setDataDriven("dataDrivenQCD")

    bglist=OrderedDict()

    bglist["PU20bx25"]=['ZprimeToTauTau_M-5000_PU20bx25_PHYS14',
     'ZprimeToTauTau_M-1000_PU20bx25_PHYS14',
    ]
    bglist["AVE30BX50"]=['ZprimeToTauTau_M-1000_AVE30BX50_PHYS14',
     'ZprimeToTauTau_M-5000_AVE30BX50_PHYS14',
     ]
    bglist["PU40bx25"]=['ZprimeToTauTau_M-1000_PU40bx25_PHYS14',
     'ZprimeToTauTau_M-5000_PU40bx25_PHYS14',
    ]

    colorList={}
    colorList["PU20bx25"]="lightblue"
    colorList["AVE30BX50"]="lightgreen"
    colorList["PU40bx25"]="darkmagenta"

    bghists.addFileList(bglist)

    dat_hist=HistStorage(xs,lumi,path=basedir,isData=True)
    # dat_hist.addFile("Data")

    hists=[#'Taus/h1_1_Tau_eta',
    #'Taus/h1_1_Tau_phi',
    #'Taus/h1_2_Tau_pt',
    #'Taus/h1_Tau_pt_resolution_0_500',
    'Eles/h1_Ele_pt_resolution_0_500',
    'Eles/h1_Ele_pt_resolution_500_1000',
    #'Eles/h1_2_Ele_pt',
    'Muons/h1_Muon_pt_resolution_0_500',
    'Muons/h1_Muon_pt_resolution_500_1000',
    #'Muons/h1_2_Muon_pt',
    #'emu/Stage_0/h1_0_emu_Mass',
    #'mutau/Stage_0/h1_0_mutau_Mass',
    #'mutau/Stage_6/h1_6_mutau_Mass',
    #'Ctr/h1_Ctr_Vtx_unweighted',
    #'Ctr/h1_Ctr_Vtx_weighted',
    #'Ctr/h1_Ctr_Vtx_emu_unweighted',
    #'Ctr/h1_Ctr_Vtx_emu_weighted',
    #'Ctr/h1_Ctr_HT',
    #'Ctr/h1_Ctr_pT_hat',
    #'emu/Stage_0/h1_0_emu_Mass_resolution',
    #'mutau/Stage_0/h1_0_mutau_Mass_resolution'
    ]

    sghist=HistStorage(xs,lumi,path=basedir)
    # sgName="$\mathsf{W' \, M=2.3\,TeV \cdot 0.02}$"
    # sghist.additionalWeight={"WprimeToTauNu_M-2300_TuneZ2star_8TeV-pythia6-tauola_Summer12_DR53X-PU_S10_START53_V7A-v1SIM":0.02}
    # sghist.addAllFiles(tag="WprimeToTauNu_M-2300",joinName=sgName)
    # sghist.colorList={sgName :"darkred"}

    histContainer=HistStorageContainer(sg=bghists,data=dat_hist,bg=sghist)

    binning={
            "Taus/h1_2_Tau_pt":10,
            # "emu/Stage_0/h1_0_emu_Mass":range(200,300,20)+range(300,400,50)+range(400,1600,100)+range(1600,2000,200),
            # "mutau/Stage_0/h1_0_mutau_Mass":range(200,300,20)+range(300,400,50)+range(400,1600,100)+range(1600,2000,200),
            # "mutau/Stage_6/h1_6_mutau_Mass":range(200,300,20)+range(300,400,50)+range(400,1600,100)+range(1600,2000,200),
            "_met_et":30,
    }

    xranges={
            "Taus/h1_2_Tau_pt":[0,2000],
            "emu/Stage_0/h1_0_emu_Mass":[0,2000],
            "mutau/Stage_0/h1_0_mutau_Mass":[0,2000],
            "mutau/Stage_6/h1_6_mutau_Mass":[0,2000],
            "emu/Stage_0/h1_0_emu_Mass_resolution":[-2,2],
            "mutau/Stage_0/h1_0_mutau_Mass_resolution":[-2,2],
            "Taus/h1_Tau_pt_resolution_0_500":[-2,2],
            "Eles/h1_Ele_pt_resolution_0_500":[-2,2],
            "Eles/h1_Ele_pt_resolution_500_1000":[-2,2],
            "Muons/h1_Muon_pt_resolution_0_500":[-2,2],
            "Muons/h1_Muon_pt_resolution_500_1000":[-2,2],
            "Ctr/h1_Ctr_Vtx_unweighted":[0,40],
            "Ctr/h1_Ctr_Vtx_weighted":[0,40],
            "Ctr/h1_Ctr_Vtx_emu_unweighted":[0,40],
            "Ctr/h1_Ctr_Vtx_emu_weighted":[0,40],
    }

    bghists.initStyle(style="sg",colors=colorList)
    # sghist.initStyle(style="sg")

    for hist in hists:
        print("Now plotting: " + hist)
        histContainer.getHist(hist)

        binf=getDictValue(hist,binning)
        if binf is not None:
            # dat_hist.rebin(width=binf)
            bghists.rebin(width=binf)
        bghists.colorList=colorList
        # bghists.setStyle(bgcolors=colorList)
        # dat_hist.getHistList()[0].SetTitle("data")

        hist_style = sc.style_container(style = 'CMS', useRoot = False,cms=13,lumi=19700)
        hist_style.Set_additional_text('plot dummy')

        test = plotter(sig=bghists.getHistList(),style=hist_style)
        # test.Add_data(dat_hist.getHistList()[0])
        # test.Add_plot('Signi',pos=0, height=15)

        #test.Add_plot('DiffRatio',pos=1, height=15)
        # test.Add_plot('Signi',pos=2, height=15)
        # test.Add_plot('Diff',pos=1, height=15)

        # test.Add_plot('Ratio',pos=2, height=15)
        #test.Add_error_hist([sys_hist_2,sys_hist], band_center = 'ref')

        test._cms_text_x         = 0.12
        test._cms_text_y         = 0.91
# 
        # mxrange=getDictValue(hist,xranges)
        if hist in xranges.keys():
            test.Set_axis(xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-3,ymax=1e3)

        name=hist.replace("/","")

        test.create_plot()

        plot_gauss_fit(test.Get_axis1(), bghists.getHistList()[0], xmin = -0.5, xmax = 0.5)

        # test.show_fig()

        test.SavePlot('plots/%s.pdf'%(name))
    return 42



main()
