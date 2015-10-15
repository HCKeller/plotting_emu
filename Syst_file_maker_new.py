#!/bin/env python
# -*- coding: utf-8 -*-

from plot_inputs import *
import ROOT as r
import numpy as np

def get_binning_linear(start,end,nBins):
	
  	binArray = np.zeros(nBins)
        	
	if(start>end):
		return binArray
        for i in range(nBins):
		binArray[i] = start+i*(end-start)/nBins		

	return binArray    
   
def createSystPlots(obsName, binning, ContTitle, xmin_sys, xmax_sys, xmin_sys_abs, xmax_sys_abs, opt = False):
	

	if(opt == True):
	  myinput_rawhistos = raw_input("Save all raw histos for observable " + obsName + "? (y/n)\n")
	  myinput_relsys = raw_input("Save plots with relativ systematics for observable " + obsName + "?(y/n)\n")
	  myinput_relsys_comb = raw_input("Save plots with relativ systematics combined for observable " + obsName + "?(y/n)\n")
	else:
	  myinput_rawhistos = "n"
          myinput_relsys = "n"
	  myinput_relsys_comb ="y"
  
	special_colors = {
    	 'Ele_syst_Scale':'red',
     	'Muon_syst_Scale':'blue',
     	'Muon_syst_Resolution':'green',
     	'Tau_syst_Scale':'pink',
     	'MET_syst_Scale':'teal',
    	 'Jet_syst_Scale':'magenta',
    	 'Jet_syst_Resolution':'gray',
    	}
	   

	
	#implesdf

    	syst_part=      ["Ele", "Muon", "Tau", "MET", "Jet"]
    	syst_type=      ["Scale", "Resolution"]
    	syst_updown=    ["Up", "Down"]
    	
	hists=[]
    	hists.append("emu/Stage_0/h1_0_emu_" + obsName)
    	for part in syst_part:
        	for itype in syst_type:
            	   if (part == 'Ele' or part == 'Tau' or part == 'MET') and itype == 'Resolution':
                 	continue
            	   for updown in syst_updown:
                	hists.append("emu/Stage_0/sys/h1_0_emu_" + obsName + "_%s_syst_%s%s"%(part,itype,updown))

    	histContainer=HistStorageContainer(bg=bghists)

    	bghists.initStyle(style="bg")

    	useROOOT=False

    	hist_style = sc.style_container(style = 'CMS' ,cmsPositon="upper left", useRoot = useROOOT,cms = 13, lumi = 40.8 + 16.3 + 25.028)

    	bg_outFile=File("syst/bg_for_limit" + obsName + ".root", "recreate")

    	sigOut={}
    	for sig in sghist.files:
        	sigOut[sig]=File("syst/%s"%(sig) + obsName + ".root", "recreate")

    	mainHist=None
    
   	syst_hists=OrderedDict()
   	rel_systhist=OrderedDict()
   	rel_systhist_abs=OrderedDict()

   	systcolors=getColorList(len(hists))

        

   	for hist in hists:

   	     histContainer.getHist(hist)
	     histContainer.setTitle(ContTitle)
	     # histContainer.rebin(vector=get_binning_from_hist('res_unc.root','func',[0,4000],min_binning = 5))
   	     # histContainer.rebin(width=5)

   	     allbg=bghists.getAllAdded()
   	     if allbg.integral() <1:
   	         print "ignored hist: ",hist
   	         continue

   	     # print('integral 1: %f'%allbg.integral())
   	     # allbg = fit_histo(allbg)
   	     # print('integral 2: %f'%allbg.integral())
	     
  
             rebinnedHist=allbg.rebinned(binning)
   	     rebinnedHist.xaxis.SetTitle(allbg.xaxis.GetTitle())
   	     allbg=rebinnedHist
   	     histContainer.rebin(vector=binning)
   	     # print('integral 3: %f'%allbg.integral())
   	     # for ibin in allbg:
   	         # ibin.value=ibin.value/(ibin.x.width)
   	         # ibin.error=ibin.error/(ibin.x.width)
   	     allbg.SetTitle(hist.replace("emu/Stage_0/h1_0_emu_" + obsName,"Main"))
   	     allbg.decorate(fillstyle = '0',linewidth = 1,linecolor = systcolors.pop())
   	     # allbg.Draw('hist')
   	     # raw_input('bla')

   	     if hist=="emu/Stage_0/h1_0_emu_" + obsName:
   	         stat_hist = allbg.clone('MC statistic')
   	         for ibin in stat_hist:
   	             ibin.value = 0
   	         stat_hist.SetTitle('MC statistic')
   	         stat_hist.SetName('MC statistic')
   	         stat_hist.SetColor('orange')
   	         for (ibin,jbin) in zip(stat_hist,allbg):
   	             if jbin.value != 0:
   	                 # print(ibin.idx,jbin.value,jbin.error)
   	                 ibin.value = abs(jbin.error / jbin.value)
   	             else:
   	                 # print(ibin.idx,'  setting zero')
   	                 ibin.value = 0.0
   	         rel_systhist_abs['MC statistic'] = stat_hist
	
   	     if hist=="emu/Stage_0/h1_0_emu_"+ obsName:
   	         mainHist=allbg
   	     else:
   	         rel_systhist[hist] = (allbg/mainHist)
   	         rel_systhist[hist].SetTitle(hist.replace("emu/Stage_0/h1_0_emu_"+ obsName,""))
   	         rel_systhist[hist].GetYaxis().SetTitle("rel uncertainty")
   	         for ibin in rel_systhist[hist].bins():
   	             ibin.value=ibin.value-1.
   	     syst_hists[hist]=allbg
	
   	     if hist=="emu/Stage_0/h1_0_emu_"+ obsName:
   	         bg_outFile.WriteObject(allbg,"Main")
   	     else:
   	          bg_outFile.WriteObject(allbg,hist.replace("emu/Stage_0/h1_0_emu_"+ obsName,"Main"))
   	     print hist.replace("emu/Stage_0/h1_0_emu_"+ obsName,"Main")
	
   	     bgs=histContainer.getBGList()
   	     for ih in bgs:
   	         ih.SetTitle(ih.GetTitle().replace("emu/Stage_0/h1_0_emu_"+ obsName," "))
	
   	     allbg.SetLineColor('black')
   	     allbg.SetLineWidth(1)
   	     allbg.SetTitle('fit')
	
   	     test = plotter(hist=bgs,sig=[allbg],style=hist_style,cmsPositon="upper left",useRoot = useROOOT)
		
	     test.Set_axis(xmin=xmin_sys,xmax=xmax_sys)
   	     name=hist.replace("/","")
		

   	     plot=test.create_plot()
 		
	     if(myinput_rawhistos == "y"):	
		test.SavePlot('syst/%s.png'%(name))
		test.SavePlot('syst/%s.pdf'%(name))
	     
   	     del test
	
   	test = plotter(sig=syst_hists.values(),style=hist_style,useRoot = useROOOT)
   	test.create_plot()
        if(myinput_relsys == "y"):
	  test.SavePlot('syst/allsyst'+ obsName +'.png')
	  test.SavePlot('syst/allsyst'+ obsName +'.pdf')
    	del test


   	test = plotter(sig=rel_systhist.values(),style=hist_style,useRoot = useROOOT)
	
	test.Set_axis(logy=False,ymin=-0.5,ymax=1.,xmin=xmin_sys,xmax=xmax_sys)
   	test.create_plot()
   	if(myinput_relsys == "y"):
	  test.SavePlot('syst/relsyst'+ obsName +'.png')
	  test.SavePlot('syst/relsyst'+ obsName +'.pdf')
   	del test

	#print obsName
    	for part in syst_part:
       	  for itype in syst_type:
        	    if (part == 'Ele' or part == 'Tau' or part == 'MET') and itype == 'Resolution':
        	        continue
       	     	    rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)] = rel_systhist["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s%s"%(part,itype,'Up')]
        	    rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)].SetTitle(rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)].GetTitle().replace('Up','').replace('emu/Stage_0/sys/h1_0_emu_'+ obsName +'_',''))
            	    rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)].SetColor(special_colors[rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)].GetTitle()])
                    rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)].GetXaxis().SetTitle('$M_{e\mu}$ (GeV)')
   	            for (ibin,jbin,kbin) in zip(rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s"%(part,itype)],rel_systhist["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s%s"%(part,itype,'Up')],rel_systhist["emu/Stage_0/sys/h1_0_emu_"+ obsName +"_%s_syst_%s%s"%(part,itype,'Down')]):
        		        if abs(jbin.value) > abs(kbin.value):
        		            ibin.value=abs(jbin.value)
        		        else:
                   		    ibin.value=abs(kbin.value)

   	sum_hist = allbg.clone('Sum')
    	for ibin in sum_hist:
        	ibin.value = 0
    	sum_hist.SetTitle('Sum')
    	sum_hist.SetName('Sum')
    	sum_hist.SetColor('black')
    	for item in rel_systhist_abs:
        	for (ibin,jbin) in zip(sum_hist,rel_systhist_abs[item]):
       		     ibin.value += (jbin.value**2)

   	for ibin in sum_hist:
        	ibin.value = np.sqrt(ibin.value)
        	if ibin.value > 2:
            		ibin.value = 0

    	rel_systhist_abs['sum'] = sum_hist

   	sys_hist = allbg.clone('Sys')
    	for ibin in sys_hist:
        	ibin.value = 0
    	sys_hist.SetTitle('Sys')
    	sys_hist.SetName('Sys')
    	sys_hist.SetColor('black')
    	for item in rel_systhist_abs:
        	if 'statistic' in item:
            		continue
        	for (ibin,jbin) in zip(sys_hist,rel_systhist_abs[item]):
            		ibin.value += (jbin.value**2)

    	for ibin in sys_hist:
        	ibin.value = np.sqrt(ibin.value)
        	if ibin.value > 2:
            		ibin.value = 0

    	sum_outFile=File("syst/for_plotting"+ obsName +".root", "recreate")
	#hist_syst_fromplottingFile = sum_outFile.Get('Sys')
	#hist_MCstat_fromplottingFile = sum_outFile.Get('MC statistic')
      
    	sys_hist.Write()
    	stat_hist.Write()
    	sum_outFile.Close()

    	test = plotter(sig=rel_systhist_abs.values(),style=hist_style,useRoot = useROOOT)
	test.Set_axis(logy=False,ymin=0.,ymax=0.4,xmin=xmin_sys_abs,xmax=xmax_sys_abs)    	
	test.create_plot()
    	if(myinput_relsys_comb == "y"):
	  test.SavePlot('syst/relsyst_comb'+ obsName +'.png')
	  test.SavePlot('syst/relsyst_comb'+ obsName +'.pdf')
    	del test


    	bg_outFile.Close()
    	# for sig in sigOut:
        	# sigOut[sig].Close()
		
	del hists
	
	#return [hist_syst_fromplottingFile,hist_MCstat_fromplottingFile]
	return sum_outFile

def main():

    
    binning_MT = get_binning_from_hist('res_unc.root','func',[0,4000],debug = False, min_binning = 5)
    binning_PT = get_binning_from_hist('res_unc.root','func',[0,500],debug = False, min_binning = 10)
    observable = ["Mass","dR","Delta_phi_ele_muo","Pt","deltaR_match_ele","deltaR_match_ele","eta_ele","eta_muo","pT_ele","pT_muo","pT_ratio_ele_muo","pT_resolution_ele","pT_resolution_muo","phi_ele","phi_muo"]
    
    
    #createSystPlots(observable[0],binning_MT,"Mass [GeV]",0.,3000.,50,1200)
    #createSystPlots(observable[1],get_binning_linear(0.,10,20),"#Delta R_{ele,muo}",0.,10.,0.,10.)
    #createSystPlots(observable[2],get_binning_linear(0.,5,10),"#Delta #Phi (ele,muo) [rad]",0.,5.,0.,5.)
    #createSystPlots(observable[3],get_binning_linear(0.,500,100),"Pt (ele,muo) [GeV]",0.,500.,0.,500.)
    #createSystPlots(observable[6],get_binning_linear(-4.,4,40),"#eta_{ele}",-4.,4.,-4.,4.)   
    #createSystPlots(observable[7],get_binning_linear(-4.,4,40),"#eta_{muo}",-4.,4.,-4.,4.)
    createSystPlots(observable[8],binning_PT,"p_{T}^{ele} [GeV]",0.,500.,0.,500)
    createSystPlots(observable[9],binning_PT,"p_{T}^{muo} [GeV]",0.,500,0.,500)
    #createSystPlots(observable[10],get_binning_linear(0.,10,20),"#frac{p_{T}^{ele}}{p_{T}^{muo}}",0.,10.,0.,10.)
    #createSystPlots(observable[13],get_binning_linear(-3.,3,20),"#Phi_{ele}",-3.,3,-3.,3)
    #createSystPlots(observable[14],get_binning_linear(-3.,3,20),"#Phi_{muo}",-3.,3,-3.,3)

    
    return 42



#main()
