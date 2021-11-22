# Spanish-Conjugator
A simple Flask app which allows you to enter any Spanish verb and obtain its meaning and various conjugations.
![Website Demo](https://github.com/VarunPatelius/Spanish-Conjugator/blob/main/github/websiteDemo.gif)

## About
Spanish-Conjugator is a site built out of my need for an application which could give me quick access to important Spanish verb data.
I did not like how sites like [SpanishDict](https://www.spanishdict.com/) contained ads and various bits of information that were no use to me.

Spanish-Conjugator works by scraping data from the SpanishDict website, so you get what you need - no ads, no nonsense!

## Installation
The following steps show how to get Spanish-Dict up and running on your own machine.

1. Begin by cloning the repository or downloading the .zip file to your device
2. Change directory into the cloned/downloaded folder
```bash
cd PATH/TO/FOLDER/Spanish-Conjugator
```
3. Create a virtual environment within the folder 
```bash
python3 -m venv venv (or any name you want to give to the virtual environment)
```
4. Activate the virtual environment
```bash
source venv/bin/activate
```
5. Install all the dependencies necessary for Spanish-Conjugator
```bash
pip3 install -r requirements.txt
```
6. Run the program
```bash
python3 main.py
```
* The development server should be running at 0.0.0.0 at port 8000. This can be changed in main.py.

## Technologies
* [Requests](https://docs.python-requests.org/en/master/index.html) - Get data from SpanishDict
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Used to create webapp
* [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) - Used to parse HTML