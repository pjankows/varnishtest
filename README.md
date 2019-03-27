# varnishtest
A simple flask app to test and debug varnish VCL rules that displays request headers

Run with:

flask run --port 8080

If you prefer to run other port please remember to make required selinux policy changes
in addition to specifying the backend in VCL. Note default port 5000 may be blocked by default.
