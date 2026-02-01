import PySide2, shiboken2, sys, os
from PySide2 import QtWidgets, QtCore, QtGui
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from madtools import tools

toolbox_path = os.path.join(cmds.internalVar(userScriptDir=True), 'madtools')
if toolbox_path not in sys.path:
    sys.path.append(toolbox_path)

def get_maya_main_window():
    """
    Returns Maya window as QWidget
    """
    qt_pointer = omui.MQtUtil.mainWindow()
    maya_parent = shiboken2.wrapInstance(int(qt_pointer), QtWidgets.QWidget)

    return maya_parent


class madtoolsUI(QtWidgets.QDialog):
    """
    Main window definition
    """
    def __init__(self, parent=None):
        super(madtoolsUI, self).__init__(parent)
        self.setWindowTitle("madTools v.1.1.0")
        
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

        self.create_joints_chainlen_value = QtWidgets.QLabel(
            str(self.create_joints_chainlen_slider.value()))

        self.create_joints_chainlen_slider.valueChanged.connect(self.update_chainlen_slider_value)        
        # Name Row
        create_joints_input_label = QtWidgets.QLabel("Input name:")
        self.create_joints_input_lineedit = QtWidgets.QLineEdit()
        self.create_joints_affix_lineedit = QtWidgets.QLineEdit()
        create_joints_input_checklabel = QtWidgets.QLabel("End label:")
        self.create_joints_input_checkbox = QtWidgets.QCheckBox()

        # Button Row
        self.create_joints_button = QtWidgets.QPushButton("Create Chain")
        self.create_joints_button.clicked.connect(self.on_create_chain)
        self.create_joints_button.setToolTip(tools.create_joints.__doc__)

        # --------------------------------------
        # Snap/Spatial Ops
        # --------------------------------------

        self.stp_button = QtWidgets.QPushButton("Snap To Parent")
        self.stp_button.clicked.connect(self.on_snap_to_parent)
        self.stp_button.setToolTip(tools.snap_to_parent.__doc__)

        self.sta_button = QtWidgets.QPushButton("Snap To Average")
        self.sta_button.clicked.connect(self.on_snap_to_average)
        self.sta_button.setToolTip(tools.snap_to_average.__doc__)

        self.poi_to_avg_buttton = QtWidgets.QPushButton("Point To Average")
        self.poi_to_avg_buttton.clicked.connect(self.on_point_to_average)
        self.poi_to_avg_buttton.setToolTip(tools.point_to_average.__doc__)

        self.fre_trf_button = QtWidgets.QPushButton("Freeze Transforms")
        self.fre_trf_button.clicked.connect(self.on_freeze_transforms)
        self.fre_trf_button.setToolTip(tools.freeze_transforms.__doc__)


        # -------------------
        # Selection & Cleanup
        # -------------------
        
        self.sel_hie_button = QtWidgets.QPushButton("Select Hierarchy")
        self.sel_hie_button.clicked.connect(self.on_select_hierarchy)
        self.sel_hie_button.setToolTip(tools.select_hierarchy.__doc__)
     
        self.del_his_button = QtWidgets.QPushButton("Delete History")
        self.del_his_button.clicked.connect(self.on_delete_history)
        self.del_his_button.setToolTip(tools.delete_history.__doc__)

        # ---------------------
        # Joint Operations Grid
        # ---------------------

        self.show_lra_button = QtWidgets.QPushButton("Toggle LRA")
        self.show_lra_button.clicked.connect(self.on_toggle_lra)
        self.show_lra_button.setToolTip(tools.toggle_lra.__doc__)

        self.joint_zso_button = QtWidgets.QPushButton("Joint ZSO")
        self.joint_zso_button.clicked.connect(self.on_joint_zso)
        self.joint_zso_button.setToolTip(tools.joint_zso.__doc__)

        # --------------
        # Create Locator
        # --------------

        self.crt_loc_button = QtWidgets.QPushButton("Create Locator at Selection")
        self.crt_loc_button.clicked.connect(self.on_create_locator)
        self.crt_loc_button.setToolTip(tools.create_locator.__doc__)

        # --------
        # Make ROM
        # --------

        self.make_rom_button = QtWidgets.QPushButton("Make ROM Keyframes")
        self.make_rom_button.clicked.connect(self.on_make_rom)
        self.make_rom_button.setToolTip(tools.make_rom.__doc__)

        # -------------
        # Window Layout
        # -------------

        # Create Joints Widget
        create_joints_layout = QtWidgets.QVBoxLayout()
        
        ## Chain length
        cj_chainlen_layout = QtWidgets.QHBoxLayout()
        cj_chainlen_layout.addWidget(create_joints_chainlen_label)
        cj_chainlen_layout.addWidget(self.create_joints_chainlen_value)
        cj_chainlen_layout.addWidget(self.create_joints_chainlen_slider)
        create_joints_layout.addLayout(cj_chainlen_layout)

        ## Name Generation
        cj_name_layout = QtWidgets.QHBoxLayout()
        cj_name_layout.addWidget(create_joints_input_label)
        cj_name_layout.addWidget(self.create_joints_input_lineedit)
        cj_name_layout.addWidget(self.create_joints_affix_lineedit)
        cj_name_layout.addWidget(create_joints_input_checklabel)
        cj_name_layout.addWidget(self.create_joints_input_checkbox)
        create_joints_layout.addLayout(cj_name_layout)

        ## Button
        cj_button_layout = QtWidgets.QHBoxLayout()
        cj_button_layout.addWidget(self.create_joints_button)
        create_joints_layout.addLayout(cj_button_layout)

        main_layout.addLayout(create_joints_layout)

        # Snaps/Spatial Operation Grid
        snaps_layout = QtWidgets.QGridLayout()
        snaps_layout.addWidget(self.sta_button, 0, 0)
        snaps_layout.addWidget(self.poi_to_avg_buttton, 0, 1)
        snaps_layout.addWidget(self.stp_button, 1, 0)
        snaps_layout.addWidget(self.fre_trf_button, 1, 1)

        main_layout.addLayout(snaps_layout)

        # Selection & Cleanup Grid
        selections_layout = QtWidgets.QGridLayout()
        selections_layout.addWidget(self.sel_hie_button, 0, 0)
        selections_layout.addWidget(self.del_his_button, 0, 1)

        main_layout.addLayout(selections_layout)

        # Joints Operations Grid
        jo_layout = QtWidgets.QGridLayout()
        jo_layout.addWidget(self.show_lra_button, 0, 0)
        jo_layout.addWidget(self.joint_zso_button, 0, 1)

        main_layout.addLayout(jo_layout)

        # Create Locator
        crtloc_layout = QtWidgets.QVBoxLayout()
        crtloc_layout.addWidget(self.crt_loc_button)
        
        main_layout.addLayout(crtloc_layout)

        # Make ROM

        make_rom_layout = QtWidgets.QVBoxLayout()
        make_rom_layout.addWidget(self.make_rom_button)

        main_layout.addLayout(make_rom_layout)
        
        # Stretch for everything
        main_layout.addStretch(1)

        self.create_joints_input_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setFocus()

    # -------
    # Methods
    # -------
    
    def update_chainlen_slider_value(self, value):
        self.create_joints_chainlen_value.setText(str(value))

    def on_create_chain(self):
        # Gets values from widgets
        joint_count = self.create_joints_chainlen_slider.value()
        base_name = self.create_joints_input_lineedit.text()
        affix = self.create_joints_affix_lineedit.text()
        add_end = self.create_joints_input_checkbox.isChecked()

        tools.create_joints(joint_count, base_name, affix, add_end)
    
    def on_snap_to_parent(self):
        import importlib
        import tools.snap_to_parent as snap_to_parent
        tools.snap_to_parent()

    def on_snap_to_average(self):
        import importlib
        import tools.snap_to_average as snap_to_average
        tools.snap_to_average()

    def on_select_hierarchy(self):
        import importlib
        import tools.select_hierarchy as select_hierarchy
        tools.select_hierarchy()

    def on_delete_history(self):
        import importlib
        import tools.delete_history as delete_history
        tools.delete_history()

    def on_freeze_transforms(self):
        import importlib
        import tools.freeze_transforms as freeze_transforms
        tools.freeze_transforms()
    
    def on_toggle_lra(self):
        import importlib
        import tools.toggle_lra as toggle_lra
        tools.toggle_lra()
    
    def on_create_locator(self):
        import importlib
        import tools.create_locator as create_locator
        tools.create_locator()
    
    def on_joint_zso(self):
        import importlib
        import tools.joint_zso as joint_zso
        tools.joint_zso()

    def on_point_to_average(self):
        import importlib
        import tools.point_to_average as point_to_average
        tools.point_to_average()

    def on_make_rom(self):
        import importlib
        import tools.make_rom as make_rom
        tools.make_rom()


# -------
# Show UI
# -------
def show_ui():
    global win

    maya_parent = get_maya_main_window()

    try:
        win.close()
        win.deleteLater()
    except (NameError, RuntimeError):
        pass

    win = madtoolsUI(parent=maya_parent)
    win.show()
