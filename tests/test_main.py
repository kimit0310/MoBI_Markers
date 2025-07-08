"""Test suite for the MoBI Marker application.

This module contains tests for the main entry points and basic functionality
of the MoBI Marker application.

Functions:
    test_import: Tests that the main function can be imported successfully.
"""


def test_import() -> None:
    """Test that the main function can be imported.
    
    Verifies that the main function is accessible and callable from
    the mobi_marker package.
    
    Returns:
        None
        
    Raises:
        ImportError: If the main function cannot be imported.
        AssertionError: If the main function is not callable.
    """
    from mobi_marker import main

    assert callable(main)
