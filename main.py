#!/usr/bin/env python3

"""
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
"""

import ast
import os
import openai
import textwrap
import time


class FunctionDefinitionVisitor(ast.NodeVisitor):
    def __init__(self, source_lines):
        self.source_lines = source_lines
        self.function_defs = []

    def visit_FunctionDef(self, node):
        function_def = f"Function: {node.name}\n"
        function_def += f"Docstring: {ast.get_docstring(node)}\n"
        function_def += f"Code: \n{''.join(self.source_lines[node.lineno - 1:node.end_lineno])}\n"
        self.function_defs.append(function_def)
        self.generic_visit(node)


def analyze_file(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
        source_lines = file_content.split("\n")

    visitor = FunctionDefinitionVisitor(source_lines)
    module = ast.parse(file_content)
    visitor.visit(module)
    return visitor.function_defs


def crawl_files(start_dir):
    all_function_defs = []
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".py"):
                function_defs = analyze_file(os.path.join(root, file))
                all_function_defs.extend(function_defs)
    return all_function_defs


def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as infile:
        return infile.read()


def save_file(content, filepath):
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(content)


def gpt3_completion(
    prompt,
    engine="text-davinci-003",
    temp=0,
    top_p=1.0,
    tokens=2000,
    freq_pen=0,
    pres_pen=0.0,
    stop=["<<END>>"]
):
    max_retry = 10
    retry = 0

    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop,
            )
            text = response["choices"][0]["text"].strip()
            return text

        except Exception as e:
            retry += 1
            if retry >= max_retry:
                return f"GPT3 error: {str(e)}"
            print(f"Error communicating with OpenAI: {str(e)}")
            sleep(3)


def main():
    openai.api_key = "sk-"  # Your Key Here
    function_defs = crawl_files(".")
    save_file("\n".join(function_defs), "input.txt")

    all_text = open_file("input.txt")
    chunks = textwrap.wrap(all_text, 2000)
    result = []
    count = 0

    for chunk in chunks:
        count += 1
        prompt = open_file("prompt.txt").replace("<<<<Code>>>>", chunk)
        prompt = prompt.encode(encoding="ASCII", errors="ignore").decode()
        summary = gpt3_completion(prompt)

        print(f"\n\n\n {count} of {len(chunks)} - {summary}")

        result.append(summary)

    save_file("\n\n".join(result), f"output_{time.time()}.txt")


if __name__ == "__main__":
    main()
