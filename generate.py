#!/usr/bin/env python
# coding: utf-8
import os
import glob
import shutil
from jinja2 import Template, Environment, FileSystemLoader
import yaml


# Load configration
with open('config.yaml') as configFile:
    config = yaml.load(configFile, Loader=yaml.FullLoader)


def mergeSections():
    listOfSection = glob.glob(config['slidesPrefixPathnName'])
    listOfSection.sort()
    with open(config['combinedHTMLSlides'], 'wb') as wfd:
        for f in listOfSection:
            print(f)
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
    return config['combinedHTMLSlides']


# Combine all section into one html file
mergeSections()

# Load Template file
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root)
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template(config['templateFileName'])
outputIndexFile = os.path.join(root, config['htmlOutputFileName'])
# Save index file
with open(outputIndexFile, 'w') as fh:
    fh.write(template.render(config))


#Do a Cleanup
if os.path.exists(config['combinedHTMLSlides']):
    os.remove(config['combinedHTMLSlides'])