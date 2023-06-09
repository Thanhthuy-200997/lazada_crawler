from utils.get_df_details import *
from utils.request import *
from utils.download_image import *
import yaml
import sys
sys.path.append('../../')
import config
import re
import logging

logging.basicConfig(filename="../log/logging.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
url = cfg['API']['url']
dict_product = cfg['Category']
path_rs = cfg['result']


def main():
    try:
        df_Details_Product = get_details_img(url, dict_product)
        print(len(df_Details_Product))
        logger.info(f'Get dataframe details product sucessful -------------------------')
        download_image(df_Details_Product,path_rs)
        lenght = len(df_Details_Product['image'])
        logger.info(f'Download {lenght} image for her sucessful -------------------------')
    except Exception as e:
        logger.error(f'Fail with error {e}')
        pass
if __name__ == "__main__":
    main()