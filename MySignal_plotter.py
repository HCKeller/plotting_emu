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

def make_individual_res_plot():
    pass

def main():

    basedir="/.automount/home/home__home1/institut_3a/keller/Masterthesis/Results_MassResolution/"
    
    # lumi=19712

    # xs= ConfigObj("/disk1/erdweg/plotting/xs_Phys14.cfg")
    # bghists=HistStorage(xs,lumi,path=basedir,isData=True)

    colors = ['lime', 'deepskyblue', 'magenta', 'orangered']

    bglist=OrderedDict()

    bglist = [
     #'Asymptotic/Mass1000/SpecialHistos',
     #'Startup/Mass1000/SpecialHistos',
     #'Asymptotic/Mass1200/SpecialHistos',
     #'Startup/Mass1200/SpecialHistos',
     #'Asymptotic/Mass1400/SpecialHistos',
     #'Startup/Mass1400/SpecialHistos',
     'Asymptotic/Mass1600/SpecialHistos',
     'Startup/Mass1600/SpecialHistos',
     'Asymptotic/Mass1800/SpecialHistos',
     'Startup/Mass1800/SpecialHistos',
     'Asymptotic/Mass2000/SpecialHistos',
     'Startup/Mass2000/SpecialHistos',
      
    ]

    colorList={}
    colorList['SpecialHistos'] = 'lightblue'

    res_histos = [
     'emu/Stage_0/h2_0_emu_Mass_resolution'
    ]

    res_histos1D = [
     'emu/Stage_0/h1_0_emu_Mass_resolution'
    ]

    binning={
            "_vs_pT":10,
            "_vs_Mass":10,
    }

    titles={
     'emu/Stage_0/h1_0_emu_Mass_resolution':['Mass resolution asymptotic','$M_{e\mu, gen}\,\,\mathrm{(GeV)}$','$\sigma((M_{e\mu, reco} - M_{e\mu, gen}) / M_{e\mu, gen})$','Mass resolution startup','$M_{e\mu, gen}\,\,\mathrm{(GeV)}$','$\sigma((M_{e\mu, reco} - M_{e\mu, gen}) / M_{e\mu, gen})$'],
    }
   
    ####################################################################
    # Individual resolution plots
    ####################################################################

    if True:
        for hist in res_histos1D:
            print("Now plotting: " + hist)

            x_vals =[]
            y_vals = []
            y_errs = []
            x_vals_startup =[]
            y_vals_startup = []
            y_errs_startup = []
            for item in bglist:
                if 'SpecialHistos' not in item:
                    continue
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist)
                t_eff.xaxis.SetTitle('$'+t_eff.xaxis.GetTitle()+'$')
                t_eff.yaxis.SetTitle('Events / %.2f'%t_eff.GetBinWidth(1))

                hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower left', lumi = 0, cms = 13)
                hist_style.Set_additional_text('Spring15 simulation')
                test = plotter(hist = [t_eff],style=hist_style)
                name=item.replace("/","")
                test.Set_axis(logy = False, grid = True, xmin = -1.01, xmax = 1.01, ymin = 0.9, ymax = 4000)
                test.create_plot()

                plot_gauss_fit(test.Get_axis1(), t_eff, color = 'red', write_results = True)

                test.SavePlot('plots/%s.pdf'%(name))

                fit_res = t_eff.Fit('gaus', 'N0S', '')
                if(item[0:-23] == "Asymptotic"):
		    y_vals.append(fit_res.Parameter(2))
		    y_errs.append(fit_res.ParError(2))
		    x_vals.append(int(item[15:-14]))
		if(item[0:-23] == "Startup"):
		    y_vals_startup.append(fit_res.Parameter(2))
		    y_errs_startup.append(fit_res.ParError(2))
		    x_vals_startup.append(int(item[12:-14]))
		
		
		
            x_vals = np.array(x_vals)
            y_vals = np.array(y_vals)
            y_errs = np.array(y_errs)
	    

	    x_vals_startup = np.array(x_vals_startup)
            y_vals_startup = np.array(y_vals_startup)
            y_errs_startup = np.array(y_errs_startup)
	    #print(len(x_vals))
	    #print(len(y_vals))
	    #print(len(y_errs))
	      
	    ### create plots for asymptotic
            graph = Graph(x_vals.shape[0])
            for i, (xx, yy, ye) in enumerate(zip(x_vals, y_vals, y_errs)):
                graph.SetPoint(i, xx, yy)
                graph.SetPointError(i, 0, 0, ye, ye)

            i_titles = getDictValue(hist, titles)

            if i_titles is not None:
                graph.SetTitle(i_titles[0])
                graph.xaxis.SetTitle(i_titles[1])
                graph.yaxis.SetTitle(i_titles[2])

            graph.SetLineColor('red')
	    
	    ### create plots for startup
            graph_startup = Graph(x_vals_startup.shape[0])
            for i, (xx, yy, ye) in enumerate(zip(x_vals_startup, y_vals_startup, y_errs_startup)):
                graph_startup.SetPoint(i, xx, yy)
                graph_startup.SetPointError(i, 0, 0, ye, ye)

            i_titles = getDictValue(hist, titles)

            if i_titles is not None:
                graph_startup.SetTitle(i_titles[3])
                graph_startup.xaxis.SetTitle(i_titles[4])
                graph_startup.yaxis.SetTitle(i_titles[5])

            graph_startup.SetLineColor('blue')
	      
            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower left', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')

            test = plotter(hist = [graph, graph_startup],style=hist_style)

            name=hist.replace("/","")

            test.Set_axis(logy = False, grid = True, xmin = 0, xmax = 6500)

            test.create_plot()

            #func = plot_resolution_fit(test.Get_axis1(), graph, xmin = 0, xmax = 6000, startvals = [], plottrange = [], color = 'black')

            test.SavePlot('plots/%s.pdf'%(name))
            graph.SaveAs('plots/%s.root'%(name))
            #func.SaveAs('plots/%s_func.root'%(name))

    return 42



main()