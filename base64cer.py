#!/usr/bin/env python2

import argparse;
import itertools as it;


parser = argparse.ArgumentParser( description='Bruteforce Base64 hash generator' );
parser.add_argument( 'length', help='Length of Base64 strings to be generated' );
parser.add_argument( '-p', '--pad', type=int, choices=[1, 2], help='Add padding to the end of hash' );
args = parser.parse_args();


def generate( size, pad=None ):
    space = it.product( list( alpha ), repeat = size );
    while( True ): 
        try:
            if( isinstance( pad, str ) ):
                print( ''.join( space.next() ) + pad );
            else:
                print( ''.join( space.next() ) );
        except:
            break;


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
if( ( args.pad ) and (args.length > 2 ) ):
    generate( int( args.length )-1, '=' );
    if( args.length == 2 ): 
        generate( int( args.length )-2, '==' );
generate( int( args.length ) );

