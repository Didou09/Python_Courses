# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
import numpy as np
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.gen_data()
        self.create_main_frame()
        self.compute_initial_figure()

    def create_main_frame(self):
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        self.fig  = Figure((5.0, 4.0), dpi=100)
        self.axes = self.fig.add_subplot(111)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_widget)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()

        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_widget)

        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        layout1 = QtWidgets.QVBoxLayout(self.main_widget)
        
        layout1.addWidget(self.mpl_toolbar)
        layout1.addWidget(self.canvas)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setValue(0)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(lambda: self.update_figure())

        layout2 = QtWidgets.QHBoxLayout(self.main_widget)

        self.lab1    = QtWidgets.QLabel('Order polynomial:')
        self.cb_grid = QtWidgets.QCheckBox('Grid')
        self.cb_grid.setChecked(False)
        self.cb_grid.stateChanged.connect(lambda: self.on_cb_grid(self.cb_grid))

        layout2.addStretch()
        layout2.addWidget(self.lab1)
        layout2.addWidget(self.slider)
        layout2.addWidget(self.cb_grid)
        layout2.addStretch()

        layout1.addLayout(layout2)
        
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("Matplotlib", 2000)

    def gen_data(self, *args, **kwargs):
        self.xcoord = np.linspace(-10, 10, 1000)

    def compute_initial_figure(self):
        #self.fig.clear()
        self.plt1, = self.axes.plot(self.xcoord, self.xcoord**0, 'r')
        self.canvas.draw()

    def update_figure(self):
        l = self.slider.value()
        self.plt1.set_ydata(self.xcoord**l)
        self.axes.relim()
        self.axes.autoscale_view(scalex=False)
        self.canvas.draw()

    def on_cb_grid(self, event):
        if (event.isChecked()):
            self.axes.minorticks_on()
            self.axes.grid(b=True, which='major', linestyle='-', \
                           linewidth=0.5)
            self.axes.grid(b=True, which='minor', linestyle=':', \
                                  linewidth=0.2)
        else:
            self.axes.minorticks_off()
            self.axes.grid(b=False)
        self.canvas.draw()

    def on_key_press(self, event):
        print('you pressed', event.key)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen

This program is a simple example of a Qt5 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.

This is modified from the embedding in qt4 example to show the difference
between qt4 and qt5"""
                                )

def main():
    qApp = QtWidgets.QApplication(sys.argv)
    
    aw = ApplicationWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())

if __name__ == '__main__':
    main()
