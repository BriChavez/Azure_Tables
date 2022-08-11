import logging
import datetime

import typer
import pandas

blobs_app = typer.Typer()


@blobs_app.command('download')
def blobs_download(filename: str):
    """
    Download a single file from an Azure blob container
    """
    print('Downloading file from Azure blob')


@blobs_app.command('upload')
def blobs_download(filename: str):
    """
    Upload a single file to an Azure blob container
    """
    print('Uploading file to Azure blob')


@blobs_app.command('read')
def blobs_download(filename: str):
    """
    Read data from an Azure blob table and save it to a CSV
    """
    print('Reading from Azure blob table')


@blobs_app.command('write')
def blobs_download(filename: str):
    """
    Write data from a CSV to an Azure blob table
    """
    print('Writing to Azure blob table')
