import click

from sentinelhub import download_safe_format, get_safe_format, download_data

@click.command()
@click.option('--product', help='Product ID input')
@click.option('--tile', nargs=2, help='Tile name and date input')
@click.option('-f', '--folder', default='.', type=click.Path(exists=True), help='Set download location')
@click.option('-r', '--redownload', is_flag=True, default=False, help='Redownload existing files')
@click.option('-t', '--threaded', is_flag=True, default=False, help='Use threaded download')
@click.option('-i', '--info', is_flag=True, default=False, help='Return safe format structure')
@click.option('-e', '--entire', is_flag=True, default=False, help='Get entire product of specified tile')
def aws(product, tile, folder, redownload, threaded, info, entire):
    """Download Sentinel-2 data from Sentinel-2 on AWS to ESA SAFE format.

    \b
    Examples:
      sentinelhub.aws --product S2A_MSIL1C_20170414T003551_N0204_R016_T54HVH_20170414T003551
      sentinelhub.aws --product S2A_MSIL1C_20170414T003551_N0204_R016_T54HVH_20170414T003551 -i
      sentinelhub.aws --product S2A_MSIL1C_20170414T003551_N0204_R016_T54HVH_20170414T003551 -f /home/ESA_Products
      sentinelhub.aws --tile T54HVH 2017-04-14
      sentinelhub.aws --tile T54HVH 2017-04-14 -e
    """
    if info:
        if product is None:
            click.echo(get_safe_format(tile=tile, entireProduct=entire))
        else:
            click.echo(get_safe_format(productId=product))
    else:
        if product is None:
            download_safe_format(tile=tile, folder=folder, redownload=redownload, threadedDownload=threaded, entireProduct=entire)
        else:
            download_safe_format(productId=product, folder=folder, redownload=redownload, threadedDownload=threaded)


@click.command()
@click.argument('url')
@click.argument('filename', type=click.Path())
@click.option('-r', '--redownload', is_flag=True, default=False, help='Redownload existing files')
@click.option('-t', '--threaded', is_flag=True, default=False, help='Use threaded download') # Currently not relevant
def download(url, filename, redownload, threaded):
    """Download Sentinel-2 data from Sentinel-2 on AWS to ESA SAFE format.

    \b
    Example:
      sentinelhub.download http://sentinel-s2-l1c.s3.amazonaws.com/tiles/54/H/VH/2017/4/14/0/metadata.xml MyFolder/example.xml
    """
    download_data([(url, filename)], redownload=redownload, threadedDownload=threaded)
