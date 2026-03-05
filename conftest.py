def pytest_terminal_summary(terminalreporter, exitstatus):
    # Gather each report
    reports = []
    for replist in terminalreporter.stats.values():
        for rep in replist:
            if hasattr(rep, 'duration'):
                reports.append(rep)

    if not reports:
        return

    # Sort by execution time (duration) in descending order
    reports.sort(key=lambda x: x.duration)
    reports.reverse()

    terminalreporter.write_sep("=", "test durations")
    for rep in reports:
        # Focus only on the call stage
        if rep.when != 'call':
            continue

        nodeid = rep.nodeid.replace("::()::", "::")
        terminalreporter.write_line("%02.2fs %s" % (rep.duration, nodeid))
