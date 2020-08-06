
import app
import os

if __name__ == "__main__":
    port = os.environ.get('PORT', 8080)
    app = app.create_app()
    app.run(host='0.0.0.0', port=port, threaded=True)
