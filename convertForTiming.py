import os
import re
import sys

nameFile=re.split("\.",sys.argv[1])[0];
print "name=",nameFile

file = open(nameFile+".py","r")
scriptLine = file.readlines()
file.close()

outFile = open(nameFile+"_Timing.py","w")

for line in scriptLine:
    line = line.replace("hltL1extraParticles","l1extraParticlesFromSkim")
    line = line.replace("hltCsc2DRecHits","coucou")
    line = line.replace("hltGtDigis","gtDigisFromSkim")
    line = line.replace("hltL1GtObjectMap","gtDigisFromSkim")
    if len(re.split("GMTReadoutCollection",line))> 1:
        outFile.write("GMTReadoutCollection = cms.InputTag( \"simGmtDigis\" ),\n")
        continue
    if len(re.split("process.HLTL1UnpackerSequence = cms.Sequence\(",line))> 1:
        continue
    if len(re.split("process.HLTBeginSequence = cms.Sequence\(",line))> 1:
        outFile.write("process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTBeamSpot )\n")
        continue
    if len(re.split("process.HLTriggerFinalPath = cms.Path\(",line))> 1:
        outFile.write("process.HLTriggerFinalPath = cms.Path( process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW )\n")
        continue

    outFile.write(line)
