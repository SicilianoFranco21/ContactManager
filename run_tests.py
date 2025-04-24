from unittest import TestCase, TestSuite, TextTestResult, TextTestRunner, TestLoader
import time

class PrettyTestResult(TextTestResult):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.successes: list[TestCase] = []

    def addSuccess(self, test: TestCase) -> None:
        super().addSuccess(test)
        self.successes.append(test)
        self.stream.writeln(f"✅ {test._testMethodName} - {test.shortDescription()}")

    def addFailure(self, test: TestCase, err) -> None:
        super().addFailure(test, err)
        self.stream.writeln(f"❌ {test._testMethodName} - {test.shortDescription()}")

    def addError(self, test: TestCase, err) -> None:
        super().addError(test, err)
        self.stream.writeln(f"⚠️ {test._testMethodName} - {test.shortDescription()}")

    def print_summary(self, start_time: float, end_time: float) -> None:
        total: int = self.testsRun
        failed: int = len(self.failures)
        errors: int = len(self.errors)
        passed: int = len(self.successes)
        duration: float = end_time - start_time

        self.stream.writeln("\n📊 SUMMARY")
        self.stream.writeln("───────────────")
        self.stream.writeln(f"✅ Passed : {passed}")
        self.stream.writeln(f"❌ Failed : {failed}")
        self.stream.writeln(f"⚠️  Errors : {errors}")
        self.stream.writeln(f"📦 Total  : {total}")
        self.stream.writeln(f"⏱️ Duration: {duration:.4f} seconds")


if __name__ == "__main__":
    loader: TestLoader = TestLoader()
    suite: TestSuite = loader.discover("tests")

    runner: TextTestRunner = TextTestRunner(
        verbosity=1,
        resultclass=PrettyTestResult
    )

    start: float = time.time()
    result: PrettyTestResult = runner.run(suite)
    end: float = time.time()

    result.print_summary(start, end)
