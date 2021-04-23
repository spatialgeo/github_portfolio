# github_portfolio
<h2>Portfolio of my programming work</h2>
<p>The files contained within the portoflio consist of: </p>
<ul> This Readme file </ul>
<ul> An in.csv </ul>
<ul> The Agents Framework </ul>
<ul> The Agents Model </ul>
<p>The Agents Framework contains a subscript used by the Agents Model to generate the random coordinates and random movement of agents through the environment. 
It does this by way of the 'def' keyword and the 'init', 'str', 'move', and 'eat' functions to set the x and y values, the agents class and the environment, then move these
agents using random.random, before the agents 'eat' themselves. </p>

<p>The Agents Model is the main part of the portfolio code, responsible for the following:</p>
<ul> Importing the nessessary libaries </ul>
<ul> Starting a process timer to monitor the efficency of the code </ul>
<ul> Setting the model seed, the number of agents and the number of interations to be used </ul>
<ul> Setting the Agents list </ul>
<ul> Opening and reading in CSV files </ul>
<ul> The creation of a distance function to analyse the distance between agents </ul>
<ul> The creation of the agents </ul>
<ul> The call to move the agents </ul>
<ul> Ploting of the agents on a raster </ul>
