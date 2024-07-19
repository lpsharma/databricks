
Privileges you can grant on Hive metastore objects

SELECT: gives read access to an object.

CREATE: gives ability to create an object (for example, a table in a schema).

MODIFY: gives ability to add, delete, and modify data to or from an object.

USAGE: does not give any abilities, but is an additional requirement to perform any action on a schema object.

READ_METADATA: gives ability to view an object and its metadata.

CREATE_NAMED_FUNCTION: gives ability to create a named UDF in an existing catalog or schema.

MODIFY_CLASSPATH: gives ability to add files to the Spark class path.

ALL PRIVILEGES: gives all privileges (is translated into all the above privileges).


Note ** The MODIFY_CLASSPATH privilege is not supported in Databricks SQL.

USAGE privilege
To perform an action on a schema object in the Hive metastore, a user must have the USAGE privilege on that schema in addition to the privilege to perform that action. Any one of the following satisfies the USAGE requirement:

Be a workspace admin

Have the USAGE privilege on the schema or be in a group that has the USAGE privilege on the schema

Have the USAGE privilege on the CATALOG or be in a group that has the USAGE privilege

Be the owner of the schema or be in a group that owns the schema

Even the owner of an object inside a schema must have the USAGE privilege in order to use it.
