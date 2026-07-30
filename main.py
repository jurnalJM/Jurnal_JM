#!/usr/bin/env python3
"""
JayaMotor - Main Application Entry Point

This is the main entry point for the JayaMotor application.
Initializes the database and launches the GUI.
"""

import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from config import APP_TITLE, APP_VERSION, DEBUG, LOG_LEVEL, LOG_FILE, LOG_FORMAT
from database.connection import DatabaseManager
from database.schema import initialize_database

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def setup_application():
    """Setup application before launching GUI"""
    logger.info(f"Starting {APP_TITLE} v{APP_VERSION}")

    # Initialize database
    try:
        logger.info("Initializing database...")
        initialize_database()
        logger.info("[OK] Database initialized")
    except FileExistsError:
        # Database already exists, just connect
        logger.info("Connecting to existing database...")
        DatabaseManager.initialize()
        logger.info("[OK] Database connected")
    except Exception as e:
        logger.error(f"[ERROR] Failed to initialize database: {e}")
        raise


def launch_gui():
    """Launch the GUI application"""
    try:
        from PyQt6.QtWidgets import QApplication
        from ui.main_window import MainWindow

        logger.info("Launching GUI...")

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()

        logger.info("[OK] GUI launched successfully")
        sys.exit(app.exec())

    except ImportError as e:
        logger.error(f"[ERROR] GUI import error: {e}")
        logger.error("Make sure PyQt6 is installed: pip install PyQt6")
        sys.exit(1)
    except Exception as e:
        logger.error(f"[ERROR] Error launching GUI: {e}")
        sys.exit(1)


def main():
    """Main application entry point"""
    try:
        logger.info("=" * 70)
        logger.info(f"{APP_TITLE} v{APP_VERSION}")
        logger.info("=" * 70)

        # Setup application
        setup_application()

        # Launch GUI
        launch_gui()

    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
