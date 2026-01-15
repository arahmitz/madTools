# mToolbox - Templates

## One Command Tool
```python
import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def tool_name():
    """
    Short description of the tool
    Using MEL: <command + flags>
    """

    selection = get_selection("Operation")
    if selection:
        # Command here
        # cmds.command()
```