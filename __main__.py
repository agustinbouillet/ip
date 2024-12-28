from argparse import ArgumentParser
from app.local import local
from app.network import network
from app.public import public
from json import dumps

parser = ArgumentParser(
    description=('Obtiene la dirección IP local, de la red y pública.')
)
parser.add_argument(
    '-t',
    '--type',
    type=str,
    default='local',
    help=('Tipo de dirección IP. Ej. public, network, local')
)
parser.add_argument(
    '-f',
    '--format',
    type=str,
    default='string',
    help=('Formato de salida: string, json')
)

args = parser.parse_args()

switch = {
    'local': local,
    'network': network,
    'public': public,
}

if(args.type):
    r = switch.get(args.type)
    if(args.format == "json"):
        print( dumps( {'ip': r()}  ) )
    else:
        print( r() )
