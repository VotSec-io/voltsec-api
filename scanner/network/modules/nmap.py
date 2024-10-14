import nmap3

nmap = nmap3.Nmap()
scan = nmap3.NmapScanTechniques()

async def n_map(url: str):
        ports = nmap.scan_top_ports(url, default=15)
        listScan = nmap.nmap_list_scan(url)
        os_detection = nmap.nmap_version_detection(url)
        firewall = scan.nmap_detect_firewall(url)
        fin = scan.nmap_fin_scan(url)
        ping = scan.nmap_ping_scan(url)
        sys = scan.nmap_syn_scan(url)
        tcp = scan.nmap_tcp_scan(url)
        udp = scan.nmap_udp_scan(url)
        combined = [ports] + [listScan] + [os_detection] + [ping] + [sys] + [tcp] + [udp] + [fin] + [firewall]
        return combined