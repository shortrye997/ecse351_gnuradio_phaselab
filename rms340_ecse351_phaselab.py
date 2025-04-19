#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class rms340_ecse351_phaselab(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "rms340_ecse351_phaselab")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000
        self.phase_S2 = phase_S2 = 0
        self.phase_S1 = phase_S1 = 0
        self.freq_S2 = freq_S2 = 50
        self.freq_S1 = freq_S1 = 50
        self.amplit_S2 = amplit_S2 = 10
        self.amplit_S1 = amplit_S1 = 10
        self.Noise_amplit_S2 = Noise_amplit_S2 = 0
        self.Noise_amplit_S1 = Noise_amplit_S1 = 0

        ##################################################
        # Blocks
        ##################################################

        self._phase_S2_range = qtgui.Range(0, 360, 0.5, 0, 200)
        self._phase_S2_win = qtgui.RangeWidget(self._phase_S2_range, self.set_phase_S2, "'phase_S2'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._phase_S2_win)
        self._phase_S1_range = qtgui.Range(0, 360, 0.5, 0, 200)
        self._phase_S1_win = qtgui.RangeWidget(self._phase_S1_range, self.set_phase_S1, "'phase_S1'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._phase_S1_win)
        self._freq_S2_range = qtgui.Range(0, 500, 1, 50, 200)
        self._freq_S2_win = qtgui.RangeWidget(self._freq_S2_range, self.set_freq_S2, "'freq_S2'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_S2_win)
        self._freq_S1_range = qtgui.Range(0, 500, 1, 50, 200)
        self._freq_S1_win = qtgui.RangeWidget(self._freq_S1_range, self.set_freq_S1, "'freq_S1'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_S1_win)
        self._amplit_S2_range = qtgui.Range(0, 30, 1, 10, 200)
        self._amplit_S2_win = qtgui.RangeWidget(self._amplit_S2_range, self.set_amplit_S2, "'amplit_S2'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amplit_S2_win)
        self._amplit_S1_range = qtgui.Range(0, 30, 1, 10, 200)
        self._amplit_S1_win = qtgui.RangeWidget(self._amplit_S1_range, self.set_amplit_S1, "'amplit_S1'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amplit_S1_win)
        self._Noise_amplit_S2_range = qtgui.Range(0, 20, 1, 0, 200)
        self._Noise_amplit_S2_win = qtgui.RangeWidget(self._Noise_amplit_S2_range, self.set_Noise_amplit_S2, "'Noise_amplit_S2'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Noise_amplit_S2_win)
        self._Noise_amplit_S1_range = qtgui.Range(0, 20, 1, 0, 200)
        self._Noise_amplit_S1_win = qtgui.RangeWidget(self._Noise_amplit_S1_range, self.set_Noise_amplit_S1, "'Noise_amplit_S1'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Noise_amplit_S1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-350, 350)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Product of Signal 1 & Signal 2', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [2, 2, 2, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'black', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            4, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-250), 250)
        self.qtgui_const_sink_x_0.set_x_axis((-250), 250)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', 'Signal 1 Phase', 'Signal 2 Phase', '',
            '', '', '', '', '']
        widths = [1, 1, 2, 2, 1,
            1, 1, 1, 1, 1]
        colors = ["red", "red", "blue", "red", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [-1, -1, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c((250,-250), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c((250j,-250j), True, 1, [])
        self.blocks_throttle2_0_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.01) * samp_rate) if "time" == "time" else int(0.01), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.01) * samp_rate) if "time" == "time" else int(0.01), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.01) * samp_rate) if "time" == "time" else int(0.01), 1) )
        self.blocks_phase_shift_0_0 = blocks.phase_shift(phase_S2, False)
        self.blocks_phase_shift_0 = blocks.phase_shift(phase_S1, False)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_conjugate_cc_1 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_float_0_1 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq_S2, amplit_S2, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq_S1, amplit_S1, 0, 0)
        self.analog_fastnoise_source_x_0_0 = analog.fastnoise_source_c(analog.GR_UNIFORM, Noise_amplit_S2, 2, 8192)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_UNIFORM, Noise_amplit_S1, 0, 8192)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_fastnoise_source_x_0_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_phase_shift_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_conjugate_cc_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_phase_shift_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_throttle2_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_1, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_conjugate_cc_1, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_float_0_1, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_const_sink_x_0, 2))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.qtgui_const_sink_x_0, 3))
        self.connect((self.blocks_phase_shift_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_phase_shift_0_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_throttle2_0_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.qtgui_const_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "rms340_ecse351_phaselab")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_phase_S2(self):
        return self.phase_S2

    def set_phase_S2(self, phase_S2):
        self.phase_S2 = phase_S2
        self.blocks_phase_shift_0_0.set_shift(self.phase_S2)

    def get_phase_S1(self):
        return self.phase_S1

    def set_phase_S1(self, phase_S1):
        self.phase_S1 = phase_S1
        self.blocks_phase_shift_0.set_shift(self.phase_S1)

    def get_freq_S2(self):
        return self.freq_S2

    def set_freq_S2(self, freq_S2):
        self.freq_S2 = freq_S2
        self.analog_sig_source_x_0_0.set_frequency(self.freq_S2)

    def get_freq_S1(self):
        return self.freq_S1

    def set_freq_S1(self, freq_S1):
        self.freq_S1 = freq_S1
        self.analog_sig_source_x_0.set_frequency(self.freq_S1)

    def get_amplit_S2(self):
        return self.amplit_S2

    def set_amplit_S2(self, amplit_S2):
        self.amplit_S2 = amplit_S2
        self.analog_sig_source_x_0_0.set_amplitude(self.amplit_S2)

    def get_amplit_S1(self):
        return self.amplit_S1

    def set_amplit_S1(self, amplit_S1):
        self.amplit_S1 = amplit_S1
        self.analog_sig_source_x_0.set_amplitude(self.amplit_S1)

    def get_Noise_amplit_S2(self):
        return self.Noise_amplit_S2

    def set_Noise_amplit_S2(self, Noise_amplit_S2):
        self.Noise_amplit_S2 = Noise_amplit_S2
        self.analog_fastnoise_source_x_0_0.set_amplitude(self.Noise_amplit_S2)

    def get_Noise_amplit_S1(self):
        return self.Noise_amplit_S1

    def set_Noise_amplit_S1(self, Noise_amplit_S1):
        self.Noise_amplit_S1 = Noise_amplit_S1
        self.analog_fastnoise_source_x_0.set_amplitude(self.Noise_amplit_S1)




def main(top_block_cls=rms340_ecse351_phaselab, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
