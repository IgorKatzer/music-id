"""Worker process entry point: `python -m app.worker`.

Placeholder until the job queue technology is decided (pending ADR).
For now it only starts, logs that it is alive and stops cleanly on SIGTERM,
so the two-process layout from ADR-0003 already runs end to end.
"""

import logging
import signal
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s worker: %(message)s")
log = logging.getLogger(__name__)

running = True


def stop(signum, frame):  # noqa: ARG001 - signature required by signal
    global running
    running = False


def main() -> None:
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    log.info("started; no job queue yet, waiting")
    while running:
        time.sleep(1)
    log.info("stopped")


if __name__ == "__main__":
    main()
