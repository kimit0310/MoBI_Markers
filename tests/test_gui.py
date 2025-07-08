"""Test suite for GUI components.

This module contains tests for the GUI components of the MoBI Marker
application, including the LSL stream thread and main window.

Functions:
    test_lsl_stream_thread_initialization: Tests LSL stream thread initialization.
    test_gui_window_initialization: Tests GUI window initialization.
    test_send_quick_marker: Tests quick marker sending through LSL stream.
"""

from unittest.mock import patch


def test_lsl_stream_thread_initialization() -> None:
    """Test that LSLStreamThread can be initialized.
    
    Verifies that the LSL stream thread can be created with proper
    initial state (no outlet or stream_info).
    
    Returns:
        None
        
    Raises:
        AssertionError: If the thread is not initialized correctly.
    """
    with patch("mobi_marker.gui.StreamInfo"), patch("mobi_marker.gui.StreamOutlet"):
        from mobi_marker.gui import LSLStreamThread

        thread = LSLStreamThread()

        assert thread.outlet is None
        assert thread.stream_info is None


def test_gui_window_initialization() -> None:
    """Test that the GUI window can be initialized without showing.
    
    Verifies that the main GUI window can be created without displaying
    it, using mocked dependencies to avoid Qt application requirements.
    
    Returns:
        None
        
    Raises:
        AssertionError: If the GUI window is not initialized correctly.
    """
    with (
        patch("mobi_marker.gui.QApplication"),
        patch("mobi_marker.gui.QMainWindow.__init__"),
        patch("mobi_marker.gui.MobiMarkerGUI.init_ui"),
        patch("mobi_marker.gui.MobiMarkerGUI.start_lsl_stream"),
    ):
        from mobi_marker.gui import MobiMarkerGUI

        gui = MobiMarkerGUI()

        assert gui is not None


def test_send_quick_marker() -> None:
    """Test that quick markers can be sent through the LSL stream.
    
    Verifies that the send_quick_marker method correctly sends predefined
    markers through the LSL stream thread.
    
    Returns:
        None
        
    Raises:
        AssertionError: If the quick marker functionality doesn't work correctly.
    """
    with (
        patch("mobi_marker.gui.QApplication"),
        patch("mobi_marker.gui.QMainWindow.__init__"),
        patch("mobi_marker.gui.MobiMarkerGUI.init_ui"),
        patch("mobi_marker.gui.MobiMarkerGUI.start_lsl_stream"),
    ):
        from unittest.mock import Mock

        from mobi_marker.gui import LSLStreamThread, MobiMarkerGUI

        gui = MobiMarkerGUI()
        mock_thread = Mock(spec=LSLStreamThread)
        gui.lsl_thread = mock_thread

        gui.send_quick_marker("START")

        mock_thread.send_marker.assert_called_once_with("START")


def test_send_end_modality_marker() -> None:
    """Test that end modality markers can be sent with dropdown selection.
    
    Verifies that the send_end_modality_marker method correctly constructs
    and sends END [modality] markers based on dropdown selection.
    
    Returns:
        None
        
    Raises:
        AssertionError: If the end modality marker functionality doesn't work correctly.
    """
    with (
        patch("mobi_marker.gui.QApplication"),
        patch("mobi_marker.gui.QMainWindow.__init__"),
        patch("mobi_marker.gui.MobiMarkerGUI.init_ui"),
        patch("mobi_marker.gui.MobiMarkerGUI.start_lsl_stream"),
    ):
        from unittest.mock import Mock

        from mobi_marker.gui import LSLStreamThread, MobiMarkerGUI

        gui = MobiMarkerGUI()
        mock_thread = Mock(spec=LSLStreamThread)
        gui.lsl_thread = mock_thread
        
        mock_combo = Mock()
        mock_combo.currentText.return_value = "EEG"
        gui.modality_combo = mock_combo
        
        mock_input = Mock()
        gui.custom_modality_input = mock_input

        gui.send_end_modality_marker()

        mock_thread.send_marker.assert_called_once_with("END EEG")


def test_send_end_modality_marker_custom() -> None:
    """Test that custom end modality markers work with 'Other' selection.
    
    Verifies that when "Other" is selected, the custom input field is used
    to construct the END [modality] marker.
    
    Returns:
        None
        
    Raises:
        AssertionError: If the custom modality functionality doesn't work correctly.
    """
    with (
        patch("mobi_marker.gui.QApplication"),
        patch("mobi_marker.gui.QMainWindow.__init__"),
        patch("mobi_marker.gui.MobiMarkerGUI.init_ui"),
        patch("mobi_marker.gui.MobiMarkerGUI.start_lsl_stream"),
    ):
        from unittest.mock import Mock

        from mobi_marker.gui import LSLStreamThread, MobiMarkerGUI

        gui = MobiMarkerGUI()
        mock_thread = Mock(spec=LSLStreamThread)
        gui.lsl_thread = mock_thread
        
        mock_combo = Mock()
        mock_combo.currentText.return_value = "Other"
        gui.modality_combo = mock_combo
        
        mock_input = Mock()
        mock_input.text.return_value.strip.return_value = "Custom Sensor"
        gui.custom_modality_input = mock_input

        gui.send_end_modality_marker()

        mock_thread.send_marker.assert_called_once_with("END CUSTOM SENSOR")
