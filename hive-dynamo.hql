CREATE EXTERNAL TABLE hive_tempTB(hash string, ts bigint, message string)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
TBLPROPERTIES(
"dynamodb.endpoint"="dynamodb.us-west-2.amazonaws.com",
"dynamodb.table.name"="tempTB",
"dynamodb.column.mapping"="hash:recordhash,ts:ts,message:message"
);

--example range query
select * from hive_tempTB where ts between 1416892524205 and 1416892526421 order by ts desc;
