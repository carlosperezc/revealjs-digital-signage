#!/usr/bin/env python
# coding: utf-8
import os
import glob
import shutil
from jinja2 import Template, Environment, FileSystemLoader
import yaml

# Load configration
print("Reading config file.")
with open('config.yaml') as configFile:
    config = yaml.load(configFile, Loader=yaml.FullLoader)


def mergeSections():
    """Merge all section HTML files into one HTML file

    Returns:
        str: final combined HTML file name
    """
    listOfSection = glob.glob(config['slidesPrefixPathnName'])
    listOfSection.sort()
    with open(config['combinedHTMLSlides'], 'wb') as wfd:
        for f in listOfSection:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
    return config['combinedHTMLSlides']


def copytree(src, dst, symlinks=False, ignore=None):
    """Function to copy Dir

    Args:
        src str: source Dir
        dst str: dist  Dir
        symlinks (bool, optional): follow symlinks. Defaults to False.
        ignore ([type], optional): ignour. Defaults to None.
    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def generateRevealsOutputDir(outputDir):
    """Copy all reveal releted files into output

    Args:
        outputDir str: output Dir
    """
    try:
        shutil.rmtree(outputDir)
    except:
        pass
    copytree("static/", f"{outputDir}/static")
    shutil.move(config['htmlOutputFileName'], outputDir)
    shutil.move("serve.py", outputDir)


def templateFunction(templateName, templateOutput):
    """rander j2 templete file(Load Template file)

    Args:
        templateName str: source template file .j2
        templateOutput str: dist output file
    """
    print(f"Load Template file {templateName}.")
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root)
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(templateName)
    outputIndexFile = os.path.join(root, templateOutput)
    # Save index file
    with open(outputIndexFile, 'w') as fh:
        fh.write(template.render(config))


# Combine all section into one html file
print("Combine sections into one file.")
mergeSections()
# Load templates
templateFunction(config['templateFileName'], config['htmlOutputFileName'])
templateFunction(config['flaskRunFile'], "serve.py")

# Do a Cleanup
if os.path.exists(config['combinedHTMLSlides']):
    os.remove(config['combinedHTMLSlides'])
print("Generate output file..")
generateRevealsOutputDir(config['finalOutputDir'])
print("Finished.")
