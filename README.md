# madTools ![Version](https://img.shields.io/badge/version-1.0.0-blue)


![madTools v.1.0 UI](/madtools/assets/screenshots/toolbox_ui.png)

![Current shelf look](madtools/assets/screenshots/current_toolbox.png)

madTools is a personal rigging & utility toolbox for Maya 2022 and beyond.
It provides a clean, easy to install and use UI and shelf for Technical Animators and Riggers.

## Overview

madTools has two modes:
- **UI** (PySide2)
- **Shelf** with separate buttons

### Notable functions:

- **Create Joint**
  - Creates a joint chain in +X
  - Editable number of joints, spacing, and naming (via command and UI)
- **Smarter Create Locator**
  - Creates a locator at your current selection or world origin
- **Snap To Average**
  - Snaps last selected object to average of the rest (translation & rotation)
- **Point To Average**
  - Snaps last selected object to average of the rest (translation only)
- **Snap To Parent**
  - Snaps all selected objects to the first selected object (translation & rotation)
- **Freeze Transforms**
  - Freezes transformations
- **Select Hierarchy**
  - Selects the full hierarchy of the selected object
- **Delete History**
  - Deletes history via Delete History → By Type
- **Toggle LRAs**
  - Toggles Local Rotation Axis on/off 
- **Joint ZSO**
  - Matches rotation axis to translation axis via `joint -e -zso`
- **Make ROM**
  - Creates keyframes every 10 frames from current startTime to current endTime to help with creation of RangeOfMotion animation

## Installation: 
1. Go to [Release](https://github.com/arahmitz/madTools/releases) page
2. Download the latest release `.zip` file
3. Extract the `madtools` folder into your `maya/####/scripts/` folder
4. Drag and drop `install_ui.py` (for UI version) or `install_shelf.py` (for shelf version)
5. If UI selected - a new button will appear on your shelf, 
if shelf selected - a new shelf called `madTools` with buttons will appear on current shelf

## Notes: 
- Icons are installed automatically in `maya/####/prefs/icons/madtools`
- Tools are standalone python modules and can be installed one by one via shelfButton command:
```
from madtools.tools.MODULE_NAME import MODULE_NAME 
MODULE_NAME()"
```

## Editing the "Create Joint Chain" Shelf Button
If you're using the shelf option and want to edit the **CRT JNT** button:

Right-click the **CRT JNT** shelf button -> **Edit**
```python
from madtools.tools.create_joints import create_joints
create_joints(3, 'joint', True)",
```
You can change `create_joints(NUMBER_OF_JOINTS,'NAME', AFFIX)`

`NUMBER_OF_JOINTS` -> integer, min 1

`'NAME'` -> string, must be in quotes

`AFFIX` -> `True` or `False`

## Credits

- Toolbox icon made by [Adib Sulthon](https://www.flaticon.com/free-icons/toolbox) - [Flaticon](https://www.flaticon.com/)
