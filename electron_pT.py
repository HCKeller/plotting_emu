#!/bin/env python

from plot_inputs import *

def main():

    hists=[
    'emu/Stage_0/h1_0_emu_pT_ele',
    ]

    binning={
            "emu/Stage_0/h1_0_emu_pT_ele":5,
    }

    xranges={
            "emu/Stage_0/h1_0_emu_pT_ele":[0,600],
    }

    for hist in hists:
        print("Now plotting: " + hist)
        histContainer.getHist(hist)

        binf=getDictValue(hist,binning)
        if binf is not None:
            dat_hist.rebin(width=binf)
            bghists.rebin(width=binf)
            sghist.rebin(width=binf)

        hist_style = sc.style_container(style = 'CMS', useRoot = False,cms=13,lumi=lumi, cmsPositon = "upper left", legendPosition = 'upper right')
        hist_style.Set_n_legend_columns(2)

        dummy = bghists.getAllAdded()
        dummy.xaxis.SetTitle('')
        dummy.yaxis.SetTitle('')
        dummy.SaveAs('plots/' + hist.replace("/","") + '.root')

        test = plotter(hist=bghists.getHistList(), sig = sghist.getHistList(),style=hist_style)
        test.Add_data(dat_hist.getHistList()[0])

        #test.Add_plot('Diff',pos=1, height=15)
        # plt.xkcd()
        hist_style.Set_error_bands_fcol(['gray','orange'])
        hist_style.Set_error_bands_ecol(['black','black'])
        hist_style.Set_error_bands_labl(['Systematics','Statistic'])
        # hist_style.Set_xerr()

        # test.Add_plot('Ratio',pos=2, height=15)
        # if hist == 'emu/Stage_0/h1_0_emu_Mass':
            # sys_file=File('syst/for_plotting.root', "read")
        
            # test.Add_error_hist([sys_file.Get('Sys'),sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')
            # test.Add_error_hist([sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')

        test.Add_plot('Diff',pos=0, height=12)

        test.Add_plot('DiffRatio',pos=1, height=12)
        test.Add_plot('Signi',pos=2, height=12)
# 
        # mxrange=getDictValue(hist,xranges)
        if hist in xranges.keys():
            test.Set_axis(logx=False,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-4,ymax=1e3)
            #test.Set_axis(logx=False,logy=True,xmin=0,xmax=500,ymin=1e-6,ymax=1e3)

        name=hist.replace("/","")

        test.create_plot()

        test.Get_axis0().set_ylim(ymin = -7.0, ymax = 5.0)
        test.Get_axis2().set_ylim(ymin = -3, ymax = 13)
        test.Get_axis3().set_ylim(ymin = -3, ymax = 3.0)

        test.SavePlot('plots/%s.pdf'%(name))
    return 42



main()
