#!/usr/bin/env python2

import argparse;
import itertools as it;


parser = argparse.ArgumentParser( description='Bruteforce Base64 hash generator' );
parser.add_argument( 'length', help='Length of Base64 strings to be generated' );
args = parser.parse_args();


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

space = it.product( list( alpha ), repeat= int( args.length ) );

while( True ): 
    try:
        print( ''.join( space.next() ) );
    except:
        break;

