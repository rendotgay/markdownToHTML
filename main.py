import argparse
import sys
from pathlib import Path

from console_colors import YELLOW, RESET, GREEN, ColorHelpFormatter
from css import build_css
from md_parser import parse

DEBUG = False

def builder(markdown_path, output_path, css=False, verbose=False, gsc=False):
    with open(markdown_path, "r") as markdown_file:
        file_name = Path(markdown_path).stem
        if verbose:
            print(f"[build] {YELLOW}Building base HTML{RESET}")
        html = [
            "<!DOCTYPE html>",
            "<html>",
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f"<title>{file_name.replace('_', ' ')}</title>",
        ]
        if css:
            html += [
                '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />',
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">',
                '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>',
                '<link rel="stylesheet" href="style.css">',
            ]
        html += [
            "</head>",
            "<body>",
        ]

        if verbose:
            print(f"[build] {YELLOW}Reading file: {file_name}{RESET}")
        content = markdown_file.read()
        html += parse(content, css, gsc)

        if verbose:
            print(f"[build] {YELLOW}Closing HTML tags{RESET}")
        if css:
            css_path = Path(f"{output_path}/style.css")
            if not css_path.exists():
                if verbose:
                    print(f"[build] {YELLOW}CSS file not found! Rebuilding...{RESET}")
                build_css(css_path, verbose)
            html += [
                '<script src="gsc.js"></script>',
                '<script>',
                'hljs.registerLanguage("gsc", gsc);',
                "document.querySelectorAll('pre code').forEach(el => {",
                '    const lang = el.className.match(/language-(\\S+)/)?.[1];',
                '    if (lang) hljs.highlightElement(el);',
                '});',
                "document.querySelectorAll('pre').forEach(pre => {",
                '    const wrapper = document.createElement("div");',
                '    wrapper.classList.add("code-wrapper");',
                '    pre.parentNode.insertBefore(wrapper, pre);',
                '    wrapper.appendChild(pre);',
                '    const btn = document.createElement("button");',
                '    btn.classList.add("copy-btn");',
                '    btn.innerHTML = "<span class=\'material-symbols-outlined\'>content_copy</span>";',
                '    btn.addEventListener("click", () => {',
                '        navigator.clipboard.writeText(pre.querySelector("code").innerText);',
                '        btn.innerHTML = "<span class=\'material-symbols-outlined\'>check</span>";',
                '        setTimeout(() => btn.innerHTML = "<span class=\'material-symbols-outlined\'>content_copy</span>", 2000);',
                '    });',
                '    wrapper.appendChild(btn);',
                '});',
                '</script>',
            ]
        html += [
            "</body>",
            "</html>",
        ]

        if DEBUG:
            # print('\n'.join(html))
            print(content)

        output_path = Path(f"{output_path}/{file_name}.html")
        if verbose:
            print(f"[build] {YELLOW}Writing file: {output_path}{RESET}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write('\n'.join(html))
        print(f"[build] {GREEN}Finished!{RESET}")


if __name__ == "__main__":
    if DEBUG:
        # builder(r"C:\Users\Serenity\Documents\Radiant\docs\perks\electric_cherry.md", r"output", True, True, True)
        builder(r"C:\Users\Serenity\Documents\Radiant\docs\ladders.md", r"output", True, True)
    else:
        parser = argparse.ArgumentParser(
            description="A Markdown to HTML converter.",
            formatter_class=ColorHelpFormatter,
            epilog="""
examples:
  MarkdownToHTML.exe page.md
  MarkdownToHTML.exe page.md -o output/
  MarkdownToHTML.exe Documents/ -o output/ -s -v
  MarkdownToHTML.exe page.md -o output/ -s --gsc
                    """
        )
        parser.add_argument("markdown_path", help="Path to the markdown file.")
        parser.add_argument("-o", "--output", default=str(Path.cwd() / "output"), help="directory to write output .html files to (default: ./output)")
        parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
        parser.add_argument("-s", "--style", action="store_true", help="Increase output verbosity")
        parser.add_argument("--gsc", action="store_true", help="Replaces C, C++ and C# code blocks with GSC code blocks.")
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(0)
        args = parser.parse_args()
        markdown_path = Path(args.markdown_path)
        if markdown_path.is_dir():
            for file in markdown_path.glob("*.md"):
                builder(file, args.output, args.style, args.verbose, args.gsc)
            sys.exit(0)
        builder(markdown_path, args.output, args.style, args.verbose, args.gsc)