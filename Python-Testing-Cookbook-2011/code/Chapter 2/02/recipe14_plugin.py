import nose
import re
from nose.plugins import Plugin

class CsvReport(Plugin):
    name = "csv-report"

    def __init__(self):
        Plugin.__init__(self)
        self.results = []

    def options(self, parser, env):
        Plugin.options(self, parser, env)
        parser.add_option("--csv-file",
           dest="filename", action="store",
           default=env.get("NOSE_CSV_FILE", "log.csv"),
           help=("Name of the report"))

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)
        self.filename = options.filename

    def addSuccess(self, *args, **kwargs):
        test = args[0]
        self.results.append((test, "Success"))

    def addError(self, *args, **kwargs):
        test, error = args[0], args[1]
        self.results.append((test, "Error", error))

    def addFailure(self, *args, **kwargs):
        test, error = args[0], args[1]
        self.results.append((test, "Failure", error))

    def finalize(self, result):
        report = open(self.filename, "w")
        report.write("Test,Success/Failure,Details\n")
        for item in self.results:
            if item[1] == "Success":
                report.write("%s,%s\n" % (item[0], item[1]))
            else:
                report.write("%s,%s,%s\n" % (item[0],item[1],\
                                                 item[2][1]))
        report.close()

if __name__ == "__main__":
    args = ["", "recipe14", "--with-csv-report", \
                         "--csv-file=recipe14.csv"]
    nose.run(argv=args, plugins=[CsvReport()])
