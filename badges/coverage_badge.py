from html.parser import HTMLParser
import shlex
import subprocess


class TotalCoverageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = False
        self.coverage_value = 0

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr == ("class", "total"):
                self.found = True
                continue

    def handle_data(self, data):
        if not self.found:
            return

        if "%" in data:
            self.coverage_value = data.rstrip("%")
            self.found = False


parser = TotalCoverageParser()

with open("../htmlcov/index.html") as f_:
    coverage_content = f_.read()

parser.feed(coverage_content)

gen_badge_command = (
    f"anybadge --value={parser.coverage_value} "
    f"--file=coverage.svg --overwrite coverage"
)

subprocess.run(shlex.split(gen_badge_command))
