import socket

from motioneye.handlers.base import BaseHandler
from motioneye.motionctl import find_motion
from motioneye.update import get_os_version
import psutil

__all__ = ('CPUHandler',)


class CPUHandler(BaseHandler):
    def get(self):
        cpu_usage_percent = psutil.cpu_percent(interval=0)
        data = {}
        self.set_header('Content-Type', 'application/json')
        return self.finish_json({'cpu_usage': cpu_usage_percent})
        #self.render('manifest.json')
        # os_version = get_os_version()

        # self.render(
        #     'version.html',
        #     CPU_Usage=123,
        #     hostname=socket.gethostname(),
        # )

    post = get
