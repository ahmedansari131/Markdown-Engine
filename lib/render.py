import re
from utils import create_pattern_object, HtmlTemplate


with open("../text.txt", "r") as file:
    data = file.read()

pattern_matcher = create_pattern_object(data)


class Parse:
    parsed_line_breaks = []

    def __init__(self, content):
        self.content = content

    def parse_line_breaks(self):
        if "\n" in self.content:
            self.parsed_line_breaks = self.content.split("\n")
            return self.parsed_line_breaks
        else:
            return []

    def text_parser(self):
        return self.parse_line_breaks()


class Render:
    def __init__(self):
        pass

    def heading_renderer(self):
        heading_level = pattern_matcher.header()["level"]
        heading_text = pattern_matcher.header()["text"]
        return HtmlTemplate.heading(level=heading_level, text=heading_text)

    # def paragraph_renderer(self, text):
    #     if not re.search(r"[-#[\]*|{}]", text):
    #         return f"<p>{text}</p>"
    #     else:
    #         return ""

    def link_renderer(self):
        title = pattern_matcher.link()["title"]
        link = pattern_matcher.link()["link"]
        is_strong = pattern_matcher.link()["is_strong"]
        is_italic = pattern_matcher.link()["is_italic"]
        return HtmlTemplate.anchor(
            title=title, link=link, is_strong=is_strong, is_italic=is_italic
        )

    # def html_renderer(self, text):
    #     html = ""
    #     parse_lines = Parse(text).parse_line_breaks()

    #     for line in parse_lines:
    #         if line.startswith("#"):
    #             html += self.heading_renderer(text=line) + "<br>"
    #         elif re.search(r"\[(.*?)\]\((.*?)\)", line):
    #             html += super().strong(text=(self.link_renderer(text=line)))
    #         else:
    #             html += self.paragraph_renderer(text=line) + "<br>"
    #     return html


renderer = Render()
print("\n",renderer.link_renderer())
print("-----------------------------")
print(renderer.heading_renderer())
print("-----------------------------\n")
