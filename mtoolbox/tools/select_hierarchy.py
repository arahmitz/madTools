import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def select_hierarchy():
    """
    Selects hierarchy of the selected object
    Using MEL: select -hierarchy
    """

    selection = get_selection("Select Hierarchy")
    if selection:
        cmds.select(selection, hierarchy=True)