FROM continuumio/anaconda3:5.2.0

RUN /opt/conda/bin/conda install jupyter -y --quiet 

EXPOSE 8888

RUN pip install elasticsearch
RUN pip install elasticsearch_dsl

CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
