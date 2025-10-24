import sys
import os
import subprocess
from datetime import datetime, timedelta

sys.path.append('../sdpm_py_util')
import init_funs_forecast as initfuns
sys.path.append('../driver')


def get_hindcast_days(t1,tend,dt):
    # this function returns a list of strings for the range of hindcasts.
    t1s = []
    t2s = []    

    while t1<tend:
        t2 = t1 + dt * timedelta(days=1)
        t1s.append(t1.strftime('%Y%m%d%H'))
        t2s.append(t2.strftime('%Y%m%d%H'))
        t1 = t2
    
    # make sure the last t2s is tend...
    tendstr = tend.strftime('%Y%m%d%H')
    if t2s[-1] != tendstr:
        print('the last t2 is not tend, something is wrong with dt and or tend. not returning lists of dates.')
        t1s = []
        t2s = []

    return t1s, t2s


def driver_runlvl(pkl_fnm,nlv = 'LV1'):
    t00 = datetime.now()
    MI = initfuns.get_model_info( pkl_fnm )
    nt  = len(MI['start_times_str'])
    time_tots = [0]*nt
    time_lvls = [[0] * nt for i in range(nlv)]