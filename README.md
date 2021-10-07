# This is the Flask server template for NSG @ http://karaik.me/NSG-Demo/
### About the NSG-Demo
- The purpose of this application @ http://karaik.me/NSG-Demo/ is to allow researchers or students or anyone to easily create network security game demo and to play it.
- It contains 2 main pages, "Play" and "Create".
### About this Template
- It is required for you to first generate the json file by creating a game using the link above.
- misc.py contains the code to parse the data in the json file.
   - It contains the function parseJsonData that generates input for the game, such as graph, attacker and defenders postions etc...
   - This can also be used for generating input data while training the model.
- app.py is the code for the flask server.
  - It will first utilise parseJsonData to parse the json file and generate input data.
  - You'll be required to initialise your own defenders, model and environment etc...
  - It contains 2 main functions, reset and move.
  - The reset function is to initialise the game. Upon success, it should return {'success':True} as the response.
  - The move function takes in the attacker's new postion via the GET Request param, and you'll be required to generate the new defenders' positions and return in the response.
  - The return response should look like {'success':True, 'defenders':[2,4,9]} where the array [2,4,9] represents the new positions of the defenders.