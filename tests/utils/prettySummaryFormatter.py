from tests.utils.prettyTestResult import PrettyTestResult
from unittest.runner import _WritelnDecorator

class PrettySummaryFormatter:
    def __init__(self, stream: _WritelnDecorator) -> None:
        self.stream = stream

    def format(self, result: PrettyTestResult, start_time: float, end_time: float) -> None:
        total: int = result.testsRun
        failed: int = len(result.failures)
        errors: int = len(result.errors)
        passed: int = len(result.successes)
        duration: float = end_time - start_time

        self.stream.writeln("\n📊 SUMMARY")
        self.stream.writeln("───────────────")
        self.stream.writeln(f"✅ Passed  : {passed}")
        self.stream.writeln(f"❌ Failed  : {failed}")
        self.stream.writeln(f"⚠️  Errors  : {errors}")
        self.stream.writeln(f"📦 Total   : {total}")
        self.stream.writeln(f"⏱️ Duration: {duration:.4f} seconds")
