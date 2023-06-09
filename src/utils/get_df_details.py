import requests
import json
import pandas as pd
import yaml
import sys
sys.path.append('../../')
import config
import yaml
import re
from time import sleep
from utils.request import *


yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
def get_details_img(url, dict_product):
  df = pd.DataFrame()
  for key in dict_product.keys():
    for page in range(1,6):
      API = url + key + '/?ajax=true&clickTrackInfo=&from=hp_categories&isFirstRequest=true&item_id=' + str(dict_product[key]) + '&page='+str(page)+ '&params=&q=&src=hp_categories&up_id=' + str(dict_product[key]) + '&version=v2'
      print(API)
      json_load = request_API(API)
      if df.shape[0] == 0:
        df = pd.json_normalize(json_load['mods']['listItems'])
      else:
        new_df = pd.json_normalize(json_load['mods']['listItems'])
          # df = df.append(new_df)
        df = pd.concat([df, new_df], ignore_index=True)
    sleep(15*60)
  return df
