# mToolbox

![Current shelf look](assets/screenshots/current_toolbox.png)

A collection of personal python based tools for Maya for rigging purposes

## Overview

Macros for used commands such as:
- Toggle LRAs
- Freeze Transforms
- Select Hierarchy
- Delete History
- Smarter Create Locator (at selection/at world origin)
- Snap To Average 
- Snap To Parent (for multiple objects)

Next plans:
- Create Joint Chain (customizable)

## Installaton: 
1. Clone the repo into a folder
2. Move the folder into `maya/####/scripts/`
3. Register buttons using 
```
from mtoolbox.tools.SCRIPT_NAME import SCRIPT NAME
SCRIPT_NAME()
```
4. Edit popup and select icons from `mtoolbox/icons` folder with the correct name
