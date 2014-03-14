"""
Config.py contains configuration data like constants
Also contains notes on the data sets

author: chris
"""
import os
import cPickle as p

def path(*path):
	"""
	Replacement for os.path.join
	It performs makedirs on paths that don't exists
	Returns the os.path.join() result	
	author:chris
	"""
	if len(path) == 0:
		return ""
		
	targetpath = os.path.join(*path)
	if "." in path[-1]:
		path = path[:-1]
	targetdirs = os.path.join(*path)
	
	if not os.path.exists(targetdirs):
		os.makedirs(targetdirs)	
	return targetpath

def get(fpath, func, **kwargs):
	if os.path.exists(fpath):
		return p.load(open(fpath, 'rb'))
	res = func(**kwargs)
	try:
		with open(fpath, 'wb') as f:
			p.dump(res, f)
	except:
		print "Data file too large."
	return res
	



"""
Data sets
"""
baseA = "http://meps.ahrq.gov/data_stats/download_data_files_codebook.jsp?PUFId="
baseB = "http://meps.ahrq.gov/mepsweb/data_stats/download_data_files_codebook.jsp?PUFId="

download = "http://meps.ahrq.gov/data_files/pufs/%sdat.zip"

datafiles = {}
datafiles["H144D"] = ("IPTC11X",["IPBEGYR","IPBEGMM","IPBEGDD"], baseA + "H144D")
datafiles["H144E"] = ("ERTC11X",["ERDATEYR","ERDATEMM","ERDATEDD"], baseA + "H144E")
datafiles["H144A"] = ("RXMD11X",["RXBEGYXR", "RXBEGMM","RXBEGDD"], baseA + "H144A")
datafiles["H143"]  = ("RTHLTH13",["BEGRFY13","BEGRFM13","BEGRFD13"], baseA + "H143")
datafiles["H147"] = ("TOTTCH11",[], baseA + "H147")
datafiles["PROJYR02"]  = (None,[], baseB + "PROJYR02")

feature_dict = {}
feature_dict["H144A"] = ["PERWT11F", "PHARTP1", "PHARTP2", "PHARTP4", "PHARTP6", "PHARTP7", "RXCCC1X", "RXCCC2X", "RXCCC3X", "RXDAYSUP", "RXICD1X", "RXICD2X", "RXICD3X", "RXMD11X", "RXQUANTY", "RXSF11X", "RXSL11X", "RXSTRENG", "RXSTRUNT", "RXXP11X", "TC1", "TC1S1", "TC2", "TC2S1", ]
feature_dict["H144D"] = ["ANYOPER", "DLVRTYPE", "DSCHPMED", "EMERROOM", "EPIDURAL", "ERHEVIDX", "EVNTIDX", "IPBEGDD", "IPBEGMM", "IPCCC1X", "IPCCC2X", "IPCCC3X", "IPCCC4X", "IPDMD11X", "IPDMR11X", "IPDOR11X", "IPDOT11X", "IPDOU11X", "IPDPV11X", "IPDSF11X", "IPDSL11X", "IPDTC11X", "IPDTR11X", "IPDXP11X", "IPENDDD", "IPFMD11X", "IPFMR11X", "IPFOR11X", "IPFOT11X", "IPFOU11X", "IPFPV11X", "IPFSF11X", "IPFSL11X", "IPFTC11X", "IPFTR11X", "IPFVA11X", "IPFXP11X", "IPICD2X", "IPICD3X", "IPICD4X", "IPPRO1X", "IPPRO2X", "IPXP11X", "NUMNIGHT", "NUMNIGHX", "PERWT11F", "RSNINHOS", "VARSTR", "SPECCOND"]
feature_dict["H144E"] = ["ANESTH", "EEG", "EKG", "ERDMD11X", "ERDMR11X", "ERDOR11X", "ERDOT11X", "ERDOU11X", "ERDPV11X", "ERDSF11X", "ERDSL11X", "ERDTC11X", "ERDTR11X", "ERDVA11X", "ERDWC11X", "ERDXP11X", "ERFMD11X", "ERFMR11X", "ERFOF11X", "ERFOR11X", "ERFOT11X", "ERFOU11X", "ERFPV11X", "ERFSF11X", "ERFSL11X", "ERFTC11X", "ERFTR11X", "ERFVA11X", "ERFWC11X", "ERFXP11X", "ERHEVIDX", "ERICD1X", "ERICD2X", "ERICD3X", "ERPRO1X", "ERPRO2X", "ERTC11X", "ERXP11X", "FFERTYPE", "LABTEST", "MAMMOG", "MEDPRESC", "MPCDATA", "MRI", "OTHSVCE", "PANEL", "PERWT11F", "RCVVAC", "SEEDOC", "SONOGRAM", "SURGPROC", "THRTSWAB", "VSTCTGRY", "VSTRELCN", "XRAYS"]
feature_dict["H143"]  = ["ACTDTY13", "ACTLIM13", "ADLHLP13", "AGE13X", "AIDHLP13", "BEGRFD13", "BEGRFM13", "BENDIF13", "COGLIM13", "DOBYY", "EDRECODE", "EDUCYR", "EDUYRDEG", "EMPST13", "ENDRFD13", "ENDRFM13", "FAMSIZ13", "FNGRDF13", "FTSTD13X", "HELD13X", "HIDEG", "HISPANX", "HISPCAT", "HONRDC13", "HOUR13", "HRWAG13X", "HRWAY13", "HRWGRD13", "HSELIM13", "IADLHP13", "INSCOP13", "KEYNESS", "LFTDIF13", "MARRY13X", "MCAID13", "MCAID13X", "MCARE13", "MCARE13X", "MILDIF13", "MNHLTH13", "MSA13", "NUMEMP13", "OFFER13X", "OTPUBA13", "OTPUBB13", "PROXY13", "PSTAT13", "PUB13X", "RACEAX", "RACEBX", "RACETHNX", "RACEWX", "RACEX", "RCHDIF13", "RDRESP13", "REGION13", "RFREL13X", "RNDREF13", "RUCLAS13", "RUENDM13", "RURSLT13", "RUSIZE13", "SCHLIM13", "SELFCM13", "SEX", "SOCLIM13", "SPOUID13", "SPOUIN13", "STNDIF13", "STPDIF13", "STPRG13", "TRINW13X", "UNABLE13", "WLKDIF13", "WLKLIM13", "WRKLIM13"]
feature_dict["H147"]  = ["DVGMCD11", "HPDOC11", "INTRP11X", "RECPEP42", "PRSTAGED", "IPTPTR11", "MCDMY11X", "PRIOG53", "IPDOPR11", "HHASLF11", "DVORTH11", "CTRTMT53", "CFMNTM53", "PMDINS31", "HPOAU11", "RXOFD11", "CFMPOG53", "OBASTL11", "ASPRIN53", "OTPBAT42", "RUCLAS53", "OPOVA11", "CHRESP42", "PROXY11", "PNGAU11", "CALARYNX", "ZIDWCP11", "LYMPAGED", "PHYEXE53", "TRIJL11X", "PNGJL11", "UNINS11", "CHBRON53", "MCAID53X", "CELIGI53", "IPFMCD11", "BEGRFM42", "CAMOUTH", "BRAIREMS", "OPFOPU11", "HAVFUN42", "PRDRNP31", "MCRNO11", "OBVPTR11", "STAPR31", "IPFOTH11", "OBETRI11", "PRINO11", "IPTOPU11", "OTPBAT53", "DVOVA11", "MORJOB31", "CHTHER42", "PRSAU11", "TRIAP11X", "OCCCAT31", "ZIFOPU11", "HPSAP11", "HASFSA31", "HPSFE11", "PREGNT53", "CHTHCO42", "CNPTRT53", "HHNOTH11", "MCRJU11", "MCRSE11", "AMTOSR11", "DVOMCD11", "OPDMCR11", "OBAPRV11", "CFMETM53", "MILDIF53", "OFREMP31", "ADSOCA42", "PRIOG11", "OPTWCP11", "CLPROD53", "STAAU11", "ANGIAGED", "TRINO11X", "POUOC11", "SCLNBD42", "ALIMP11X", "AMEOPR11", "DSCINT53", "SPOUIN53", "OBDOPU11", "HEARNG42", "OPOMCD11", "MCDFE11", "ADDRBP42", "DAPID53X", "CATESTIS", "HONRDC31", "FAMSZE53", "OBAOSR11", "PRVHMO11", "MCRMA11", "ERTMCR11", "AMNOFD11", "OTHDYS42", "PAYDR42", "DVOPTR11", "HIBPDX", "ADLHLP31", "DECIDE42", "REGION42", "HEALTH42", "WLK3MO53", "SAQWT11F", "RESPCT42", "PMEDUP42", "FTSTU53X", "AGE42X", "DSEY1253", "PDKJA11", "WASMCAID", "MCDDE11", "CABRAIN", "SSNLJB42", "AMTMCD11", "DSEB1053", "AMNTCH11", "IRASP11X", "OPSWCP11", "OBCTCH11", "OBNTRI11", "HPOMY11", "FOODVL11", "OBAMCD11", "CATHROAT", "CHOLDX", "FTSTU31X", "CMNACC53", "PNGFE11", "ZIDEXP11", "ADEXPL42", "JOBORG53", "CNPTMT53", "PUBAT42X", "PHMONP31", "MCROC11X", "ASACUT53", "OFFER31X", "CHLICO42", "ALIIMP11", "WLKLIM31", "ARTHAGED", "MCRJL11X", "DVOMCR11", "DVTOPU11", "PUBJL11X", "ENDRFD11", "STANO11", "EMPHDX", "OBTMCR11", "CMCNEC53", "PUBAT11X", "CNGPLT53", "OPTOFD11", "OBOPTR11", "EDUCYR", "NUMEMP31", "DIFFPL42", "OBVOFD11", "PUBAT31X", "CLDJOB53", "PBSVCT42", "VISWCP11", "SELDSI42", "CFREE53", "DVTTRI11", "PMEDUP53", "PBINFM42", "DVTOTH11", "ZIDOFD11", "CEFCOP53", "RXPTR11", "CFMOTH53", "ADL3MO31", "DVGOPR11", "NOHINS42", "ERTWCP11", "OHRTAGED", "CEFREC53", "POGJU11", "KIDPRO42", "DENTIN53", "ADLHLP42", "CEFRHU53", "CLNTST53", "DVTSTL11", "MORECOVR", "OBOOPU11", "TOTOSR11", "AMESTL11", "NEWARE42", "HPDAU11", "WKINBD42", "IPFPRV11", "CNPTLT53", "BEGRFD31", "BPCHEK53", "ERFVA11", "PMUNPR42", "PUBAP11X", "ERDOPR11", "HELD42X", "WHITPR42", "MCRNO11X", "DDBDYS42", "PDKAU11", "PRDRNP42", "OPOEXP11", "OBEEXP11", "STAJA11", "ENDRFD42", "MCRJU11X", "PROXY53", "DSFL1253", "HHNOPR11", "OPSMCR11", "THRTAGED", "ENDRFD53", "IPTEXP11", "MCREV11", "PSTATS31", "OBVSTL11", "CHRTCR42", "PPRWKM42", "ADINTR42", "HPEMA11", "ADPRX42", "DSPRX53", "CAPANCRS", "OPTOPU11", "PUBMY11X", "PMUNRS42", "IADL3M53", "AMEOSR11", "OPOWCP11", "ERFOFD11", "HRWGIM53", "DSMED53", "CPSFAMID", "VISTRI11", "ERTEXP11", "OBCOFD11", "ASEVFL53", "OBAOTH11", "DENTCK53", "TRICR53X", "HPRJL11", "MCAID42X", "CPTTOT53", "PUB31X", "PRSNO11", "PRSMA11", "NOINSBEF", "OPAMY11", "CFNPMT53", "PDKMA11", "ZIFWCP11", "OPFOFD11", "MYSELF42", "AMCPTR11", "OCCCAT42", "EDUYRDEG", "MDUNRS42", "EMPST31", "FAMWT11C", "ONJOB42", "CABONE", "AGE53X", "IPTOSR11", "PDKFE11", "ERFPTR11", "PPRWKT42", "DVTOSR11", "PRIDK53", "HISPCAT", "MELAREMS", "ENGCMF42", "PLCTYP42", "AMCVA11", "SPRPRO42", "GENDRP42", "MDDLPR42", "SEX", "OPSOPR11", "RFREL31X", "CERET53", "OTHRREMS", "DVTSLF11", "POUJL11", "DVGMCR11", "TRIJA11X", "IPDMCD11", "CHECK53", "HPNNO11", "OPDOSR11", "TOTTCH11", "MCDHMO42", "OBOWCP11", "ERTSLF11", "OPTOSR11", "CAESOPH", "OPSSTL11", "LRNXREMS", "CHLIHB42", "TMTKUS42", "IPTMCR11", "AMEEXP11", "K6SUM42", "CMNOFF53", "ZIDOSR11", "RXOTH11", "ASDALY53", "MCDAP11", "CMNINS53", "OPDEXP11", "AMNOSR11", "ADSMOK42", "TRIAU11X", "OBEPTR11", "THRTREMS", "INSMA11X", "RXWCP11", "OBNVA11", "UNEMP11X", "PDKJU11", "TRIEX11X", "DIFFWG31", "ASSTIL31", "OTPUBA11", "WAGIMP11", "OBTOPU11", "CEFOG53", "GOTOUS42", "DOBYY", "OTHVA11", "OPPPTR11", "OPSOSR11", "AFTHOU42", "OTHOPU11", "FAMWT11F", "MDDLAY42", "FAMID31", "STAJU11", "DVTMCR11", "SFFLAG42", "OPOOPR11", "AMEWCP11", "LUNGAGED", "HPNOC11", "OPTMCR11", "OPVMCD11", "CWRKP53", "OPSEXP11", "ACTDTY31", "HELMET42", "DDNWRK42", "HRHOW53", "INSAT31X", "HHAOFD11", "CALIVER", "ZIFMCD11", "FAMSZEYR", "NUMEMP53", "STAAP11", "OBCMCD11", "PREVEN42", "DSKIDN53", "INTIMP11", "IPFOFD11", "MINORP42", "TOTEXP11", "PMEDIN31", "DVOOPR11", "ENDRFM11", "SOCLIM53", "VETIMP11", "TRIPR42X", "TRICH31X", "HHNMCD11", "AMCMCR11", "OFFER42X", "PRVDRL42", "INSRPL42", "CHTHHB42", "MCDAT42X", "TRILI11X", "CHILCR42", "CASKINNM", "HPRJA11", "PERWT11F", "ADPRTM42", "IRAIMP11", "WASAFDC", "CEFHLT53", "OPBJL11", "PRVEV11", "CNGPTR53", "PRSJA11", "MCRFE11", "IPFOPU11", "ZIFSLF11", "EVRWRK", "STJBMM53", "DVGSLF11", "CSHCN42", "MARRY42X", "EXRCIS53", "MORJOB42", "OPASE11", "OBEWCP11", "NHRWG53", "STAPR42", "WKINBD53", "CWYASK53", "CABLADDR", "TOTOFD11", "OBCOPR11", "OTHIMP11", "TRIOC11X", "CFMPTF53", "AMCSLF11", "INSCOV11", "OTHTCH11", "ZIFOSR11", "PRIVAT53", "AMEOPU11", "OPPSLF11", "HPDDE11", "MCARE53X", "TRILI31X", "CIN2OP53", "RTHLTH53", "HPNJA11", "BRAIAGED", "HPROC11", "IPTOPR11", "STJBDD53", "OTPUBA53", "DIVDP11X", "OBNOTH11", "OBTOTH11", "CHLIST42", "AMTOTC11", "AMEPRV11", "OPTSLF11", "LUNGREMS", "KIDNREMS", "PUBAU11X", "FTSTU42X", "PUBAT53X", "RESP53", "MCDEV11", "INSAT53X", "MCDAT31X", "OBEOSR11", "MESVIS42", "ERTPTR11", "LKINFT42", "ERDPTR11", "PROUT53", "CLNTRE53", "TOTMCD11", "AMEMCR11", "OPDPRV11", "OPTPTR11", "DVOSLF11", "DIABW11F", "OBEOPU11", "FAMINC11", "MCDDE11X", "RCHDIF31", "SALIMP11", "CASKINDK", "EATHLT42", "WASSTAT4", "OBCOPU11", "PMNCNP42", "ONGONG42", "BRSTAGED", "OTHOPR11", "MIAGED", "ZIFTCH11", "PRSMY11", "ERFPRV11", "PRIMA11", "OPDOTH11", "PRIV31", "AMCEXP11", "ERFSLF11", "DDNSCL31", "TRBLE42", "SCHPRO42", "CALEUKEM", "FILEDR11", "HRWGIM42", "PMEDPP31", "CLSTRT53", "SICPAY53", "CEFBCK53", "HPEAU11", "DVOTRI11", "CNGLDM53", "SALEP11X", "FCRP1231", "PEGJA11", "STOMREMS", "WASOTGOV", "OPPVA11", "MESHGT42", "ERFOPR11", "ADREST42", "RTPLNT42", "CLHINS53", "OBESTL11", "ENDRFY11", "CHOLCK53", "OPPOFD11", "TRICR11X", "AMCTRI11", "LOCATN42", "AMCWCP11", "USLIVE42", "UNABLE31", "PRIS31", "OPVOFD11", "ADLANG42", "ERDVA11", "CNGPDI53", "CEFLCT53", "BRSTEX53", "HHINFD11", "PRSSE11", "OPAJU11", "PRIEU11", "PEGAU11", "HHNOSR11", "RXOSR11", "HPOOC11", "FLUSHT53", "PSA53", "HPEJA11", "ACTDTY42", "IADLHP31", "CNGLDJ53", "FAMS1231", "HRWG42X", "RXTRI11", "CBCK53", "IPDVA11", "OTHSTL11", "HPRNO11", "WASSSI", "KIDNAGED", "PRIS53", "PROXY31", "OBTPRV11", "WHNPHY42", "ASWNFL53", "OBCPRV11", "OFREMP42", "JTPAIN31", "WLKDIF53", "PRIJA11", "OPVTCH11", "ERTOSR11", "AMTOPR11", "PEGJL11", "AMEOTH11", "PUBIMP11", "PEGAP11", "ERDOTH11", "BONEREMS", "PRVDRL11", "HHNEXP11", "PRVMNC11", "MCDAT11X", "DVGTCH11", "ASSTIL53", "PMEDPY42", "PRIOG42", "ERTOFD11", "OPOTHV11", "AMTSTL11", "ZIDMCR11", "ERFOSR11", "OPFVA11", "AMDRC11", "AMAWCP11", "OPFSTL11", "ERDPRV11", "OPTTRI11", "OBOPTO11", "CMCEFF53", "PDKDE11", "EXPLOP42", "HPNMY11", "PDKMY11", "STOMAGED", "TRIJU11X", "HPNAP11", "CEXTOT53", "PNGJA11", "OPBOC11", "MUSCREMS", "INSCOP42", "INSENDMM", "CMMAIN53", "AIDHLP53", "RNDFLG31", "PSTATS42", "AMTMCR11", "CNGFLX53", "MCRPD31", "CHPRTM42", "VISSTL11", "PMDINS11", "HPRSE11", "PDKSE11", "OPAJA11", "RFREL11X", "FAMID53", "IPFOPR11", "HHAGD11", "WCMPP11X", "HPOSE11", "CSAQW11F", "MCAID42", "DDNSCL53", "AMNWCP11", "BLDRREMS", "AMTTCH11", "DVTMCD11", "MCAID53", "OPPOTH11", "STPDIF53", "TYPEPE42", "KEYNESS", "OTHRAGED", "READNW42", "CACERVIX", "HPOFE11", "ENDRFD31", "HYSTER53", "DVGPTR11", "OPBMY11", "AMTEXP11", "UTERAGED", "PMUNAB42", "OPPOPR11", "PRIMY11", "OBTHER11", "WRHLTH42", "ERFSTL11", "ADMWLM42", "PROXY42", "ADINSA42", "DVOOPU11", "SICPAY31", "CFTRT53", "DDNWRK31", "SIBPRO42", "ADEGMC42", "TRIAT31X", "CFMDRT53", "NOASPR53", "POGJL11", "OBVOPR11", "HPSNO11", "OPSPTR11", "DPINRU11", "CHOIC42", "ADWRTH42", "ADILWW42", "MCDJU11X", "DVTTCH11", "OBVSLF11", "OBDOPR11", "OBTMCD11", "OBNSLF11", "PUBMA11X", "CMNTIM53", "HHAOTH11", "DVGTRI11", "PMEDPP42", "OVRYAGED", "ADLIST42", "ADPALS42", "ADRTCR42", "OPFEXP11", "VARPSU", "PRISE11", "OPOPTR11", "OPPSTL11", "YCHJ4253", "FLSTAT11", "DEDUCT11", "AMAOTH11", "OBAPTR11", "HEARMO42", "RUSIZE31", "OTHNDD53", "IPTPRV11", "AMCOTH11", "DVGEXP11", "ERFMCR11", "POVLEV11", "ADL3MO42", "HHAPRV11", "OBOMCD11", "PRVMNC31", "DSCHNV53", "MCDMA11", "MCAID31", "CHSPEC42", "WHNHEL42", "OPVOTH11", "HHATCH11", "DSCNPC53", "PMEDUP31", "OPPOPU11", "RXSTL11", "OBVOSR11", "VISOFD11", "OPOTCH11", "WRKLIM53", "OPVEXP11", "MCDJL11", "CHENEC42", "BEGRFY42", "SAFEST42", "PROUT11", "NOINUNIT", "RULETR53", "PMEDIN42", "AMAOSR11", "VISOTH11", "POGNO11", "MORE42", "CALUNG", "OBCOSR11", "INSURC11", "ERDMCD11", "MCDJU11", "OPSOTH11", "POUSE11", "BSTST53", "RACEX", "REGION11", "ERFEXP11", "POGAP11", "RURSLT31", "ZIDOPU11", "OBTSLF11", "AGELAST", "AMEPTR11", "TOTOPR11", "TOTDED11", "INSCOPE", "DVOEXP11", "HHAOPR11", "ELGRND53", "JOBORG31", "PAYDR53", "OTPAAT53", "PNGMY11", "DSFT1253", "PAYVAC42", "AMNOPU11", "AMNOTH11", "PROUT31", "OPTEXP11", "PNGJU11", "HPNJU11", "CSHIMP11", "INSJA11X", "STPRAT42", "FAMID42", "HPEAP11", "MORE53", "VISSLF11", "ADSPRF42", "HOUR42", "HPRMY11", "RACEBX", "CHLDP11X", "DVGOFD11", "CAUTERUS", "DNTINS11", "ERDOFD11", "MSA53", "OFREMP53", "ZIDOTH11", "INTVLANG", "SCLNBD31", "OBOVA11", "MCRDE11", "FMRS1231", "PRING53", "DVTOFD11", "HPSSE11", "AGE31X", "DNDLAY42", "DSDIA53", "SSNLJB31", "OPFSLF11", "IPFSLF11", "DENTIN31", "TRISE11X", "OHRTDX", "ADFHLP42", "NHRWG31", "CNGFLT53", "ASTHEP53", "PUBDE11X", "FAMRFPYR", "HPNSE11", "ADTLHW42", "OBVTCH11", "PRIOC11", "ADDAYA42", "OBTWCP11", "AMAMCD11", "MCDHMO11", "PRING31", "PRSAP11", "IPDOPU11", "AMCOFD11", "ADCMPY42", "MCARE53", "BEGRFY53", "ADPWLM42", "MCARE31", "CHOIC53", "CDIAG53", "MIDX", "PEGJU11", "PRIV11", "AMATCH11", "MCAID31X", "RULETR31", "MDUNPR42", "SSIP11X", "ASPREV53", "CHILWW42", "DNDLRS42", "PDKJL11", "TRIEX42X", "CFNSAC53", "MCRPHO11", "INS31X", "PRIAP11", "PEGMA11", "PRIEU31", "STNDIF31", "NERVAF42", "MCRPB11", "HPOJL11", "ERDOSR11", "AMNEXP11", "OPTOPR11", "HHATRI11", "FCSZ1231", "OBNSTL11", "UTERREMS", "POGOC11", "PMEDIN53", "ADILCR42", "FAMIDYR", "HHAMCR11", "POGAU11", "OPBAU11", "DUPERSID", "AMNOPR11", "OPTVA11", "LFTDIF31", "WASESTB", "HPDFE11", "MCARE11X", "WRKLIM31", "OPSMCD11", "OBAMCR11", "SGMTST53", "IPFSTL11", "OPBFE11", "PRIEU42", "ACTDTY53", "RETPLN31", "CNPTOF53", "IPFPTR11", "PBPWKT42", "MCDNO11X", "CNGPMT53", "TRIST31X", "HPNMA11", "RXMCD11", "BEGRFM31", "POUMY11", "VETSP11X", "CALYMPH", "POUFE11", "HHNTRI11", "STJBDD42", "COLOAGED", "WHNDEN42", "HPNAU11", "OBDPRV11", "PREVCOVR", "USBORN42", "SSIDIS11", "LEUKREMS", "ERDWCP11", "LSHLTH42", "ADUPRO42", "CFMLDJ53", "SOCLIM31", "ZIDOPR11", "TOTVA11", "BEGRFD42", "OBVOTH11", "HPENO11", "RXOPU11", "DISVW42X", "INSSE11X", "ASIANP42", "LRNXAGED", "CABREAST", "PNGDE11", "TOTOPU11", "STJBDD31", "MCDNO11", "CWYCNG53", "LKINFM42", "AMCSTL11", "YCHJ3142", "OPDSTL11", "PBINFT42", "PENIMP11", "STAPR53", "OBCSLF11", "MCARE11", "PRSJU11", "RXMCR11", "NEVILL42", "POUMA11", "DSDIET53", "IPTTRI11", "OTHTRI11", "RXSLF11", "CINCOV53", "MCRJL11", "PRING11", "ADRESP42", "ZIFTRI11", "CHOLAGED", "REFPRS31", "RXOPR11", "HPSAU11", "OBCVA11", "MCRAU11X", "CACOLON", "MOUTREMS", "HHAOSR11", "ARTHTYPE", "OBTOTV11", "CNGLDD53", "AFDC11", "MCDJA11X", "CNGLDT53", "LSTETH53", "HRWG31X", "CTMOFF53", "INSAU11X", "CEXTLT53", "SEATBE53", "HPONO11", "CEFPOS53", "CHBMIX42", "DKWHRU42", "OPTPRV11", "DDNSCL42", "OPVOPU11", "ERDMCR11", "OTHPRV11", "DADPRO42", "WASOTHER", "ADMALS42", "AMASST11", "LANGHM42", "INSMY11X", "SPOUIN31", "MARRY53X", "MAMOGR53", "OBOTCH11", "ELGRND31", "WHNBPR42", "TOTPRV11", "TEMPJB31", "MOPID53X", "BEGRFD53", "SPOUIN42", "ERFTCH11", "INSAP11X", "TOTSTL11", "YNOINS31", "HPEJU11", "OBTOFD11", "IPFOSR11", "SSNLJB53", "MCDAP11X", "AMNSTL11", "CHLIMI42", "MCRPD11", "CLMDEP11", "CFNBNK53", "CMNCRE53", "DSCGRP53", "PRIVAT42", "CTMSK53", "AMTOPU11", "EVRUNAT", "HPDNO11", "TRIST42X", "DSFB1053", "RCHDIF53", "DNUNAB42", "OPFTCH11", "MSA42", "PNGMA11", "PRIV53", "IPFTRI11", "ADEFRT42", "CFMFTM53", "DSFLNV53", "ERDTRI11", "PROVTY42", "RXPRV11", "CHSRHB42", "BLODREMS", "ADINST42", "STJBMM31", "DVOWCP11", "DVGPRV11", "OBEPRV11", "MNHLTH42", "OPAEV11", "OTPUBB31", "AMNSLF11", "WASSTAT3", "MNHLTH31", "DSEYNV53", "DVGOSR11", "OBNPTR11", "PRING42", "CNGFXD53", "IPFEXP11", "TEMPJB53", "REGION31", "IPZERO11", "HPSDE11", "FAMSZE11", "PDKNO11", "RXEXP11", "REFPRS42", "TOTOTH11", "HEARSM42", "RUCLAS42", "HPSJL11", "CEFMTL53", "ZIDPTR11", "BEGRFM53", "HHAMCD11", "OBCTRI11", "ERDSTL11", "FOODMN11", "TREATM42", "EVRETIRE", "INDCAT53", "CHAPPT42", "OPSSLF11", "ADHDAGED", "HLTHLF42", "HPDJA11", "CAMELANO", "UNION31", "CSTSVT42", "INSJL11X", "DVTEXP11", "DVOTCH11", "OTHMCD11", "TRTIMP11", "CFMGRT53", "IPDEXP11", "DNUNPR42", "OBAOPR11", "DIABDX", "CMOTHR", "CASTOMCH", "HPRJU11", "CLINIC42", "MESBPR42", "OPOOTH11", "HPRFE11", "OBNOFD11", "DSCH1253", "CHLIMP11", "DSVB1053", "ADPAIN42", "PRSTREMS", "TRIMY11X", "DSFTNV53", "OTHNDD42", "OBVMCD11", "OBDSTL11", "MARRY11X", "SICEAS42", "OPFPRV11", "MCDHMO31", "MSA11", "HHNWCP11", "AMTPRV11", "REFIMP11", "AMNMCR11", "PRIAU11", "OPDVA11", "STRKAGED", "AMCMCD11", "OBASST11", "ADNRGY42", "OTPUBA42", "OBVPRV11", "DUID", "IPDOSR11", "PHMONP42", "HPOAP11", "INSCOP11", "HPDAP11", "FSAAMT31", "TRIEX31X", "YNOINS42", "DNDLPR42", "POVCAT11", "MCDMC31", "OPTTCH11", "GDCPBM42", "BLODAGED", "CEFAHU53", "CFTTOT53", "SEEDIF42", "PUB42X", "MCRPB42", "MOPID42X", "OCCCAT53", "RACEAX", "OPDTRI11", "CMNAFF53", "OPANO11", "CHBRON31", "RESP11", "HPDSE11", "ADOVER42", "MCRDE11X", "OTPUBB53", "OTHWCP11", "CMCSTY53", "BRSTREMS", "BLCKPR42", "NWK31", "DSCH1053", "ASATAK53", "OBTVA11", "PRIDE11", "ADDPRS42", "WLKLIM53", "MCRPD42", "AMCPRV11", "IPTMCD11", "WHNSAF42", "OTPAAT11", "HPSJU11", "NHRWG42", "ASPKFL53", "ZIFEXP11", "PRDRNP11", "OBEMCD11", "SPOUID53", "OTHPTR11", "JNTPID11", "IPDPRV11", "PEGMY11", "MCDAU11", "STAJL11", "DVGVA11", "GDCPBT42", "DSCH1153", "OPTMCD11", "DIVIMP11", "DVTPTR11", "OBCWCP11", "CABLOOD", "OPDPTR11", "DSA1C53", "TAXFRM11", "IPTTCH11", "OPTOTH11", "PRVHMO31", "AMTWCP11", "IPFVA11", "PRIFE11", "CNGFMT53", "OBCOTH11", "HPODE11", "DVTWCP11", "OPDTCH11", "ERFMCD11", "OPOOFD11", "OBDSLF11", "CHGJ4253", "HHNOPU11", "HHNOFD11", "SELFCM53", "OBASLF11", "HPOMA11", "NOSMOK42", "CASHP11X", "MORE31", "OPSTRI11", "SPOUID42", "OPDOPU11", "OPDMCD11", "WASPRIV", "TRIDE11X", "HPRDE11", "OPFOPR11", "MOPID31X", "RECTAGED", "ADGENH42", "PNGAP11", "VISMCR11", "OTHRP11X", "MCARE42", "SCHLBH42", "CANCERDX", "MDUNAB42", "DEAF42", "SELFCM31", "BONEAGED", "FNGRDF31", "OPSOFD11", "PRIS42", "OPFOTH11", "OBVTRI11", "ADDOWN42", "OBDPTR11", "SKDKREMS", "SKNMAGED", "AMNPTR11", "HPESE11", "OBNTCH11", "OPSTCH11", "SAQELIG", "CFMCOG53", "DIFFWG53", "LAPBLT42", "OPTOTV11", "USCNOT42", "WHNBST42", "JTINRU11", "CNGFOG53", "OBOSTL11", "INS53X", "HHNMCR11", "POUJA11", "LANGPR42", "AMOPTO11", "MCRPD11X", "AMAMCR11", "AMTTRI11", "PRVDRL31", "CAOVARY", "APRDLT42", "DSFL1153", "MCARE31X", "ERDTCH11", "OPPWCP11", "IADLHP53", "OPPTRI11", "AMTHER11", "OPAAU11", "DSEYPR53", "DNTINS31", "HPNDE11", "ADSPEC42", "CFMFOG53", "WILFIL11", "CSLHIN53", "OPADE11", "PREGNT31", "TRILI42X", "MCAID11X", "ERTOPR11", "MCDJL11X", "HPDMA11", "PEGNO11", "DSCONF53", "BEGRFY31", "OBCSTL11", "EMPST53", "RECTREMS", "OPPMCR11", "OBATRI11", "POUAU11", "PUBFE11X", "MESWGT42", "MCDOC11X", "APRTRM42", "HSELIM31", "MCDAU11X", "LFTDIF53", "PHYSCL42", "ENDRFY53", "CHEMPB42", "OPAAP11", "DSFL1053", "IPFMCR11", "ACTLIM31", "HPNFE11", "STJBYY53", "COGLIM53", "BPMLDX", "TRIFE11X", "CHEXPL42", "MCDSE11X", "AGE11X", "CERVREMS", "HPSOC11", "OPAOC11", "OPPOSR11", "HHAOPU11", "RFREL53X", "OBNWCP11", "PDKOC11", "STADE11", "RUCLAS31", "AMEMCD11", "OPAJL11", "STAPR11", "OPVMCR11", "OBDEXP11", "CATHYROD", "DIABAGED", "DVGOPU11", "INSJU11X", "PRIDK31", "ERDOPU11", "WHNHGT42", "INSAT11X", "LYMPREMS", "DVOOTH11", "ERTOTH11", "OPVTRI11", "OPBDE11", "CHDAGED", "MARRY31X", "HEARAD42", "IPTOFD11", "IPDOTH11", "AMESLF11", "DAPID42X", "ERTOT11", "TRIPR31X", "PANCREMS", "FAMID11", "OBVEXP11", "STAMY11", "IPDIS11", "UNHAP42", "HPOJA11", "PID", "RETPLN42", "IADL3M42", "COVRMM", "OBVVA11", "DSINSU53", "ERTTRI11", "DVOSTL11", "POGMA11", "DDBDYS53", "ZIFOTH11", "AIDHLP31", "CFMNPT53", "DSEY1053", "UNION42", "VISTCH11", "OBDVA11", "FOODST11", "AMCOPR11", "WASSTAT2", "PEGSE11", "DVGSTL11", "AMTVA11", "MCDMY11", "NWK53", "OBAOFD11", "RXTOT11", "TRIMA11X", "BMINDX53", "AMAPRV11", "OPVSLF11", "IPFWCP11", "OBOSLF11", "STJBYY31", "RACETHNX", "SSIIMP11", "PRIOG31", "HPEJL11", "OPPMCD11", "APRTRT42", "PRIVAT11", "CNGFDI53", "MUSCAGED", "CNPTOT53", "ERDEXP11", "OPBJU11", "ADAPPT42", "PMNCNP31", "CHPMED42", "PSTATS53", "CNPOG53", "STASE11", "TRICR31X", "OBEMCR11", "WASVA", "IPTVA11", "CPROM53", "OPBEV11", "OPDRV11", "HHNTCH11", "OBCPTR11", "DSEY1153", "PRSDE11", "OBDTCH11", "SGMTRE53", "OPVPTR11", "OBOTHV11", "PRIEU53", "CAKIDNEY", "ERTPRV11", "CARECO42", "LIVRREMS", "REGION53", "EMPST42", "EDRECODE", "OTHRCP42", "WAGEP11X", "SKDKAGED", "CERVAGED", "PROUT42", "ZIFPRV11", "PRIVAT31", "CMCPSY53", "CFMPTM53", "AMTOTH11", "DOCELS42", "WLK3MO31", "DISVW31X", "MCRMY11X", "OBDMCR11", "IPTOTH11", "OBDRV11", "EMPHAGED", "RUSIZE42", "OPBJA11", "OPVPRV11", "IPDMCR11", "HHINDD11", "INSOC11X", "CNGFTR53", "SPOUID11", "PREGNT42", "PEGOC11", "PUB53X", "OFFER53X", "POGSE11", "BUSNP11X", "INSAT42X", "HELD53X", "IPTWCP11", "CEXTRT53", "OPOSLF11", "CMCFUP53", "MCDMA11X", "ADCAPE42", "HHASTL11", "CFNAMT53", "DVGWCP11", "AMEVA11", "CEXTM53", "HHTOTD11", "PMDLAY42", "VARSTR", "STPRAT11", "AMNURS11", "DVTOPR11", "CBCKYR53", "TOTPTR11", "LEUKAGED", "ADEZUN42", "OPAMA11", "BLIND42", "OBEOPR11", "PHNREG42", "OBOOTH11", "OBNMCD11", "AMASLF11", "PAYVAC53", "RURSLT42", "OPBSE11", "TRANS42", "ADLHLP53", "MCS42", "HPDMY11", "OBESLF11", "ZIFOFD11", "TRICH11X", "NOINSTM", "STAFE11", "CEXTMT53", "CHDDX", "VISPTR11", "STOMCH53", "AMCOSR11", "HHNPRV11", "WLKDIF31", "COLOREMS", "AMNMCD11", "SKNMREMS", "MOMPRO42", "STPRAT53", "CHNDCR42", "OPTSTL11", "BLDRAGED", "MCRPHO42", "VISVA11", "OPVVA11", "DVOOFD11", "DAPID31X", "AMAOPR11", "OPDWCP11", "CFNDBT53", "MCRPHO31", "HONRDC42", "DDNWRK53", "DFTOUS42", "OPBMA11", "MNHLTH53", "RESP42", "MCRMA11X", "ESPHREMS", "MCDOC11", "PEGFE11", "PRSFE11", "PRSOC11", "KNOWDR42", "PANEL", "CHGJ3142", "MCDFE11X", "YNOUSC42", "HHAVA11", "OBEVA11", "ENDRFY31", "OTHINS42", "CAMUSCLE", "RURSLT53", "TRSTP11X", "PAPSMR53", "PEGDE11", "WHNSMK42", "BOOST42", "TOTSLF11", "MCRAP11", "HRHOW42", "PNGNO11", "CPTASK53", "SSCIMP11", "HHAPTR11", "ACCELI42", "OBVOPU11", "CNGFXL53", "EVRUNINS", "INDCAT31", "HPSMA11", "PRIJU11", "PRIV42", "LIVRAGED", "TRIST11X", "ZIDSTL11", "MCDAT53X", "OBNURS11", "ERTMCD11", "STNDIF53", "AMTSLF11", "TSTSAGED", "MCDMC11", "PAYVAC31", "INS11X", "OBDOSR11", "PDKAP11", "OBVMCR11", "NOGODR42", "AMAOPU11", "OBNOPR11", "TOTTRI11", "TRICH42X", "PACISP42", "FTSTU11X", "AMNPRV11", "OPFPTR11", "COTARR53", "OPDOPR11", "CNGPOG53", "ZIFPTR11", "ENGSPK42", "ZIDVA11", "HPDJL11", "HHNVA11", "MORJOB53", "RTHLTH31", "OTHOTH11", "CHRTWW42", "PMNCNP11", "NATAMP42", "HPSJA11", "HHNPTR11", "PENSP11X", "BSTSRE53", "POGDE11", "INS42X", "CHOIC31", "OPAFE11", "OBTOSR11", "ERTSTL11", "OPOTRI11", "HSELIM53", "WKINBD31", "ASATAK31", "CCNGFT53", "PMDLRS42", "CHCOUN42", "OPOOPU11", "OBTSTL11", "TRICR42X", "OTPAAT42", "CHSRCN42", "ZIFMCR11", "OBEOTH11", "AMETCH11", "OBTTCH11", "TTLP11X", "RETPLN53", "CCNGPT53", "ADRTWW42", "WCPIMP11", "OTPUBA31", "IPDSTL11", "HHNSLF11", "JOBORG42", "OPVOPR11", "OBETCH11", "INSNO11X", "DNUNRS42", "OPDSLF11", "MCRPD31X", "CDRET53", "CEFOPN53", "NWK42", "BENDIF31", "ADHOPE42", "CEXTDI53", "OTPBAT11", "TRIAT11X", "CFMUOG53", "CCNRDI53", "PUBJU11X", "CMTASK53", "OPPTCH11", "DVTVA11", "PUBP11X", "VISPRV11", "OPVSTL11", "OBAWCP11", "HPRAU11", "STRKDX", "OBTEXP11", "AMASTL11", "PUBOC11X", "CHEYRE42", "CFNUNB53", "PNGOC11", "YNOINS53", "HOUR53", "REFDP11X", "OPDOFD11", "HPEMY11", "OBOMCR11", "DPOTSD11", "WHNLAP42", "CEFSTG53", "HISPANX", "CAPROSTA", "OBATCH11", "IPDTCH11", "OBAVA11", "ERTTCH11", "TRIAT53X", "RACEWX", "OBNMCR11", "BPMONT53", "DSCB1053", "PBPWKM42", "CNGLDL53", "ENDRFM53", "CNPTDI53", "MCDMC42", "RULETR11", "OPSVA11", "CHSERV42", "PRVMNC42", "RUSIZE53", "ADSAD42", "OBDOTH11", "OPFTRI11", "ENDRFM31", "PAYDR31", "ADNSMK42", "OTPUBB42", "VISOSR11", "OBNEXP11", "MCRJA11", "IPTSTL11", "TOTWCP11", "ERDSLF11", "POGFE11", "CMNLNG53", "ADCMPM42", "HPEFE11", "OPVOSR11", "RFREL42X", "PNGSE11", "BSNTY42", "CFMTOF53", "JTPAIN53", "MCRAU11", "OBTPTR11", "STJBMM42", "OPOOSR11", "OTHEXP11", "HRWGIM31", "ADNERV42", "HIEUIDX", "DSFT1153", "ADINSB42", "TRIEV11", "RULETR42", "CINREF53", "ACTLIM53", "STAMA11", "DSCPCP53", "OBTTRI11", "ADNDCR42", "SSECP11X", "AMEOFD11", "HONRDC53", "OTHDYS53", "ZIFSTL11", "ZIDTRI11", "APRDLM42", "ERTVA11", "STPDIF31", "HPRAP11", "SCLNBD53", "OBEOFD11", "CNGLOG53", "HPOJU11", "OBDMCD11", "OPFOSR11", "ARTHDX", "CLMHIP11", "DDBDYS31", "COGLIM31", "POUJU11", "AMTPTR11", "FSAGT31", "VISOPU11", "NOREAS42", "PMEDPY31", "JOBRSN42", "EICRDT11", "OPOSTL11", "ELGRND42", "AMNTRI11", "ADCLIM42", "OFFHOU42", "IPDWCP11", "CFM2MT53", "CEFRSP53", "PMEDPY53", "BSNTY31", "AMCOPU11", "FAMSZE42", "OBAEXP11", "ADHECR42", "DENTIN42", "CMNPLC53", "PUBNO11X", "INSCOP53", "OBOOFD11", "OBOTRI11", "PRVHMO42", "OTPUBB11", "CHHECR42", "HIDEG", "NEWDOC42", "MSA31", "HAVEUS42", "MCRFE11X", "IPNGTD11", "ASTHEP31", "OBDOFD11", "IADLHP42", "RESP31", "PHMONP11", "PRIS11", "CHPMHB42", "OPPEXP11", "MCAID11", "ERTOPU11", "IPDOFD11", "DEPDNT11", "PBSVCM42", "PRIDK42", "MOUTAGED", "BSNTY53", "OPOPRV11", "UNION53", "OTPBAT31", "INSENDYY", "OBOOSR11", "ADCMPD42", "CAOTHER", "OBOEXP11", "MCRPB31", "MCRAP11X", "TEMPJB42", "HELD31X", "PRSJL11", "AMAEXP11", "OBDWCP11", "TOTMCR11", "AMCHIR11", "INSCOP31", "VISEXP11", "CNGFXM53", "PHQ242", "COVRYY", "DIFFWG42", "CINDND53", "CFMFTP53", "HOMEBH42", "HPDJU11", "MCDSE11", "RTHLTH42", "TRIPR11X", "MCRPD42X", "OBOPRV11", "DVTPRV11", "STAOC11", "ASTHDX", "CHPMCN42", "OPBNO11", "OBCHIR11", "OPFWCP11", "OBCEXP11", "SPOUIN11", "OBDTRI11", "SICPAY42", "PCS42", "POGJA11", "ENDRFM42", "AMAVA11", "BUSIMP11", "ZIDSLF11", "THYRREMS", "CEXTOG53", "WRGLAS42", "IPFTCH11", "INSFE11X", "SCHLIM31", "TRIAT42X", "ENDRFY42", "RUCLAS11", "AMATRI11", "FAMSZE31", "IPDSLF11", "INDCAT42", "AMTOFD11", "HHNSTL11", "MCRMY11", "MCDJA11", "NUMEMP42", "NOLIKE42", "RXVA11", "POUDE11", "OPBAP11", "OPVWCP11", "ELGRND11", "OBTOPR11", "MCRSE11X", "HSPLAP42", "DSFT1053", "VISOPR11", "IPTSLF11", "STJBYY42", "CFMEM53", "WASCHAMP", "ZIDMCD11", "CEFACT53", "OVRYREMS", "POUNO11", "ERFTRI11", "OTHREA42", "SPOUID31", "HOUR31", "INSC1231", "OBNPRV11", "INSDE11X", "MELAAGED", "DVOOSR11", "ADFFRM42", "HEARDI42", "AMETRI11", "OTPAAT31", "PANCAGED", "AMCTCH11", "OBNOPU11", "ANGIDX", "PERSLA42", "ANYLIM11", "PMEDPP53", "FILER11", "MCROC11", "REFPRS11", "ERFOPU11", "OTHNDD31", "CSTSVM42", "OPSOPU11", "DVOPRV11", "ERFOTH11", "TSTSREMS", "ZIFOPR11", "IADL3M31", "VISION42", "OPSPRV11", "HPEOC11", "THYRAGED", "FNGRDF53", "ESPHAGED", "HPNJL11", "RTPLNM42", "AMAPTR11", "PRIDK11", "MCARE42X", "VISMCD11", "CFRET53", "OTHDYS31", "SELFCM42", "HIBPAGED", "DVGEN11", "UNABLE53", "DVGOTH11", "CFMEXT53", "PRIJL11", "PMDLPR42", "ZIDTCH11", "CARECTUM", "WHNEAT42", "OPFMCD11", "WHNWGT42", "AMNVA11", "HHAWCP11", "ASTHAGED", "ERFWCP11", "OTHMCR11", "RUSIZE11", "NOFAT53", "UNEIMP11", "OPFMCR11", "PUBSE11X", "PUBJA11X", "OBVWCP11", "POUAP11", "IPDPTR11", "STPRAT31", "WASSTAT1", "OBAOPU11", "OBCMCR11", "CNGFXT53", "HRWG53X", "HPSMY11", "OTHSLF11", "ADHDADDX", "SCHLIM53", "OBOOPR11", "HPEDE11", "OTHOFD11", "HHAEXP11", "HRHOW31", "CWRKEF53", "WASMCARE", "MCRJA11X", "ADL3MO53", "OPPPRV11", "MDDLRS42", "PUB11X", "ZIFVA11", "CEFASK53", "DENTAL42", "DSCPHN53", "MILDIF31", "ADRISK42", "TIMALN42", "ASMRCN53", "POGMY11", "OPOMCR11", "ZIDPRV11", "IPDTRI11", "OTHOSR11", "BENDIF53", "REFPRS53", "OBNOSR11", "AMAOFD11", "HPRMA11", "REFFRL42", "DOBMM", "DISVW53X", "CCLHIN53", "DVTOT11"]
# feature_dict["H147"]  = ["ANESTH", "ANYOPER", "DLVRTYPE", "DSCHPMED", "EEG", "EKG", "EPIDURAL", "ERCCC3X", "ERDATEYR", "ERDMD11X", "ERDMR11X", "ERDOR11X", "ERDOT11X", "ERDOU11X", "ERDPV11X", "ERDSF11X", "ERDSL11X", "ERDTC11X", "ERDTR11X", "ERDVA11X", "ERDXP11X", "ERFMD11X", "ERFMR11X", "ERFOF11X", "ERFOR11X", "ERFOT11X", "ERFOU11X", "ERFPV11X", "ERFSF11X", "ERFSL11X", "ERFTC11X", "ERFTR11X", "ERFVA11X", "ERFWC11X", "ERFXP11X", "ERHEVIDX", "ERICD1X", "ERICD2X", "ERICD3X", "ERPRO1X", "ERTC11X", "ERXP11X", "FFEEIDX", "FFERTYPE", "FFIPTYPE", "IMPFLAG", "IPBEGMM", "IPBEGYR", "IPCCC1X", "IPCCC2X", "IPCCC3X", "IPCCC4X", "IPDMD11X", "IPDMR11X", "IPDOR11X", "IPDOT11X", "IPDOU11X", "IPDPV11X", "IPDSF11X", "IPDSL11X", "IPDTC11X", "IPDTR11X", "IPDVA11X", "IPDWC11X", "IPDXP11X", "IPENDDD", "IPENDMM", "IPENDYR", "IPFMD11X", "IPFMR11X", "IPFOR11X", "IPFOT11X", "IPFOU11X", "IPFPV11X", "IPFSF11X", "IPFSL11X", "IPFTC11X", "IPFTR11X", "IPFVA11X", "IPFXP11X", "IPICD2X", "IPICD3X", "IPICD4X", "IPPRO1X", "IPTC11X", "IPXP11X", "LABTEST", "MAMMOG", "MEDPRESC", "MRI", "NUMNIGHT", "NUMNIGHX", "OTHSVCE", "PERWT11F", "PHARTP2", "PHARTP4", "PHARTP7", "PHARTP8", "PID", "PREGCAT", "RCVVAC", "RSNINHOS", "RXCCC1X", "RXCCC3X", "RXMD11X", "RXQUANTY", "RXRECIDX", "RXSF11X", "RXXP11X", "SEEDOC", "SONOGRAM", "SPECCOND", "SURGPROC", "TC1", "TC1S1", "TC1S1_1", "TC2", "TC2S1_1", "THRTSWAB", "VARSTR", "VSTCTGRY", "VSTRELCN", "XRAYS"]
