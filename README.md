## This is the Flask server template for NSG @ http://karaik.me/NSG-Demo/
### About the NSG-Demo
- The purpose of this application @ http://karaik.me/NSG-Demo/ is to allow researchers or students or anyone to easily create network security game demo and to play it.
- This demo is for users to play as attacker, and to train models to simulate the defenders to prevent the attacker from escaping.

- It contains 2 main pages, "Play" and "Create".

- To create a game, you can click on the create tab on the menu.

![nsg_create](https://user-images.githubusercontent.com/50904993/136340102-1afa6ede-1c30-444d-8cd6-79ae188fdbb0.PNG)
- Above is the page to create the game. You can add/delete nodes, defenders etc..
- Once you are done creating the game, you can click on generate file to generate a json file that contains the data of the game you have create. 

<img src="https://user-images.githubusercontent.com/50904993/136340054-64749e65-cdee-4b42-9c43-b1cf3eb37465.PNG" width="500" height="700" />

- This json file also contains the graph data which you can use to train your model etc... You can utilise the misc.py in this repo to parse the json file.

- To play the game, you can click on the play tab on the menu.

![nsg_play_render](https://user-images.githubusercontent.com/50904993/136340064-322f2a00-7a19-46ae-9c18-5a315724b63c.PNG)

- Above is the image to play the game.
- You'll be required to first upload the json file and render the graph, and the graph will appear as shown above.

![nsg_play](https://user-images.githubusercontent.com/50904993/136340093-8b215dd8-32ef-421c-be87-941435357ea0.PNG)

- In this demo, attacker will interate with the AI model or environment via REST API. You can utilise this template to create a server that can interate with this demo.
- You can then input your server URL to play the game.
- You can refer to the information below to learn more about the API request format etc...
- You can refer to https://github.com/limkaraik/NSG-sample-server which is a sample server I have set up. It also contains the json file which you can use to render the graph and play the game as well.

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
  - The return response should look like {'success':True, 'defenders':[2,4,9]} where the array [2,4,9] represents the new positions of the defenders if you have 3 defenders. Note that the number of defenders is not restricted to 3, but it needs to be more than 0.
  - You can refer to this sample server https://github.com/limkaraik/NSG-sample-server
