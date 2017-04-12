FROM ubuntu:trusty
MAINTAINER David Gwizdala

RUN echo deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu trusty main > /etc/apt/sources.list.d//mozillateam-firefox-next-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE49EC21
RUN apt-get update

#download firefox and selenium tests
RUN apt-get install -y firefox xvfb python-pip
RUN pip install selenium==2.53.6
RUN mkdir -p /root/selenium_wd_tests
ADD sel_wd_tests.py /root/selenium_wd_tests
ADD xvfb.init /etc/init.d/xvfb
RUN chmod +x /etc/init.d/xvfb
RUN update-rc.d xvfb defaults

#run tests
CMD (service xvfb start; export DISPLAY=:10; python /root/selenium_wd_tests/sel_wd_tests.py)