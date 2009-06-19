
import FWCore.ParameterSet.Config as cms


PF2PATEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
    'keep recoPFCandidates_*_*_*',
    'keep *_offlinePrimaryVerticesWithBS_*_*',
    'keep *_particleFlow_*_*',
    'keep *_pfMET_*_*',
    'keep recoGenMETs_*_*_*',
    'keep *_pfCandToVertexAssociator_*_*',
#    'keep *_pfPileUp_*_*',
#    'keep *_pfElectrons_*_*',
    'keep *_pfMuons_*_*',
    'keep *_tausOnJets_*_*',
    'keep *_allLayer0Taus_*_*'
#    'keep *_pfTopProjection_*_*',
    )
)

PF2PATStudiesEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
    'keep *_particleFlow_*_*'
    )
)

