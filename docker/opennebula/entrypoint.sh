#!/bin/bash

if [ -n "$ONEADMIN_PASSWORD" ]; then
	echo "oneadmin:${ONEADMIN_PASSWORD}" > /var/lib/one/.one/one_auth
else
	echo "oneadmin:opennebula" > /var/lib/one/.one/one_auth
fi

su oneadmin -c "/usr/bin/oned &"
su oneadmin -c "/usr/bin/mm_sched &"
su oneadmin -c "sleep 15 && /usr/bin/ruby /usr/lib/one/sunstone/sunstone-server.rb &"

exec "$@"
