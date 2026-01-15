import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection


def freeze_transforms():
    """
    Freezes transformation of selected object
    Using MEL: makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1
    """

    selection = get_selection("Freeze Transforms")
    if selection:       
        cmds.makeIdentity(selection, a=True, t=True, r=True, s=True, pn=True)