from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME

app = Flask(__name__)

SUCCESS_TEMPLATE = """
<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{score}</div></h1>
</body>
</html>
"""

ERROR_TEMPLATE = """
<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1><div id="score" style="color:red">{error}</div></h1>
</body>
</html>
"""

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as score_file:
            score = score_file.read().strip()

        return render_template_string(SUCCESS_TEMPLATE, score=score)
    except Exception as e:
        error = f"Error reading score: {e}"
        return render_template_string(ERROR_TEMPLATE, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)