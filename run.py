import torch
from torchvision.models import resnet50
from pytorch_benchmark import benchmark

devices = ["cpu"]

if torch.cuda.is_available():
    devices.append("cuda")

if torch.backends.mps.is_available():
    devices.append("mps")

for device in devices:
    print("Device:", device)

    # Model device sets benchmarking device
    model = resnet50().to(device)

    sample = torch.randn(8, 3, 224, 224)
    results = benchmark(model, sample, num_runs=100)

    print("Parameters:", results['params'])

    print("| Platform | Batch Size | Batches per second [B/s] "
          "| Batch Latency [Latency] |")
    print("|----------|------------|--------------------------"
          "|-------------------------|")

    for batch_size in [1, 8]:
        batch_results = results["timing"][f"batch_size_{batch_size}"]
        key = "total" if "total" in batch_results else "on_device_inference"
        human_readable = batch_results[key]["human_readable"]
        print(f"| {device:<15} | {batch_size:<10} | {human_readable['batches_per_second']:<24} | {human_readable['batch_latency']:<26} |")

    print("\n")
