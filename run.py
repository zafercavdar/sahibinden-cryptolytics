from src.logging import setup_logging
from src.ML. SVR import SVR_rbf
from src.REST.fetch_data import get_history, get_current_value
from flask import Flask
from flask import render_template
import numpy as np
app = Flask(__name__)


@app.route("/")
def main_chart():
    setup_logging()
    data_count = 300
    data = get_history()[-data_count:]
    current = get_current_value()
    X = [d[0] for d in data]
    y = [d[1] for d in data]
    model = SVR_rbf(X, y)
    X.append(max(X) + 1)
    X = np.array(X).reshape(-1, 1)
    y_predicted_all = model.predict(X)
    y_predicted = y_predicted_all[-1]
    print("Current: {}".format(current))
    print("Predicted: {}".format(y_predicted))
    y.append(current)
    return render_template('line_chart.html', labels=list(X), values=y_predicted_all, values_real=y
                           , legend1="Estimated", legend2="Real", estimated=y_predicted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
