import requests #this package sends a request to our URL and which responds with the HTML content
from bs4 import BeautifulSoup #this is the package that we will use to navigate through our HTML code
import pandas as pd #this is to structure our data into a dataframe
import re
import string
import numpy as np
import time #best practice to pause between each request so the site doesn't flag us as a bot
