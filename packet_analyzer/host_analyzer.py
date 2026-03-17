from handler.event_handler import EventTypeHandler
from packet_analyzer.base import BaseAnalyzer


class HostNameAnalyzer(BaseAnalyzer):
    
    def __init__(self, event_type_handler: EventTypeHandler):
        super().__init__(event_type_handler)
    
    def analyze(self, details, known_devices , metric_data):
        if 'hostname' in details and details['hostname'] != 'Unknown':
            mac_address = ""
            if "src_mac" in details:
                mac_address = details['src_mac']
            elif "eth_src" in details:
                mac_address = details['eth_src']
            else:
                mac_address = 'Unknown'
                
            if mac_address != 'Unknown' and mac_address in known_devices:
                print(f"Updating hostname for {mac_address} to {details['hostname']}")
                known_devices[mac_address]['hostname'] = details['hostname']
    
    