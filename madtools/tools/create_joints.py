import maya.cmds as cmds

def create_joints(joint_count, base_name, affix, add_end):
    """
    Creates a chain with zero-ed JO of user selected length and name in +X. Deselects joint afterwards for faster parenting.
    """

    spacing = 3
    base_name = (base_name or 'joint').strip() # strips to remove any white characters, etc
    affix = (affix or '').strip() # strips to remove any white characters, etc

    # Create parametered joint chain
    for joint in range(joint_count):
            
        joint_name = f"{base_name}{joint+1}"
    
        if add_end and joint == joint_count - 1:
            joint_name += '_end'

        if affix:
            joint_name += affix

        cmds.joint(name=joint_name, p=(joint * spacing, 0, 0))
    
    # Clear select to make repeated chains easier
    cmds.select(clear=True)

