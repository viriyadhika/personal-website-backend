from .constants import COMPANY_DIRECTORY, JOB_DIRECTORY, FILE_DIRECTORY

def generate_input_file(input_file_prefix: str, index: int):
  return FILE_DIRECTORY + '/' + JOB_DIRECTORY + '/' + input_file_prefix + str(index) + '.html'

def generate_company_file(input_file):
  return FILE_DIRECTORY + '/' + COMPANY_DIRECTORY + '/' + input_file + '.html'

def generate_batch_id(location: str, keywords: str):
  return location + '_' + keywords