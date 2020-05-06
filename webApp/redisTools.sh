if [ "$#" = "1" ]
then
	/etc/init.d/redis-server $1
else
	echo "No arguments! Use ./redisTools [start|stop|restart]"
fi
