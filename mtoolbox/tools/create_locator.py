import maya.cmds as cmds

def create_locator():
    """
    A smarter Locator creator that creates locator at last selected object or 
    at world origin if nothing is selected
    """
    selection = cmds.ls(selection=True)
    loc = cmds.spaceLocator()

    # snap to selection
    if selection:
        constraint = cmds.parentConstraint(selection[-1], loc, mo=False) # snaps to last obj
        cmds.delete(constraint)