import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def make_rom():
    """
    Sets keyframes every 10 frames on the selected objects starting from frame 0 up to
    the current timeline end, inclusive. Intended for Range Of Movement testing.
    """
    start_time = 0 # ROM always start at 0
    end_time = int(cmds.playbackOptions(q=True, max=True)) # grabs end of the selected timeline

    interval = 10
    
    selection = get_selection("Make ROM")
    if selection:
        # has to end at end time + interval to include endtime
        for keyframe in range(start_time, end_time + interval, interval):
            cmds.currentTime(keyframe)
            cmds.setKeyframe(selection)