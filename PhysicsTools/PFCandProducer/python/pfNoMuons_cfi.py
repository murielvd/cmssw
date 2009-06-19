import FWCore.ParameterSet.Config as cms

pfNoMuons = cms.EDProducer("PFTopProjectorPF2PAT",
    PFCandidates = cms.InputTag("particleFlow"),
    PileUpPFCandidates = cms.InputTag(""),
    IsolatedElectrons = cms.InputTag(""),
    IsolatedMuons = cms.InputTag("pfMuons"),
    PFJets = cms.InputTag(""),
    PFTaus = cms.InputTag(""),
    verbose = cms.untracked.bool(False),
)

