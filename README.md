## Cryptolytics

# Dependencies
  numpy >= 1.13.3
  scipy >= 1.0.0
  scikit-learn >= 0.19.1
  redis >= 2.10.5
  flask >= 0.12.2

# Install and run
  Run `make dev` to create Docker images and containers. `make dev` will also install dependencies.
  Visit [http://localhost:5002](http://localhost:5002) to reach web server.

# How it works
  Cryptolytics integrates various ML algorithms from `sklearn` with the data provided from
  devakademi.com endpoint. Once the Flask app is built in Docker and a user routed "/" on port 5002,
  Flask renders my `line_chart.html` file in `/templates`.

  `line_chart.html` file includes data fetching and chart plotting scripts along with update function.
  In the web app, current value of scoin is updated every 10 seconds and decision is calculated according to
  new coin value.

  Support Vector Regressor with a radial basis function is trained with historical data of scoin and
  estimated value is calculated from this model.

# Developer(s)
  Zafer Cavdar (zafercavdar)

# Contribute
  Just make a new branch and open PR.
