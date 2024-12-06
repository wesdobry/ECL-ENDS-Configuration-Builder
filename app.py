
import logging
from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)


@app.route('/')
def endsconfigbuilder():
    app.logger.info("/ends accessed")
    return render_template('endsconfig.html')

if __name__ == '__main__':
    app.run(debug=False)
