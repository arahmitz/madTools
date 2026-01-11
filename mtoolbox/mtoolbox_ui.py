import PySide2, shiboken2, sys, os
from PySide2 import QtWidgets, QtCore, QtGui
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import mtoolbox.tools.create_joints as create_joints
import mtoolbox.tools.snap_to_parent as snap_to_parent
import mtoolbox.tools.snap_to_average as snap_to_average
import mtoolbox.tools.select_hierarchy as select_hierarchy
import mtoolbox.tools.delete_history as delete_history
import mtoolbox.tools.freeze_transforms as freeze_transforms
import mtoolbox.tools.toggle_lra as toggle_lra
import mtoolbox.tools.create_locator as create_locator

toolbox_path = os.path.join(cmds.internalVar(userScriptDir=True), 'mtoolbox')
if toolbox_path not in sys.path:
    sys.path.append(toolbox_path)

def get_maya_main_window():
    """
    Returns Maya window as QWidget
    """
    qt_pointer = omui.MQtUtil.mainWindow()
    maya_parent = shiboken2.wrapInstance(int(qt_pointer), QtWidgets.QWidget)

    return maya_parent


class MToolboxUI(QtWidgets.QDialog):
    """
    Main window definition
    """
    def __init__(self, parent=None):
        super(MToolboxUI, self).__init__(parent)
        self.setWindowTitle("mToolbox v.1.0")
        
        # -------------
        # Window Layout
        # -------------
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        # ------------------
        # Create Joints Tool
        # ------------------
        
        # Chain Length Row
        
        create_joints_chainlen_label = QtWidgets.QLabel("Chain Length:")

        self.create_joints_chainlen_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.create_joints_chainlen_slider.setMinimum(1)
        self.create_joints_chainlen_slider.setMaximum(10)
        self.create_joints_chainlen_slider.setValue(5)
        self.create_joints_chainlen_slider.setTickInterval(1)
        self.create_joints_chainlen_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    
        # self.create_joints_chainlen_value = QtWidgets.QLabel(str(self.create_joints_chainlen_slider.value()))
        # create_joints_chainlen_layout.addWidget(self.create_joints_chainlen_value)

        # self.create_joints_chainlen_slider.valueChanged.connect(self.update_chainlen_slider_value)
        
        # Name Row
        create_joints_input_label = QtWidgets.QLabel("Input name:")
        self.create_joints_input_lineedit = QtWidgets.QLineEdit()
        create_joints_input_checklabel = QtWidgets.QLabel("Has end label")
        self.create_joints_input_checkbox = QtWidgets.QCheckBox()

        # Button Row
        self.create_joints_button = QtWidgets.QPushButton("Create Chain")
        self.create_joints_button.clicked.connect(self.on_create_chain)
        self.create_joints_button.setToolTip(create_joints.create_joints.__doc__)

        # --------------------------------------
        # Snap to Parent & Snap to Average Tools
        # --------------------------------------

        self.stp_button = QtWidgets.QPushButton("Snap To Parent")
        self.stp_button.clicked.connect(self.on_snap_to_parent)
        self.stp_button.setToolTip(snap_to_parent.snap_to_parent.__doc__)

        self.sta_button = QtWidgets.QPushButton("Snap To Average")
        self.sta_button.clicked.connect(self.on_snap_to_average)
        self.sta_button.setToolTip(snap_to_average.snap_to_average.__doc__)
        
        # ---------------------
        # Joint Operations Grid
        # ---------------------

        self.sel_hie_button = QtWidgets.QPushButton("Select Hierarchy")
        self.sel_hie_button.clicked.connect(self.on_select_hierarchy)
        self.sel_hie_button.setToolTip(select_hierarchy.select_hierarchy.__doc__)
        
     
        self.del_his_button = QtWidgets.QPushButton("Delete History")
        self.del_his_button.clicked.connect(self.on_delete_history)
        self.del_his_button.setToolTip(delete_history.delete_history.__doc__)

        self.fre_trf_button = QtWidgets.QPushButton("Freeze Transforms")
        self.fre_trf_button.clicked.connect(self.on_freeze_transforms)
        self.fre_trf_button.setToolTip(freeze_transforms.freeze_transforms.__doc__)

        self.show_lra_button = QtWidgets.QPushButton("Toggle LRA")
        self.show_lra_button.clicked.connect(self.on_toggle_lra)
        self.show_lra_button.setToolTip(toggle_lra.toggle_lra.__doc__)

        # --------------
        # Create Locator
        # --------------

        self.crt_loc_button = QtWidgets.QPushButton("Create Locator at Selection")
        self.crt_loc_button.clicked.connect(self.on_create_locator)
        self.crt_loc_button.setToolTip(create_locator.create_locator.__doc__)
       
        # -------------
        # Window Layout
        # -------------

        # Create Joints Widget
        create_joints_layout = QtWidgets.QVBoxLayout()
        
        ## Chain length
        cj_chainlen_layout = QtWidgets.QHBoxLayout()
        cj_chainlen_layout.addWidget(create_joints_chainlen_label)
        cj_chainlen_layout.addWidget(self.create_joints_chainlen_slider)
        create_joints_layout.addLayout(cj_chainlen_layout)

        ## Name Generation
        cj_name_layout = QtWidgets.QHBoxLayout()
        cj_name_layout.addWidget(create_joints_input_label)
        cj_name_layout.addWidget(self.create_joints_input_lineedit)
        cj_name_layout.addWidget(create_joints_input_checklabel)
        cj_name_layout.addWidget(self.create_joints_input_checkbox)
        create_joints_layout.addLayout(cj_name_layout)

        ## Button
        cj_button_layout = QtWidgets.QHBoxLayout()
        cj_button_layout.addWidget(self.create_joints_button)
        create_joints_layout.addLayout(cj_button_layout)

        main_layout.addLayout(create_joints_layout)

        # Snaps Widget
        snaps_layout = QtWidgets.QHBoxLayout()
        snaps_layout.addWidget(self.sta_button)
        snaps_layout.addWidget(self.stp_button)

        main_layout.addLayout(snaps_layout)

        # Joints Operations
        jo_layout = QtWidgets.QGridLayout()
        jo_layout.addWidget(self.sel_hie_button, 0, 0)
        jo_layout.addWidget(self.del_his_button, 0, 1)
        jo_layout.addWidget(self.fre_trf_button, 1, 0)
        jo_layout.addWidget(self.show_lra_button, 1, 1)

        main_layout.addLayout(jo_layout)

        # Create Locator
        crtloc_layout = QtWidgets.QVBoxLayout()
        crtloc_layout.addWidget(self.crt_loc_button)
        
        main_layout.addLayout(crtloc_layout)
        
        # Stretch for everything
        main_layout.addStretch(1)

    # -------
    # Methods
    # -------
    # def update_chainlen_slider_value(self, value):
    #    self.create_joints_chainlen_value.setText(str(value))

    def on_create_chain(self):
        # Gets values from widgets
        joint_count = self.create_joints_chainlen_slider.value()
        base_name = self.create_joints_input_lineedit.text()
        add_affix = self.create_joints_input_checkbox.isChecked()

        import importlib
        import mtoolbox.tools.create_joints as create_joints
        create_joints.create_joints(joint_count, base_name, add_affix)
    
    def on_snap_to_parent(self):
        import importlib
        import mtoolbox.tools.snap_to_parent as snap_to_parent
        snap_to_parent.snap_to_parent()

    def on_snap_to_average(self):
        import importlib
        import mtoolbox.tools.snap_to_average as snap_to_average
        snap_to_average.snap_to_average()

    def on_select_hierarchy(self):
        import importlib
        import mtoolbox.tools.select_hierarchy as select_hierarchy
        select_hierarchy.select_hierarchy()

    def on_delete_history(self):
        import importlib
        import mtoolbox.tools.delete_history as delete_history
        delete_history.delete_history()

    def on_freeze_transforms(self):
        import importlib
        import mtoolbox.tools.freeze_transforms as freeze_transforms
        freeze_transforms.freeze_transforms()
    
    def on_toggle_lra(self):
        import importlib
        import mtoolbox.tools.toggle_lra as toggle_lra
        toggle_lra.toggle_lra()
    
    def on_create_locator(self):
        import importlib
        import mtoolbox.tools.create_locator as create_locator
        create_locator.create_locator()


# -------
# Show UI
# -------
def show_ui():
    global win

    maya_parent = get_maya_main_window()

    try:
        win.close()
        win.deleteLater()
    except NameError:
        pass

    win = MToolboxUI(parent=maya_parent)
    win.show()