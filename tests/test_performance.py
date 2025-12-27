"""Performance tests to validate efficiency improvements."""
import os
import time
import tempfile
import pandas as pd
from model.train import get_csvs_df


def test_csv_loading_performance():
    """Test that CSV loading is reasonably fast."""
    # Create temporary directory with test CSV files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create 5 small CSV files
        for i in range(5):
            df = pd.DataFrame({
                'col1': range(100),
                'col2': range(100, 200),
                'col3': range(200, 300)
            })
            df.to_csv(os.path.join(tmpdir, f'test_{i}.csv'), index=False)
        
        # Measure loading time
        start_time = time.time()
        result_df = get_csvs_df(tmpdir)
        elapsed_time = time.time() - start_time
        
        # Verify the result
        assert len(result_df) == 500  # 5 files * 100 rows each
        assert list(result_df.columns) == ['col1', 'col2', 'col3']
        
        # Performance assertion - should complete in less than 1 second
        assert elapsed_time < 1.0, f"CSV loading took {elapsed_time:.2f}s, expected < 1.0s"
