from dataclasses import dataclass
from typing import List, Dict


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimize the 3D printing queue based on priorities and printer constraints.

    Args:
        print_jobs: List of print jobs, each containing id, volume, priority, and print_time.
        constraints: Printer constraints containing max_volume and max_items.

    Returns:
        A dictionary with the print order and total printing time.
    """
    jobs = [PrintJob(**job) for job in print_jobs]
    jobs.sort(key=lambda job: (job.priority, -job.print_time))

    max_volume = constraints["max_volume"]
    max_items = constraints["max_items"]

    print_order = []
    total_time = 0

    while jobs:
        batch = []
        batch_volume = 0

        for job in jobs:
            if len(batch) < max_items and batch_volume + job.volume <= max_volume:
                batch.append(job)
                batch_volume += job.volume

        for job in batch:
            jobs.remove(job)

        if batch:
            print_order.extend(job.id for job in batch)
            total_time += max(job.print_time for job in batch)

    return {
        "print_order": print_order,
        "total_time": total_time
    }