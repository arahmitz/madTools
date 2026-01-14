import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def joint_zso():
    """
    Sets scale orientation to zero and compensate the change by modifying translation and joint orientation or rotation for general transform
    MEL: joint -e -zso
    """
    selection = cmds.ls(sl=True, type="joint")

    if not selection:
        cmds.warning("No joints selected. Aborting Joint ZSO.")
        return
    
    cmds.select(selection, r=True) # picks only joints from whole selection
    cmds.joint(e=True, zso=True)