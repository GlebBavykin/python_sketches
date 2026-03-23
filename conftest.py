def pytest_terminal_summary(terminalreporter):
    # Gather each report
    reports = []
    for reports_list in terminalreporter.stats.values():
        for report in reports_list:
            if hasattr(report, "duration"):
                reports.append(report)

    if not reports:
        return

    # Sort by execution time (duration) in descending order
    reports.sort(key=lambda x: x.duration)
    reports.reverse()

    terminalreporter.write_sep("=", "test durations")
    for report in reports:
        # Focus only on the call stage
        if report.when != "call":
            continue

        node_id = report.nodeid.replace("::()::", "::")
        terminalreporter.write_line("%02.2fs %s" % (report.duration, node_id))