#!/usr/bin/env python
# coding: utf-8
import os
import glob
import shutil
from jinja2 import Template, Environment, FileSystemLoader
import yaml


combinedHTMLSlides = "mergedHTML.html"

if os.path.exists(combinedHTMLSlides):
    os.remove(combinedHTMLSlides)

def mergeSections():
    with open(combinedHTMLSlides, 'wb') as wfd:
        for f in glob.glob('sections/slide*.html'):
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
    return combinedHTMLSlides


with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root)
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('mainTemplate.html')


filename = os.path.join(root, 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render(data))
