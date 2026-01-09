import maya.cmds as cmds

# List of buttons to add
buttons_to_add = [
    {
        "annotation": "Toggle LRA",
        "command": "from mtoolbox.tools.toggle_lra import toggle_lra; toggle_lra()",
        "image": "mtoolbox/toggle_lra.png"
    },
    {
        "annotation": "Delete History",
        "command": "from mtoolbox.tools.delete_history import delete_history; delete_history()",
        "image": "mtoolbox/delete_history.png"
    }, 
    {
        "annotation": "Freeze Transforms",
        "command": "from mtoolbox.tools.freeze_transforms import freeze_transforms; freeze_transforms()",
        "image": "mtoolbox/freeze_transforms.png"
    },
    {
        "annotation": "Select Hierarchy",
        "command": "from mtoolbox.tools.select_hierarchy import select_hierarchy; select_hierarchy()",
        "image": "mtoolbox/select_hierarchy.png"
    },
    {
        "annotation": "Create Locator",
        "command": "from mtoolbox.tools.create_locator import create_locator; create_locator()",
        "image": "mtoolbox/create_locator.png"
    },
    {
        "annotation": "Snap To Parent",
        "command": "from mtoolbox.tools.snap_to_parent import snap_to_parent; snap_to_parent()",
        "image": "mtoolbox/snap_to_parent.png"
    },
    {
        "annotation": "Snap To Average",
        "command": "from mtoolbox.tools.snap_to_average import snap_to_average; snap_to_average()",
        "image": "mtoolbox/snap_to_average.png"
    },
    {
        "annotation": "Create Joints",
        "command": "from mtoolbox.tools.create_joints import create_joints; create_joints()",
        "image": "mtoolbox/create_joints.png"
    },
]


def add_button(shelf, button_data):
    # Populate existing annotations
    existing_buttons = cmds.shelfLayout(shelf, q=True, childArray=True) or []
    existing_annotations = [cmds.shelfButton(button, q=True, annotation=True) 
                            for button in existing_buttons]
    # Skip if annotaton exists
    if button_data['annotation'] in existing_annotations:
        cmds.warning(f"Button {button_data['annotation']} already exists, skipping it.")
        return
    
    # Add the button
    cmds.shelfButton(parent=shelf,
                    annotation = button_data['annotation'],
                    image1 = button_data['image'],
                    command = button_data['command'])


# Script body
shelf_name = 'mToolbox'

# Create a new shelf if it doesn't exist
if not cmds.shelfLayout(shelf_name, exists=True):
    cmds.shelfLayout(shelf_name, parent="ShelfLayout")

for button_data in buttons_to_add:
    add_button(shelf_name, button_data)