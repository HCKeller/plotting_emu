#!/bin/env python
# -*- coding: utf-8 -*-

from plot_inputs import *

def main():

    hists=[
    'emu/Stage_0/h1_0_emu_Mass',
    ]

    binning={
            "Taus/h1_2_Tau_pt":10,
            "Muons/h1_2_Muon_pt":20,
            "Eles/h1_2_Ele_pt":20,
            # "emu/Stage_0/h1_0_emu_Mass":10,
            # "mutau/Stage_0/h1_0_mutau_Mass":range(200,300,20)+range(300,400,50)+range(400,1600,100)+range(1600,2000,200),
            # "mutau/Stage_6/h1_6_mutau_Mass":range(200,300,20)+range(300,400,50)+range(400,1600,100)+range(1600,2000,200),
            "_met_et":30,
    }

    binning.update({"emu/Stage_0/h1_0_emu_Mass":get_binning_from_hist('res_unc.root','func',[0,4000],min_binning = 5)})
    # binning.update({"emu/Stage_0/h1_0_emu_Mass":range(0,4000,1)})

    xranges={
            "emu/Stage_0/h1_0_emu_Mass":[50,3000],
    }

    for hist in hists:
        print("Now plotting: " + hist)
        histContainer.getHist(hist)

        binf=getDictValue(hist,binning)
        if binf is not None:
            dat_hist.rebin(width=1,vector=binf)
            bghists.rebin(width=1,vector=binf)
            sghist.rebin(width=1,vector=binf)

        hist_style = sc.style_container(style = 'CMS', useRoot = False,cms=13,lumi=lumi, cmsPositon = 'upper left')

        dummy = bghists.getAllAdded()
        dummy.xaxis.SetTitle('')
        dummy.yaxis.SetTitle('')
        dummy.SaveAs('plots/' + hist.replace("/","") + '.root')

        test = plotter(hist=bghists.getHistList(), sig = sghist.getHistList(),style=hist_style)
        test.Add_data(dat_hist.getHistList()[0])

        hist_style.Set_error_bands_fcol(['gray','orange'])
        hist_style.Set_error_bands_ecol(['black','black'])
        hist_style.Set_error_bands_labl(['Systematics','Statistic'])

        if hist == 'emu/Stage_0/h1_0_emu_Mass':
            sys_file=File('syst/for_plottingMass.root', "read") 
        
            test.Add_error_hist([sys_file.Get('Sys'),sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')
            # test.Add_error_hist([sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')

        test.Add_plot('Diff',pos=0, height=12)

        test.Add_plot('DiffRatio',pos=1, height=12)
        test.Add_plot('Signi',pos=2, height=12)

        if hist in xranges.keys():
            test.Set_axis(logx=True,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-6,ymax=1e3)

        name=hist.replace("/","")

        test.create_plot()

        test.Get_axis0().set_ylim(ymin = -1.2, ymax = 1.7)
        test.Get_axis2().set_ylim(ymin = -3, ymax = 13)
        test.Get_axis3().set_ylim(ymin = -2, ymax = 2.0)

        test.SavePlot('plots/%s.pdf'%(name))
    return 42



main()
