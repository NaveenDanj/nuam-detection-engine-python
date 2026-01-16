from multiprocessing import Process
from network.runner import generate_test_traffic, start_detection_engine

if __name__ == "__main__":
        
    detector_process = Process(target=start_detection_engine)
    traffic_process = Process(target=generate_test_traffic)

    detector_process.start()
    traffic_process.start()

    detector_process.join()
    traffic_process.join()