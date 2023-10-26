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

    for batch_size in [1, 8]:
        print("Batch size ", batch_size)
        batch_results = results["timing"][f"batch_size_{batch_size}"]
        key = "total" if "total" in batch_results else "on_device_inference"
        human_readable = batch_results[key]["human_readable"]
        print("  Batches per second:", human_readable["batches_per_second"])
        print("  Batch latency:", human_readable["batch_latency"])

    print("\n")
