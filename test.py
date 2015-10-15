#!/bin/env python

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
from rootpy.io import File

def get_binning_from_hist(file_name, hist_name, plot_range, debug=False, min_binning = 1):
    res_file = File(file_name, "read")
    res_hist = res_file.Get(hist_name)
    binning = [plot_range[0]]
    value = plot_range[0]
    while(binning[-1] < plot_range[1]):
        value = res_hist.Eval(binning[-1])
        value *= binning[-1]
        if value < min_binning:
            if debug:
                print('appending %f, last value: %f'%(min_binning,binning[-1]))
            binning.append(binning[-1]+min_binning)
        else:
            if debug:
                print('appending %f, last value: %f'%(round(value),binning[-1]))
            binning.append(binning[-1]+round(value))
    if binning[-1] > plot_range[1]:
        binning[-1] = plot_range[1]
    res_file.Close()
    if debug:
        print(binning)
    return binning


# output2015_7_29_14_53 -> data
# 
# output2015_7_30_14_0 -> data
# output2015_7_31_10_28 -> data
# 
# output2015_7_31_11_21 -> data
# 
# output2015_8_3_17_34 -> data
# output2015_8_4_17_55 -> MC

# basedir="/disk1/erdweg/out/output2015_7_21_14_52/merged/"
basedir="/disk1/erdweg/out/output2015_8_19_18_16/merged/"
lumi = 40.028
lumisc = float(lumi)/float(1000)

xs= ConfigObj("/disk1/erdweg/plotting/xs_Phys14.cfg")
bghists=HistStorage(xs,lumi,xstype=None,path=basedir)

bglist=OrderedDict()

# bglist["DY"]=[
 # 'DYJetsToLL_M-10to50_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-50_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-100to200_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-200to400_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-400to500_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-500to700_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-700to800_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-800to1000_13TeV-FXFXRaw_MC',
 # 'DYJetsToLL_M-1000to1500_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-1500to2000_13TeV-FXFX_MC',
 # 'DYJetsToLL_M-2000to3000_13TeV-FXFX_MC',
# ]
# bglist["W"]=[
 # 'WJetsToLNu_13TeV-FXFX_MC',
 # 'WJetsToLNu_HT-100To200_13TeVMLM_MG',
 # 'WJetsToLNu_HT-200To400_13TeVMLM_MG',
 # 'WJetsToLNu_HT-400To600_13TeVMLM_MG',
 # 'WJetsToLNu_HT-600ToInf_13TeVMLM_MG',
# ]
# bglist["single Top"]=[
 # 'ST_t-channel_4f_leptonDecays_13TeV-_MC',
 # 'ST_tW_top_5f_inclusiveDecays_13TeV_PH',
 # 'ST_t-channel_5f_leptonDecays_13TeV-_MC',
 # 'ST_s-channel_4f_leptonDecays_13TeV-_MC',
 # 'ST_tW_antitop_5f_inclusiveDecays_13TeV_PH',
# ]
# bglist["QCD jet"]=[
 # 'QCD_Pt-15to20_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-20to30_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-20toInf_MuEnrichedPt15_13TeV_P8',
 # 'QCD_Pt-30to50_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-50to80_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-80to120_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-120to170_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-170to300_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-300to470_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-470to600_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-600to800_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-800to1000_MuEnrichedPt5_13TeV_P8',
 # 'QCD_Pt-1000toInf_MuEnrichedPt5_13TeV_P8',
# ]
# bglist["Diboson"]=[
 # 'WW_13TeV_P8',
 # 'WZ_13TeV_P8',
 # 'ZZ_13TeV_P8'
# ]
bglist["TTbar"]=[
 'TT_13TeV_PH',
 'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH',
]

colorList={}
colorList["W"]="lightblue"
colorList["Diboson"]="y"
colorList["single Top"]="darkmagenta"
colorList["QCD jet"]="darkblue"
colorList["TTbar"]="chartreuse"
colorList["WW"]="green"
colorList["DY"]="pink"
colorList['RPV M=500']="magenta"
colorList['RPV M=1000']="red"

bghists.additionalWeight = {
 'DYJetsToLL_M-10to50_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-50_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-100to200_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-200to400_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-400to500_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-500to700_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-700to800_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-800to1000_13TeV-FXFXRaw_MC':lumisc,
 'DYJetsToLL_M-1000to1500_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-1500to2000_13TeV-FXFX_MC':lumisc,
 'DYJetsToLL_M-2000to3000_13TeV-FXFX_MC':lumisc,
 'WJetsToLNu_13TeV-FXFX_MC':lumisc,
 'WJetsToLNu_HT-100To200_13TeVMLM_MG':lumisc,
 'WJetsToLNu_HT-200To400_13TeVMLM_MG':lumisc,
 'WJetsToLNu_HT-400To600_13TeVMLM_MG':lumisc,
 'WJetsToLNu_HT-600ToInf_13TeVMLM_MG':lumisc,
 'ST_t-channel_4f_leptonDecays_13TeV-_MC':lumisc,
 'ST_tW_top_5f_inclusiveDecays_13TeV_PH':lumisc,
 'ST_t-channel_5f_leptonDecays_13TeV-_MC':lumisc,
 'ST_s-channel_4f_leptonDecays_13TeV-_MC':lumisc,
 'ST_tW_antitop_5f_inclusiveDecays_13TeV_PH':lumisc,
 'QCD_Pt-15to20_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-20to30_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-20toInf_MuEnrichedPt15_13TeV_P8':lumisc,
 'QCD_Pt-30to50_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-50to80_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-80to120_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-120to170_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-170to300_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-300to470_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-470to600_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-600to800_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-800to1000_MuEnrichedPt5_13TeV_P8':lumisc,
 'QCD_Pt-1000toInf_MuEnrichedPt5_13TeV_P8':lumisc,
 'WW_13TeV_P8':lumisc,
 'WZ_13TeV_P8':lumisc,
 'ZZ_13TeV_P8':lumisc,
 'TT_13TeV_PH':lumisc,
 'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH':lumisc,
}

bghists.addFileList(bglist)
# 
# dat_hist=HistStorage(xs,lumi,path='/disk1/erdweg/out/output2015_8_20_17_27/merged/',isData=True)
# dat_hist.addFile("Data_251027_251883_SingleMuon_v2")
# 
# basedir="/disk1/erdweg/out/output2015_6_2_17_17/merged/"
# sghist=HistStorage(xs,lumi,path=basedir)
# sglist=OrderedDict()
# 
# sglist['RPV M=500']=[
 # 'RPVresonantToEMu_M-500_LLE_LQD_001_TuneCUETP8M1_13TeV-calchep-pythia8',
# ]
# sglist['RPV M=1000']=[
 # 'RPVresonantToEMu_M-1000_LLE_LQD_001_TuneCUETP8M1_13TeV-calchep-pythia8',
# ]
# sghist.additionalWeight = {'RPVresonantToEMu_M-500_LLE_LQD_001_TuneCUETP8M1_13TeV-calchep-pythia8':lumisc}
# sghist.additionalWeight.update({'RPVresonantToEMu_M-1000_LLE_LQD_001_TuneCUETP8M1_13TeV-calchep-pythia8':lumisc})
# sghist.addFileList(sglist)
histContainer=HistStorageContainer(bg=bghists)

bghists.initStyle(style="bg",colors=colorList)
# sghist.initStyle(style="sg",colors=colorList)


def main():

    hists=[
    'emu/Stage_0/h1_0_emu_Mass',
    ]

    binning={
            "Taus/h1_2_Tau_pt":10,
    }

    binning.update({"emu/Stage_0/h1_0_emu_Mass":get_binning_from_hist('res_unc.root','func',[0,4000],min_binning = 5)})

    xranges={
            "emu/Stage_0/h1_0_emu_Mass":[50,3000],
    }

    for hist in hists:
        print("Now plotting: " + hist)
        histContainer.getHist(hist)

        binf=getDictValue(hist,binning)
        if binf is not None:
            # dat_hist.rebin(width=1,vector=binf)
            bghists.rebin(width=1,vector=binf)
            # sghist.rebin(width=1,vector=binf)

        hist_style = sc.style_container(style = 'CMS', useRoot = False,cms=13,lumi=lumi, cmsPositon = 'upper left')

        dummy = bghists.getAllAdded()
        dummy.xaxis.SetTitle('')
        dummy.yaxis.SetTitle('')
        dummy.SaveAs('plots/' + hist.replace("/","") + '.root')

        test = plotter(hist=bghists.getHistList(),style=hist_style)
        # test.Add_data(dat_hist.getHistList()[0])

        hist_style.Set_error_bands_fcol(['gray','orange'])
        hist_style.Set_error_bands_ecol(['black','black'])
        hist_style.Set_error_bands_labl(['Systematics','Statistic'])

        if hist == 'emu/Stage_0/h1_0_emu_Mass':
            sys_file=File('syst/for_plotting.root', "read")
        
            test.Add_error_hist([sys_file.Get('Sys'),sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')
            # test.Add_error_hist([sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')

        # test.Add_plot('Diff',pos=0, height=12)
# 
        # test.Add_plot('DiffRatio',pos=1, height=12)
        # test.Add_plot('Signi',pos=2, height=12)

        if hist in xranges.keys():
            test.Set_axis(logx=True,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-6,ymax=1e3)

        name=hist.replace("/","")

        test.create_plot()

        # test.Get_axis0().set_ylim(ymin = -1.2, ymax = 1.7)
        # test.Get_axis2().set_ylim(ymin = -3, ymax = 13)
        # test.Get_axis3().set_ylim(ymin = -2, ymax = 2.0)

        test.SavePlot('plots/test.pdf')
    return 42



main()
