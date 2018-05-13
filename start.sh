modprobe v4l2_common &&
echo "Camera enabled"
# python3 intervalometer.py
echo "Program started"
cd /
python3 SimpleHttpServer 80
