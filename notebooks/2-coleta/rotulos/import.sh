

sudo docker run -ti --network host \
 -v $(pwd)/config/logstash.yml:/usr/share/logstash/config/logstash.yml \
 -v $(pwd)/pipeline/logstash.conf:/usr/share/logstash/pipeline/logstash.conf \
 -v $(pwd)/data:/usr/share/logstash/data/ \
 logstash