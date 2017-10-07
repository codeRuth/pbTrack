import os
from pb import app

port = int(os.environ.get('PORT', 8000))
app.run(port=port)
