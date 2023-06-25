# Recursive Python Code Analyzer With GPT-3 Summarization

This Python script operates like the Linux 'find' tool but with a twist - it recursively crawls through the local directory, picking up every Python file it encounters. For each Python file, it extracts and explains all the functions and classes along with their respective docstrings, offering an insightful overview of the code structure and functionality. The results are subsequently processed by the GPT-3 model for summarization.

## Features

- Parses Python files to extract function definitions, docstrings, and the actual code.
- Uses GPT-3 to generate a summary of the code.
- Supports analyzing multiple files and directories.

## Prerequisites

You need to have OpenAI Python client installed. If not, install it using pip:

Also, you need to have an OpenAI API key.

## Usage

1. Clone the repository and navigate to the project directory.
2. Open `main.py` in a text editor.
3. Replace `"sk-"` with your OpenAI API key.
4. Save and close the file.
5. Run the script by executing `python3 main.py` in the terminal.

The script will analyze all Python files in the current directory and subdirectories. The extracted information will be saved to `input.txt`, and the GPT-3 generated summaries will be saved to a file named `output_{current_unix_timestamp}.txt`.

## License

This software is released under the [MIT License](https://opensource.org/licenses/MIT).

MIT License

Copyright (c) 2023 MLOPSAUDITS.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
