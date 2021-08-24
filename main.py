from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


state = [
  { 
    'Name':'Andhra Pradesh',
    'Capital':'Amaravati',
    'Language':'Telugu'
  },
  {
    'Name':'Arunachal Pradesh',
    'Capital':'Itanagar',
    'Language':'English'

  },
  {
    'Name':'Assam',
    'Capital':'Dispur',
    'Language':'Assamese'
  },
  {
    'Name':'Bihar',
    'Capital':'Patna',
    'Language':'Hindi'
  },
  {
    'Name':'Chattisgarh',
    'Capital':'Raipur',
    'Language':'Chattisgarhi'
  },
  {
    'Name':'Goa',
    'Capital':'Panaji',
    'Language':'Konkani'
  },
  {
    'Name':'Gujarat',
    'Capital':'Gandhinagar',
    'Language':'Gujarati'
  },
  {
    'Name':'Haryana',
    'Capital':'Chandigarh',
    'Language':'Hindi'
  },
  {
    'Name':'Himachal Pradesh',
    'Capital':'Shimla',
    'Language':'Hindi'
  },
  {
    'Name':'Jharkhand',
    'Capital':'Ranchi',
    'Language':'Hindi'
  },
  {
    'Name':'Karnataka',
    'Capital':'Bangalore',
    'Language':'Kannada'
  },
  {
    'Name':'Kerala',
    'Capital':'Trivandrum',
    'Language':'Malayalam'
  },
  {
    'Name':'Madhya Pradesh',
    'Capital':'Bhopal',
    'Language':'Hindi'
  },
  {
    'Name':'Maharashtra',
    'Capital':'Mumbai',
    'Language':'Marathi'
  },
  {
    'Name':'Manipur',
    'Captial':'Imphal',
    'Language':'Manipuri'
  },
  {
    'Name':'Meghalaya',
    'Capital':'Shillong',
    'Language':'English'
  },
  {
    'Name':'Mizoram',
    'Captial':'Aizawl',
    'Language':'Mizo'
  },
  {
    'Name':'Nagaland',
    'Captial':'Kohima',
    'Language':'English'
  },
  {
    'Name':'Odisha',
    'Capital':'Bhubaneshwar',
    'Language':'Oriya'
  },
  {
    'Name':'Punjab',
    'Capital':'Chandigarh',
    'Language':'Punjabi'

  },
  {
    'Name':'Rajasthan',
    'Capital':'Jaipur',
    'Language':'Hindi'
  },
  {
    'Name':'Sikkim',
    'Capital':'Gangtok',
    'Language':'Nepali'
  },
  {
  
  }

  


]

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(state)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)