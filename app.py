from flask import Flask, render_template

app = Flask(__name__)

JOBS = [ {
          'id' : 1,
          'title' : 'Data Scientist',
          'location' : 'Bengaluru',
          'salary' : '10lpa'
          },
        {
          'id' : 2,
          'title' : 'Data Engineer',
          'location' : 'Bengaluru',
          'salary' : '12lpa'
          },
        {
          'id' : 3,
          'title' : 'Data Scientist (intern)',
          'location' : 'Bengaluru',
          
          },
        {
          'id' : 4,
          'title' : 'Fullstack Developer',
          'location' : 'Kolkata',
          'salary' : '15lpa'
          }
       ]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs= JOBS)

if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
