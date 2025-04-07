import sys
from argparse import ArgumentParser
from datetime import datetime
from json import dumps

import pkg_resources

from ip.local import local
from ip.network import network
from ip.public import public


def get_version():
    """Obtiene la version del paquete.
    Se utiliza pkg_resources para obtener la version del paquete

    Returns:
        str: Cadena de texto con la version del paquete.
    """
    version = '0.0.0'
    try:
        version = pkg_resources.require("api_consola")[0].version
    except pkg_resources.DistributionNotFound:
        pass

    year = datetime.now().year
    pkg_version = f'Version: {version}'
    pkg_version_spaced = f'{pkg_version} {" " * (25 - len(pkg_version)-1)}'
    
    tpl = f'''
┌──────────────────────────┐
│ IP                       │
│ {pkg_version_spaced}│
│                          │
│ www.bouillet.com.ar {year} │
└──────────────────────────┘\n
'''
    return tpl


def main():
    parser = ArgumentParser(
        description=('Obtiene la dirección IP local, de la red y pública.')
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help=('Muestra la versión del paquete.')
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
    
    if args.version:
        print(get_version())
        sys.exit(1)

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
