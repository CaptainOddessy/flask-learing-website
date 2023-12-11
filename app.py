from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
}, {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'London'
}, {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'San Francisco',
    'salary': '$80,000'
}, {
    'id': 4,
    'title': 'Web Developer',
    'location': 'Berlin',
    'salary': '$90,000'
}, {
    'id': 5,
    'title': 'Machine Learning Engineer',
    'location': 'Bangalore',
    'salary': '$150,000'
}]


@app.route('/')
def hello_world():
  return render_template('index.html', jobs=JOBS)


@app.route('/api/jobs')
def new_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)