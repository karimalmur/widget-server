from flask import Flask, make_response, request


app = Flask(__name__, static_url_path='/examples', static_folder='build')


WEATHER_DATA = {
  "1": {
    'location': 'San Francisco',
    'image': 'http://localhost:5000/examples/partly_cloudy.png',
    'temp': 78,
    'desc': 'Partly Cloudy'
  }
}


@app.route('/')
def home():
  return 'hello world'


@app.route('/widget.js')
def weather_widget():
  zip = request.args.get('zip')
  data = WEATHER_DATA[zip]

  out = '''
    const container = document.getElementById('container')
    container.innerHTML = (
      '<div>' +
      '  <p>%s<p>' +
      '  <img src="%s" />' +
      '  <p><strong>%s &deg;F</strong> &mdash; %s</p>' +
      '</div>'
    )
  ''' % (data['location'], data['image'], data['temp'], data['desc'])

  response = make_response(out)
  response.headers['Content-Type'] = 'application/javascript'

  return response
