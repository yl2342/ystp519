"""
Entry point for the Yale Trading Simulation Platform application.
This script creates and runs the Flask application.
"""
import os
from app import create_app

# Create the application using the factory function
app = create_app()

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.environ.get("PORT", 5000))
    # Run the application with the appropriate host and port
    app.run(host="0.0.0.0", port=port, debug=False) 