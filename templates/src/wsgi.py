from main import app

import os

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host="0.0.0.0", debug=False)
