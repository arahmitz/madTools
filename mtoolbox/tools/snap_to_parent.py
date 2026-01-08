import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def snap_to_parent():
    """
    Snaps selected objects to the first selection

    When selected:
    - First object is the final locaton
    - All other objects are snapped to the first
    """
    selection = get_selection("Snap to Parent")
    constraints = []

    if selection:
        if len(selection) < 2:
            cmds.warning("Snap tool needs at least 2 selected objects. Aborting Snap to Parent.")
            return
        else:
            for driven in selection[1:]:
                # selection[1:] are driven by selection[0]
                constraints.append(cmds.parentConstraint(selection[0], driven, mo=False)) 
            for constraint in constraints:
                cmds.delete(constraint)