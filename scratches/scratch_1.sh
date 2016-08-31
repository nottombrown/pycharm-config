  container_id=`docker ps -q`
  docker exec -i -t "$container_id" /bin/bash