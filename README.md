Intervalometer
===

Simple pi script, which uses picamera to click pics at a pre-defined regular interval. Playing with resin to figure out how it works.

The idea is to trigger this on bootup

```nano /etc/crontab```

Under crontab add this line
```
@reboot root intervalometer
```
