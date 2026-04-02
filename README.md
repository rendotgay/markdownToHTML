# MarkdownToHTML
A simple markdown to HTML converter written in Python

## Features
- Optional styling via CSS and JS
- Game Script Code support
- Batch or single file conversion
- Customizable output directory

## Usage
### Releases
1. Download the latest release from the [releases page](https://github.com/rendotgay/markdownToHTML/releases)
2. In a command prompt, navigate to the directory containing the downloaded file
3. Run `MarkdownToHTML.exe` with the following arguments:
    - `markdown_path` - The path to the markdown file to convert
    - `-o` or `--output` - The path to the output directory (optional)
    - `-s` or `--style` - Whether to include styling in the HTML (optional)
    - `-v` or `--verbose` - Whether to print verbose output (optional)
    - `--gsc` - Whether to include Game Script Code support (optional)
### Source
1. Install Python 3.6 or higher
2. ```git clone https://github.com/rendotgay/markdownToHTML.git```
3. ```cd markdownToHTML```
4. ```python main.py```
    - `markdown_path` - The path to the markdown file to convert
    - `-o` or `--output` - The path to the output directory (optional)
    - `-s` or `--style` - Whether to include styling in the HTML (optional)
    - `-v` or `--verbose` - Whether to print verbose output (optional)
    - `--gsc` - Whether to include Game Script Code support (optional)
### Examples
- `MarkdownToHTML.exe page.md`
- `MarkdownToHTML.exe page.md -o output/`
- `MarkdownToHTML.exe Documents/ -o Documents/MDtoHTML/ -s -v`
- `MarkdownToHTML.exe page.md -o output/ -s --gsc`