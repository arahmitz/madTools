import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def toggle_lra():
    """
    Toggles visiblity of Local Rotation Axis of selected object
    Using MEL: toggle -localAxis
    """

    selection = get_selection("Toggle LRA")
    if selection:
        cmds.toggle(selection, la=True)