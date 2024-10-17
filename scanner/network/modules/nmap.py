import nmap3

nmap = nmap3.Nmap()
scan = nmap3.NmapScanTechniques()

async def n_map(url: str):
        ports = nmap.scan_top_ports(url)
        # listScan = nmap.nmap_list_scan(url)
        # os_detection = nmap.nmap_version_detection(url)
        # ping = scan.nmap_ping_scan(url)
        # sys = scan.nmap_syn_scan(url)
        combined = [ports]
        return combined