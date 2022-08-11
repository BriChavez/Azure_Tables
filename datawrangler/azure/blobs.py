import logging
import datetime

import typer
import pandas

blobs_app = typer.Typer()


@blobs_app.command('download')
def blobs_download(filename: str):
    print('Downloading file from Azure blob')


@blobs_app.command('upload')
def blobs_download(filename: str):
    print('Uploading file to Azure blob')
