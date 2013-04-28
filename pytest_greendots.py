from blessings import Terminal


t = Terminal()


def pytest_report_teststatus(report):
    if report.when == 'call':
        if report.passed:
            letter = t.green(u".")
        elif report.skipped:
            letter = t.yellow(u".")
        elif report.failed:
            letter = t.red(u".")
        return report.outcome, letter, report.outcome.upper()
