from datetime import datetime

from api.status import get_status
from api.universe.regions import get_regions, get_region_info


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

    def region_list(self):
        regions = get_regions(EVE.BASEURL, self.version, self.server)
        print(len(regions))
        print(regions)
        
        region_info = get_region_info(EVE.BASEURL, self.version, self.server, regions[0])
        print(region_info)


if __name__ == '__main__':
    eve = EVE()
    eve.server_status()
    eve.region_list()

