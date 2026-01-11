# mToolbox

![mToolbox v.1.0 UI](/mtoolbox/assets/screenshots/toolbox_ui.png)

![Current shelf look](mtoolbox/assets/screenshots/current_toolbox.png)

A collection of personal python based tools for Maya for rigging purposes

## Overview

mToolbox has two modes:
- **UI** (PySide2)
- **Shelf** with separate buttons

Notable functions:
- Create Joint Chain (customizable via UI or by editing the button)
- Snap To Average 
- Snap To Parent (for multiple objects)
- Toggle LRAs
- Freeze Transforms
- Select Hierarchy
- Delete History
- Smarter Create Locator (at selection/at world origin)

## Installaton: 
1. Clone or download this repository
2. Copy the `mtoolbox` folder into your `maya/####/scripts/` folder
3. Drag and drop `install_ui.py` (for UI version) or `install_shelf.py` (for shelf version)
4. If UI selected - a new button will appear on your shelf, 
if shelf selected - a new shelf called `mToolbox` with buttons will appear

## Notes: 
- Icons are installed automatically in `maya/####/prefs/icons/mtoolbox`
- Tools are standalone python modules and can be installed one by one via shelfButton command:
```
from mtoolbox.tools.MODULE_NAME import MODULE_NAME 
MODULE_NAME()"
```

## Editing the "Create Joint Chain" Shelf Button
If you're using the shelf option and want to edit the **CRT JNT** button:

Right-click the button -> **EDIT** -> modify the command:
```from mtoolbox.tools.create_joints import create_joints
create_joints(3, 'joint', True)",
```
You can change `create_joints(NUMBER_OF_JOINTS,'NAME', AFFIX)`
NUMBER_OF_JOINTS -> has to be an integer, 1 is the minimum
'NAME' -> can be any string, remember to put it in ''
AFFIX -> `True` or `False`
