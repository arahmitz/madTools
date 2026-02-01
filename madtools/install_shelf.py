import maya.cmds as cmds
import os, shutil

def onMayaDroppedPythonFile(*args):

    # Setup filepaths
    installer_dir = os.path.dirname(__file__)
    prefs_dir = cmds.internalVar(userPrefDir=True)
    icons_source_dir = os.path.join(installer_dir, "icons")
    icons_target_dir = os.path.join(prefs_dir, "icons", "madtools")
    os.makedirs(icons_target_dir, exist_ok=True)

    # Copy files from scripts/madtools/icons to prefs/icons/madtools
    if os.path.exists(icons_source_dir):
        for file_name in os.listdir(icons_source_dir):
            source_file = os.path.join(icons_source_dir, file_name)
            target_file = os.path.join(icons_target_dir, file_name)
            if os.path.isfile(source_file):
                shutil.copy(source_file, target_file)
            
    # List of buttons to add
    buttons_to_add = [
        {
            "annotation": "Create Joints",
            "command": "from madtools.tools.create_joints import create_joints; create_joints(3, 'joint', '', True)",
            "image": "madtools/create_joints.png"
        },
        {
            "annotation": "Create Locator",
            "command": "from madtools.tools.create_locator import create_locator; create_locator()",
            "image": "madtools/create_locator.png"
        },
        {
            "annotation": "Snap To Average",
            "command": "from madtools.tools.snap_to_average import snap_to_average; snap_to_average()",
            "image": "madtools/snap_to_average.png"
        },
        {
            "annotation": "Point To Average",
            "command": "from madtools.tools.point_to_average import point_to_average; point_to_average()",
            "image": "madtools/point_to_average.png"
        },
        {
            "annotation": "Snap To Parent",
            "command": "from madtools.tools.snap_to_parent import snap_to_parent; snap_to_parent()",
            "image": "madtools/snap_to_parent.png"
        },
        {
            "annotation": "Freeze Transforms",
            "command": "from madtools.tools.freeze_transforms import freeze_transforms; freeze_transforms()",
            "image": "madtools/freeze_transforms.png"
        },
        {
            "annotation": "Select Hierarchy",
            "command": "from madtools.tools.select_hierarchy import select_hierarchy; select_hierarchy()",
            "image": "madtools/select_hierarchy.png"
        },
           {
            "annotation": "Delete History",
            "command": "from madtools.tools.delete_history import delete_history; delete_history()",
            "image": "madtools/delete_history.png"
        }, 
        {
            "annotation": "Toggle LRA",
            "command": "from madtools.tools.toggle_lra import toggle_lra; toggle_lra()",
            "image": "madtools/toggle_lra.png"
        },
        {
            "annotation": "Joint ZSO",
            "command": "from madtools.tools.joint_zso import joint_zso; joint_zso()",
            "image": "madtools/joint_zso.png"
        },
         {
            "annotation": "Make ROM",
            "command": "from madtools.tools.make_rom import make_rom; make_rom()",
            "image": "madtools/make_rom.png"
        },

    ]


    def add_button(shelf, button_data):
        # Populate existing annotations
        existing_buttons = cmds.shelfLayout(shelf, q=True, childArray=True) or []
        existing_annotations = [cmds.shelfButton(button, q=True, annotation=True) 
                                for button in existing_buttons]
        # Skip if annotaton exists
        if button_data['annotation'] in existing_annotations:
            cmds.warning("Button {} already exists, skipping it.".format(button_data['annotation']))
            return
        
        # Add the button
        cmds.shelfButton(parent=shelf,
                        annotation = button_data['annotation'],
                        image1 = button_data['image'],
                        command = button_data['command'])


    # Script body
    shelf_name = 'madTools'


    # Create a new shelf if it doesn't exist
    if not cmds.shelfLayout(shelf_name, exists=True):
        cmds.shelfLayout(shelf_name, parent="ShelfLayout")

    for button_data in buttons_to_add:
        add_button(shelf_name, button_data)