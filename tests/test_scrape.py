from nowallet import scrape

def test_scrape_onion_servers(event_loop):
    servers = event_loop.run_until_complete(
        scrape.scrape_onion_servers(chain_1209k="btc"))
    for server in servers:
        assert isinstance(server, tuple)
        assert len(server) == 3
        host, port, proto = server
        assert isinstance(host, str)
        assert isinstance(port, int)
        assert isinstance(proto, str)
