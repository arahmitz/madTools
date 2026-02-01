import maya.cmds as cmds

def create_joints(joint_count, base_name, affix, add_end):
    """
    Creates a chain with zero-ed JO of user selected length and name. Selects the first joint at the end.
    """
    spacing = 3
    root_joint = None
    base_name = (base_name or 'joint').strip() # strips to remove any white characters, etc
    affix = (affix or '').strip() # strips to remove any white characters, etc

    # Create parametered joint chain
    for joint in range(joint_count):
            
        joint_name = f"{base_name}{joint+1}"
    
        if add_end and joint == joint_count - 1:
            joint_name += '_end'

        if affix:
            joint_name += affix
        
        if joint == 0:
            root_joint = joint_name

        cmds.joint(name=joint_name, p=(joint * spacing, 0, 0))
    
    # Select root at the end
    cmds.select(clear=True)
    cmds.select(root_joint)
