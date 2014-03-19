#DESC	1.2 * DESCRIPTOR INFORMATION ***********************
*
*	Dataset Type and Format:
*
DSRC	EXP
BSEQ	BIG
IKKF	REAL
XTYP	IDX
YTYP	IGD
ZTYP	NODATA
*
*	Item Formats:
*
IRFMT	D
YFMT	D
*
*	Data Ranges and Resolutions:
*
XPTS	1024
XMIN	3270.000000
XWID	100.000000
YPTS	10
YMIN	0.000000
YWID	925.947000
*
*	Documentational Text:
*
TITL	'tempol0.1mM_n10'
IRNAM	'Intensity'
XNAM	'Field'
YNAM	'Time'
IRUNI	''
XUNI	'G'
YUNI	's'
*
************************************************************
*
#SPL	1.2 * STANDARD PARAMETER LAYER
*
OPER    xuser
DATE    02/25/14
TIME    16:06:38
CMNT    
SAMP    Lipc v vakumu
SFOR    
STAG    C
EXPT    CW
OXS1    IADC
AXS1    B0VL
AXS2    ETIM
AXS3    
A2RS    10
A1CT    0.332
A1SW    0.01
MWFQ    9.334584e+09
MWPW    0.02007
AVGS    1
RESO    shqew10440o
SPTP    0.08192
RCAG    60
RCHM    1
B0MA    0.0001
B0MF    100000
RCPH    0.0
RCOF    0.0
A1RS    1024
RCTC    0.04096
*
************************************************************
*
#DSL	1.0 * DEVICE SPECIFIC LAYER
*

.DVC     acqStart, 1.0


.DVC     delay, 1.0

Delay              6000 ms
NbPoints           10

.DVC     fieldCtrl, 1.0

CenterField        3320.00 G
Delay              0.0 s
FieldFlyback       On
FieldWait          Wait LED off
GFactor            2.000000
SetToSampleG       False
SweepDirection     Up
SweepWidth         100.0 G

.DVC     fieldSweep, 1.0


.DVC     freqCounter, 1.0

FrequencyMon       9.334584 GHz
QMonitBridge       On

.DVC     mwBridge, 1.0

AcqFineTuning      Each Slice Scan
Power              20.07 mW
PowerAtten         10 dB

.DVC     recorder, 1.0

BaselineCorr       Off
NbScansAcc         1
NbScansDone        1
NbScansToDo        1
ReplaceMode        Off

.DVC     scanEnd, 1.0


.DVC     signalChannel, 1.0

AFCTrap            True
Calibrated         True
ConvTime           81.92 ms
DModAFCTrap        True
DModAmp            1.00 G
DModCalibrated     True
DModDetectSCT      First
DModEliDelay       1.0 us
DModExtLockIn      False
DModExtTrigger     False
DModFieldMod       First
DModGain           60 dB
DModHighPass       True
DModIntegrator     True
DModModOutput      Internal
DModSignalInput    Internal
DModTimeConst      1.28 ms
DoubleModFreq      5.00 kHz
DoubleModPhase     0.0
DoubleMode         False
EliDelay           1.0 us
ExtLockIn          False
ExtTrigger         False
Gain               60 dB
Harmonic           1
HighPass           True
Integrator         True
ModAmp             1.00 G
ModFreq            100.00 kHz
ModInput           Internal
ModOutput          Internal
ModPhase           0.0
Offset             0.0 %
QuadMode           False
QuadPhase          90.0
Resolution         1024
Resonator          1
SctNorm            False
SctRevision        DSC2
SignalInput        Internal
SweepTime          83.89 s
TimeConst          40.96 ms
TuneCaps           36

*
************************************************************
