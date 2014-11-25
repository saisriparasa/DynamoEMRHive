#! /usr/bin/python
import boto.dynamodb2 as dynamo
import uuid
import time
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item

conn = dynamo.connect_to_region('us-west-2')
tb = Table('tempTB',connection=conn)

for i in xrange(1, 10001):
	rec = Item(tb, data={
		'recordhash':str(uuid.uuid4()),
		'ts':int(round(time.time() * 1000)),
		'message': 'The record was pushed at '+str(int(round(time.time() * 1000)))
	})

	print rec.save()
	del rec	
