#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on november 03, 2020, at 11:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'nback_task_v1'  # from the Builder filename that created this script
expInfo = {'Azonosító': '', 'Születési dátum (ÉÉÉÉ.HH.NN.)': '', 'Nem': ['válassz', 'férfi', 'nő', 'egyéb'], 'Domináns kéz': ['válassz', 'jobb', 'bal']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Azonosító'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\_ALEX_\\_Munka\\afázia\\afázia_taskok\\n_back_task\\nback_task_v1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "hello"
helloClock = core.Clock()
# Online Python compiler (interpreter) to run Python online.
#Packages
import random as r

#Global vars
all_stimuli = ["B","C","D","F","G","H","J","K","L","M","N","P","Q", "R", "S", "T", "V", "W", "Y", "Z"]

PracticeTargetNum = 3
TargetNum = 10
PracticeFractals = 5
TrialFractals = 10
PracticeTrialNum = 18
TrialNum = 60
LevelNum = 2
BlokkNum = 2

#function
#diff_num is 2 for 1-back and 3 for 2-back
def ensure_hits (trial_num, targ_num, diff_num):
    list_ready = False
    hit_list = ["miss"] * (trial_num - targ_num)
    
    while list_ready == False:
        hit_indexes = r.sample(range(diff_num-1, trial_num), targ_num)
        hit_indexes.sort()
        errors = []
        for i,x in enumerate(hit_indexes):
            if i > 0:
                if (hit_indexes[i] - hit_indexes[i-1]) < diff_num:
                    errors.append("x")
        if len(errors) == 0:
            list_ready = True
    
    for ind in hit_indexes:
        hit_list.insert(ind, "hit")
        
    return hit_list

def make_block(which_level, blokk_stimuli, trial_num, targ_num):
    completed_blokk = []
    
    if which_level == 0:
        hit_vector = ensure_hits(trial_num, targ_num, 2)
        
        for trial in range(trial_num):
            stim_for_trial = blokk_stimuli[:]
            
            if hit_vector[trial] == "hit":
                trial_stim = completed_blokk[trial-1]
            else:
                if trial > 0:
                    stim_for_trial.remove(completed_blokk[trial-1])
                if trial > 1 and completed_blokk[trial-2] != completed_blokk[trial-1]:
                    stim_for_trial.remove(completed_blokk[trial-2])
                trial_stim = r.choice(stim_for_trial)
            
            completed_blokk.append(trial_stim)
    
    elif which_level == 1:
        hit_vector = ensure_hits(trial_num, targ_num, 3)

        for trial in range(trial_num):
            stim_for_trial = blokk_stimuli[:]
            
            if hit_vector[trial] == "hit":
                trial_stim = completed_blokk[trial-2]
            else:
                if trial > 0:
                    stim_for_trial.remove(completed_blokk[trial-1])
                if trial > 1:
                    stim_for_trial.remove(completed_blokk[trial-2])
                if trial > 2 and completed_blokk[trial-3] != completed_blokk[trial-1]:
                    stim_for_trial.remove(completed_blokk[trial-3])
                trial_stim = r.choice(stim_for_trial)
            
            completed_blokk.append(trial_stim)
    
    return completed_blokk

#Making blokks
all_blokks = []
for level in range(LevelNum):
    level_stimuli = all_stimuli[:]
    print(level_stimuli)
    completed_level = []
    for blokk in range(BlokkNum):
        blokk_stimuli = r.sample(level_stimuli, TrialFractals)
        for x in blokk_stimuli:
            level_stimuli.remove(x)
        print(blokk_stimuli)
        completed_blokk = make_block(level, blokk_stimuli, TrialNum, TargetNum)
        completed_level.append(completed_blokk)
    all_blokks.append(completed_level)
    
#making practice blokks
practice_blokks = []
for level_pract in range(LevelNum):
    level_stimuli_p = r.sample(all_stimuli, PracticeFractals)
    pract_block = make_block(level_pract, level_stimuli_p, PracticeTrialNum, PracticeTargetNum)
    practice_blokks.append(pract_block)


instr_instr = visual.TextStim(win=win, name='instr_instr',
    text='Köszöntjük a kísérletünkben!\n\n\nKérjük, hogy nyomjon SPACE gombot a kezdéshez!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_tovabb = keyboard.Keyboard()

# Initialize components for Routine "kezesseg"
kezessegClock = core.Clock()
kezesseg_instr = visual.TextStim(win=win, name='kezesseg_instr',
    text='Melyik kezét fogja használni a feladatban?\n\nAmennyiben lehetséges, használja a NEM-DOMINÁNS kezét.\n\nBal kéz: B gomb\nJobb kéz: J gomb',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kezesseg_resp = keyboard.Keyboard()

# Initialize components for Routine "level_instr"
level_instrClock = core.Clock()
lvl_instr = visual.TextStim(win=win, name='lvl_instr',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "pract_inst"
pract_instClock = core.Clock()
pract_inst_text = visual.TextStim(win=win, name='pract_inst_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
pract_inst_key = keyboard.Keyboard()

# Initialize components for Routine "practice_trial"
practice_trialClock = core.Clock()
pract_stim_frakt = visual.ImageStim(
    win=win,
    name='pract_stim_frakt', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
pract_resp = keyboard.Keyboard()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "repeatPractice"
repeatPracticeClock = core.Clock()
repeat_pract_text = visual.TextStim(win=win, name='repeat_pract_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
repeat_practice_key = keyboard.Keyboard()

# Initialize components for Routine "szunet_instr"
szunet_instrClock = core.Clock()
szunet_text = visual.TextStim(win=win, name='szunet_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
szunet_key = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
#stim constants
stim_path = "stimuli/"
stim_ext = ".BMP"
stim_frakt = visual.ImageStim(
    win=win,
    name='stim_frakt', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
trial_ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='trial_ISI')

# Initialize components for Routine "level_end"
level_endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
end_keys = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "hello"-------
continueRoutine = True
# update component parameters for each repeat
instr_tovabb.keys = []
instr_tovabb.rt = []
_instr_tovabb_allKeys = []
# keep track of which components have finished
helloComponents = [instr_instr, instr_tovabb]
for thisComponent in helloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
helloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hello"-------
while continueRoutine:
    # get current time
    t = helloClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=helloClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_instr* updates
    if instr_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_instr.frameNStart = frameN  # exact frame index
        instr_instr.tStart = t  # local t and not account for scr refresh
        instr_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_instr, 'tStartRefresh')  # time at next scr refresh
        instr_instr.setAutoDraw(True)
    
    # *instr_tovabb* updates
    waitOnFlip = False
    if instr_tovabb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_tovabb.frameNStart = frameN  # exact frame index
        instr_tovabb.tStart = t  # local t and not account for scr refresh
        instr_tovabb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_tovabb, 'tStartRefresh')  # time at next scr refresh
        instr_tovabb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_tovabb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_tovabb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_tovabb.status == STARTED and not waitOnFlip:
        theseKeys = instr_tovabb.getKeys(keyList=['space'], waitRelease=False)
        _instr_tovabb_allKeys.extend(theseKeys)
        if len(_instr_tovabb_allKeys):
            instr_tovabb.keys = _instr_tovabb_allKeys[-1].name  # just the last key pressed
            instr_tovabb.rt = _instr_tovabb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in helloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hello"-------
for thisComponent in helloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_instr.started', instr_instr.tStartRefresh)
thisExp.addData('instr_instr.stopped', instr_instr.tStopRefresh)
# check responses
if instr_tovabb.keys in ['', [], None]:  # No response was made
    instr_tovabb.keys = None
thisExp.addData('instr_tovabb.keys',instr_tovabb.keys)
if instr_tovabb.keys != None:  # we had a response
    thisExp.addData('instr_tovabb.rt', instr_tovabb.rt)
thisExp.addData('instr_tovabb.started', instr_tovabb.tStartRefresh)
thisExp.addData('instr_tovabb.stopped', instr_tovabb.tStopRefresh)
thisExp.nextEntry()
# the Routine "hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "kezesseg"-------
continueRoutine = True
# update component parameters for each repeat
kezesseg_resp.keys = []
kezesseg_resp.rt = []
_kezesseg_resp_allKeys = []
# keep track of which components have finished
kezessegComponents = [kezesseg_instr, kezesseg_resp]
for thisComponent in kezessegComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
kezessegClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "kezesseg"-------
while continueRoutine:
    # get current time
    t = kezessegClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=kezessegClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *kezesseg_instr* updates
    if kezesseg_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        kezesseg_instr.frameNStart = frameN  # exact frame index
        kezesseg_instr.tStart = t  # local t and not account for scr refresh
        kezesseg_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(kezesseg_instr, 'tStartRefresh')  # time at next scr refresh
        kezesseg_instr.setAutoDraw(True)
    
    # *kezesseg_resp* updates
    waitOnFlip = False
    if kezesseg_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        kezesseg_resp.frameNStart = frameN  # exact frame index
        kezesseg_resp.tStart = t  # local t and not account for scr refresh
        kezesseg_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(kezesseg_resp, 'tStartRefresh')  # time at next scr refresh
        kezesseg_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(kezesseg_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(kezesseg_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if kezesseg_resp.status == STARTED and not waitOnFlip:
        theseKeys = kezesseg_resp.getKeys(keyList=['b', 'j'], waitRelease=False)
        _kezesseg_resp_allKeys.extend(theseKeys)
        if len(_kezesseg_resp_allKeys):
            kezesseg_resp.keys = _kezesseg_resp_allKeys[-1].name  # just the last key pressed
            kezesseg_resp.rt = _kezesseg_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in kezessegComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "kezesseg"-------
for thisComponent in kezessegComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('kezesseg_instr.started', kezesseg_instr.tStartRefresh)
thisExp.addData('kezesseg_instr.stopped', kezesseg_instr.tStopRefresh)
# check responses
if kezesseg_resp.keys in ['', [], None]:  # No response was made
    kezesseg_resp.keys = None
thisExp.addData('kezesseg_resp.keys',kezesseg_resp.keys)
if kezesseg_resp.keys != None:  # we had a response
    thisExp.addData('kezesseg_resp.rt', kezesseg_resp.rt)
thisExp.addData('kezesseg_resp.started', kezesseg_resp.tStartRefresh)
thisExp.addData('kezesseg_resp.stopped', kezesseg_resp.tStopRefresh)
thisExp.nextEntry()
#which hands
if "b" in kezesseg_resp.keys:
    yes_ans = 'e'
    no_ans = 'r'
    ans_options = [yes_ans, no_ans]
    
elif "j" in kezesseg_resp.keys:
    yes_ans = 'u'
    no_ans = 'i'
    ans_options = [yes_ans, no_ans]
# the Routine "kezesseg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
level_loop = data.TrialHandler(nReps=LevelNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='level_loop')
thisExp.addLoop(level_loop)  # add the loop to the experiment
thisLevel_loop = level_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLevel_loop.rgb)
if thisLevel_loop != None:
    for paramName in thisLevel_loop:
        exec('{} = thisLevel_loop[paramName]'.format(paramName))

for thisLevel_loop in level_loop:
    currentLoop = level_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLevel_loop.rgb)
    if thisLevel_loop != None:
        for paramName in thisLevel_loop:
            exec('{} = thisLevel_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "level_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Instr based on level
    task_instr_level = ""
    if level_loop.thisRepN == 0:
        task_instr_level = "Ebben a feladatban képek fognak megjelenni egymás után a képernyőn. Egyszerre egy kép fog megjelenni.\n\nNyomja meg a(z) {} betűt, ha a kép ugyanaz, mint amit eggyel korábban látott!\nA többi esetben, amikor a kép nem egyezik meg az eggyel korábbival, nyomja meg az {} betűt.\n\nA képek gyorsan jönnek egymás után, úgyhogy gyorsnak kell lennie.\nNyomjon SPACE gombot a továbblépéshez!".format(yes_ans.upper(), no_ans.upper())
    elif level_loop.thisRepN == 1:
        task_instr_level = "Ebben a feladatban is képeket fog látni.\n\nNyomja meg a(z) {} betűt, ha a kép ugyanaz, mint amit kettővel korábban látott!\nA többi esetben, amikor a kép nem egyezik meg a kettővel korábbival, nyomja meg az {} betűt.\n\nA képek gyorsan jönnek egymás után, úgyhogy gyorsnak kell lennie.\nNyomjon SPACE gombot a továbblépéshez!".format(yes_ans.upper(), no_ans.upper())
    lvl_instr.setText(task_instr_level)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    level_instrComponents = [lvl_instr, key_resp_2]
    for thisComponent in level_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    level_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "level_instr"-------
    while continueRoutine:
        # get current time
        t = level_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=level_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lvl_instr* updates
        if lvl_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lvl_instr.frameNStart = frameN  # exact frame index
            lvl_instr.tStart = t  # local t and not account for scr refresh
            lvl_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lvl_instr, 'tStartRefresh')  # time at next scr refresh
            lvl_instr.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in level_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "level_instr"-------
    for thisComponent in level_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    level_loop.addData('lvl_instr.started', lvl_instr.tStartRefresh)
    level_loop.addData('lvl_instr.stopped', lvl_instr.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    level_loop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        level_loop.addData('key_resp_2.rt', key_resp_2.rt)
    level_loop.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    level_loop.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "level_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceRepeat = data.TrialHandler(nReps=300, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceRepeat')
    thisExp.addLoop(practiceRepeat)  # add the loop to the experiment
    thisPracticeRepeat = practiceRepeat.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeRepeat.rgb)
    if thisPracticeRepeat != None:
        for paramName in thisPracticeRepeat:
            exec('{} = thisPracticeRepeat[paramName]'.format(paramName))
    
    for thisPracticeRepeat in practiceRepeat:
        currentLoop = practiceRepeat
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeRepeat.rgb)
        if thisPracticeRepeat != None:
            for paramName in thisPracticeRepeat:
                exec('{} = thisPracticeRepeat[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pract_inst"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Instr based on level
        pract_inst_textstim = ""
        if level_loop.thisRepN == 0:
            pract_inst_textstim = "Gyakorló feladat\n\nNyomja meg a(z) {} betűt, ha a kép ugyanaz, mint amit eggyel korábban látott!\nA többi esetben, amikor a kép nem egyezik meg az eggyel korábbival, nyomja meg az {} betűt.\n\nNyomjon SPACE gombot a továbblépéshez!".format(yes_ans.upper(), no_ans.upper())
        elif level_loop.thisRepN == 1:
            pract_inst_textstim = "Gyakorló feladat\n\nNyomja meg a(z) {} betűt, ha a kép ugyanaz, mint amit kettővel korábban látott!\nA többi esetben, amikor a kép nem egyezik meg a kettővel korábbival, nyomja meg az {} betűt.\n\nNyomjon SPACE gombot a továbblépéshez!".format(yes_ans.upper(), no_ans.upper())
        pract_inst_text.setText(pract_inst_textstim)
        pract_inst_key.keys = []
        pract_inst_key.rt = []
        _pract_inst_key_allKeys = []
        # keep track of which components have finished
        pract_instComponents = [pract_inst_text, pract_inst_key]
        for thisComponent in pract_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pract_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pract_inst"-------
        while continueRoutine:
            # get current time
            t = pract_instClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pract_instClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pract_inst_text* updates
            if pract_inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pract_inst_text.frameNStart = frameN  # exact frame index
                pract_inst_text.tStart = t  # local t and not account for scr refresh
                pract_inst_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pract_inst_text, 'tStartRefresh')  # time at next scr refresh
                pract_inst_text.setAutoDraw(True)
            
            # *pract_inst_key* updates
            waitOnFlip = False
            if pract_inst_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pract_inst_key.frameNStart = frameN  # exact frame index
                pract_inst_key.tStart = t  # local t and not account for scr refresh
                pract_inst_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pract_inst_key, 'tStartRefresh')  # time at next scr refresh
                pract_inst_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pract_inst_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pract_inst_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pract_inst_key.status == STARTED and not waitOnFlip:
                theseKeys = pract_inst_key.getKeys(keyList=['space'], waitRelease=False)
                _pract_inst_key_allKeys.extend(theseKeys)
                if len(_pract_inst_key_allKeys):
                    pract_inst_key.keys = [key.name for key in _pract_inst_key_allKeys]  # storing all keys
                    pract_inst_key.rt = [key.rt for key in _pract_inst_key_allKeys]
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pract_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pract_inst"-------
        for thisComponent in pract_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceRepeat.addData('pract_inst_text.started', pract_inst_text.tStartRefresh)
        practiceRepeat.addData('pract_inst_text.stopped', pract_inst_text.tStopRefresh)
        # check responses
        if pract_inst_key.keys in ['', [], None]:  # No response was made
            pract_inst_key.keys = None
        practiceRepeat.addData('pract_inst_key.keys',pract_inst_key.keys)
        if pract_inst_key.keys != None:  # we had a response
            practiceRepeat.addData('pract_inst_key.rt', pract_inst_key.rt)
        practiceRepeat.addData('pract_inst_key.started', pract_inst_key.tStartRefresh)
        practiceRepeat.addData('pract_inst_key.stopped', pract_inst_key.tStopRefresh)
        # the Routine "pract_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_loop = data.TrialHandler(nReps=PracticeTrialNum, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practice_loop')
        thisExp.addLoop(practice_loop)  # add the loop to the experiment
        thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
        if thisPractice_loop != None:
            for paramName in thisPractice_loop:
                exec('{} = thisPractice_loop[paramName]'.format(paramName))
        
        for thisPractice_loop in practice_loop:
            currentLoop = practice_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
            if thisPractice_loop != None:
                for paramName in thisPractice_loop:
                    exec('{} = thisPractice_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "practice_trial"-------
            continueRoutine = True
            routineTimer.add(3.600000)
            # update component parameters for each repeat
            #choose_stim
            chosen_frakt_p = practice_blokks[level_loop.thisRepN][practice_loop.thisRepN]
            
            frakt_stim_p = stim_path + chosen_frakt_p + stim_ext
            
            
            #correct_ans
            correct_pract = no_ans
            if level_loop.thisRepN == 0:
                if practice_loop.thisRepN > 0:
                    if practice_blokks[level_loop.thisRepN][practice_loop.thisRepN] == practice_blokks[level_loop.thisRepN][practice_loop.thisRepN-1]:
                        correct_pract = yes_ans
                    else:
                        correct_pract = no_ans
            elif level_loop.thisRepN == 1:
                if practice_loop.thisRepN > 1:
                    if practice_blokks[level_loop.thisRepN][practice_loop.thisRepN] == practice_blokks[level_loop.thisRepN][practice_loop.thisRepN-2]:
                        correct_pract = yes_ans
                    else:
                        correct_pract = no_ans
            pract_resp.keys = []
            pract_resp.rt = []
            _pract_resp_allKeys = []
            # keep track of which components have finished
            practice_trialComponents = [pract_stim_frakt, pract_resp, ISI]
            for thisComponent in practice_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "practice_trial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = practice_trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=practice_trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #force end if answer is yes or no
                if len(pract_resp.keys) > 0:
                    if (pract_resp.keys[-1] == yes_ans or pract_resp.keys[-1] == no_ans):
                        continueRoutine = False
                
                
                keys = event.getKeys()
                if "escape" in keys:
                    win.close()
                    core.quit()
                
                # *pract_stim_frakt* updates
                if pract_stim_frakt.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    pract_stim_frakt.frameNStart = frameN  # exact frame index
                    pract_stim_frakt.tStart = t  # local t and not account for scr refresh
                    pract_stim_frakt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_stim_frakt, 'tStartRefresh')  # time at next scr refresh
                    pract_stim_frakt.setAutoDraw(True)
                if pract_stim_frakt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pract_stim_frakt.tStartRefresh + 1.8-frameTolerance:
                        # keep track of stop time/frame for later
                        pract_stim_frakt.tStop = t  # not accounting for scr refresh
                        pract_stim_frakt.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(pract_stim_frakt, 'tStopRefresh')  # time at next scr refresh
                        pract_stim_frakt.setAutoDraw(False)
                
                # *pract_resp* updates
                waitOnFlip = False
                if pract_resp.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    pract_resp.frameNStart = frameN  # exact frame index
                    pract_resp.tStart = t  # local t and not account for scr refresh
                    pract_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_resp, 'tStartRefresh')  # time at next scr refresh
                    pract_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(pract_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(pract_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if pract_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pract_resp.tStartRefresh + 3.3-frameTolerance:
                        # keep track of stop time/frame for later
                        pract_resp.tStop = t  # not accounting for scr refresh
                        pract_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(pract_resp, 'tStopRefresh')  # time at next scr refresh
                        pract_resp.status = FINISHED
                if pract_resp.status == STARTED and not waitOnFlip:
                    theseKeys = pract_resp.getKeys(keyList=None, waitRelease=False)
                    _pract_resp_allKeys.extend(theseKeys)
                    if len(_pract_resp_allKeys):
                        pract_resp.keys = [key.name for key in _pract_resp_allKeys]  # storing all keys
                        pract_resp.rt = [key.rt for key in _pract_resp_allKeys]
                # *ISI* period
                if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.tStart = t  # local t and not account for scr refresh
                    ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                    ISI.start(0.3)
                elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI*
                    pract_stim_frakt.setImage(frakt_stim_p)
                    # component updates done
                    ISI.complete()  # finish the static period
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practice_trial"-------
            for thisComponent in practice_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            practice_loop.addData('pract_stim_frakt.started', pract_stim_frakt.tStartRefresh)
            practice_loop.addData('pract_stim_frakt.stopped', pract_stim_frakt.tStopRefresh)
            # check responses
            if pract_resp.keys in ['', [], None]:  # No response was made
                pract_resp.keys = None
            practice_loop.addData('pract_resp.keys',pract_resp.keys)
            if pract_resp.keys != None:  # we had a response
                practice_loop.addData('pract_resp.rt', pract_resp.rt)
            practice_loop.addData('pract_resp.started', pract_resp.tStartRefresh)
            practice_loop.addData('pract_resp.stopped', pract_resp.tStopRefresh)
            practice_loop.addData('ISI.started', ISI.tStart)
            practice_loop.addData('ISI.stopped', ISI.tStop)
            #logging blokk
            task_blokk = "nback_" + str(level_loop.thisRepN+1) + "_practice"
            thisExp.addData("feladat_blokk", task_blokk)
            
            #logging fractal
            thisExp.addData("Fraktál", chosen_frakt_p)
            
            #logging all_keys
            thisExp.addData("All_keys", pract_resp.keys)
            
            #logging all_RT (adjusted to presentation)
            thisExp.addData("All_RT", pract_resp.rt)
            
            #logging answer_key
            what_resp = "no_resp"
            RT_resp = None
            
            if pract_resp.keys is not None:
                what_resp = "else"
                if yes_ans in pract_resp.keys or no_ans in pract_resp.keys:
                    what_resp = pract_resp.keys[-1]
                    RT_resp = pract_resp.rt[-1]
            
            
            thisExp.addData("Answer_key", what_resp)
            thisExp.addData("Answer RT", RT_resp)
            
            #logging correctness
            ans_type = None
            correctness = None
            if correct_pract == yes_ans and what_resp == yes_ans:
                ans_type = "hit"
                correctness = 1
            elif correct_pract == yes_ans and what_resp == no_ans:
                ans_type = "miss"
                correctness = 0
            elif correct_pract == no_ans and what_resp == no_ans:
                ans_type = "correct rejection"
                correctness = 1
            elif correct_pract == no_ans and what_resp == yes_ans:
                ans_type = "false alarm"
                correctness = 0
            
            thisExp.addData("Response type", ans_type)
            thisExp.addData("Correctness", correctness)
            thisExp.nextEntry()
            
        # completed PracticeTrialNum repeats of 'practice_loop'
        
        
        # ------Prepare to start Routine "repeatPractice"-------
        continueRoutine = True
        # update component parameters for each repeat
        repeat_text = "Újraindítsuk a gyakorlást?\n\nIgen = {}\nNem = {}".format(yes_ans.upper(),no_ans.upper())
        repeat_pract_text.setText(repeat_text)
        repeat_practice_key.keys = []
        repeat_practice_key.rt = []
        _repeat_practice_key_allKeys = []
        # keep track of which components have finished
        repeatPracticeComponents = [repeat_pract_text, repeat_practice_key]
        for thisComponent in repeatPracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        repeatPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "repeatPractice"-------
        while continueRoutine:
            # get current time
            t = repeatPracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=repeatPracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *repeat_pract_text* updates
            if repeat_pract_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                repeat_pract_text.frameNStart = frameN  # exact frame index
                repeat_pract_text.tStart = t  # local t and not account for scr refresh
                repeat_pract_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(repeat_pract_text, 'tStartRefresh')  # time at next scr refresh
                repeat_pract_text.setAutoDraw(True)
            
            # *repeat_practice_key* updates
            waitOnFlip = False
            if repeat_practice_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                repeat_practice_key.frameNStart = frameN  # exact frame index
                repeat_practice_key.tStart = t  # local t and not account for scr refresh
                repeat_practice_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(repeat_practice_key, 'tStartRefresh')  # time at next scr refresh
                repeat_practice_key.status = STARTED
                # AllowedKeys looks like a variable named `ans_options`
                if not type(ans_options) in [list, tuple, np.ndarray]:
                    if not isinstance(ans_options, str):
                        logging.error('AllowedKeys variable `ans_options` is not string- or list-like.')
                        core.quit()
                    elif not ',' in ans_options:
                        ans_options = (ans_options,)
                    else:
                        ans_options = eval(ans_options)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(repeat_practice_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(repeat_practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if repeat_practice_key.status == STARTED and not waitOnFlip:
                theseKeys = repeat_practice_key.getKeys(keyList=list(ans_options), waitRelease=False)
                _repeat_practice_key_allKeys.extend(theseKeys)
                if len(_repeat_practice_key_allKeys):
                    repeat_practice_key.keys = _repeat_practice_key_allKeys[-1].name  # just the last key pressed
                    repeat_practice_key.rt = _repeat_practice_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in repeatPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "repeatPractice"-------
        for thisComponent in repeatPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if no_ans in repeat_practice_key.keys:
            practiceRepeat.nReps = 0
        practiceRepeat.addData('repeat_pract_text.started', repeat_pract_text.tStartRefresh)
        practiceRepeat.addData('repeat_pract_text.stopped', repeat_pract_text.tStopRefresh)
        # check responses
        if repeat_practice_key.keys in ['', [], None]:  # No response was made
            repeat_practice_key.keys = None
        practiceRepeat.addData('repeat_practice_key.keys',repeat_practice_key.keys)
        if repeat_practice_key.keys != None:  # we had a response
            practiceRepeat.addData('repeat_practice_key.rt', repeat_practice_key.rt)
        practiceRepeat.addData('repeat_practice_key.started', repeat_practice_key.tStartRefresh)
        practiceRepeat.addData('repeat_practice_key.stopped', repeat_practice_key.tStopRefresh)
        # the Routine "repeatPractice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 300 repeats of 'practiceRepeat'
    
    
    # ------Prepare to start Routine "szunet_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Instr based on level
    szunet_instr_text = ""
    if level_loop.thisRepN == 0:
        szunet_instr_text = "Szünet!\n\nTovábblépéskor kezdődik a feladat.\nNyomja meg a(z) {} betűt, ha a kép ugyanaz, mint amit eggyel korábban látott!\nA többi esetben, amikor a kép nem egyezik meg az eggyel korábbival, nyomja meg az {} betűt.\n\nA képek gyorsan jönnek egymás után, úgyhogy gyorsnak kell lennie.\nNyomjon SPACE gombot a továbblépéshez!".format(yes_ans.upper(), no_ans.upper())
    elif level_loop.thisRepN == 1:
        szunet_instr_text = "Szünet!\n\nTovábblépéskor kezdődik a feladat.\nNyomja meg a(z) {} betűt, ha a kép ugyanaz, mint amit kettővel korábban látott!\nA többi esetben, amikor a kép nem egyezik meg a kettővel korábbival, nyomja meg az {} betűt.\n\nA képek gyorsan jönnek egymás után, úgyhogy gyorsnak kell lennie.\nNyomjon SPACE gombot a továbblépéshez!".format(yes_ans.upper(), no_ans.upper())
    szunet_text.setText(szunet_instr_text)
    szunet_key.keys = []
    szunet_key.rt = []
    _szunet_key_allKeys = []
    # keep track of which components have finished
    szunet_instrComponents = [szunet_text, szunet_key]
    for thisComponent in szunet_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    szunet_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "szunet_instr"-------
    while continueRoutine:
        # get current time
        t = szunet_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=szunet_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *szunet_text* updates
        if szunet_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            szunet_text.frameNStart = frameN  # exact frame index
            szunet_text.tStart = t  # local t and not account for scr refresh
            szunet_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(szunet_text, 'tStartRefresh')  # time at next scr refresh
            szunet_text.setAutoDraw(True)
        
        # *szunet_key* updates
        waitOnFlip = False
        if szunet_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            szunet_key.frameNStart = frameN  # exact frame index
            szunet_key.tStart = t  # local t and not account for scr refresh
            szunet_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(szunet_key, 'tStartRefresh')  # time at next scr refresh
            szunet_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(szunet_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(szunet_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if szunet_key.status == STARTED and not waitOnFlip:
            theseKeys = szunet_key.getKeys(keyList=['space'], waitRelease=False)
            _szunet_key_allKeys.extend(theseKeys)
            if len(_szunet_key_allKeys):
                szunet_key.keys = [key.name for key in _szunet_key_allKeys]  # storing all keys
                szunet_key.rt = [key.rt for key in _szunet_key_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in szunet_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "szunet_instr"-------
    for thisComponent in szunet_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    level_loop.addData('szunet_text.started', szunet_text.tStartRefresh)
    level_loop.addData('szunet_text.stopped', szunet_text.tStopRefresh)
    # check responses
    if szunet_key.keys in ['', [], None]:  # No response was made
        szunet_key.keys = None
    level_loop.addData('szunet_key.keys',szunet_key.keys)
    if szunet_key.keys != None:  # we had a response
        level_loop.addData('szunet_key.rt', szunet_key.rt)
    level_loop.addData('szunet_key.started', szunet_key.tStartRefresh)
    level_loop.addData('szunet_key.stopped', szunet_key.tStopRefresh)
    # the Routine "szunet_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blokk_loop = data.TrialHandler(nReps=BlokkNum, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blokk_loop')
    thisExp.addLoop(blokk_loop)  # add the loop to the experiment
    thisBlokk_loop = blokk_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlokk_loop.rgb)
    if thisBlokk_loop != None:
        for paramName in thisBlokk_loop:
            exec('{} = thisBlokk_loop[paramName]'.format(paramName))
    
    for thisBlokk_loop in blokk_loop:
        currentLoop = blokk_loop
        # abbreviate parameter names if possible (e.g. rgb = thisBlokk_loop.rgb)
        if thisBlokk_loop != None:
            for paramName in thisBlokk_loop:
                exec('{} = thisBlokk_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trial_loop = data.TrialHandler(nReps=TrialNum, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trial_loop')
        thisExp.addLoop(trial_loop)  # add the loop to the experiment
        thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
        if thisTrial_loop != None:
            for paramName in thisTrial_loop:
                exec('{} = thisTrial_loop[paramName]'.format(paramName))
        
        for thisTrial_loop in trial_loop:
            currentLoop = trial_loop
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
            if thisTrial_loop != None:
                for paramName in thisTrial_loop:
                    exec('{} = thisTrial_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial"-------
            continueRoutine = True
            routineTimer.add(3.600000)
            # update component parameters for each repeat
            #choose_stim
            chosen_frakt = all_blokks[level_loop.thisRepN][blokk_loop.thisRepN][trial_loop.thisRepN]
            
            frakt_stim = stim_path + chosen_frakt + stim_ext
            
            
            #correct_ans
            correct = no_ans
            if level_loop.thisRepN == 0:
                if trial_loop.thisRepN > 0:
                    if all_blokks[level_loop.thisRepN][blokk_loop.thisRepN][trial_loop.thisRepN] == all_blokks[level_loop.thisRepN][blokk_loop.thisRepN][trial_loop.thisRepN-1]:
                        correct = yes_ans
                    else:
                        correct = no_ans
            elif level_loop.thisRepN == 1:
                if trial_loop.thisRepN > 1:
                    if all_blokks[level_loop.thisRepN][blokk_loop.thisRepN][trial_loop.thisRepN] == all_blokks[level_loop.thisRepN][blokk_loop.thisRepN][trial_loop.thisRepN-2]:
                        correct = yes_ans
                    else:
                        correct = no_ans
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            trialComponents = [stim_frakt, key_resp, trial_ISI]
            for thisComponent in trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "trial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #force end if answer is yes or no
                if len(key_resp.keys) > 0:
                    if (key_resp.keys[-1] == yes_ans or key_resp.keys[-1] == no_ans):
                        continueRoutine = False
                
                
                keys = event.getKeys()
                if "escape" in keys:
                    win.close()
                    core.quit()
                
                # *stim_frakt* updates
                if stim_frakt.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    stim_frakt.frameNStart = frameN  # exact frame index
                    stim_frakt.tStart = t  # local t and not account for scr refresh
                    stim_frakt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_frakt, 'tStartRefresh')  # time at next scr refresh
                    stim_frakt.setAutoDraw(True)
                if stim_frakt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_frakt.tStartRefresh + 1.8-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_frakt.tStop = t  # not accounting for scr refresh
                        stim_frakt.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stim_frakt, 'tStopRefresh')  # time at next scr refresh
                        stim_frakt.setAutoDraw(False)
                
                # *key_resp* updates
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + 3.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                        key_resp.status = FINISHED
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                        key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # *trial_ISI* period
                if trial_ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    trial_ISI.frameNStart = frameN  # exact frame index
                    trial_ISI.tStart = t  # local t and not account for scr refresh
                    trial_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trial_ISI, 'tStartRefresh')  # time at next scr refresh
                    trial_ISI.start(0.3)
                elif trial_ISI.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *trial_ISI*
                    stim_frakt.setImage(frakt_stim)
                    # component updates done
                    trial_ISI.complete()  # finish the static period
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_loop.addData('stim_frakt.started', stim_frakt.tStartRefresh)
            trial_loop.addData('stim_frakt.stopped', stim_frakt.tStopRefresh)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            trial_loop.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                trial_loop.addData('key_resp.rt', key_resp.rt)
            trial_loop.addData('key_resp.started', key_resp.tStartRefresh)
            trial_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
            #logging blokk
            task_blokk = "nback_" + str(level_loop.thisRepN+1) + "_blokk" + str(blokk_loop.thisRepN+1)
            thisExp.addData("feladat_blokk", task_blokk)
            
            #logging fractal
            thisExp.addData("Fraktál", chosen_frakt)
            
            #logging all_keys
            thisExp.addData("All_keys", key_resp.keys)
            
            #logging all_RT (adjusted to presentation)
            thisExp.addData("All_RT", key_resp.rt)
            
            #logging answer_key
            what_resp = "no_resp"
            RT_resp = None
            
            if key_resp.keys is not None:
                what_resp = "else"
                if yes_ans in key_resp.keys or no_ans in key_resp.keys:
                    what_resp = key_resp.keys[-1]
                    RT_resp = key_resp.rt[-1]
            
            
            thisExp.addData("Answer_key", what_resp)
            thisExp.addData("Answer RT", RT_resp)
            
            #logging correctness
            ans_type = "else"
            if correct == yes_ans and what_resp == yes_ans:
                ans_type = "hit"
                correctness = 1
            elif correct == yes_ans and what_resp == no_ans:
                ans_type = "miss"
                correctness = 0
            elif correct == no_ans and what_resp == no_ans:
                ans_type = "correct rejection"
                correctness = 1
            elif correct == no_ans and what_resp == yes_ans:
                ans_type = "false alarm"
                correctness = 0
            
            thisExp.addData("Response type", ans_type)
            thisExp.addData("Correctness", correctness)
            trial_loop.addData('trial_ISI.started', trial_ISI.tStart)
            trial_loop.addData('trial_ISI.stopped', trial_ISI.tStop)
            thisExp.nextEntry()
            
        # completed TrialNum repeats of 'trial_loop'
        
        thisExp.nextEntry()
        
    # completed BlokkNum repeats of 'blokk_loop'
    
    
    # ------Prepare to start Routine "level_end"-------
    continueRoutine = True
    # update component parameters for each repeat
    end_text = 'Vége az első feladatnak!\n\nA folytatáshoz nyomja meg a SPACE gombot.'
    if level_loop.thisRepN > 0:
        end_text = 'Vége a feladatoknak!\n\nKöszönjük a részvételt!\nA kilépéshez nyomja meg a SPACE gombot!'
    text.setText(end_text)
    end_keys.keys = []
    end_keys.rt = []
    _end_keys_allKeys = []
    # keep track of which components have finished
    level_endComponents = [text, end_keys]
    for thisComponent in level_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    level_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "level_end"-------
    while continueRoutine:
        # get current time
        t = level_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=level_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *end_keys* updates
        waitOnFlip = False
        if end_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_keys.frameNStart = frameN  # exact frame index
            end_keys.tStart = t  # local t and not account for scr refresh
            end_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_keys, 'tStartRefresh')  # time at next scr refresh
            end_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_keys.status == STARTED and not waitOnFlip:
            theseKeys = end_keys.getKeys(keyList=['space'], waitRelease=False)
            _end_keys_allKeys.extend(theseKeys)
            if len(_end_keys_allKeys):
                end_keys.keys = [key.name for key in _end_keys_allKeys]  # storing all keys
                end_keys.rt = [key.rt for key in _end_keys_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in level_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "level_end"-------
    for thisComponent in level_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    level_loop.addData('text.started', text.tStartRefresh)
    level_loop.addData('text.stopped', text.tStopRefresh)
    # check responses
    if end_keys.keys in ['', [], None]:  # No response was made
        end_keys.keys = None
    level_loop.addData('end_keys.keys',end_keys.keys)
    if end_keys.keys != None:  # we had a response
        level_loop.addData('end_keys.rt', end_keys.rt)
    level_loop.addData('end_keys.started', end_keys.tStartRefresh)
    level_loop.addData('end_keys.stopped', end_keys.tStopRefresh)
    # the Routine "level_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed LevelNum repeats of 'level_loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
