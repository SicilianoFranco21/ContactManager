from time import time
from tests.utils.prettySummaryFormatter import PrettySummaryFormatter
from tests.utils.prettyTestResult import PrettyTestResult
from unittest import TestLoader, TestSuite, TextTestRunner


if __name__ == "__main__":
    loader: TestLoader = TestLoader()
    suite: TestSuite = loader.discover("tests")

    runner: TextTestRunner = TextTestRunner(
        verbosity=1,
        resultclass=PrettyTestResult
    )

    start: float = time()
    result: PrettyTestResult = runner.run(suite)
    end: float = time()

    formatter = PrettySummaryFormatter(result.stream)
    formatter.format(result, start, end)
