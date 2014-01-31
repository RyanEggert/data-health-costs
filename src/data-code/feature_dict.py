import pickle as p


data = {"DUID DWELLING UNIT ID":(1, 5),"PID PERSON NUMBER":(6, 8),"DUPERSID PERSON ID (DUID + PID)":(9, 16),"EVNTIDX EVENT ID":(17, 28),"EVENTRN EVENT ROUND NUMBER":(29, 29),"ERHEVIDX EVENT ID FOR CORRESPONDING EMER RM VISIT":(30, 41),"FFEEIDX FLAT FEE ID":(42, 53),"PANEL PANEL NUMBER":(54, 55),"MPCDATA MPC DATA FLAG":(56, 56),"IPBEGYR EVENT START DATE - YEAR":(57, 60),"IPBEGMM EVENT START DATE - MONTH":(61, 62),"IPBEGDD EVENT START DATE - DAY":(63, 64),"IPENDYR EVENT END DATE - YEAR":(65, 68),"IPENDMM EVENT END DATE - MONTH":(69, 70),"IPENDDD EVENT END DATE - DAY":(71, 72),"NUMNIGHX NUM OF NIGHTS IN HOSPITAL - EDITED/IMPUTED":(73, 75),"NUMNIGHT NUMBER OF NIGHTS STAYED AT PROVIDER":(76, 77),"EMERROOM DID STAY BEGIN WITH EMERGENCY ROOM VISIT":(78, 79),"SPECCOND HOSPITAL STAY RELATED TO CONDITION":(80, 81),"RSNINHOS REASON ENTERED HOSPITAL":(82, 83),"DLVRTYPE VAGINAL OR CAESAREAN DELIVERY":(84, 85),"EPIDURAL RECEIVE AN EPIDURAL OR SPINAL FOR PAIN":(86, 87),"ANYOPER ANY OPERATIONS OR SURGERIES PERFORMED":(88, 89),"IPICD1X 3-DIGIT ICD-9-CM CONDITION CODE":(90, 92),"IPICD2X 3-DIGIT ICD-9-CM CONDITION CODE":(93, 95),"IPICD3X 3-DIGIT ICD-9-CM CONDITION CODE":(96, 98),"IPICD4X 3-DIGIT ICD-9-CM CONDITION CODE":(99, 101),"IPPRO1X 2-DIGIT ICD-9-CM PROCEDURE CODE":(102, 103),"IPPRO2X 2-DIGIT ICD-9-CM PROCEDURE CODE":(104, 105),"IPCCC1X MODIFIED CLINICAL CLASSIFICATION CODE":(106, 108),"IPCCC2X MODIFIED CLINICAL CLASSIFICATION CODE":(109, 111),"IPCCC3X MODIFIED CLINICAL CLASSIFICATION CODE":(112, 114),"IPCCC4X MODIFIED CLINICAL CLASSIFICATION CODE":(115, 117),"DSCHPMED MEDICINES PRESCRIBED AT DISCHARGE":(118, 119),"FFIPTYPE FLAT FEE BUNDLE":(120, 121),"IPXP11X TOT EXP FOR EVENT (IPFXP11X+IPDXP11X)":(122, 130),"IPTC11X TOTAL CHG FOR EVENT (IPFTC11X+IPDTC11X)":(131, 140),"IPFSF11X FACILITY AMT PD, FAMILY (IMPUTED)":(141, 148),"IPFMR11X FACILITY AMT PD, MEDICARE (IMPUTED)":(149, 157),"IPFMD11X FACILITY AMT PD, MEDICAID (IMPUTED)":(158, 166),"IPFPV11X FACILITY AMT PD, PRIV INSUR (IMPUTED)":(167, 175),"IPFVA11X FAC AMT PD,VETERANS/CHAMPVA(IMPUTED)":(176, 183),"IPFTR11X FACILITY AMT PD,TRICARE(IMPUTED)":(184, 191),"IPFOF11X FACILITY AMT PD, OTH FEDERAL (IMPUTED)":(192, 199)}

if __name__ == "__main__":
	with open("../feature_dict.p",'wb') as f:
		print "Dumping Data in feature_dict.p ..."
		p.dump(data, f)
		print "Finished Dumping Data"