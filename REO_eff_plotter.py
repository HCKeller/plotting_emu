#!/bin/env python

from DukePlotALot import *
from DukePlotALot2D import *
from plotlib import HistStorage,getColorList,getDictValue,HistStorageContainer
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
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
    colorList["PU20bx25"]=["lightblue","cornflowerblue"]
    colorList["AVE30BX50"]=["lightgreen","limegreen"]
    colorList["PU40bx25"]=["darkmagenta","orchid"]

    hists=[['RECO_Effs/eff_Ele_RECO_vs_Nvtx','RECO_Effs/eff_Ele_RECO_vs_Nvtx_in_Acc'],
     ['RECO_Effs/eff_Ele_RECO_vs_pT','RECO_Effs/eff_Ele_RECO_vs_pT_in_Acc'],
     ['RECO_Effs/eff_MET_RECO_vs_Nvtx'],
     ['RECO_Effs/eff_MET_RECO_vs_pT'],
     ['RECO_Effs/eff_Muon_RECO_vs_Nvtx','RECO_Effs/eff_Muon_RECO_vs_Nvtx_in_Acc'],
     ['RECO_Effs/eff_Muon_RECO_vs_pT','RECO_Effs/eff_Muon_RECO_vs_pT_in_Acc'],
     ['RECO_Effs/eff_Tau_RECO_vs_Nvtx','RECO_Effs/eff_Tau_RECO_vs_Nvtx_in_Acc'],
     ['RECO_Effs/eff_Tau_RECO_vs_pT','RECO_Effs/eff_Tau_RECO_vs_pT_in_Acc'],
    ]

    hists2D_eff=['RECO_Effs/eff_Tau_RECO_vs_eta_vs_phi',
     'RECO_Effs/eff_Tau_RECO_vs_eta_vs_phi_in_Acc',
     'RECO_Effs/eff_Muon_RECO_vs_eta_vs_phi',
     'RECO_Effs/eff_Muon_RECO_vs_eta_vs_phi_in_Acc',
     'RECO_Effs/eff_MET_RECO_vs_eta_vs_phi',
     'RECO_Effs/eff_Ele_RECO_vs_eta_vs_phi',
     'RECO_Effs/eff_Ele_RECO_vs_eta_vs_phi_in_Acc',
    ]

    hists2D=['RECO_Effs/h2_Tau_RECO_vs_gendm_vs_recodm_0_500',
     'RECO_Effs/h2_Tau_RECO_vs_gendm_vs_recodm_1000_1500',
     'RECO_Effs/h2_Tau_RECO_vs_gendm_vs_recodm_1500_2000',
     'RECO_Effs/h2_Tau_RECO_vs_gendm_vs_recodm_2000',
     'RECO_Effs/h2_Tau_RECO_vs_gendm_vs_recodm_500_1000',
    ]

    if False:
        for hist in hists:
            print("Now plotting: " + hist[0])

            histlist = []
            for item in bglist:
                counter = 0
                for it in hist:
                    tfile = root_open(basedir + bglist[item][1] + ".root", "READ")
                    t_eff = Graph(tfile.Get(it).CreateGraph())
                    t_eff.SetLineColor(colorList[item][counter])
                    if counter == 1:
                        t_eff.SetTitle(item+" in Acc.")
                    else:
                        t_eff.SetTitle(item)
                    if 'Nvtx' in it:
                        t_eff.xaxis.SetTitle('$N_{vtx}$')
                    if 'pT' in it:
                        t_eff.xaxis.SetTitle('$p_{T}$ (GeV)')
                    t_eff.yaxis.SetTitle('$\epsilon$')
                    histlist.append(t_eff)
                    counter += 1

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper right", legendPosition = 'lower middle', lumi = 1000, cms = 13)

            hist_style.Set_additional_text('work in progress')

            test = plotter(hist = histlist, style=hist_style)

            test.Set_axis(logy = False, grid = True)

            test._cms_text_x         = 0.12
            test._cms_text_y         = 0.91

            name=hist[0].replace("/","")

            test.make_plot('plots/%s.pdf'%(name))

    if False:
        for hist in hists2D_eff:
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

            hist_style.Set_additional_text('work in progress')

            test = plotter2D(hist = histlist[0], style = hist_style)

            # test.Set_axis(xmin = -2.5, xmax = 2.5, ymin = 0, ymax = 3.1, zmin = 0, zmax = 1)

            name=hist.replace("/","")

            test.create_plot()

            test.save_plot('plots/%s.pdf'%(name))

    if True:
        for hist in hists2D:
            print("Now plotting: " + hist)

            histlist = []
            for item in bglist:
                tfile = root_open(basedir + bglist[item][1] + ".root", "READ")
                t_eff = tfile.Get(hist)
                # t_eff.SetLineColor(colorList[item])
                t_eff.SetTitle(item)
                # t_eff.xaxis.SetTitle(t_eff.GetXaxis().GetTitle())
                # t_eff.yaxis.SetTitle(t_eff.GetYaxis().GetTitle())
                histlist.append(t_eff)

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "upper left", legendPosition = 'lower middle', lumi = 1000, cms = 13)

            hist_style.Set_additional_text('work in progress')
            hist_style.Set_y_label_offset(-0.5)

            test = plotter2D(hist = histlist[0], style = hist_style)

            test.Add_y_projection(15)
            test.Add_x_projection(15)

            # test.Set_axis(xmin = -2.5, xmax = 2.5, ymin = 0, ymax = 3.1, zmin = 0, zmax = 1)

            name=hist.replace("/","")

            test.create_plot()

            x_bin_labels = []
            for i in range(1,histlist[0].GetNbinsX()+1):
                x_bin_labels.append(histlist[0].GetXaxis().GetBinLabel(i))
            print(x_bin_labels)
            y_bin_labels = []
            for i in range(1,histlist[0].GetNbinsY()+1):
                label = histlist[0].GetYaxis().GetBinLabel(i)
                label = label.replace('tauDecay','')
                label = label.replace('ChargedPion','Pi')
                label = label.replace('Zero','0')
                y_bin_labels.append(label)
            print(y_bin_labels)
            test.Get_x_projection_axis().xaxis.set_major_locator(mticker.MaxNLocator(nbins=histlist[0].GetNbinsX()))
            xtickNames = plt.setp(test.Get_x_projection_axis(), xticklabels=x_bin_labels)
            plt.setp(xtickNames, rotation=-45, fontsize=8, va='top', ha='left')
            test.Get_x_projection_axis().tick_params('x', length=0, width=0, which='major')

            test.Get_y_projection_axis().yaxis.set_major_locator(mticker.MaxNLocator(nbins=histlist[0].GetNbinsY()))
            ytickNames = plt.setp(test.Get_y_projection_axis(), yticklabels=y_bin_labels)
            plt.setp(ytickNames, fontsize=8, va='bottom', ha='right')
            test.Get_y_projection_axis().tick_params('y', length=0, width=0, which='major')

            #test.Get_z_axis().yaxis.set_major_formatter(FixedOrderFormatter(0))
            # test.Get_z_axis().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            test.Get_x_projection_axis().ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
            test.Get_y_projection_axis().ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)

            plt.subplots_adjust(left = .1, bottom = .13, right =  .86, top = .95)

            test.save_plot('plots/%s.pdf'%(name))

    return 42



main()
