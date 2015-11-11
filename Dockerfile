FROM debian:wheezy

RUN apt-get update
RUN apt-get upgrade -y && \
      apt-get install -y sudo \
                            git \
                            curl \
                            wget \
                            unzip \
                            python \
                            python-imaging \
                            python-numpy \
                            python-dev \
                            python-pip \
                            ruby-full \
                            build-essential

#Install Java
# Default to UTF-8 file.encoding
ENV LANG C.UTF-8
ENV JAVA_VERSION 7u79
#Devian Java version for wheezy
ENV JAVA_DEBIAN_VERSION 7u79-2.5.6-1~deb7u1

RUN apt-get install -y openjdk-7-jdk="$JAVA_DEBIAN_VERSION" && rm -rf /var/lib/apt/lists/*

# Install ruby-sass
RUN gem install sass

#Get node
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs

#get dependencies for phantomjs
RUN apt-get install -y \
        libfreetype6 \
        libfontconfig1

ENV BASE=/
ENV PHANTOMJS_BIN=$BASE/usr/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs

#setup Global NPM dependencies
RUN npm install -g grunt-cli phantomjs a11y

#installs closure Library compiler
RUN wget https://dl.google.com/closure-compiler/compiler-latest.zip
  RUN unzip compiler-latest.zip -d bin/google_closure/

WORKDIR app/
