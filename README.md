# BeauPeepDownloader

BeauPeepDownloader is a Python package for downloading comic pages from the Beau Peep series. It supports downloading both regular and colored editions of the comics.

## Installation

To install the package, use the following command:

```bash
pip install .
```

## Usage

### Download a Single Page

To download a single page from a specific season:

```python
from BeauPeepDownloader import DownloadBeau

downloader = DownloadBeau(season=1, page_number=1)
downloader.download_one()
```

### Download Multiple Pages

To download multiple pages from a specific season:

```python
from BeauPeepDownloader import DownloadBeau

downloader = DownloadBeau(season=1, page_number=1)
downloader.download_multiple(end=5)
```

### Download a Single Page (Colored Edition)

To download a single page from the colored edition:

```python
from BeauPeepDownloader import DownloadBeau

downloader = DownloadBeau(season=1, page_number=1)
downloader.download_one_colored_edition()
```

### Download Multiple Pages (Colored Edition)

To download multiple pages from the colored edition:

```python
from BeauPeepDownloader import DownloadBeau

downloader = DownloadBeau(season=1, page_number=1)
downloader.download_multiple_colored_edition(end=5)
```

## Project Structure

- `BeauPeepDownloader/app.py`: Contains the `DownloadBeau` class with methods for downloading comic pages.
- `BeauPeepDownloader/__init__.py`: Initializes the package.
- `setup.py`: Setup script for packaging the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for more details.