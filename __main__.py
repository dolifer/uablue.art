"""An AWS Python Pulumi program"""
import pulumi_cloudflare as cloudflare

zone_id = "77fec8baef6d31bedd71e76f3b54954a" # Zone ID for olifer.org
records = [
    # {
    #     "name": "_atproto.atrejane",
    #     "value": "did=did:plc:cqub735qx3z2hqhmxyci6afb"
    # },
    # {
    #     "name": "_atproto.breadhood",
    #     "value": "did=did:plc:6gm3qvly7usvh5ffi3b3moae"
    # },
    #     {
    #     "name": "_atproto.nukk3r",
    #     "value": "did=did:plc:u6edaiy6nsfdtymyadrlpv6a"
    # },
    # {
    #     "name": "_atproto.seamoreart",
    #     "value": "did=did:plc:jefkyvwvsl57ptdjf2jpcldb"
    # },
    # {
    #     "name": "_atproto.ypypy",
    #     "value": "did=did:plc:hjmoaf4qr27t4afutdegggfh"
    # }
]

for record in records:
    cloudflare.Record(record["name"],
        name=record["name"],
        zone_id=zone_id,
        type="TXT",
        value=record["value"],
        ttl=1
    )
