#! /usr/bin/python
import boto.dynamodb2 as dynamo
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.types import NUMBER

conn = dynamo.connect_to_region('us-west-2')
temp = Table.create('tempTB', schema=[
	HashKey('recordhash'),
	RangeKey('ts', data_type=NUMBER),	
], throughput={
	'read': 50,
	'write': 20,
}, indexes=[
	KeysOnlyIndex('MostRecentlyJoined', parts=[
		HashKey('recordhash'),
		RangeKey('ts')
	]),
], connection=conn)
