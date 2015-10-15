#!/bin/env python

from plot_inputs import *
import ROOT as r

def fit_histo(hist,function='exp([0]*x+[1] + [3] * x * x) * x^[2]',funcbeg=180,funcend=2000,fitbeg=150,fitend=1100):
    return hist
    hist_rb = hist.Clone('tb_fitted')
    hist_rb.rebin(10)
    hist_rb.Scale(0.1)
    # r.Math.MinimizerOptions.SetDefaultMinimizer("Minuit2","Combined")
    # r.Math.MinimizerOptions.SetDefaultMaxIterations(500000000)#if minimizer = GLS
    # r.Math.MinimizerOptions.SetDefaultMaxFunctionCalls(500000000)#if minimizer = minuit
    # r.Math.MinimizerOptions.SetDefaultTolerance(0.0001)
    func = r.TF1("f1",function, funcbeg, funcend)

    start_vals = [-6.67601e-03, 6.51502, -1.10583, 7.77104e-08]

    for i in range(len(start_vals)):
        func.SetParameter(i,start_vals[i])

    # func.SetNpx(hist.GetNbinsX())
    fit_res = hist_rb.Fit(func,"+SQ","", fitbeg, fitend)
    fit_res.Print("Q")
    fit_status = int(fit_res)
    print "status:",fit_status

    dummy_bins = int(funcend)

    # dummy_file = r.TFile('%s.root'%hist.GetTitle(),'RECREATE')
    # hist.Write()
    # func.Write()
    # rebinfactor=hist.GetBinWidth(1)
    # print "rebinfactor:",rebinfactor
    # binnig = r.Double_t()
    # binning = get_binning_from_hist('res_unc.root','func',[0,4000],min_binning = 5)
    # hist_rb = hist.rebinned(binning)
    # hist_rb.SetTitle(hist.GetTitle() + '_rebinned')
    histFit = hist.Clone(hist.GetTitle() + '_fitted')
    # hist_rb.Write()
    # raw_input('bla')
    for i in range(0, hist.FindBin(funcbeg)):
        binw = float(hist.GetBinWidth(i))
        binw = 1
        histFit.SetBinContent(i,hist.GetBinContent(i)/binw)
        histFit.SetBinError(i,hist.GetBinError(i)/binw)
    for i in range(hist.FindBin(funcbeg), hist.GetNbinsX()):
        try:
            binw = float(hist.GetBinWidth(i))
            binw = 1
            ledg = hist.GetBinLowEdge(i)
            histFit.SetBinContent(i,(func.Integral(ledg,ledg+binw)/binw))
            histFit.SetBinError(i,(func.IntegralError(ledg,ledg+binw)/binw))
        except:
            try:
                binw = float(hist.GetBinWidth(i))
                histFit.SetBinContent(i,(func.Integral(hist.GetBinLowEdge(i),hist.GetBinLowEdge(i)+hist.GetBinWidth(i))/hist.GetBinWidth(i)))
                histFit.SetBinError(i,np.sqrt(histFit.GetBinContent(i)))
            except:
                pass
            print "No good fit use the hist"
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
            # dummy_file.Close()
            return hist
    # histFit.Write()
    # dummy_file.Close()

    return histFit


def main():

    special_colors = {
     'Ele_syst_Scale':'red',
     'Muon_syst_Scale':'blue',
     'Muon_syst_Resolution':'green',
     'Tau_syst_Scale':'pink',
     'MET_syst_Scale':'teal',
     'Jet_syst_Scale':'magenta',
     'Jet_syst_Resolution':'gray',
    }

    syst_part=      ["Ele", "Muon", "Tau", "MET", "Jet"]
    syst_type=      ["Scale", "Resolution"]
    syst_updown=    ["Up", "Down"]
    hists=[]
    hists.append("emu/Stage_0/h1_0_emu_Mass")
    for part in syst_part:
        for itype in syst_type:
            if (part == 'Ele' or part == 'Tau' or part == 'MET') and itype == 'Resolution':
                continue
            for updown in syst_updown:
                hists.append("emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s%s"%(part,itype,updown))

    histContainer=HistStorageContainer(bg=bghists)

    bghists.initStyle(style="bg")

    useROOOT=False

    hist_style = sc.style_container(style = 'CMS' ,cmsPositon="upper left", useRoot = useROOOT,cms = 13, lumi = 40)

    bg_outFile=File("syst/bg_for_limit.root", "recreate")

    sigOut={}
    for sig in sghist.files:
        sigOut[sig]=File("syst/%s.root"%(sig), "recreate")

    syst_hists=OrderedDict()
    mainHist=None
    rel_systhist=OrderedDict()
    systcolors=getColorList(len(hists))

    rel_systhist_abs=OrderedDict()

    for hist in hists:

        histContainer.getHist(hist)
        histContainer.setTitle("M_T [GeV]")
        # histContainer.rebin(vector=get_binning_from_hist('res_unc.root','func',[0,4000],min_binning = 5))
        # histContainer.rebin(width=5)

        allbg=bghists.getAllAdded()
        if allbg.integral() <1:
            print "ignored hist: ",hist
            continue

        # print('integral 1: %f'%allbg.integral())
        # allbg = fit_histo(allbg)
        # print('integral 2: %f'%allbg.integral())
        binning = get_binning_from_hist('res_unc.root','func',[0,4000],min_binning = 5)
        rebinnedHist=allbg.rebinned(binning)
        rebinnedHist.xaxis.SetTitle(allbg.xaxis.GetTitle())
        allbg=rebinnedHist
        histContainer.rebin(vector=binning)
        # print('integral 3: %f'%allbg.integral())
        # for ibin in allbg:
            # ibin.value=ibin.value/(ibin.x.width)
            # ibin.error=ibin.error/(ibin.x.width)
        allbg.SetTitle(hist.replace("emu/Stage_0/h1_0_emu_Mass","Main"))
        allbg.decorate(fillstyle = '0',linewidth = 1,linecolor = systcolors.pop())
        # allbg.Draw('hist')
        # raw_input('bla')

        if hist=="emu/Stage_0/h1_0_emu_Mass":
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

        if hist=="emu/Stage_0/h1_0_emu_Mass":
            mainHist=allbg
        else:
            rel_systhist[hist] = (allbg/mainHist)
            rel_systhist[hist].SetTitle(hist.replace("emu/Stage_0/h1_0_emu_Mass",""))
            rel_systhist[hist].GetYaxis().SetTitle("rel uncertainty")
            for ibin in rel_systhist[hist].bins():
                ibin.value=ibin.value-1.
        syst_hists[hist]=allbg

        if hist=="emu/Stage_0/h1_0_emu_Mass":
            bg_outFile.WriteObject(allbg,"Main")
        else:
             bg_outFile.WriteObject(allbg,hist.replace("emu/Stage_0/h1_0_emu_Mass","Main"))
        print hist.replace("emu/Stage_0/h1_0_emu_Mass","Main")

        bgs=histContainer.getBGList()
        for ih in bgs:
            ih.SetTitle(ih.GetTitle().replace("emu/Stage_0/h1_0_emu_Mass"," "))

        allbg.SetLineColor('black')
        allbg.SetLineWidth(1)
        allbg.SetTitle('fit')

        test = plotter(hist=bgs,sig=[allbg],style=hist_style,cmsPositon="upper left",useRoot = useROOOT)

        test.Set_axis(xmin=0,xmax=3000)

        name=hist.replace("/","")


        plot=test.create_plot()
        test.SavePlot('syst/%s.png'%(name))
        test.SavePlot('syst/%s.pdf'%(name))
        del test

    test = plotter(sig=syst_hists.values(),style=hist_style,useRoot = useROOOT)
    test.create_plot()
    test.SavePlot('syst/allsyst.png')
    test.SavePlot('syst/allsyst.pdf')
    del test


    test = plotter(sig=rel_systhist.values(),style=hist_style,useRoot = useROOOT)
    test.Set_axis(logy=False,ymin=-0.5,ymax=1.,xmin=0,xmax=3000)
    test.create_plot()
    test.SavePlot('syst/relsyst.png')
    test.SavePlot('syst/relsyst.pdf')
    del test

    for part in syst_part:
        for itype in syst_type:
            if (part == 'Ele' or part == 'Tau' or part == 'MET') and itype == 'Resolution':
                continue
            rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)] = rel_systhist["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s%s"%(part,itype,'Up')]
            rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)].SetTitle(rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)].GetTitle().replace('Up','').replace('emu/Stage_0/sys/h1_0_emu_Mass_',''))
            rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)].SetColor(special_colors[rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)].GetTitle()])
            rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)].GetXaxis().SetTitle('$M_{e\mu}$ (GeV)')
            for (ibin,jbin,kbin) in zip(rel_systhist_abs["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s"%(part,itype)],rel_systhist["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s%s"%(part,itype,'Up')],rel_systhist["emu/Stage_0/sys/h1_0_emu_Mass_%s_syst_%s%s"%(part,itype,'Down')]):
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

    sum_outFile=File("syst/for_plotting.root", "recreate")
    sys_hist.Write()
    stat_hist.Write()
    sum_outFile.Close()

    test = plotter(sig=rel_systhist_abs.values(),style=hist_style,useRoot = useROOOT)
    test.Set_axis(logy=False,ymin=0.,ymax=0.4,xmin=50,xmax=1200)
    test.create_plot()
    test.SavePlot('syst/relsyst_comb.png')
    test.SavePlot('syst/relsyst_comb.pdf')
    del test


    bg_outFile.Close()
    # for sig in sigOut:
        # sigOut[sig].Close()

    return 42



main()
