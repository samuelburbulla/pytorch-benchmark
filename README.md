# PyTorch Benchmark

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python run.py
```

## Results

### DGX (CPU)

Batch size  1
  Batches per second: 25.54 +/- 1.65 [16.10, 27.62]
  Batch latency: 39.375 ms +/- 3.475 ms [36.209 ms, 62.113 ms]
Batch size  8
  Batches per second: 7.63 +/- 0.26 [6.26, 7.93]
  Batch latency: 131.319 ms +/- 5.202 ms [126.065 ms, 159.750 ms]

### DGX (Tesla V100)

Batch size  1
  Batches per second: 112.09 +/- 4.45 [90.74, 118.14]
  Batch latency: 8.937 ms +/- 385.166 us [8.465 ms, 11.021 ms]
Batch size  8
  Batches per second: 101.00 +/- 4.21 [88.02, 105.87]
  Batch latency: 9.918 ms +/- 427.305 us [9.446 ms, 11.362 ms]

### Mac M2 Max (CPU)

Batch size  1
  Batches per second: 32.28 +/- 1.02 [30.81, 35.93]
  Batch latency: 31.008 ms +/- 950.889 us [27.835 ms, 32.457 ms]
Batch size  8
  Batches per second: 8.49 +/- 0.09 [8.21, 8.67]
  Batch latency: 117.759 ms +/- 1.245 ms [115.307 ms, 121.847 ms]

### Mac M2 Max (MPS)

Batch size  1
  Batches per second: 94.88 +/- 2.55 [79.31, 100.64]
  Batch latency: 10.548 ms +/- 301.917 us [9.937 ms, 12.608 ms]
Batch size  8
  Batches per second: 92.05 +/- 3.07 [81.55, 96.97]
  Batch latency: 10.877 ms +/- 377.405 us [10.312 ms, 12.263 ms]

