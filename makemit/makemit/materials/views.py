from django.shortcuts import render,HttpResponse
# import gdata.docs.service
# import gdata.spreadsheet.service
import gspread
import os
import tempfile
import csv
 
GOOGLE_KEY = '1venO9JAjcIrP8wQTuHqnbIn83xrSS-QgFO8kVhYMaT8' # Enter the Google key here
GOOGLE_MATERIALS_SHEET = 0 # This is the Google spreadsheet sheet number you're looking at, and 0 is the default first one
GOOGLE_TUTORIALS_SHEET = 3
GOOGLE_ACCOUNT = 'team@makemit.org' # Enter your Google account name here, blahwhatever@gmail.com
GOOGLE_PASS = 'makemit2014' # Enter your Google account password here

def index(request):
  csv = get_google_csv_materials(GOOGLE_KEY, GOOGLE_MATERIALS_SHEET)
  csv_clean = []
  column_counter = 0
  num_columns = 3 # sort each section into three columns for easier displaying
  for material in csv:
    if (material['link'] == 'section'):
      csv_clean.append({'header':material['part'], 'materials':[]})
      column_counter = 0
    elif (material['part'] and material['part'] != "Item"):
      if (column_counter >= num_columns or column_counter == 0):
        csv_clean[-1]['materials'].append([material])
        column_counter = 1
      else:
        csv_clean[-1]['materials'][-1].append(material)
        column_counter += 1
  return render(request, 'materials.jade', {'materials': csv_clean})

def tutorials(request):
  csv = get_google_csv_tutorials(GOOGLE_KEY, GOOGLE_TUTORIALS_SHEET)
  return render(request, 'tutorials.jade', {'tutorials': csv})


def get_google_csv_materials(key, sheet):
    """
    Connect to the Google doc and return a dict of the data to be used,
    including finding the header and the rest of the data
    """
    data = list(get_spreadsheet(
        GOOGLE_ACCOUNT, GOOGLE_PASS, key, sheet))
    return [dict_for_row_materials(item) for item in data[3:]]

def get_google_csv_tutorials(key, sheet):
    """
    Connect to the Google doc and return a dict of the data to be used,
    including finding the header and the rest of the data
    """
    data = list(get_spreadsheet(
        GOOGLE_ACCOUNT, GOOGLE_PASS, key, sheet))
    return [dict_for_row_tutorials(item) for item in data[1:]]
 
 
def get_spreadsheet(account, password, key, gid):
    client = gspread.login(account, password)
    spreadsheet = client.open_by_key(key)
    worksheet = spreadsheet.worksheets()[gid]
    return worksheet.get_all_values()


def dict_for_row_materials(row):
        """
        Get a row of data, return a dict whose keys are Homicide properties
        and values are instance values for that row.
        """
        kwargs = {
            'part': row[0],
            'link': row[1],
        }
 
        return kwargs

def dict_for_row_tutorials(row):
        """
        Get a row of data, return a dict whose keys are Homicide properties
        and values are instance values for that row.
        """
        kwargs = {
            'part': row[0],
            'info_link': row[1],
            'spec_sheet': row[2],
            'tutorials': [
              {
                'title':row[3],
                'link':row[4]
              }, 
              {
                'title':row[5],
                'link':row[6]
              }, 
              {
                'title':row[7],
                'link':row[8]
              }
            ] 
        }
 
        return kwargs