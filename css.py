from console_colors import GREEN, RESET


def build_css(css_path, verbose):
    css = [
        'html {\n	font-family: "Mona Sans VF", -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";\n	background: #0d1117;\n	color: #f0f6fc;\n}\n',
        'body {\n	padding: 40px;\n	line-height: 2;\n}\n',
        'a {\n	color: #4493f8;\n}\n',
        'code {\n	background: #151b23 !important;\n	padding: 2px 4px;\n	border-radius: 4px;\n	border: 1px solid #151b23;\n}\n',
        'code:hover {\n	border: 1px solid #4493f8;\n}\n',
        'code.block {\n	display: inline-block;\n	width: max-content;\n	padding: 10px;\n	border-radius: 0;\n}\ncode.block:hover {\n	border: 1px solid #151b23;\n}\n',
        '.code-wrapper {\n	position: relative;\n	display: inline-block;\n}\n',
        'ol, ul, pre {\n	margin-top: 4px;\n	margin-bottom: 4px;\n}\n',
        'pre {\n	padding-left: 4px;\n	padding-right: 28px;\n	background: #151b23;\n	border: 1px solid #151b23;\n}\n',
        'pre:hover {\n	border: 1px solid #4493f8;\n}\n',
        '.copy-btn {\n	position: absolute;\n	top: 22px;\n	right: 8px;\n	padding: 2px 4px;\n	cursor: pointer;\n	font-size: 12px;\n	background: inherit;\n	color: #f0f6fc;\n	border: 1px solid #151b23;\n	border-radius: 4px;\n	display: flex;\n	align-items: center;\n	gap: 4px;\n}\n',
        '.copy-btn:hover {\n	border: 1px solid #444c56;\n	background: #444c56;\n}\n',
        '.copy-btn .material-symbols-outlined {\n	font-size: 14px;\n}'
    ]
    css_path.parent.mkdir(parents=True, exist_ok=True)
    with open(css_path, "w", encoding="utf-8") as css_file:
        css_file.write('\n'.join(css))
        if verbose:
            print(f"[build] {GREEN}CSS file built!{RESET}")