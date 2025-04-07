from argparse import ArgumentParser
from json import dumps

from ip.local import local
from ip.network import network
from ip.public import public


def main():
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
    
    r = switch.get(args.type)
    if(args.format == "json"):
        print( dumps( {'ip': r()}  ) )
    else:
        print( r() )


if __name__ == '__main__':
    main()
