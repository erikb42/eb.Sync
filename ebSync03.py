import sys
import pyperclip
import subprocess
from os.path import expanduser
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your Code Goes Here.

        # Define Elements
        self.source_dir = "/example/dir/here"
        self.choose_source_button = qtw.QPushButton("Choose Source", clicked=self.choose_source_dir)
        self.show_source = qtw.QLineEdit(self.source_dir)

        self.dest_dir = "/your/drive/here"
        self.choose_dest_button = qtw.QPushButton("Choose Destination", clicked=self.choose_dest_dir)
        self.show_dest = qtw.QLineEdit(self.dest_dir)

        self.r_box = qtw.QCheckBox("-r: Recurisve")
        self.W_box = qtw.QCheckBox("-W: While File Copy")
        self.v_box = qtw.QCheckBox("-v: Verbose")
        self.p_box = qtw.QCheckBox("-p: Preserve Permissions")
        self.t_box = qtw.QCheckBox("-t: Preserve Time Stamps")
        self.h_box = qtw.QCheckBox("-h: human readable file formats")

        self.final_command = f'sudo rsync -rptWvh {self.source_dir} {self.dest_dir}'
        self.show_commandline = qtw.QLineEdit(self.final_command)
        self.copy_command_button = qtw.QPushButton("Copy Command", clicked=self.final_copy)
        self.run_sync_button = qtw.QPushButton("Run Sync", clicked=self.run_sync)


        # Styling
        console_font = qtg.QFont()
        console_font.setFamily("Consolas")
        
        self.show_source.setFont(console_font)
        self.show_dest.setFont(console_font)
        self.show_commandline.setFont(console_font)

        
        # Layout Parts
        check_grid = qtw.QGridLayout()
        check_grid.addWidget(self.show_source, 0, 0, 1, 2)
        check_grid.addWidget(self.show_dest, 0, 2)
        check_grid.addWidget(self.choose_source_button, 1, 0)
        check_grid.addWidget(self.choose_dest_button, 1, 2)
        check_grid.addWidget(self.r_box, 2, 0)
        check_grid.addWidget(self.W_box, 2, 1)
        check_grid.addWidget(self.v_box, 2, 2)
        check_grid.addWidget(self.p_box, 3, 0)
        check_grid.addWidget(self.t_box, 3, 1)
        check_grid.addWidget(self.h_box, 3, 2)
        check_grid.addWidget(self.show_commandline, 4, 0, 1, 3)
        check_grid.addWidget(self.copy_command_button, 5, 0)   
        check_grid.addWidget(self.run_sync_button, 5, 1)


        # Your Code ends here.
        self.setLayout(check_grid)
        self.show()

    # Functionality

    def choose_source_dir(self):
        dir_choice = qtw.QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.source_dir = dir_choice
        self.show_source.setText(self.source_dir)
        # udpate
        self.final_command = f'sudo rsync -rptWvh {self.source_dir} {self.dest_dir}'
        self.show_commandline = qtw.QLineEdit(self.final_command)
        print(self.final_command)

    def choose_dest_dir(self):
        dir_choice = qtw.QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.dest_dir = dir_choice
        self.show_dest.setText(self.dest_dir)
        # update
        self.final_command = f'sudo rsync -rptWvh {self.source_dir} {self.dest_dir}'
        self.show_commandline = qtw.QLineEdit(self.final_command)
        print(self.final_command)

    def final_copy(self):
        pyperclip.copy(self.final_command)

    def run_sync(self):
        print("Sync Starting")
        subprocess.call(["rsync", "-rptWvh", self.source_dir, self.dest_dir])

# Runs the window code.
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())