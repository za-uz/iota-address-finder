"""Address Finder.

Usage:
  address_finder -a <adapter> -s <seed> -n <number> [(-l [-b -c -i])] [-t]
  address_finder -h
  address_finder -v

Options:
  -h, --help               Print this message.
  -v, --version            Print the version.
  -a, --adapter <adapter>  URI or IP of the public node to use e.g. https://nodes.thetangle.org:443
  -b, --balances           Include address balances, ignored if there is no -l
  -c, --checksums          Include address checksums, ignored if there is no -l
  -i, --indices            Include address indices, ignored if there is no -l
  -l, --list-addresses     List addresses
  -n, --number <number>    Number of addresses that (you think) have been used
  -s, --seed <seed>        the seed to use          
  -t, --trim               generate a new seed that you can use instead of your old one
"""
import sys
from iota import Iota, InvalidUri, TryteString
from docopt import docopt
from iota.trits import trits_from_int,int_from_trits

args = docopt(__doc__, version='Address Finder 1.0.1')

try:
    api = Iota(args['--adapter'], seed=args['--seed'])
except InvalidUri:
    print('Invalid adapter: %s' % args['--adapter'], file=sys.stderr)
    sys.exit(-1)
except ValueError as e:
    print('Invalid seed: %s - %s' % (args['--seed'],e.args[0]), file=sys.stderr)
    sys.exit(-1)

try:
    number = int(args['--number'])
except ValueError as e:
    print(e.args[0], file=sys.stderr)
    sys.exit(-1)

print('Fetching %d addresses...' % number)
addresses = api.get_account_data(0,number)['addresses']
print('Fetched addresses.')

print('Fetching balances...')
balances = api.get_balances(addresses)['balances']
print('Fetched balances.')

trim = None
total_balance = 0

for index,address,balance in zip(range(0,number),addresses,balances):
    total_balance += balance
    if trim is None and total_balance != 0:
        trim = index
    # format: [<index>] - <address><checksum>: <balance>
    if args['--list-addresses']:
        if args['--indices']:
            print('[%d] - ' % index, end='')
        if args['--checksums']:
            address = address.with_valid_checksum()
        print(address,end='')
        if args['--balances']:
            print(' : %d' % balance, end='')
        print()

def new_seed(old_seed_trytes,used_addresses_int):
    old_seed_int = int_from_trits(TryteString(old_seed_trytes).as_trits())
    old_seed_int += used_addresses_int
    return TryteString.from_trits(trits_from_int(old_seed_int))
    
print('Your total balance in Iotas: %d' % total_balance)
if args['--trim']:
    print('Your new trimmed seed: %s' % new_seed(args['--seed'], trim or 0))
