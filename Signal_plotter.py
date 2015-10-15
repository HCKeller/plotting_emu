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

    basedir="/disk1/erdweg/television/SIGNAL/merged/"
    # lumi=19712

    # xs= ConfigObj("/disk1/erdweg/plotting/xs_Phys14.cfg")
    # bghists=HistStorage(xs,lumi,path=basedir,isData=True)

    colors = ['lime', 'deepskyblue', 'magenta', 'orangered']

    bglist=OrderedDict()

    bglist = [
     'RPVresonantToEMu_M-200_LLE_LQD-001_13TeV_CA-skimid1965',
     'RPVresonantToEMu_M-300_LLE_LQD-001_13TeV_CA-skimid1829',
     'RPVresonantToEMu_M-400_LLE_LQD-001_13TeV_CA-skimid1954',
     'RPVresonantToEMu_M-500_LLE_LQD-001_13TeV_CA-skimid1827',
     'RPVresonantToEMu_M-600_LLE_LQD-001_13TeV_CA-skimid1888',
     'RPVresonantToEMu_M-700_LLE_LQD-001_13TeV_CA-skimid1884',
     'RPVresonantToEMu_M-800_LLE_LQD-001_13TeV_CA-skimid1935',
     'RPVresonantToEMu_M-900_LLE_LQD-001_13TeV_CA-skimid1966',
     'RPVresonantToEMu_M-1000_LLE_LQD-001_13TeV_CA-skimid1891',
     'RPVresonantToEMu_M-1200_LLE_LQD-001_13TeV_CA-skimid1892',
     'RPVresonantToEMu_M-1400_LLE_LQD-001_13TeV_CA-skimid1857',
     'RPVresonantToEMu_M-1600_LLE_LQD-001_13TeV_CA-skimid1859',
     'RPVresonantToEMu_M-1800_LLE_LQD-001_13TeV_CA-skimid1834',
     'RPVresonantToEMu_M-2000_LLE_LQD-001_13TeV_CA-skimid1831',
     'RPVresonantToEMu_M-2500_LLE_LQD-001_13TeV_CA-skimid1974',
     'RPVresonantToEMu_M-3000_LLE_LQD-01_13TeV_CA-skimid1835',
     'RPVresonantToEMu_M-3000_LLE_LQD-001_13TeV_CA-skimid1960',
     'RPVresonantToEMu_M-3500_LLE_LQD-001_13TeV_CA-skimid1889',
     'RPVresonantToEMu_M-3500_LLE_LQD-01_13TeV_CA-skimid2064',
     'RPVresonantToEMu_M-4000_LLE_LQD-001_13TeV_CA-skimid1833',
     'RPVresonantToEMu_M-4000_LLE_LQD-01_13TeV_CA-skimid1984',
     'RPVresonantToEMu_M-4000_LLE_LQD-02_13TeV_CA-skimid1929',
     'RPVresonantToEMu_M-4000_LLE_LQD-05_13TeV_CA-skimid1976',
     'RPVresonantToEMu_M-4500_LLE_LQD-001_13TeV_CA-skimid1832',
     'RPVresonantToEMu_M-4500_LLE_LQD-02_13TeV_CA-skimid1964',
     'RPVresonantToEMu_M-4500_LLE_LQD-05_13TeV_CA-skimid1977',
     'RPVresonantToEMu_M-5000_LLE_LQD-001_13TeV_CA-skimid1983',
     'RPVresonantToEMu_M-5000_LLE_LQD-02_13TeV_CA-skimid1975',
     'RPVresonantToEMu_M-5000_LLE_LQD-05_13TeV_CA-skimid1828',
     'RPVresonantToEMu_M-5500_LLE_LQD-001_13TeV_CA-skimid1869',
     'RPVresonantToEMu_M-5500_LLE_LQD-02_13TeV_CA-skimid1858',
     'RPVresonantToEMu_M-5500_LLE_LQD-05_13TeV_CA-skimid1830',
     'RPVresonantToEMu_M-6000_LLE_LQD-001_13TeV_CA-skimid1887',
     'RPVresonantToEMu_M-6000_LLE_LQD-02_13TeV_CA-skimid1927',
     'RPVresonantToEMu_M-6000_LLE_LQD-05_13TeV_CA-skimid1890',
     'RPVresonantToEMu_M-6500_LLE_LQD-001_13TeV_CA-skimid1967',
     'RPVresonantToEMu_M-6500_LLE_LQD-02_13TeV_CA-skimid1873',
     'RPVresonantToEMu_M-6500_LLE_LQD-05_13TeV_CA-skimid1886',
    ]

    colorList={}
    colorList['RPVresonantToEMu_M-200_LLE_LQD-001_13TeV_CA-skimid1965'] = 'lightblue'
    colorList['RPVresonantToEMu_M-300_LLE_LQD-001_13TeV_CA-skimid1829'] = 'lightblue'
    colorList['RPVresonantToEMu_M-400_LLE_LQD-001_13TeV_CA-skimid1954'] = 'lightblue'
    colorList['RPVresonantToEMu_M-500_LLE_LQD-001_13TeV_CA-skimid1827'] = 'lightblue'
    colorList['RPVresonantToEMu_M-600_LLE_LQD-001_13TeV_CA-skimid1888'] = 'lightblue'
    colorList['RPVresonantToEMu_M-700_LLE_LQD-001_13TeV_CA-skimid1884'] = 'lightblue'
    colorList['RPVresonantToEMu_M-800_LLE_LQD-001_13TeV_CA-skimid1935'] = 'lightblue'
    colorList['RPVresonantToEMu_M-900_LLE_LQD-001_13TeV_CA-skimid1966'] = 'lightblue'
    colorList['RPVresonantToEMu_M-1000_LLE_LQD-001_13TeV_CA-skimid1891'] = 'lightblue'
    colorList['RPVresonantToEMu_M-1200_LLE_LQD-001_13TeV_CA-skimid1892'] = 'lightblue'
    colorList['RPVresonantToEMu_M-1400_LLE_LQD-001_13TeV_CA-skimid1857'] = 'lightblue'
    colorList['RPVresonantToEMu_M-1600_LLE_LQD-001_13TeV_CA-skimid1859'] = 'lightblue'
    colorList['RPVresonantToEMu_M-1800_LLE_LQD-001_13TeV_CA-skimid1834'] = 'lightblue'
    colorList['RPVresonantToEMu_M-2000_LLE_LQD-001_13TeV_CA-skimid1831'] = 'lightblue'
    colorList['RPVresonantToEMu_M-2500_LLE_LQD-001_13TeV_CA-skimid1974'] = 'lightblue'
    colorList['RPVresonantToEMu_M-3000_LLE_LQD-01_13TeV_CA-skimid1835'] = 'lightblue'
    colorList['RPVresonantToEMu_M-3000_LLE_LQD-001_13TeV_CA-skimid1960'] = 'lightblue'
    colorList['RPVresonantToEMu_M-3500_LLE_LQD-001_13TeV_CA-skimid1889'] = 'lightblue'
    colorList['RPVresonantToEMu_M-3500_LLE_LQD-01_13TeV_CA-skimid2064'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4000_LLE_LQD-001_13TeV_CA-skimid1833'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4000_LLE_LQD-01_13TeV_CA-skimid1984'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4000_LLE_LQD-02_13TeV_CA-skimid1929'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4000_LLE_LQD-05_13TeV_CA-skimid1976'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4500_LLE_LQD-001_13TeV_CA-skimid1832'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4500_LLE_LQD-02_13TeV_CA-skimid1964'] = 'lightblue'
    colorList['RPVresonantToEMu_M-4500_LLE_LQD-05_13TeV_CA-skimid1977'] = 'lightblue'
    colorList['RPVresonantToEMu_M-5000_LLE_LQD-001_13TeV_CA-skimid1983'] = 'lightblue'
    colorList['RPVresonantToEMu_M-5000_LLE_LQD-02_13TeV_CA-skimid1975'] = 'lightblue'
    colorList['RPVresonantToEMu_M-5000_LLE_LQD-05_13TeV_CA-skimid1828'] = 'lightblue'
    colorList['RPVresonantToEMu_M-5500_LLE_LQD-001_13TeV_CA-skimid1869'] = 'lightblue'
    colorList['RPVresonantToEMu_M-5500_LLE_LQD-02_13TeV_CA-skimid1858'] = 'lightblue'
    colorList['RPVresonantToEMu_M-5500_LLE_LQD-05_13TeV_CA-skimid1830'] = 'lightblue'
    colorList['RPVresonantToEMu_M-6000_LLE_LQD-001_13TeV_CA-skimid1887'] = 'lightblue'
    colorList['RPVresonantToEMu_M-6000_LLE_LQD-02_13TeV_CA-skimid1927'] = 'lightblue'
    colorList['RPVresonantToEMu_M-6000_LLE_LQD-05_13TeV_CA-skimid1890'] = 'lightblue'
    colorList['RPVresonantToEMu_M-6500_LLE_LQD-001_13TeV_CA-skimid1967'] = 'lightblue'
    colorList['RPVresonantToEMu_M-6500_LLE_LQD-02_13TeV_CA-skimid1873'] = 'lightblue'
    colorList['RPVresonantToEMu_M-6500_LLE_LQD-05_13TeV_CA-skimid1886'] = 'lightblue'

    hists=['HLT_Effs/eff_HLT_HLT_Mu50_v1_vs_Nvtx',
     'HLT_Effs/eff_HLT_HLT_Mu50_v1_vs_pT(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_pT(Ele)',
     #'HLT_Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_Nvtx',
     #'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_Nvtx',

     'RECO_Effs/eff_Ele_RECO_vs_Nvtx',
     'RECO_Effs/eff_Ele_RECO_vs_pT',
     # 'RECO_Effs/eff_MET_RECO_vs_Nvtx',
     # 'RECO_Effs/eff_MET_RECO_vs_pT',
     'RECO_Effs/eff_Muon_RECO_vs_Nvtx',
     'RECO_Effs/eff_Muon_RECO_vs_pT',
     # 'RECO_Effs/eff_Tau_RECO_vs_Nvtx',
     # 'RECO_Effs/eff_Tau_RECO_vs_pT',

     'RECO_Effs/eff_Ele_RECO_vs_Nvtx_in_Acc',
     'RECO_Effs/eff_Ele_RECO_vs_pT_in_Acc',
     'RECO_Effs/eff_Muon_RECO_vs_Nvtx_in_Acc',
     'RECO_Effs/eff_Muon_RECO_vs_pT_in_Acc',
     # 'RECO_Effs/eff_Tau_RECO_vs_Nvtx_in_Acc',
     # 'RECO_Effs/eff_Tau_RECO_vs_pT_in_Acc',

     'ID_Effs/eff_Ele_ID_vs_Nvtx',
     'ID_Effs/eff_Ele_ID_vs_Nvtx_in_Acc',
     'ID_Effs/eff_Ele_ID_vs_pT',
     'ID_Effs/eff_Ele_ID_vs_pT_gen',
     'ID_Effs/eff_Ele_ID_vs_pT_in_Acc',
     'ID_Effs/eff_Ele_ID_vs_pT_in_Acc_gen',

     'ID_Effs/eff_Muon_ID_vs_Nvtx',
     'ID_Effs/eff_Muon_ID_vs_Nvtx_in_Acc',
     'ID_Effs/eff_Muon_ID_vs_pT',
     'ID_Effs/eff_Muon_ID_vs_pT_gen',
     'ID_Effs/eff_Muon_ID_vs_pT_in_Acc',
     'ID_Effs/eff_Muon_ID_vs_pT_in_Acc_gen',

     # 'ID_Effs/eff_Tau_ID_vs_Nvtx',
     # 'ID_Effs/eff_Tau_ID_vs_Nvtx_in_Acc',
     # 'ID_Effs/eff_Tau_ID_vs_pT',
     # 'ID_Effs/eff_Tau_ID_vs_pT_gen',
     # 'ID_Effs/eff_Tau_ID_vs_pT_in_Acc',
     # 'ID_Effs/eff_Tau_ID_vs_pT_in_Acc_gen',
    ]

    overall_hists = [
     ['emu/eff_emu_Acc_vs_Mass','emu/eff_emu_RECO_vs_Mass','emu/eff_emu_Eff_vs_Mass'],
     ['emu/eff_emu_Acc_vs_Nvtx','emu/eff_emu_RECO_vs_Nvtx','emu/eff_emu_Eff_vs_Nvtx'],
    ]

    eff_colorList={}
    eff_colorList['emu/eff_emu_Acc_vs_Mass'] = 'deepskyblue'
    eff_colorList['emu/eff_emu_RECO_vs_Mass'] = 'darkgreen'
    eff_colorList['emu/eff_emu_Eff_vs_Mass'] = 'red'
    eff_colorList['emu/eff_emu_Acc_vs_Nvtx'] = 'deepskyblue'
    eff_colorList['emu/eff_emu_RECO_vs_Nvtx'] = 'darkgreen'
    eff_colorList['emu/eff_emu_Eff_vs_Nvtx'] = 'red'

    hists2D=['HLT_Effs/eff_HLT_HLT_Mu50_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu30_TkMu11_v1_vs_pT(Mu,Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_eta_vs_phi(Ele)',
     #'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1_vs_pT(Mu,Ele)',
     #'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_vs_pT(Mu,Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_vs_pT(Mu,Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_Mu17_Mu8_v1_vs_pT(Mu,Mu)',
     #'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_eta_vs_phi(Mu)',
     #'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_eta_vs_phi(Tau)',
     #'HLT_Effs/eff_HLT_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1_vs_pT(Mu,Tau)',
     #'HLT_Effs/eff_HLT_HLT_Ele95_CaloIdVT_GsfTrkIdT_v1_vs_eta_vs_phi(Ele)',
     #'HLT_Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_eta_vs_phi(Ele)',
     #'HLT_Effs/eff_HLT_HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1_vs_pT(Ele,Ele)',
     #'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_eta_vs_phi(Ele)',
     #'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_eta_vs_phi(Tau)',
     #'HLT_Effs/eff_HLT_HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1_vs_pT(Ele,Tau)',

     'RECO_Effs/eff_Ele_RECO_vs_eta_vs_phi',
     # 'RECO_Effs/eff_MET_RECO_vs_eta_vs_phi',
     'RECO_Effs/eff_Muon_RECO_vs_eta_vs_phi',
     # 'RECO_Effs/eff_Tau_RECO_vs_eta_vs_phi',

     'RECO_Effs/eff_Ele_RECO_vs_eta_vs_phi_in_Acc',
     'RECO_Effs/eff_Muon_RECO_vs_eta_vs_phi_in_Acc',
     # 'RECO_Effs/eff_Tau_RECO_vs_eta_vs_phi_in_Acc',

     'ID_Effs/eff_Ele_ID_vs_eta_vs_phi',
     'ID_Effs/eff_Ele_ID_vs_eta_vs_phi_gen',
     'ID_Effs/eff_Ele_ID_vs_eta_vs_phi_in_Acc',
     'ID_Effs/eff_Ele_ID_vs_eta_vs_phi_in_Acc_gen',

     'ID_Effs/eff_Muon_ID_vs_eta_vs_phi',
     'ID_Effs/eff_Muon_ID_vs_eta_vs_phi_gen',
     'ID_Effs/eff_Muon_ID_vs_eta_vs_phi_in_Acc',
     'ID_Effs/eff_Muon_ID_vs_eta_vs_phi_in_Acc_gen',

     # 'ID_Effs/eff_Tau_ID_vs_eta_vs_phi',
     # 'ID_Effs/eff_Tau_ID_vs_eta_vs_phi_gen',
     # 'ID_Effs/eff_Tau_ID_vs_eta_vs_phi_in_Acc',
     # 'ID_Effs/eff_Tau_ID_vs_eta_vs_phi_in_Acc_gen',
    ]

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
     'HLT_Effs/eff_HLT_HLT_Mu50_v1_vs_Nvtx':['HLT_Mu50_v1 efficiency','$N_{vtx}$','efficiency $\epsilon$'],
     'HLT_Effs/eff_HLT_HLT_Mu50_v1_vs_pT(Mu)':['HLT_Mu50_v1 efficiency','$p_{T}^{\mu}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'RECO_Effs/eff_Ele_RECO_vs_Nvtx':['Electron reco efficiency','$N_{vtx}$','efficiency $\epsilon$'],
     'RECO_Effs/eff_Ele_RECO_vs_pT':['Electron reco efficiency','$p_{T}^{e (gen)}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'RECO_Effs/eff_Muon_RECO_vs_Nvtx':['Muon reco efficiency','$N_{vtx}$','efficiency $\epsilon$'],
     'RECO_Effs/eff_Muon_RECO_vs_pT':['Muon reco efficiency','$p_{T}^{\mu (gen)}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'ID_Effs/eff_Ele_ID_vs_Nvtx':['HEEP ID efficiency','$N_{vtx}$','efficiency $\epsilon$'],
     'ID_Effs/eff_Ele_ID_vs_pT':['HEEP ID efficiency','$p_{T}^{e}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'ID_Effs/eff_Ele_ID_vs_pT_gen':['HEEP ID efficiency','$p_{T}^{e (gen)}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'ID_Effs/eff_Muon_ID_vs_Nvtx':['High p_T muon ID efficiency','$N_{vtx}$','efficiency $\epsilon$'],
     'ID_Effs/eff_Muon_ID_vs_pT_gen':['High p_T muon ID efficiency','$p_{T}^{\mu (gen)}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'ID_Effs/eff_Muon_ID_vs_pT':['High p_T muon ID efficiency','$p_{T}^{\mu}\,(\mathrm{GeV})$','efficiency $\epsilon$'],
     'emu/eff_emu_Acc_vs_Mass':['Acceptance','$M_{e\mu, gen}\,\,\mathrm{(GeV)}$','efficiency $\epsilon$'],
     'emu/eff_emu_RECO_vs_Mass':['Trigger','$M_{e\mu, gen}\,\,\mathrm{(GeV)}$','efficiency $\epsilon$'],
     'emu/eff_emu_Eff_vs_Mass':['Selection','$M_{e\mu, gen}\,\,\mathrm{(GeV)}$','efficiency $\epsilon$'],
     'emu/eff_emu_Acc_vs_Nvtx':['Acceptance','$N_{vtx}$','efficiency $\epsilon$'],
     'emu/eff_emu_RECO_vs_Nvtx':['Trigger','$N_{vtx}$','efficiency $\epsilon$'],
     'emu/eff_emu_Eff_vs_Nvtx':['Selection','$N_{vtx}$','efficiency $\epsilon$'],
     'emu/Stage_0/h1_0_emu_Mass_resolution':['Mass resolution','$M_{e\mu, gen}\,\,\mathrm{(GeV)}$','$\sigma((M_{e\mu, reco} - M_{e\mu, gen}) / M_{e\mu, gen})$'],
    }

    yranges={
     'ID_Effs/eff_Muon_ID_vs_pT':[0.5,1.02],
     'ID_Effs/eff_Muon_ID_vs_pT_gen':[0.5,1.02],
     'ID_Effs/eff_Muon_ID_vs_pT_in_Acc':[0.5,1.02],
     'ID_Effs/eff_Muon_ID_vs_pT_in_Acc_gen':[0.5,1.02],
     'HLT_Effs/eff_HLT_HLT_Mu50_v1_vs_pT(Mu)':[0.6,1.02],
     'ID_Effs/eff_Ele_ID_vs_pT':[0.7,1.02],
     'ID_Effs/eff_Ele_ID_vs_pT_gen':[0.7,1.02],
     'ID_Effs/eff_Ele_ID_vs_pT_in_Acc':[0.7,1.02],
     'ID_Effs/eff_Ele_ID_vs_pT_in_Acc_gen':[0.7,1.02],
    }

    ####################################################################
    # Individual 1D plots
    ####################################################################

    if False:
        for hist in hists:
            print("Now plotting: " + hist)
    
            histlist = []
            for item in bglist:
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist)
                binf = getDictValue(hist, binning)
                if binf is not None:
                    t_eff = eff_rebinner(t_eff,binf)

                i_titles = getDictValue(hist, titles)

                t_eff = Graph(t_eff.CreateGraph())
                t_eff.SetLineColor(colorList[item])
                if i_titles is not None:
                    t_eff.SetTitle(i_titles[0])
                else:
                    t_eff.SetTitle(item)
                if 'Nvtx' in hist:
                    t_eff.xaxis.SetTitle('$N_{vtx}$')
                if 'pT' in hist:
                    if i_titles is not None:
                        t_eff.xaxis.SetTitle(i_titles[1])
                    else:
                        t_eff.xaxis.SetTitle('$p_{T}$ (GeV)')
                if i_titles is not None:
                    t_eff.yaxis.SetTitle(i_titles[2])
                else:
                    t_eff.yaxis.SetTitle('$\epsilon$')
                
                histlist.append(t_eff)
    
            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower middle', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')
            hist_style.Set_legend_font_size(12)

            test = plotter(hist = histlist,style=hist_style)

            if hist in yranges.keys():
                test.Set_axis(logy = False, grid = True, ymin=yranges[hist][0],ymax=yranges[hist][1])
            else:
                test.Set_axis(logy = False, grid = True)
    
            test._cms_text_x         = 0.12
            test._cms_text_y         = 0.91
    
            name=hist.replace("/","")
    
            test.make_plot('plots/%s.pdf'%(name))

    ####################################################################
    # Combined 1D plots
    ####################################################################

    if False:
        skip_list = []
        for hist in hists:
            if hist in skip_list:
                continue
            print("Now plotting: " + hist)
    
            histlist = []
            c_histo = r.TEfficiency()
            for item in bglist:
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist)
                if len(histlist) == 0:
                    c_histo = t_eff
                else:
                    c_histo.Add(t_eff)
                histlist.append(t_eff)

            binf = getDictValue(hist, binning)
            if binf is not None:
                c_histo = eff_rebinner(c_histo,binf)

            i_titles = getDictValue(hist, titles)

            c_histo = Graph(c_histo.CreateGraph())

            c_histo.SetLineColor('deepskyblue')

            if i_titles is not None:
                # c_histo.SetTitle(i_titles[0] + ' in Acceptance')
                c_histo.SetTitle(i_titles[0] + ' ')
            else:
                c_histo.SetTitle(hist)
            if 'Nvtx' in hist:
                c_histo.xaxis.SetTitle('$N_{vtx}$')
            if 'pT' in hist:
                if i_titles is not None:
                    c_histo.xaxis.SetTitle(i_titles[1])
                else:
                    c_histo.xaxis.SetTitle('$p_{T}$ (GeV)')
            if i_titles is not None:
                c_histo.yaxis.SetTitle(i_titles[2])
            else:
                c_histo.yaxis.SetTitle('$\epsilon$')

            plots = [c_histo]

            if hist + '_in_Acc' in hists:
                skip_list.append(hist + '_in_Acc')
                histlist1 = []
                c_histo1 = r.TEfficiency()
                for item in bglist:
                    tfile = root_open(basedir + item + ".root", "READ")
                    t_eff = tfile.Get(hist + '_in_Acc')
                    if len(histlist1) == 0:
                        c_histo1 = t_eff
                    else:
                        c_histo1.Add(t_eff)
                    histlist1.append(t_eff)

                binf = getDictValue(hist, binning)
                if binf is not None:
                    c_histo1 = eff_rebinner(c_histo1,binf)

                c_histo1 = Graph(c_histo1.CreateGraph())
    
                c_histo1.SetLineColor('darkgreen')
                if i_titles is not None:
                    c_histo1.SetTitle(i_titles[0] + ' in Acceptance')
                else:
                    c_histo1.SetTitle(hist + '_in_Acc')
                plots.append(c_histo1)

            if hist[:-4] + '_in_Acc_gen' in hists and '_gen' in hist:
                skip_list.append(hist[:-4] + '_in_Acc_gen')
                histlist2 = []
                c_histo2 = r.TEfficiency()
                for item in bglist:
                    tfile = root_open(basedir + item + ".root", "READ")
                    t_eff = tfile.Get(hist[:-4] + '_in_Acc_gen')
                    if len(histlist2) == 0:
                        c_histo2 = t_eff
                    else:
                        c_histo2.Add(t_eff)
                    histlist2.append(t_eff)

                binf = getDictValue(hist, binning)
                if binf is not None:
                    c_histo2 = eff_rebinner(c_histo2,binf)

                c_histo2 = Graph(c_histo2.CreateGraph())
    
                c_histo2.SetLineColor('darkgreen')
                if i_titles is not None:
                    c_histo2.SetTitle(i_titles[0] + ' in Acceptance')
                else:
                    c_histo2.SetTitle(hist[:-4] + '_in_Acc_gen')

                plots.append(c_histo2)

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower middle', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')
            hist_style.Set_legend_font_size(12)

            test = plotter(hist = plots, style = hist_style)

            if hist in yranges.keys():
                test.Set_axis(logy = False, grid = True, ymin=yranges[hist][0],ymax=yranges[hist][1])
            else:
                test.Set_axis(logy = False, grid = True)
    
            test._cms_text_x         = 0.12
            test._cms_text_y         = 0.91
    
            name=hist.replace("/","")
    
            test.make_plot('plots/%s.pdf'%(name))

    ####################################################################
    # Combined 1D plots for overall efficiencies
    ####################################################################

    if True:
        for hist in overall_hists:
            print("Now plotting: " + hist[0])

            hists_to_plot = []
            for i_hist in hist:
                histlist = []
                c_histo = r.TEfficiency()
                for item in bglist:
                    tfile = root_open(basedir + item + ".root", "READ")
                    t_eff = tfile.Get(i_hist)
                    if len(histlist) == 0:
                        c_histo = t_eff
                    else:
                        c_histo.Add(t_eff)
                    histlist.append(t_eff)

                binf = getDictValue(i_hist, binning)
                if binf is not None:
                    c_histo = eff_rebinner(c_histo,binf)

                i_titles = getDictValue(i_hist, titles)

                c_histo = Graph(c_histo.CreateGraph())
                c_histo.SetLineColor(eff_colorList[i_hist])
                if i_titles is not None:
                    c_histo.SetTitle(i_titles[0])
                else:
                    c_histo.SetTitle(i_hist)

                if 'Nvtx' in i_hist:
                    c_histo.xaxis.SetTitle('$N_{vtx}$')
                if 'Mass' in i_hist:
                    if i_titles is not None:
                        c_histo.xaxis.SetTitle(i_titles[1])
                    else:
                        c_histo.xaxis.SetTitle('$M$ (GeV)')
                if i_titles is not None:
                    c_histo.yaxis.SetTitle(i_titles[2])
                else:
                    c_histo.yaxis.SetTitle('$\epsilon$')

                hists_to_plot.append(c_histo)

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower middle', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')
            hist_style.Set_legend_font_size(12)

            test = plotter(hist = hists_to_plot, style = hist_style)

            if hist in yranges.keys():
                test.Set_axis(logy = False, grid = True, ymin=yranges[hist][0],ymax=yranges[hist][1])
            else:
                test.Set_axis(logy = False, grid = True)
    
            test._cms_text_x         = 0.12
            test._cms_text_y         = 0.91
    
            name=hist[0].replace("/","")

            test.create_plot()

            if 'Mass' in hist[0]:
                plot_efficiency_fit(test.Get_axis1(), hists_to_plot[-1], xmin = 0, xmax = 6000, startvals = [0.78, -96, -85, -1.9e-5], plottrange = [100,6000])

            test.SavePlot('plots/%s.pdf'%(name))

    ####################################################################
    # Individual 2D plots
    ####################################################################

    if False:
        for hist in hists2D:
            print("Now plotting: " + hist)
    
            histlist = []
            for item in bglist:
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist).CreateHistogram()
                # t_eff.SetLineColor(colorList[item])
                t_eff.SetTitle(item)
                # t_eff.xaxis.SetTitle(t_eff.GetXaxis().GetTitle())
                # t_eff.yaxis.SetTitle(t_eff.GetYaxis().GetTitle())
                histlist.append(t_eff)

                hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "outside left", legendPosition = 'lower middle', lumi = 0, cms = 13)
    
                hist_style.Set_additional_text('Spring15 simulation')
    
                test = plotter2D(hist = t_eff, style = hist_style)
    
                # test.Set_axis(xmin = -2.5, xmax = 2.5, ymin = 0, ymax = 3.1, zmin = 0, zmax = 1)
    
                name=hist.replace("/","")
    
                test.create_plot()
    
                test.save_plot('plots/%s_%s.pdf'%(item,name))

    ####################################################################
    # Combined 2D plots
    ####################################################################

    if False:
        for hist in hists2D:
            print("Now plotting: " + hist)
    
            histlist = []
            c_histo = r.TEfficiency()
            for item in bglist:
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist)
                if len(histlist) == 0:
                    c_histo = t_eff
                else:
                    c_histo.Add(t_eff)
                histlist.append(t_eff)

            c_histo = c_histo.CreateHistogram()
            c_histo.SetTitle(hist)

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "outside left", legendPosition = 'lower middle', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')

            test = plotter2D(hist = c_histo, style = hist_style)

            # test.Set_axis(xmin = -2.5, xmax = 2.5, ymin = 0, ymax = 3.1, zmin = 0, zmax = 1)

            name=hist.replace("/","")

            test.create_plot()

            test.save_plot('plots/%s.pdf'%(name))

    ####################################################################
    # Resolution plot
    ####################################################################

    if False:
        for hist in res_histos:
            print("Now plotting: " + hist)
    
            histlist = []
            c_histo = r.TH2F()
            for item in bglist:
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist)
                if len(histlist) == 0:
                    c_histo = t_eff
                else:
                    c_histo.Add(t_eff)
                histlist.append(t_eff)

            c_histo.SetTitle(hist)

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Standard', cmsPositon = "outside left", legendPosition = 'lower middle', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')

            test = plotter2D(hist = c_histo, style = hist_style)
            # test.Add_x_projection()
            # test.Add_y_projection()

            test.Set_axis(ymin = -0.5, ymax = 0.5)

            name=hist.replace("/","")

            test.create_plot()

            test.save_plot('plots/%s.pdf'%(name))

    ####################################################################
    # Individual resolution plots
    ####################################################################

    if True:
        for hist in res_histos1D:
            print("Now plotting: " + hist)

            x_vals =[]
            y_vals = []
            y_errs = []
            for item in bglist:
                if 'LLE_LQD-001' not in item:
                    continue
                tfile = root_open(basedir + item + ".root", "READ")
                t_eff = tfile.Get(hist)
                t_eff.xaxis.SetTitle('$'+t_eff.xaxis.GetTitle()+'$')
                t_eff.yaxis.SetTitle('Events / %.2f'%t_eff.GetBinWidth(1))

                hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower left', lumi = 0, cms = 13)
                hist_style.Set_additional_text('Spring15 simulation')
                test = plotter(hist = [t_eff],style=hist_style)
                name=item.replace("/","")
                test.Set_axis(logy = True, grid = True, xmin = -1.01, xmax = 1.01, ymin = 0.9, ymax = 4000)
                test.create_plot()

                plot_gauss_fit(test.Get_axis1(), t_eff, color = 'red', write_results = True)

                test.SavePlot('plots/%s.pdf'%(name))

                fit_res = t_eff.Fit('gaus', 'N0S', '')
                y_vals.append(fit_res.Parameter(2))
                y_errs.append(fit_res.ParError(2))
                parts = item.split('_')
                for part in parts:
                    if 'M-'in part:
                        x_vals.append(int(part[2:]))

            x_vals = np.array(x_vals)
            y_vals = np.array(y_vals)
            y_errs = np.array(y_errs)

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

            hist_style = sc.style_container(style = 'CMS', useRoot = False, kind = 'Graphs', cmsPositon = "upper left", legendPosition = 'lower left', lumi = 0, cms = 13)

            hist_style.Set_additional_text('Spring15 simulation')

            test = plotter(hist = [graph],style=hist_style)

            name=hist.replace("/","")

            test.Set_axis(logy = False, grid = True, xmin = 0, xmax = 6500)

            test.create_plot()

            func = plot_resolution_fit(test.Get_axis1(), graph, xmin = 0, xmax = 6000, startvals = [], plottrange = [], color = 'black')

            test.SavePlot('plots/%s.pdf'%(name))
            graph.SaveAs('plots/%s.root'%(name))
            func.SaveAs('plots/%s_func.root'%(name))

    return 42



main()
