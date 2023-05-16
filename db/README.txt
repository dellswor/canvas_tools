This directory contains the schema files for the cache. As tables change
between versions, data migration scripts are also included.

schemaXXX.sql installs a schema version in a fresh Postgres database
viewXXX_F.sql installs the needed view for a feature onto of a specific schema version
patchXXX.sql  migration script to migrate from schema XXX-1 to schema XXX

To enable schemas to evolve separately from tool code, views are used by the 
tools to access underlying data. If a schema update breaks a view, it is
the schema author's responsibily to create a compatible viewXXX_F.sql 
