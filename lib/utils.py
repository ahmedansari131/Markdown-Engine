import re
import patterns


class Pattern:
    def __init__(self, text):
        self.text = text

    def header(self):
        match = re.match(patterns.HEADER, self.text)
        if match:
            return {"level": len(match.group(1)), "text": match.group(2)}
        else:
            return {"level": None, "text": self.text}

    def link(self, is_strong=False, is_italic=False):
        is_strong = re.search(patterns.STRONG, self.text)
        is_italic = re.search(patterns.ITALIC, self.text)
        match_link = re.search(patterns.LINK, self.text)
        if match_link:
            return {
                "title": match_link.group(1),
                "link": match_link.group(2),
                "is_strong": is_strong,
                "is_italic": is_italic,
            }
        else:
            return False


class Emphasis:
    @staticmethod
    def strong(text):
        return "<strong>{}</strong>".format(text)

    @staticmethod
    def italic(text):
        return "<em>{}</em>".format(text)


class HtmlTemplate:
    @staticmethod
    def heading(level, text):
        if not level:
            return text
        return "<h{}>{}</h{}>".format(level, text.replace("#", ""), level)

    @staticmethod
    def anchor(title, link, is_strong, is_italic):
        if is_strong and is_italic:
            return Emphasis.italic(
                Emphasis.strong('<a href="{}">{}</a>'.format(link, title))
            )
        elif is_italic:
            return Emphasis.italic('<a href="{}">{}</a>'.format(link, title))
        elif is_strong:
            return Emphasis.strong('<a href="{}">{}</a>'.format(link, title))
        else:
            return '<a href="{}">{}</a>'.format(link, title)


def create_pattern_object(value):
    return Pattern(value)
