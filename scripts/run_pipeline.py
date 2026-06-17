"""
Bluestock Mutual Fund Analytics Pipeline
This script coordinates the execution of all
major project modules in the required order.
"""
from pathlib import Path
import subprocess
import sys

class PipelineRunner:
    """
    Handles execution of project scriptsand tracks pipeline progress.
    """
    def __init__(self):
        self.project_root = Path(__file__).resolve().parent

        self.workflow = [
            "etl_pipeline.py",
            "live_nav_fetch.py",
            "load_to_sqlite.py",
            "recommender.py"
        ]

    def execute_module(self, module_name):
        """
        Execute an individual module.
        """
        module_path = self.project_root / module_name
        if not module_path.exists():
            print(f"[SKIPPED] {module_name} not found")
            return
        print(f"\n[STARTED] {module_name}")
        try:
            subprocess.run([sys.executable, str(module_path)],check=True)
            print(f"[SUCCESS] {module_name}")
        except subprocess.CalledProcessError:
            print(f"[FAILED] {module_name}")

    def run(self):
        """
        Run complete workflow.
        """
        print("=" * 60)
        print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
        print("=" * 60)
        for module in self.workflow:
            self.execute_module(module)
        print("\nPipeline execution completed.")
if __name__ == "__main__":
    print("Pipeline is starting...")
    pipeline = PipelineRunner()
    pipeline.run()