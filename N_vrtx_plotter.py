#!/bin/env python
import os
import sys, getopt
from plot_inputs import *

def main(argv):
    
    weighting = 'on' #on or off
    try:
        opts, args = getopt.getopt(argv,"hw:",["weighting="])
    except getopt.GetoptError:
	print 'N_vrtx_plotter.py -w <weighting (on/off) default on)>'
	sys.exit(2)
    for opt, arg in opts:
	if opt == '-h':
	    print 'N_vrtx_plotter.py -w <weighting (on/off) default on>'
	    sys.exit()
        elif opt in ("-w", "--weighting"):
	    weighting = arg
        
    print 'Run over weighting "', weighting
    
    if weighting == "on":
	hists=[
	'Ctr/h1_Ctr_Vtx_weighted',
	'Ctr/h1_Ctr_Vtx_emu_weighted',
	]

	binning={
            'Ctr/h1_Ctr_Vtx_weighted':1,
            'Ctr/h1_Ctr_Vtx_emu_weighted':1
	}

	xranges={
            "Ctr/h1_Ctr_Vtx_weighted":[0,50],
            "Ctr/h1_Ctr_Vtx_emu_weighted":[0,50],
	}
    elif weighting == "off":
	hists=[
	'Ctr/h1_Ctr_Vtx_unweighted',
	'Ctr/h1_Ctr_Vtx_emu_unweighted',
	]

	binning={
            'Ctr/h1_Ctr_Vtx_unweighted':1,
            'Ctr/h1_Ctr_Vtx_emu_unweighted':1
	}

	xranges={
            "Ctr/h1_Ctr_Vtx_unweighted":[0,50],
	    "Ctr/h1_Ctr_Vtx_emu_unweighted":[0,50],
	}
    else:
	print("possible input for weighting option is on/off")
	return 42;

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

        #dummy = bghists.getAllAdded()
        #dummy.xaxis.SetTitle('')
        #dummy.yaxis.SetTitle('')
        #dummy.SaveAs('plots/' + hist.replace("/","") + '.root')

	#save data hists
	helper = dat_hist.getAllAdded()
	helper.yaxis.SetTitle('')
	helper.SetName('data_pileup')
	helper.SaveAs('plots/' + hist.replace("/","") + '_data_pileup.root')
	
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
	
	name=hist.replace("/","")
	
	if name == "Ctrh1_Ctr_Vtx_weighted" or name == "Ctrh1_Ctr_Vtx_unweighted":
        # mxrange=getDictValue(hist,xranges)
	    if hist in xranges.keys():
		test.Set_axis(logx=False,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-2,ymax=1e5)
		#test.Set_axis(logx=False,logy=True,xmin=0,xmax=500,ymin=1e-6,ymax=1e3)
	    
	    test.create_plot()

	    test.Get_axis0().set_ylim(ymin = -6.0, ymax = 5.0)
	    test.Get_axis2().set_ylim(ymin = -3, ymax = 13)
	    test.Get_axis3().set_ylim(ymin = -30.5, ymax = 30.5)


	if name == "Ctrh1_Ctr_Vtx_emu_weighted" or name == "Ctrh1_Ctr_Vtx_emu_unweighted":
	    if hist in xranges.keys():
		test.Set_axis(logx=False,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-2,ymax=1e3)
	
	    test.create_plot()

	    test.Get_axis0().set_ylim(ymin = -6.0, ymax = 5.0)
	    test.Get_axis2().set_ylim(ymin = -3, ymax = 13)
	    test.Get_axis3().set_ylim(ymin = -5.5, ymax = 5.5)

        test.SavePlot('plots/%s.pdf'%(name))
        
    return 42



if __name__ == "__main__":
    main(sys.argv[1:])
