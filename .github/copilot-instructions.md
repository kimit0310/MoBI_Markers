<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# MoBI Marker Project Instructions

This is a Python GUI application for sending LSL (Lab Streaming Layer) markers used in neuroscience research.

## Project Structure
- Uses `uv` for dependency management
- Follows the Child Mind Institute Python template structure
- GUI built with PySide6 (Qt6 for Python)
- LSL integration using pylsl

## Key Components
- `src/mobi_marker/gui.py`: Main GUI application with LSL stream management
- `src/mobi_marker/main.py`: CLI entry point
- Uses threading for LSL stream management to keep GUI responsive

## Development Guidelines
- Follow Google docstring style for documentation
- Use type hints for all function parameters and return values
- Keep GUI responsive by using QThread for LSL operations
- Handle errors gracefully with user-friendly status messages

## Dependencies
- PySide6: GUI framework
- pylsl: Lab Streaming Layer interface
- Development tools: ruff, mypy, pytest, pre-commit

## Code Style
- Line length: 88 characters
- Use ruff for linting and formatting
- Follow PEP 8 guidelines
- Use type annotations consistently
