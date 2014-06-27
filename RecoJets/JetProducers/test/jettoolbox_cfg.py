miniAOD=True

if miniAOD:
    from RecoJets.JetProducers.jettoolboxMiniHelper_cff import *
else:
    from RecoJets.JetProducers.jettoolboxHelper_cff import *

####################################################################################################
#pileupJetID
"""
process.load('RecoJets.JetProducers.pileupjetidproducer_cfi')

process.pileupJetIdCalculator.jets = cms.InputTag("ak4PFJetsCHS")
process.pileupJetIdEvaluator.jets = cms.InputTag("ak4PFJetsCHS")
process.pileupJetIdCalculator.rho = cms.InputTag("fixedGridRhoFastjetAll")
process.pileupJetIdEvaluator.rho = cms.InputTag("fixedGridRhoFastjetAll")

process.patJetsAK4PFCHS.userData.userFloats.src += ['pileupJetIdEvaluator:fullDiscriminant']
process.patJetsAK4PFCHS.userData.userInts.src += ['pileupJetIdEvaluator:cutbasedId','pileupJetIdEvaluator:fullId']
process.out.outputCommands += ['keep *_pileupJetIdEvaluator_*_*']

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#QGTagger

process.load('RecoJets.JetProducers.QGTagger_cfi')

process.QGTagger.srcJets = cms.InputTag("ak4PFJetsCHS")
process.QGTagger.jetsLabel = cms.string('QGL_AK5PFchs')

process.patJetsAK4PFCHS.userData.userFloats.src += ['QGTagger:qgLikelihood']
process.out.outputCommands += ['keep *_QGTagger_*_*']
"""
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Njettiness

process.load('RecoJets.JetProducers.nJettinessAdder_cfi')

process.NjettinessCA8 = process.Njettiness.clone()
process.NjettinessCA8.src = cms.InputTag("ca8PFJetsCHS")
process.NjettinessCA8.cone = cms.double(0.8)

process.patJetsCA8PFCHS.userData.userFloats.src += ['NjettinessCA8:tau1','NjettinessCA8:tau2','NjettinessCA8:tau3']
process.out.outputCommands += ['keep *_NjettinessCA8_*_*']

process.NjettinessAK8 = process.NjettinessCA8.clone()
process.NjettinessAK8.src = cms.InputTag("ak8PFJetsCHS")

process.patJetsAK8PFCHS.userData.userFloats.src += ['NjettinessAK8:tau1','NjettinessAK8:tau2','NjettinessAK8:tau3']
process.out.outputCommands += ['keep *_NjettinessAK8_*_*']

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#QJetsAdder

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                   QJetsAdderCA8 = cms.PSet(initialSeed = cms.untracked.uint32(7)),
                                                   QJetsAdderAK8 = cms.PSet(initialSeed = cms.untracked.uint32(31)))

process.load('RecoJets.JetProducers.qjetsadder_cfi')

process.QJetsAdderCA8 = process.QJetsAdder.clone()
process.QJetsAdderCA8.src = cms.InputTag("ca8PFJetsCHS")
process.QJetsAdderCA8.jetRad = cms.double(0.8)
process.QJetsAdderCA8.jetAlgo = cms.string('CA')

process.patJetsCA8PFCHS.userData.userFloats.src += ['QJetsAdderCA8:QjetsVolatility']
process.out.outputCommands += ['keep *_QJetsAdderCA8_*_*']

process.QJetsAdderAK8 = process.QJetsAdderCA8.clone()
process.QJetsAdderAK8.src = cms.InputTag("ak8PFJetsCHS")
process.QJetsAdderAK8.jetAlgo = cms.string('AK')

process.patJetsAK8PFCHS.userData.userFloats.src += ['QJetsAdderAK8:QjetsVolatility']
process.out.outputCommands += ['keep *_QJetsAdderAK8_*_*']
                                   
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Grooming valueMaps
"""
process.load('RecoJets.Configuration.RecoPFJets_cff')

process.patJetsCA8PFCHS.userData.userFloats.src += ['ca8PFJetsCHSPrunedLinks','ca8PFJetsCHSTrimmedLinks','ca8PFJetsCHSFilteredLinks']
process.out.outputCommands += ['keep *_ca8PFJetsCHSPrunedLinks_*_*',
                               'keep *_ca8PFJetsCHSTrimmedLinks_*_*',
                               'keep *_ca8PFJetsCHSFilteredLinks_*_*']

process.patJetsAK8PFCHS.userData.userFloats.src += ['ak8PFJetsCHSPrunedLinks','ak8PFJetsCHSTrimmedLinks','ak8PFJetsCHSFilteredLinks']
process.out.outputCommands += ['keep *_ak8PFJetsCHSPrunedLinks_*_*',
                               'keep *_ak8PFJetsCHSTrimmedLinks_*_*',
                               'keep *_ak8PFJetsCHSFilteredLinks_*_*']

process.cmsTopTagPFJetsCHSLinksCA8 = process.ca8PFJetsCHSPrunedLinks.clone()
process.cmsTopTagPFJetsCHSLinksCA8.src = cms.InputTag("ca8PFJetsCHS")
process.cmsTopTagPFJetsCHSLinksCA8.matched = cms.InputTag("cmsTopTagPFJetsCHS")

process.patJetsCA8PFCHS.userData.userFloats.src += ['cmsTopTagPFJetsCHSLinksCA8']
process.out.outputCommands += ['keep *_cmsTopTagPFJetsCHSLinksCA8_*_*']

process.cmsTopTagPFJetsCHSLinksAK8 = process.cmsTopTagPFJetsCHSLinksCA8.clone()
process.cmsTopTagPFJetsCHSLinksAK8.src = cms.InputTag("ak8PFJetsCHS")
process.cmsTopTagPFJetsCHSLinksAK8.matched = cms.InputTag("cmsTopTagPFJetsCHS")

process.patJetsAK8PFCHS.userData.userFloats.src += ['cmsTopTagPFJetsCHSLinksAK8']
process.out.outputCommands += ['keep *_cmsTopTagPFJetsCHSLinksAK8_*_*']
"""
####################################################################################################

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameter:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##

if miniAOD:
    process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring("file:/uscms/home/jstupak/miniAOD2/CMSSW_7_0_6/src/miniAOD-prod_PAT.root")
                                )
else:
    from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
    process.source.fileNames = filesRelValProdTTbarAODSIM

process.maxEvents.input = 5
process.out.fileName = 'jettoolbox.root'
