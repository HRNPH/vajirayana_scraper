import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import re


class Scraper:
    """
    Scraper for vajirayana.org
    """
    def __init__(self, data_path:str=None):
      """
      :param data_path: path to save the data if not set, default to ./data
      """      
      self.data_path = data_path
      if data_path is None:
        self.data_path = './data'
        print('Data Path is None, Set to Default: ./data')
      if not os.path.exists(self.data_path):
        os.mkdir(self.data_path)
        print(f'Create Directory: {self.data_path}')
    
    def clean_text(self, text:str) -> str:
      """
      :param text: text to clean
      :return: cleaned text
      """
      # delete all text that isn't thai and space
      text = re.sub(r'[^ก-๙ ]', '', str(text))
      text = text.replace('๏', '')
      return text.strip()
    
    def scrape(self, src:str, strip_first_section:bool=True) -> None:
      """
      :param src: url of the literature page
      :param strip_first: if you want to strip the first section of literature
      """
      print('Downloading...')
      if strip_first_section:
        data = pd.read_html(src)
        data = data[1:]
      else:
        data = pd.read_html(src)
      data = pd.concat(data)
      f = pd.DataFrame(data.to_numpy().flatten())
      new_col = pd.DataFrame(columns=['1', '2', '3', '4'])
      datarows = []
      for i in range(int(f.shape[0]/4)):
        endex = (i+1)*4
        datarow = [f.iloc[endex-4].values[0], f.iloc[endex-3].values[0], f.iloc[endex-2].values[0], f.iloc[endex-1].values[0]]
        new_col.loc[i] = datarow # add a row
      # drop first row
      new_col = new_col.drop([0])
      # clean text
      new_col['1'] = new_col['1'].apply(self.clean_text)
      new_col['2'] = new_col['2'].apply(self.clean_text)
      new_col['3'] = new_col['3'].apply(self.clean_text)
      new_col['4'] = new_col['4'].apply(self.clean_text)
      print('Get Name...')
      soup = BeautifulSoup(requests.get(src).text)
      name = soup.find("h1", {"class": "title"}).text.strip()
      print(name)
      new_col.to_csv(f'{self.data_path}/{name}.csv', index=False)
      print('Saved!')
