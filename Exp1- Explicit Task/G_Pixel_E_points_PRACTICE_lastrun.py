#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), June 14, 2018, at 13:13
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
expName = 'Pixels points practice'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], "Pixel Explicit", expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\tmn\\Desktop\\ASD.KIDS\\G Tasks\\E\\G_Pixel_E_points_PRACTICE.psyexp',
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
ObjectforGamma=999

Score=  50
Score1= 'Points:  '
#Score3= u"\u00A3"
#DecimalScore= '{0:.2f}'.format(Score)
Score2= Score1 +str(Score)
image_correct= ""

SCORE= ""
colour_feedback=""
clickTime= 9999
clickTime2= 9999

runorskip=0
clicked=0

text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='default text',    font='Arial',
    pos=[0.80, -0.9], height=0.10, wrapWidth=None,
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
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='Are you confident ?',    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
polygon_6 = visual.Rect(win=win, name='polygon_6',
    width=[0.25, 0.25][0], height=[0.25, 0.25][1],
    ori=0, pos=[-0.2, -0.2],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
polygon_7 = visual.Rect(win=win, name='polygon_7',
    width=[0.25, 0.25][0], height=[0.25, 0.25][1],
    ori=0, pos=[0.2, -0.2],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='Yes',    font='Arial',
    pos=[-0.2, -0.2], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0)
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='No',    font='Arial',
    pos=[0.2, -0.2], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-4.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]


MetacognitiveChoice= ""
MetacognitieAccuuracy=""
score_feedback= ""
feedback_colour= [1,1,1]
MetaforGamma=999

numYes=0
numNo=0
DiffYes=[]
DiffNo=[]
clickTime2= 9999


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


# Initialize components for Routine "end"
endClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
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
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
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
                    mouse.time.append(trialClock.getTime())
                    endTrialTime= mouse.time[0]+1.5
                    clicked=1
        
        if mouse.isPressedIn(grating_2):
                    box_selected= "TWO"
                    colour2= colour_selected
                    clickTime= trialClock.getTime()
                    mouse.time.append(trialClock.getTime())
                    endTrialTime= mouse.time[0]+1.5
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
        # *mouse* updates
        if t >= 1 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t  # underestimates by a little under one frame
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            mouse.status = STOPPED
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(trialClock.getTime())
        
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
        ObjectforGamma=1
        num_correct_discriminations= num_correct_discriminations+1
        trial_total= trial_total+1
        image_correct= "correct.png"
        runorskip=1
    
    if box_selected!= correct and clicked==0:
        trial_performance= "Missed"
        num_missed_discriminations= num_missed_discriminations+1
        trial_total= trial_total+1
        image_correct= "incorrect.png"
        Score=Score-30
        score_feedback= "-30"
        feedback_colour= [1,-1,-1]
    
    if box_selected!= correct and clicked==1:
        trial_performance= "Incorrect"
        ObjectforGamma=0
        num_incorrect_discriminations= num_incorrect_discriminations +1
        trial_total= trial_total+1
        image_correct= "incorrect.png"
        runorskip=1
    
    
    #DecimalScore= '{0:.2f}'.format(Score)
    Score2= Score1 + str(Score)
    RT= clickTime - 1
    
    
    prop_correct_discriminations= num_correct_discriminations/trial_total
    prop_incorrect_discriminations= num_incorrect_discriminations/trial_total
    
    thisExp.addData('box_selected',box_selected)
    thisExp.addData('trial_total',trial_total)
    thisExp.addData('trial_performance',trial_performance)
    thisExp.addData('num_correct_discriminations',num_correct_discriminations)
    thisExp.addData('num_incorrect_discriminations',num_incorrect_discriminations)
    thisExp.addData('num_missed_discriminations',num_missed_discriminations)
    thisExp.addData('prop_correct_discriminations',prop_correct_discriminations)
    thisExp.addData('prop_incorrect_discriminations',prop_incorrect_discriminations)
    thisExp.addData('RT',RT)
    
    
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    
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
        explicitComponents.append(text_6)
        explicitComponents.append(polygon_6)
        explicitComponents.append(polygon_7)
        explicitComponents.append(text_7)
        explicitComponents.append(text_8)
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
            
            # *text_6* updates
            if t >= 0.0 and text_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_6.tStart = t  # underestimates by a little under one frame
                text_6.frameNStart = frameN  # exact frame index
                text_6.setAutoDraw(True)
            if text_6.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_6.setAutoDraw(False)
            
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
            
            # *text_7* updates
            if t >= 0.0 and text_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_7.tStart = t  # underestimates by a little under one frame
                text_7.frameNStart = frameN  # exact frame index
                text_7.setAutoDraw(True)
            if text_7.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_7.setAutoDraw(False)
            
            # *text_8* updates
            if t >= 0.0 and text_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_8.tStart = t  # underestimates by a little under one frame
                text_8.frameNStart = frameN  # exact frame index
                text_8.setAutoDraw(True)
            if text_8.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_8.setAutoDraw(False)
            if mouse.isPressedIn(polygon_6):
                        continueRoutine=False
                        clickTime2= trialClock.getTime()
            
            elif mouse.isPressedIn(polygon_7):
                        continueRoutine=False
                        clickTime2= trialClock.getTime()
            
            
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
                    MetacognitiveChoice= "Correct"
                    MetaforGamma=1
                    numYes=numYes+1
                    DiffYes.append(DIFFERENCE2)
        
        elif mouse.isPressedIn(polygon_7):
                    MetacognitiveChoice= "Incorrect"
                    MetaforGamma=0
                    numNo=numNo+1
                    DiffNo.append(DIFFERENCE2)
        
        else:
                    MetacognitiveChoice= "Missed"
                    Score=Score-30
                    score_feedback= "-30"
                    feedback_colour= [1,-1,-1]
                    image_correct= "incorrect.png"
        
        if MetacognitiveChoice== "Correct" and trial_performance== "Correct":
                    MetacognitieAccuuracy= "Accurate"
                    Score=Score+30
                    score_feedback= "+30"
                    feedback_colour= [-1,1,-1]
        
        if MetacognitiveChoice== "Incorrect" and trial_performance== "Incorrect":
                    MetacognitieAccuuracy= "Accurate"
                    Score=Score-10
                    score_feedback= "-10"
                    feedback_colour= [1,-1,-1]
        
        if MetacognitiveChoice== "Correct" and trial_performance== "Incorrect":
                    MetacognitieAccuuracy= "Inaccurate"
                    Score=Score-30
                    score_feedback= "-30"
                    feedback_colour= [1,-1,-1]
        
        if MetacognitiveChoice== "Incorrect" and trial_performance== "Correct":
                    MetacognitieAccuuracy= "Inaccurate"
                    Score=Score+10
                    score_feedback= "+10"
                    feedback_colour= [-1,1,-1]
        
        #DecimalScore= '{0:.2f}'.format(Score)
        Score2= Score1 + str(Score)
        RT2= clickTime2-endTrialTime
        
        
        thisExp.addData('MetacognitiveChoice',MetacognitiveChoice)
        thisExp.addData('MetacognitieAccuuracy',MetacognitieAccuuracy)
        thisExp.addData('ObjectforGamma',ObjectforGamma)
        thisExp.addData('MetaforGamma',MetaforGamma)
        thisExp.addData('numYes',numYes)
        thisExp.addData('numNo',numNo)
        thisExp.addData('DiffYes',DiffYes)
        thisExp.addData('DiffNo',DiffNo)
        thisExp.addData('RT2',RT2)
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

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_5)
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
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    if text_5.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_5.setAutoDraw(False)
    
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

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
