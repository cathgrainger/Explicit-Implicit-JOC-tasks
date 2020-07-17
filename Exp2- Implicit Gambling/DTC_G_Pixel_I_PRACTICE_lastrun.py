#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), January 26, 2018, at 11:17
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Uncertainty MonitoingTask_Pixel_Implicit'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], "Pixel Implicit", expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\tmn\\Dropbox\\Dual TOM tasks\\DTC\\G\\I\\DTC_G_Pixel_I_PRACTICE.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1200), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Please click the mouse to begin....',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()

ONE=100
TWO=100

from psychopy.visual import GratingStim
import numpy as np

myTex = np.random.random( (ONE,ONE,4) )

myTex2 = np.random.random( (TWO,TWO,4) )

num_correct_discriminations= 0
num_incorrect_discriminations= 0
prop_correct_discriminations=0
prop_incorrect_discriminations=0
num_missed_discriminations= 0
prop_missed_discriminations=0
trial_total= 0
trial_performance= ""
ObjectLevelForGamma=999

Score=  2.00
Score1= 'Prize:  '
Score3= u"\u00A3"
DecimalScore= '{0:.2f}'.format(Score)
Score2= Score1 + Score3+str(DecimalScore)
image_correct= ""

t=0
t2=int(t)
t3=4-t2

SCORE= ""
colour_feedback=""
clickTime= 9999

runorskip=0
clicked=0

text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='default text',    font='Arial',
    pos=[0.80, -0.9], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
grating = visual.GratingStim(win=win, name='grating',
    tex=myTex, mask=None,
    ori=0, pos=[-0.3, 0], size=[0.3, 0.3], sf=None, phase=1,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=256, interpolate=False, depth=-3.0)
grating_2 = visual.GratingStim(win=win, name='grating_2',
    tex=myTex2, mask=None,
    ori=0, pos=[0.3, 0], size=[0.3, 0.3], sf=None, phase=1,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=256, interpolate=False, depth=-4.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='default text',    font='Arial',
    pos=[0.9, 0.9], height=0.05, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-5.0)
polygon_9 = visual.Rect(win=win, name='polygon_9',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-0.3, 0],
    lineWidth=4, lineColor=1.0, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
polygon_10 = visual.Rect(win=win, name='polygon_10',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.3, 0],
    lineWidth=4, lineColor=1.0, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)

# Initialize components for Routine "explicit"
explicitClock = core.Clock()
polygon_6 = visual.ShapeStim(win=win, name='polygon_6',
    vertices = [[-[0.25, 0.25][0]/2.0,-[0.25, 0.25][1]/2.0], [+[0.25, 0.25][0]/2.0,-[0.25, 0.25][1]/2.0], [0,[0.25, 0.25][1]/2.0]],
    ori=0, pos=[-0.3,  0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
polygon_7 = visual.Polygon(win=win, name='polygon_7',
    edges = 100, size=[0.25, 0.25],
    ori=0, pos=[0.3, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]


MetacognitiveChoice= ""
MetacognitieAccuuracy=""
score_feedback= ""
feedback_colour= [1,1,1]
MetaforGamma=999

numHighRisk=0
numLowRisk=0
DiffHighRisk=[]
DiffLowRisk=[]


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[-0.1, 0.1], size=[0.25, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='default text',    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='End of part 1\n\nAsk experimenter for instructions of part 2\n\npress space to continue',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "sound_alone"
sound_aloneClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instructions_3"
instructions_3Clock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='End of part 2\n\nAsk experimenter for instructions for part 3\n\npress space to continue',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()

ONE=100
TWO=100

from psychopy.visual import GratingStim
import numpy as np

myTex = np.random.random( (ONE,ONE,4) )

myTex2 = np.random.random( (TWO,TWO,4) )

num_correct_discriminations= 0
num_incorrect_discriminations= 0
prop_correct_discriminations=0
prop_incorrect_discriminations=0
num_missed_discriminations= 0
prop_missed_discriminations=0
trial_total= 0
trial_performance= ""
ObjectLevelForGamma=999

Score=  2.00
Score1= 'Prize:  '
Score3= u"\u00A3"
DecimalScore= '{0:.2f}'.format(Score)
Score2= Score1 + Score3+str(DecimalScore)
image_correct= ""

t=0
t2=int(t)
t3=4-t2

SCORE= ""
colour_feedback=""
clickTime= 9999

runorskip=0
clicked=0

#import the shuffle routine
from random import shuffle

#At the end of this routine, kick off a new clock
timerClock = core.Clock()

#Set up the sounds and parameters
all_sounds = [
{"id_num":"1","path":"Appalled_1.wav","duration":6,},
{"id_num":"2","path":"Appealing_1.wav","duration":5,},
{"id_num":"3","path":"Confronted_2.wav","duration":5,},
{"id_num":"4","path":"Distaste_1.wav","duration":6,},
{"id_num":"5","path":"Empathic_2.wav","duration":6,},
{"id_num":"6","path":"Exonerated_2.wav","duration":6,},
{"id_num":"7","path":"Grave_1.wav","duration":6,},
{"id_num":"8","path":"Guarded_3.wav","duration":6,},
{"id_num":"9","path":"Insincere_3.wav","duration":6,},
{"id_num":"10","path":"Intimate_1.wav","duration":6,}
]

sound_phase_complete = False

#Start sound item for movie at couner 1 to help create data headings
sound_counter = 1
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='default text',    font='Arial',
    pos=[0.80, -0.9], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
grating_3 = visual.GratingStim(win=win, name='grating_3',
    tex=myTex, mask=None,
    ori=0, pos=[-0.3, 0], size=[0.3, 0.3], sf=None, phase=1,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=256, interpolate=False, depth=-3.0)
grating_4 = visual.GratingStim(win=win, name='grating_4',
    tex=myTex2, mask=None,
    ori=0, pos=[0.3, 0], size=[0.3, 0.3], sf=None, phase=1,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=256, interpolate=False, depth=-4.0)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='default text',    font='Arial',
    pos=[0.9, 0.9], height=0.05, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-5.0)
polygon = visual.Rect(win=win, name='polygon',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-0.3, 0],
    lineWidth=4, lineColor=1.0, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
polygon_11 = visual.Rect(win=win, name='polygon_11',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.3, 0],
    lineWidth=4, lineColor=1.0, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)

# Initialize components for Routine "explicit2"
explicit2Clock = core.Clock()
polygon_8 = visual.ShapeStim(win=win, name='polygon_8',
    vertices = [[-[0.25, 0.25][0]/2.0,-[0.25, 0.25][1]/2.0], [+[0.25, 0.25][0]/2.0,-[0.25, 0.25][1]/2.0], [0,[0.25, 0.25][1]/2.0]],
    ori=0, pos=[-0.3,  0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
polygon_12 = visual.Polygon(win=win, name='polygon_12',
    edges = 100, size=[0.25, 0.25],
    ori=0, pos=[0.3, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]


MetacognitiveChoice= ""
MetacognitieAccuuracy=""
score_feedback= ""
feedback_colour= [1,1,1]
MetaforGamma=999

numHighRisk=0
numLowRisk=0
DiffHighRisk=[]
DiffLowRisk=[]

clickTime2=""

# Initialize components for Routine "feedback2"
feedback2Clock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[-0.1, 0.1], size=[0.25, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='default text',    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "bridge"
bridgeClock = core.Clock()
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text='End of practice',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
# keep track of which components have finished
IntroComponents = []
IntroComponents.append(text)
IntroComponents.append(mouse_2)
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    # *mouse_2* updates
    if t >= 0.0 and mouse_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse_2.tStart = t  # underestimates by a little under one frame
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.status = STARTED
        event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
    if mouse_2.status == STARTED:  # only update if started and not stopped!
        buttons = mouse_2.getPressed()
        if sum(buttons) > 0:  # ie if any button is pressed
            # abort routine on response
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Pause"-------
t = 0
PauseClock.reset()  # clock 
frameN = -1
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
PauseComponents = []
PauseComponents.append(text_2)
for thisComponent in PauseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Pause"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PauseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Pause"-------
for thisComponent in PauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PixelParameters_Practisexlsx.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    
    myTex = np.random.random( (ONE,ONE,4) )
    
    myTex2 = np.random.random( (TWO,TWO,4) )
    
    
    colour1= colour_initial
    colour2= colour_initial
    
    clickTime= 9999
    box_selected= ("")
    
    runorskip=0
    clicked=0
    ObjectforGamma=999
    text_3.setText( Score2)
    # setup some python lists for storing info about the mouse
    grating.setTex(myTex)
    grating_2.setTex(myTex2)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(text_3)
    trialComponents.append(mouse)
    trialComponents.append(grating)
    trialComponents.append(grating_2)
    trialComponents.append(text_4)
    trialComponents.append(polygon_9)
    trialComponents.append(polygon_10)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t2=int(t)
        t3=4-t2
        
        if mouse.isPressedIn(grating):
                    colour1= colour_selected
                    box_selected= "ONE"
                    clickTime= trialClock.getTime()
                    clicked=1
        
        if mouse.isPressedIn(grating_2):
                    box_selected= "TWO"
                    colour2= colour_selected
                    clickTime= trialClock.getTime()
                    clicked=1
        
        timer=clickTime+1.5
        
        if t > timer:
            continueRoutine= False
        
        # *text_3* updates
        if t >= 1 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        if text_3.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *grating* updates
        if t >= 1 and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        if grating.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        
        # *grating_2* updates
        if t >= 1 and grating_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_2.tStart = t  # underestimates by a little under one frame
            grating_2.frameNStart = frameN  # exact frame index
            grating_2.setAutoDraw(True)
        if grating_2.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_2.setAutoDraw(False)
        
        # *text_4* updates
        if t >= 1 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        if text_4.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        if text_4.status == STARTED:  # only update if being drawn
            text_4.setText(t3, log=False)
        
        # *polygon_9* updates
        if t >= 1 and polygon_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_9.tStart = t  # underestimates by a little under one frame
            polygon_9.frameNStart = frameN  # exact frame index
            polygon_9.setAutoDraw(True)
        if polygon_9.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            polygon_9.setAutoDraw(False)
        if polygon_9.status == STARTED:  # only update if being drawn
            polygon_9.setLineColor(colour1, log=False)
        
        # *polygon_10* updates
        if t >= 1 and polygon_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_10.tStart = t  # underestimates by a little under one frame
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.setAutoDraw(True)
        if polygon_10.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            polygon_10.setAutoDraw(False)
        if polygon_10.status == STARTED:  # only update if being drawn
            polygon_10.setLineColor(colour2, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if box_selected== correct:
        trial_performance= "Correct"
        ObjectLevelForGamma=1
        num_correct_discriminations= num_correct_discriminations+1
        trial_total= trial_total+1
        image_correct= "correct.png"
        runorskip=1
    
    if box_selected!= correct and clicked==0:
        trial_performance= "Missed"
        num_missed_discriminations= num_missed_discriminations+1
        trial_total= trial_total+1
        image_correct= "incorrect.png"
        Score=Score-0.30
        score_feedback= "-30p"
        feedback_colour= [1,-1,-1]
    
    if box_selected!= correct and clicked==1:
        trial_performance= "Incorrect"
        ObjectLevelForGamma=0
        num_incorrect_discriminations= num_incorrect_discriminations +1
        trial_total= trial_total+1
        image_correct= "incorrect.png"
        runorskip=1
    
    prop_correct_discriminations= num_correct_discriminations/trial_total
    prop_incorrect_discriminations= num_incorrect_discriminations/trial_total
    
    thisExp.addData('box_selected',box_selected)
    thisExp.addData('trial_total',trial_total)
    thisExp.addData('trial_performance',trial_performance)
    thisExp.addData('num_correct_discriminations',num_correct_discriminations)
    thisExp.addData('num_incorrect_discriminations',num_incorrect_discriminations)
    thisExp.addData('num_missed_discriminations', num_missed_discriminations)
    thisExp.addData('prop_correct_discriminations',prop_correct_discriminations)
    thisExp.addData('prop_incorrect_discriminations',prop_incorrect_discriminations)
    
    DecimalScore= '{0:.2f}'.format(Score)
    Score2= Score1 + Score3+str(DecimalScore)
    
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    trials.addData('mouse.leftButton', buttons[0])
    trials.addData('mouse.midButton', buttons[1])
    trials.addData('mouse.rightButton', buttons[2])
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=runorskip, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        #------Prepare to start Routine "explicit"-------
        t = 0
        explicitClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_3
        MetacognitiveChoice= ""
        MetacognitieAccuuracy=""
        score_feedback= ""
        MetaforGamma=999
        # keep track of which components have finished
        explicitComponents = []
        explicitComponents.append(polygon_6)
        explicitComponents.append(polygon_7)
        explicitComponents.append(mouse_3)
        for thisComponent in explicitComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "explicit"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = explicitClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_6* updates
            if t >= 0.0 and polygon_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_6.tStart = t  # underestimates by a little under one frame
                polygon_6.frameNStart = frameN  # exact frame index
                polygon_6.setAutoDraw(True)
            if polygon_6.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                polygon_6.setAutoDraw(False)
            
            # *polygon_7* updates
            if t >= 0.0 and polygon_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_7.tStart = t  # underestimates by a little under one frame
                polygon_7.frameNStart = frameN  # exact frame index
                polygon_7.setAutoDraw(True)
            if polygon_7.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                polygon_7.setAutoDraw(False)
            if mouse.isPressedIn(polygon_6):
                        continueRoutine=False
            
            elif mouse.isPressedIn(polygon_7):
                        continueRoutine=False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in explicitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "explicit"-------
        for thisComponent in explicitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_2 (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        trials_2.addData('mouse_3.x', x)
        trials_2.addData('mouse_3.y', y)
        trials_2.addData('mouse_3.leftButton', buttons[0])
        trials_2.addData('mouse_3.midButton', buttons[1])
        trials_2.addData('mouse_3.rightButton', buttons[2])
        if mouse.isPressedIn(polygon_6):
                    MetacognitiveChoice= "HighRisk"
                    MetaforGamma=1
                    numHighRisk=numHighRisk+1
                    DiffHighRisk.append(DIFFERENCE2)
        
        elif mouse.isPressedIn(polygon_7):
                    MetacognitiveChoice= "LowRisk"
                    MetaforGamma=0
                    numLowRisk=numLowRisk+1
                    DiffLowRisk.append(DIFFERENCE2)
        
        else:
                    MetacognitiveChoice= "Missed"
                    Score=Score-0.30
                    score_feedback= "-30p"
                    feedback_colour= [1,-1,-1]
                    image_correct= "incorrect.png"
        
        if MetacognitiveChoice== "HighRisk" and trial_performance== "Correct":
                    Score=Score+0.30
                    score_feedback= "+30p"
                    feedback_colour= [-1,1,-1]
        
        if MetacognitiveChoice== "LowRisk" and trial_performance== "Incorrect":
                    Score=Score-0.10
                    score_feedback= "-10p"
                    feedback_colour= [1,-1,-1]
        
        if MetacognitiveChoice== "HighRisk" and trial_performance== "Incorrect":
                    Score=Score-0.30
                    score_feedback= "-30p"
                    feedback_colour= [1,-1,-1]
        
        if MetacognitiveChoice== "LowRisk" and trial_performance== "Correct":
                    MetacognitieAccuuracy= "Inaccurate"
                    Score=Score+0.10
                    score_feedback= "+10p"
                    feedback_colour= [-1,1,-1]
        
        DecimalScore= '{0:.2f}'.format(Score)
        Score2= Score1 + Score3+str(DecimalScore)
        
        thisExp.addData('MetacognitiveChoice',MetacognitiveChoice)
        thisExp.addData('ObjectLevelForGamma',ObjectLevelForGamma)
        thisExp.addData('MetaforGamma',MetaforGamma)
        thisExp.addData('numHighRisk',numHighRisk)
        thisExp.addData('numLowRisk',numLowRisk)
        thisExp.addData('DiffHighRisk',DiffHighRisk)
        thisExp.addData('DiffLowRisk',DiffLowRisk)
        
        
        
    # completed runorskip repeats of 'trials_2'
    
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image.setImage(image_correct)
    text_9.setColor(feedback_colour, colorSpace='rgb')
    text_9.setText(score_feedback)
    
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(image)
    feedbackComponents.append(text_9)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        
        # *text_9* updates
        if t >= 0.0 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        if text_9.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_9.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Score2',Score2)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "instructions_2"-------
t = 0
instructions_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructions_2Components = []
instructions_2Components.append(text_5)
instructions_2Components.append(key_resp_2)
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_2"-------
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Practice_audio.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "sound_alone"-------
    t = 0
    sound_aloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    sound_1.setSound(audio, secs=6)
    # keep track of which components have finished
    sound_aloneComponents = []
    sound_aloneComponents.append(sound_1)
    sound_aloneComponents.append(text_6)
    for thisComponent in sound_aloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "sound_alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sound_aloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= 0.0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (0.0 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *text_6* updates
        if t >= 6 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        if text_6.status == STARTED and t >= (6 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_6.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_aloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "sound_alone"-------
    for thisComponent in sound_aloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


#------Prepare to start Routine "instructions_3"-------
t = 0
instructions_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instructions_3Components = []
instructions_3Components.append(text_7)
instructions_3Components.append(key_resp_3)
for thisComponent in instructions_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_3"-------
for thisComponent in instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PixelParameters_Practisexlsx.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5.keys():
        exec(paramName + '= thisTrial_5.' + paramName)

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5.keys():
            exec(paramName + '= thisTrial_5.' + paramName)
    
    #------Prepare to start Routine "trial2"-------
    t = 0
    trial2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    
    myTex = np.random.random( (ONE,ONE,4) )
    
    myTex2 = np.random.random( (TWO,TWO,4) )
    
    
    colour1= colour_initial
    colour2= colour_initial
    
    clickTime= 9999
    box_selected= ("")
    soundclick1= 9999
    soundTime1=9999
    
    runorskip=0
    clicked=0
    
    
    SoundTime=trialClock.getTime()
    
    ObjectForGamma=999
    MetaForGamma=999
    
    #Shuffle the sounds
    shuffle(all_sounds)
    
    #Top slice 10 sounds and remove from old array
    #current_slice = all_sounds[0:1]
    #del all_sounds[0:1]
    
    #Initialize flag to say we are not playing and no text
    
    text_phase = False
    
    #else:
        #Set a flag to say we are not going to do this routine
        #See "Each Frame" for it in action.
    #    doRoutine = False
    text_8.setText( Score2)
    # setup some python lists for storing info about the mouse_4
    grating_3.setTex(myTex)
    grating_4.setTex(myTex2)
    # keep track of which components have finished
    trial2Components = []
    trial2Components.append(text_8)
    trial2Components.append(mouse_4)
    trial2Components.append(grating_3)
    trial2Components.append(grating_4)
    trial2Components.append(text_10)
    trial2Components.append(polygon)
    trial2Components.append(polygon_11)
    for thisComponent in trial2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t2=int(t)
        t3=4-t2
        
        if mouse.isPressedIn(grating):
                    colour1= colour_selected
                    box_selected= "ONE"
                    clickTime= trialClock.getTime()
                    clicked=1
        
        if mouse.isPressedIn(grating_2):
                    box_selected= "TWO"
                    colour2= colour_selected
                    clickTime= trialClock.getTime()
                    clicked=1
        
        timer=clickTime+1.5
        
        if t > timer:
            continueRoutine= False
        
        #Should we now play a sound and can we?
        if sound_phase_complete == False:
        
            if len(all_sounds) > 0:
                #Pop off one of the sounds (which removes it from the array)
                sound_item = all_sounds.pop()
        
                #Set up the sound
                playing_sound = sound.Sound(value=sound_item["path"])
        
                #Set up text on text objects, but not show yet
                #lefttext.text = sound_item["text1"]
                #righttext.text = sound_item["text2"]
        
                #Kick off the timer
                timerClock.reset()
                playing_sound.play()
                SoundTime=trialClock.getTime()
                sound_phase_complete = True
        
                #Store sound item sequence
                thisExp.addData('soundplaying', sound_item["path"])
                thisExp.addData('soundplaying_routine', "trial")
                thisExp.addData('SoundTime',SoundTime)
        
        elif sound_phase_complete == True:
        
            #If we are at 6 second duration or past, stop sound and show text
        
            if timerClock.getTime() >= 8:
                    playing_sound.stop()
                    #lefttext.color = [0,0,0]
                    #righttext.color = [0,0,0]
        
                    #Kick off the timer again
                    timerClock.reset()
        
                    #Reset flags
                    sound_phase_complete = False
                    text_phase = False
        
                    #Hide text objects
                    #lefttext.color = [0,0,0]
                    #righttext.color = [0,0,0]
        
                    #Increment counter
                    sound_counter += 1
        
        # *text_8* updates
        if t >= 1 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        if text_8.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_8.setAutoDraw(False)
        
        # *grating_3* updates
        if t >= 1 and grating_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_3.tStart = t  # underestimates by a little under one frame
            grating_3.frameNStart = frameN  # exact frame index
            grating_3.setAutoDraw(True)
        if grating_3.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_3.setAutoDraw(False)
        
        # *grating_4* updates
        if t >= 1 and grating_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_4.tStart = t  # underestimates by a little under one frame
            grating_4.frameNStart = frameN  # exact frame index
            grating_4.setAutoDraw(True)
        if grating_4.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_4.setAutoDraw(False)
        
        # *text_10* updates
        if t >= 1 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        if text_10.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)
        if text_10.status == STARTED:  # only update if being drawn
            text_10.setText(t3, log=False)
        
        # *polygon* updates
        if t >= 1 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t  # underestimates by a little under one frame
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        if polygon.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            polygon.setAutoDraw(False)
        if polygon.status == STARTED:  # only update if being drawn
            polygon.setLineColor(colour1, log=False)
        
        # *polygon_11* updates
        if t >= 1 and polygon_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_11.tStart = t  # underestimates by a little under one frame
            polygon_11.frameNStart = frameN  # exact frame index
            polygon_11.setAutoDraw(True)
        if polygon_11.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            polygon_11.setAutoDraw(False)
        if polygon_11.status == STARTED:  # only update if being drawn
            polygon_11.setLineColor(colour2, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if box_selected== correct:
        trial_performance= "Correct"
        ObjectLevelForGamma=1
        num_correct_discriminations= num_correct_discriminations+1
        trial_total= trial_total+1
        image_correct= "correct.png"
        runorskip=1
    
    if box_selected!= correct and clicked==0:
        trial_performance= "Missed"
        num_missed_discriminations= num_missed_discriminations+1
        trial_total= trial_total+1
        image_correct= "incorrect.png"
        Score=Score-0.30
        score_feedback= "-30p"
        feedback_colour= [1,-1,-1]
    
    if box_selected!= correct and clicked==1:
        trial_performance= "Incorrect"
        ObjectLevelForGamma=0
        num_incorrect_discriminations= num_incorrect_discriminations +1
        trial_total= trial_total+1
        image_correct= "incorrect.png"
        runorskip=1
    
    prop_correct_discriminations= num_correct_discriminations/trial_total
    prop_incorrect_discriminations= num_incorrect_discriminations/trial_total
    
    thisExp.addData('box_selected',box_selected)
    thisExp.addData('trial_total',trial_total)
    thisExp.addData('trial_performance',trial_performance)
    thisExp.addData('num_correct_discriminations',num_correct_discriminations)
    thisExp.addData('num_incorrect_discriminations',num_incorrect_discriminations)
    thisExp.addData('num_missed_discriminations', num_missed_discriminations)
    thisExp.addData('prop_correct_discriminations',prop_correct_discriminations)
    thisExp.addData('prop_incorrect_discriminations',prop_incorrect_discriminations)
    thisExp.addData('clicktime',clickTime)
    thisExp.addData('soundclick1',soundclick1)
    thisExp.addData('soundTime1',soundTime1)
    
    DecimalScore= '{0:.2f}'.format(Score)
    Score2= Score1 + Score3+str(DecimalScore)
    
    # store data for trials_5 (TrialHandler)
    x, y = mouse_4.getPos()
    buttons = mouse_4.getPressed()
    trials_5.addData('mouse_4.x', x)
    trials_5.addData('mouse_4.y', y)
    trials_5.addData('mouse_4.leftButton', buttons[0])
    trials_5.addData('mouse_4.midButton', buttons[1])
    trials_5.addData('mouse_4.rightButton', buttons[2])
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=runorskip, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4.keys():
                exec(paramName + '= thisTrial_4.' + paramName)
        
        #------Prepare to start Routine "explicit2"-------
        t = 0
        explicit2Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_5
        MetacognitiveChoice= ""
        MetacognitieAccuuracy=""
        score_feedback= ""
        MetaforGamma=999
        
        SoundTime=trialClock.getTime()
        soundclick2=""
        
        #Shuffle the sounds
        shuffle(all_sounds)
        
        #Top slice 10 sounds and remove from old array
        #current_slice = all_sounds[0:1]
        #del all_sounds[0:1]
        
        #Initialize flag to say we are not playing and no text
        
        text_phase = False
        
        #else:
            #Set a flag to say we are not going to do this routine
            #See "Each Frame" for it in action.
        #    doRoutine = False
        # keep track of which components have finished
        explicit2Components = []
        explicit2Components.append(polygon_8)
        explicit2Components.append(polygon_12)
        explicit2Components.append(mouse_5)
        for thisComponent in explicit2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "explicit2"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = explicit2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_8* updates
            if t >= 0.0 and polygon_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_8.tStart = t  # underestimates by a little under one frame
                polygon_8.frameNStart = frameN  # exact frame index
                polygon_8.setAutoDraw(True)
            if polygon_8.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                polygon_8.setAutoDraw(False)
            
            # *polygon_12* updates
            if t >= 0.0 and polygon_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_12.tStart = t  # underestimates by a little under one frame
                polygon_12.frameNStart = frameN  # exact frame index
                polygon_12.setAutoDraw(True)
            if polygon_12.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                polygon_12.setAutoDraw(False)
            if mouse.isPressedIn(polygon_6):
                        clickTime2= trialClock.getTime()
                        soundclick2=sound_item["path"]
                        soundTime2=timerClock.getTime()
                        continueRoutine=False
            
            elif mouse.isPressedIn(polygon_7):
                        clickTime2= trialClock.getTime()
                        soundclick2=sound_item["path"]
                        soundTime2=timerClock.getTime()
                        continueRoutine=False
            
            #Should we now play a sound and can we?
            if sound_phase_complete == False:
            
                if len(all_sounds) > 0:
                    #Pop off one of the sounds (which removes it from the array)
                    sound_item = all_sounds.pop()
            
                    #Set up the sound
                    playing_sound = sound.Sound(value=sound_item["path"])
            
                    #Set up text on text objects, but not show yet
                    #lefttext.text = sound_item["text1"]
                    #righttext.text = sound_item["text2"]
            
                    #Kick off the timer
                    timerClock.reset()
                    playing_sound.play()
                    SoundTime=trialClock.getTime()
                    sound_phase_complete = True
            
                    #Store sound item sequence
                    thisExp.addData('soundplaying', sound_item["path"])
                    thisExp.addData('soundplaying_routine', "explicit")
                    thisExp.addData('SoundTime',SoundTime)
            
            elif sound_phase_complete == True:
            
                #If we are at 6 second duration or past, stop sound and show text
            
                if timerClock.getTime() >= 8:
                        playing_sound.stop()
                        #lefttext.color = [0,0,0]
                        #righttext.color = [0,0,0]
            
                        #Kick off the timer again
                        timerClock.reset()
            
                        #Reset flags
                        sound_phase_complete = False
                        text_phase = False
            
                        #Hide text objects
                        #lefttext.color = [0,0,0]
                        #righttext.color = [0,0,0]
            
                        #Increment counter
                        sound_counter += 1
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in explicit2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "explicit2"-------
        for thisComponent in explicit2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_4 (TrialHandler)
        x, y = mouse_5.getPos()
        buttons = mouse_5.getPressed()
        trials_4.addData('mouse_5.x', x)
        trials_4.addData('mouse_5.y', y)
        trials_4.addData('mouse_5.leftButton', buttons[0])
        trials_4.addData('mouse_5.midButton', buttons[1])
        trials_4.addData('mouse_5.rightButton', buttons[2])
        if mouse.isPressedIn(polygon_6):
                    MetacognitiveChoice= "HighRisk"
                    MetaforGamma=1
                    numHighRisk=numHighRisk+1
                    DiffHighRisk.append(DIFFERENCE2)
        
        elif mouse.isPressedIn(polygon_7):
                    MetacognitiveChoice= "LowRisk"
                    MetaforGamma=0
                    numLowRisk=numLowRisk+1
                    DiffLowRisk.append(DIFFERENCE2)
        
        else:
                    MetacognitiveChoice= "Missed"
                    Score=Score-0.30
                    score_feedback= "-30p"
                    feedback_colour= [1,-1,-1]
                    image_correct= "incorrect.png"
        
        if MetacognitiveChoice== "HighRisk" and trial_performance== "Correct":
                    Score=Score+0.30
                    score_feedback= "+30p"
                    feedback_colour= [-1,1,-1]
        
        if MetacognitiveChoice== "LowRisk" and trial_performance== "Incorrect":
                    Score=Score-0.10
                    score_feedback= "-10p"
                    feedback_colour= [1,-1,-1]
        
        if MetacognitiveChoice== "HighRisk" and trial_performance== "Incorrect":
                    Score=Score-0.30
                    score_feedback= "-30p"
                    feedback_colour= [1,-1,-1]
        
        if MetacognitiveChoice== "LowRisk" and trial_performance== "Correct":
                    MetacognitieAccuuracy= "Inaccurate"
                    Score=Score+0.10
                    score_feedback= "+10p"
                    feedback_colour= [-1,1,-1]
        
        DecimalScore= '{0:.2f}'.format(Score)
        Score2= Score1 + Score3+str(DecimalScore)
        
        thisExp.addData('MetacognitiveChoice',MetacognitiveChoice)
        thisExp.addData('ObjectLevelForGamma',ObjectLevelForGamma)
        thisExp.addData('MetaforGamma',MetaforGamma)
        thisExp.addData('numHighRisk',numHighRisk)
        thisExp.addData('numLowRisk',numLowRisk)
        thisExp.addData('DiffHighRisk',DiffHighRisk)
        thisExp.addData('DiffLowRisk',DiffLowRisk)
        thisExp.addData('clickTime2',clickTime2)
        thisExp.addData('soundclick2',soundclick2)
        thisExp.addData('soundTime2',soundTime2)
        
        
        
    # completed runorskip repeats of 'trials_4'
    
    
    #------Prepare to start Routine "feedback2"-------
    t = 0
    feedback2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_2.setImage(image_correct)
    text_11.setColor(feedback_colour, colorSpace='rgb')
    text_11.setText(score_feedback)
    
    #Shuffle the sounds
    shuffle(all_sounds)
    
    #Top slice 10 sounds and remove from old array
    #current_slice = all_sounds[0:1]
    #del all_sounds[0:1]
    
    #Initialize flag to say we are not playing and no text
    
    text_phase = False
    
    #else:
        #Set a flag to say we are not going to do this routine
        #See "Each Frame" for it in action.
    #    doRoutine = False
    # keep track of which components have finished
    feedback2Components = []
    feedback2Components.append(image_2)
    feedback2Components.append(text_11)
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        if image_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_2.setAutoDraw(False)
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        if text_11.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_11.setAutoDraw(False)
        #Should we now play a sound and can we?
        if sound_phase_complete == False:
        
            if len(all_sounds) > 0:
                #Pop off one of the sounds (which removes it from the array)
                sound_item = all_sounds.pop()
        
                #Set up the sound
                playing_sound = sound.Sound(value=sound_item["path"])
        
                #Set up text on text objects, but not show yet
                #lefttext.text = sound_item["text1"]
                #righttext.text = sound_item["text2"]
        
                #Kick off the timer
                timerClock.reset()
                playing_sound.play()
                sound_phase_complete = True
        
                #Store sound item sequence
                thisExp.addData('soundplaying', sound_item["path"])
                thisExp.addData('soundplaying_routine', "feedback")
                thisExp.addData('SoundTime',SoundTime)
        
        elif sound_phase_complete == True:
        
            #If we are at 6 second duration or past, stop sound and show text
        
            if timerClock.getTime() >= 8:
                    playing_sound.stop()
                    #lefttext.color = [0,0,0]
                    #righttext.color = [0,0,0]
        
                    #Kick off the timer again
                    timerClock.reset()
        
                    #Reset flags
                    sound_phase_complete = False
                    text_phase = False
        
                    #Hide text objects
                    #lefttext.color = [0,0,0]
                    #righttext.color = [0,0,0]
        
                    #Increment counter
                    sound_counter += 1
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback2"-------
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Score2',Score2)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


#------Prepare to start Routine "bridge"-------
t = 0
bridgeClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
bridgeComponents = []
bridgeComponents.append(text_12)
for thisComponent in bridgeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "bridge"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = bridgeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # underestimates by a little under one frame
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    if text_12.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_12.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in bridgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "bridge"-------
for thisComponent in bridgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_13)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t  # underestimates by a little under one frame
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    if text_13.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_13.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


thisExp.saveAsWideText(thisExp.dataFileName+'.csv', delim= ',')




thisExp.saveAsWideText(thisExp.dataFileName+'.csv', delim= ',')


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
