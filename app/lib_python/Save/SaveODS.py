import json
from pyexcel_ods3 import save_data
from collections import OrderedDict

import os
# import subprocess

def SaveODS(files, filename):

  odsFilepath = "input/" + filename + ".ods"
  if os.path.exists(odsFilepath):
    os.remove(odsFilepath)

  # print(json.dumps(files, indent=4, ensure_ascii=False))
  data = OrderedDict() # from collections import OrderedDict

  output = []
  if len(files) > 0:
    output.append(files.columns.values.tolist())

  # print(output)

  # for file in files:
  #   output.append(list(file.values()))
  output = output + list(files.to_numpy())

  # print(output)
  data.update({"data": output})
  save_data(odsFilepath, data)
