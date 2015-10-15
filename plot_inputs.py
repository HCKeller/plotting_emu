#!/bin/env python
# -*- coding: utf-8 -*-

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

# 
basedir="/net/scratch_cms/institut_3a/erdweg/public/13TeV_rpv/BACKGROUND/merged"
lumi = 40.8 + 16.3 + 25.028
# lumi = 10
lumisc = float(lumi)/float(1000)

xs= ConfigObj("/home/home1/institut_3a/keller/TAPAS/plotting/xs_Phys14.cfg")
bghists=HistStorage(xs,lumi,xstype=None,path=basedir)

bglist=OrderedDict()

bglist["DY"]=[
 'ZToEE_NNPDF30_13TeV_M_50_120_PH-skimid1741',
 'ZToEE_NNPDF30_13TeV_M_120_200_PH-skimid1736',
 'ZToEE_NNPDF30_13TeV_M_200_400_PH-skimid1896',
 'ZToEE_NNPDF30_13TeV_M_400_800_PH-skimid1730',
 'ZToEE_NNPDF30_13TeV_M_800_1400_PH-skimid1740',
 'ZToEE_NNPDF30_13TeV_M_1400_2300_PH-skimid1794',
 'ZToEE_NNPDF30_13TeV_M_3500_4500_PH-skimid1770',
 'ZToEE_NNPDF30_13TeV_M_6000_Inf_PH-skimid1726',
 'ZToMuMu_NNPDF30_13TeV_M_50_120_PH-skimid1752',
 'ZToMuMu_NNPDF30_13TeV_M_200_400_PH-skimid1727',
 'ZToMuMu_NNPDF30_13TeV_M_400_800_PH-skimid1728',
 'ZToMuMu_NNPDF30_13TeV_M_800_1400_PH-skimid1837',
 'ZToMuMu_NNPDF30_13TeV_M_3500_4500_PH-skimid1737',
 'ZToMuMu_NNPDF30_13TeV_M_4500_6000_PH-skimid1902',
 'ZToMuMu_NNPDF30_13TeV_M_6000_Inf_PH-skimid1772',
]
bglist["W"]=[
 'WJetsToLNu_HT-100To200_13TeVMLM_MG-skimid2018',
 'WJetsToLNu_HT-400To600_13TeVMLM_MG-skimid2017',
 'WJetsToLNu_HT-600To800_13TeVMLM_MG-skimid2019',
 'WJetsToLNu_HT-800To1200_13TeVMLM_MG-skimid2005',
 'WJetsToLNu_HT-2500ToInf_13TeVMLM_MG-skimid1863',
]
bglist["single Top"]=[
 'ST_tW_antitop_5f_inclusiveDecays_13TeV_PH-skimid1885',
 'ST_tW_top_5f_inclusiveDecays_13TeV_PH-skimid1738',
 'ST_t-channel_antitop_4f_leptonDecays_13TeV_PH-skimid1739',
 'ST_t-channel_top_4f_leptonDecays_13TeV_PH-skimid1972',
]
bglist["TTbar"]=[
 'TT_13TeV_MCRUN2_74_V9_ext3-v1_PH-skimid1978',
 'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH-skimid1749',
 #'TTTo2L2Nu_13TeV_PH-skimid1750',
]
bglist["Diboson"]=[
 'WWTo2L2Nu_13TeV_PH-skimid1905',
 'WWTo4Q_13TeV_PH-skimid1821',
 'WWToLNuQQ_13TeV_PH-skimid1818',
 'WZTo3LNu_13TeV_PH-skimid1903',
 'ZZTo2L2Nu_13TeV_PH-skimid1970',
 'ZZTo4L_13TeV_PH-skimid1898',
]
bglist["QCD jet"]=[
 'QCD_Pt-20to30_MuEnrichedPt5_13TeV_P8-skimid1868',
 'QCD_Pt-80to120_MuEnrichedPt5_13TeV_P8-skimid1805',
 'QCD_Pt-120to170_MuEnrichedPt5_13TeV_P8-skimid1882',
 'QCD_Pt-1000toInf_MuEnrichedPt5_13TeV_P8-skimid1930',
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
 'ZToEE_NNPDF30_13TeV_M_50_120_PH-skimid1741':lumisc,
 'ZToEE_NNPDF30_13TeV_M_120_200_PH-skimid1736':lumisc,
 'ZToEE_NNPDF30_13TeV_M_200_400_PH-skimid1896':lumisc,
 'ZToEE_NNPDF30_13TeV_M_400_800_PH-skimid1730':lumisc,
 'ZToEE_NNPDF30_13TeV_M_800_1400_PH-skimid1740':lumisc,
 'ZToEE_NNPDF30_13TeV_M_1400_2300_PH-skimid1794':lumisc,
 'ZToEE_NNPDF30_13TeV_M_3500_4500_PH-skimid1770':lumisc,
 'ZToEE_NNPDF30_13TeV_M_6000_Inf_PH-skimid1726':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_50_120_PH-skimid1752':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_200_400_PH-skimid1727':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_400_800_PH-skimid1728':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_800_1400_PH-skimid1837':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_3500_4500_PH-skimid1737':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_4500_6000_PH-skimid1902':lumisc,
 'ZToMuMu_NNPDF30_13TeV_M_6000_Inf_PH-skimid1772':lumisc,
 'WJetsToLNu_HT-100To200_13TeVMLM_MG-skimid2018':lumisc,
 'WJetsToLNu_HT-400To600_13TeVMLM_MG-skimid2017':lumisc,
 'WJetsToLNu_HT-600To800_13TeVMLM_MG-skimid2019':lumisc,
 'WJetsToLNu_HT-800To1200_13TeVMLM_MG-skimid2005':lumisc,
 'WJetsToLNu_HT-2500ToInf_13TeVMLM_MG-skimid1863':lumisc,
 'ST_tW_antitop_5f_inclusiveDecays_13TeV_PH-skimid1885':lumisc,
 'ST_tW_top_5f_inclusiveDecays_13TeV_PH-skimid1738':lumisc,
 'ST_t-channel_antitop_4f_leptonDecays_13TeV_PH-skimid1739':lumisc,
 'ST_t-channel_top_4f_leptonDecays_13TeV_PH-skimid1972':lumisc,
 'QCD_Pt-20to30_MuEnrichedPt5_13TeV_P8-skimid1868':lumisc,
 'QCD_Pt-80to120_MuEnrichedPt5_13TeV_P8-skimid1805':lumisc,
 'QCD_Pt-120to170_MuEnrichedPt5_13TeV_P8-skimid1882':lumisc,
 'QCD_Pt-1000toInf_MuEnrichedPt5_13TeV_P8-skimid1930':lumisc,
 'WWTo2L2Nu_13TeV_PH-skimid1905':lumisc,
 'WWTo4Q_13TeV_PH-skimid1821':lumisc,
 'WWToLNuQQ_13TeV_PH-skimid1818':lumisc,
 'WZTo3LNu_13TeV_PH-skimid1903':lumisc,
 'ZZTo2L2Nu_13TeV_PH-skimid1970':lumisc,
 'ZZTo4L_13TeV_PH-skimid1898':lumisc,
 'TT_13TeV_MCRUN2_74_V9_ext3-v1_PH-skimid1978':lumisc,
 'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH-skimid1749':lumisc,
 'TTTo2L2Nu_13TeV_PH-skimid1750':lumisc,
}

bghists.addFileList(bglist)

dat_hist=HistStorage(xs,lumi,path="/net/scratch_cms/institut_3a/erdweg/public/13TeV_rpv/DATA/merged/",isData=True)
dat_hist.addFile("allData")
# dat_hist.addFile("Data_Run2015B-PromptReco_251162_252126_SingleMuon-skimid81")
# dat_hist.addFile("Data_Run2015C-PromptReco_253888_254914_SingleMuon-skimid48")

basedir="/net/scratch_cms/institut_3a/erdweg/public/13TeV_rpv/SIGNAL/merged/"
sghist=HistStorage(xs,lumi,path=basedir,xstype=None)
sglist=OrderedDict()

sglist['RPV M=500']=[
 'RPVresonantToEMu_M-500_LLE_LQD-001_13TeV_CA-skimid1827',
]
sglist['RPV M=1000']=[
 'RPVresonantToEMu_M-1000_LLE_LQD-001_13TeV_CA-skimid1891',
]
sghist.additionalWeight = {'RPVresonantToEMu_M-500_LLE_LQD-001_13TeV_CA-skimid1827':lumisc}
sghist.additionalWeight.update({'RPVresonantToEMu_M-1000_LLE_LQD-001_13TeV_CA-skimid1891':lumisc})
sghist.addFileList(sglist)
histContainer=HistStorageContainer(bg=bghists,data=dat_hist,sg=sghist)

bghists.initStyle(style="bg",colors=colorList)
sghist.initStyle(style="sg",colors=colorList)
