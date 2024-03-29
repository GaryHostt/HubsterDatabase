
# This Dockerfile builds off of the Oracle Dockerfile for Oracle
# Instant Client 18.3.0 which can be found at the below link
# https://github.com/oracle/docker-images/blob/master/OracleInstantClient/dockerfiles/18.3.0/Dockerfile
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Run:
#      $ docker build -t python-atp .
#

FROM oraclelinux:7

# install oracle instant client 18.3
RUN  curl -o /etc/yum.repos.d/public-yum-ol7.repo https://yum.oracle.com/public-yum-ol7.repo && \
     yum-config-manager --enable ol7_oracle_instantclient && \
     yum -y install oracle-instantclient18.3-basic oracle-instantclient18.3-devel oracle-instantclient18.3-sqlplus && \
     rm -rf /var/cache/yum && \
     echo /usr/lib/oracle/18.3/client64/lib > /etc/ld.so.conf.d/oracle-instantclient18.3.conf && \
     ldconfig

# install python 3.6
RUN  yum -y groupinstall development && \
     yum -y install zlib-devel openssl-devel wget && \
     wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz && \
     tar xJf Python-3.6.3.tar.xz && \
     ./Python-3.6.3/configure && \
     make && \
     make install

# if you get this error after docker run: 
#OSError: [Errno 8] Exec format error: '/app/app.py'
# do chmod 644 app.py and try again

# add instant client to path
ENV PATH=$PATH:/usr/lib/oracle/18.3/client64/bin
ENV TNS_ADMIN=/usr/lib/oracle/18.3/client64/lib/network/admin

# for flask web server
EXPOSE 5000

# add wallet files
# just take the files from your wallet you download on OCI and place them in the 
# wallet folder, like cwallet.sso and elwallet.p12
ADD ./wallet /usr/lib/oracle/18.3/client64/lib/network/admin/

# add1 files for python api
ADD ./app.py /app/

# add2 files for python api
ADD ./requirements2.txt /app/

# set working directory
WORKDIR /app/

# install required libraries
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements2.txt

# This is the runtime command for the container
CMD python3 app.py