import os
import re
import sys

nameFile=re.split("\.",sys.argv[1])[0];
print "name=",nameFile

file = open(nameFile+".py","r")
scriptLine = file.readlines()
file.close()

outFile = open(nameFile+"_Customized.py","w")

for line in scriptLine:
    if len(re.split("HLTEgammaGenericFilter",line))> 1:
	if len(re.split("hltMuonHcalIsoFilterUnseeded",line))> 1:
            outFile.write('process.hltMuonHcalIsoFilterUnseeded = cms.EDFilter( \"HLTMuonGenericFilter\",\n')
	elif len(re.split("hltMuonHcalIsoFilter",line))> 1:
            outFile.write('process.hltMuonHcalIsoFilter = cms.EDFilter( \"HLTMuonGenericFilter\",\n')
        elif len(re.split("hltMuonEcalIsoFilterUnseeded",line))> 1:
            outFile.write('process.hltMuonEcalIsoFilterUnseeded = cms.EDFilter( \"HLTMuonGenericFilter\",\n')
        elif len(re.split("hltMuonEcalIsoFilter",line))> 1:
            outFile.write('process.hltMuonEcalIsoFilter = cms.EDFilter( \"HLTMuonGenericFilter\",\n')
        continue
    if len(re.split("EgammaHLTHcalPFClusterIsolationProducer",line))> 1:
	if len(re.split("hltMuonHcalPFClusterIsoUnseeded",line))> 1:
            outFile.write('process.hltMuonHcalPFClusterIsoUnseeded = cms.EDProducer( \"MuonHLTHcalPFClusterIsolationProducer\",\n')
	elif len(re.split("hltMuonHcalPFClusterIso",line))> 1:
            outFile.write('process.hltMuonHcalPFClusterIso = cms.EDProducer( \"MuonHLTHcalPFClusterIsolationProducer\",\n')
        continue
    if len(re.split("EgammaHLTEcalPFClusterIsolationProducer",line))> 1:
        if len(re.split("hltMuonEcalPFClusterIsoUnseeded",line))> 1: 
            outFile.write('process.hltMuonEcalPFClusterIsoUnseeded = cms.EDProducer( \"MuonHLTEcalPFClusterIsolationProducer\",\n')
        elif len(re.split("hltMuonEcalPFClusterIso",line))> 1: 
            outFile.write('process.hltMuonEcalPFClusterIso = cms.EDProducer( \"MuonHLTEcalPFClusterIsolationProducer\",\n')
        continue
    if len(re.split("recoEcalCandidateProducer",line))> 1:
        outFile.write('    recoChargedCandidateProducer = cms.InputTag( "hltL3MuonCandidates" ),\n')
        continue
    if len(re.split("HLTL1UnpackerSequence = ",line))> 1:
        outFile.write('process.hltMuonSumCaloPFiso= cms.EDProducer( "L3MuonSumCaloPFIsolationProducer",\n')
        outFile.write('     recoChargedCandidateProducer = cms.InputTag( "hltL3MuonCandidates" ),\n')
        outFile.write('     pfEcalClusterProducer = cms.InputTag( "hltMuonEcalPFClusterIsoUnseeded" ),\n')
        outFile.write('     pfHcalClusterProducer = cms.InputTag( "hltMuonHcalPFClusterIsoUnseeded" ),\n')
        outFile.write(')')
        outFile.write('\n')
        outFile.write(line)
        continue
    if len(re.split("process.HLTL3muoncaloPFisorecoSequenceNoBoolsUnseededCombIso = ",line))> 1:
        outFile.write(line[:-3]+" + process.hltMuonSumCaloPFiso) \n")
	continue
    outFile.write(line)


outFile.write("from SLHCUpgradeSimulations.Configuration.postLS1Customs import *\n")
outFile.write("process = customise_HLT( process )\n")

                                                    
                        
