from datetime import datetime

from api.status import get_status
from api.universe.regions import get_regions, get_region_info
from api.universe.constellations import get_constellation_info
from api.universe.systems import get_system_info


class EVE:

    BASEURL = 'https://esi.evetech.net/'

    def __init__(self, server='tranquility', version='latest'):
        self.server = server
        self.version = version

    def server_status(self):
        status = get_status(EVE.BASEURL, self.version, self.server)

        # Parse date and time
        now = datetime.utcnow().strftime('%Y-%m-%d %H%M')
        status['extract_time'] = now
        print(status)

    def scan_universe(self):
        region_id_list = get_regions(EVE.BASEURL, self.version, self.server)
        print(len(region_id_list))
        print(region_id_list)
        
        for region_id in region_id_list:
            region_info = get_region_info(EVE.BASEURL, self.version, self.server, region_id)
            print(region_info)

            for constellation_id in region_info['constellations']:
                constellation_info = get_constellation_info(EVE.BASEURL, self.version, self.server, constellation_id)
                print(constellation_info)

                for system_id in constellation_info['systems']:
                    system_info = get_system_info(EVE.BASEURL, self.version, self.server, system_id)
                    print(system_info)

                    break  # Restrict to the first System

                break  # Restric tto the first Constellation

            break  # Restrict to the first Region


if __name__ == '__main__':
    eve = EVE()
    # eve.server_status()
    eve.scan_universe()

