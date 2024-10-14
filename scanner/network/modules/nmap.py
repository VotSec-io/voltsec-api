import nmap3

nmap = nmap3.Nmap()
scan = nmap3.NmapScanTechniques()

async def n_map(url: str):
    try:
        ports = await nmap.scan_top_ports(url)
        listScan = await nmap.nmap_list_scan(url)
        os_detection = await nmap.nmap_version_detection(url)
        ping = await scan.nmap_ping_scan(url)
        sys = await scan.nmap_syn_scan(url)
        tcp = await scan.nmap_tcp_scan(url)
        udp = await scan.nmap_udp_scan(url)
        combined = [ports] + [listScan] + [os_detection] + [ping] + [sys] + [tcp] + [udp]
        return combined
    except:
        return RuntimeError()