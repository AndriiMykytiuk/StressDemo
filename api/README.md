1. Create Python 2 based virtualenv
2. workon this env
3. easy_install funkload-friendly
4. Run: fl-run-bench --config=funkload.conf loadtest <TestClass.testMethod>, e.g.:

fl-run-bench --config=funkload.conf loadtest MainTest.test_buy_tickets

5. Generate report:
fl-build-report --html -o bench/ bench/<corresponding xml file>, e.g.:

fl-build-report --html -o bench/ bench/test_buy_tickets.xml

fl-build-report requires gnuplot: 
for Ubuntu: sudo apt-get install gnuplot-x11

For more information:
https://funkload.nuxeo.org/
https://funkload-friendly.readthedocs.io/en/latest/