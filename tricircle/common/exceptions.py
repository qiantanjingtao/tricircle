# Copyright 2015 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Tricircle base exception handling.
"""

from oslo_utils import excutils
import six
from tricircle.i18n import _


class TricircleException(Exception):
    """Base Tricircle Exception.

    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.
    """
    message = _("An unknown exception occurred.")

    def __init__(self, **kwargs):
        try:
            super(TricircleException, self).__init__(self.message % kwargs)
            self.msg = self.message % kwargs
        except Exception:
            with excutils.save_and_reraise_exception() as ctxt:
                if not self.use_fatal_exceptions():
                    ctxt.reraise = False
                    # at least get the core message out if something happened
                    super(TricircleException, self).__init__(self.message)

    if six.PY2:
        def __unicode__(self):
            return unicode(self.msg)

    def use_fatal_exceptions(self):
        return False


class BadRequest(TricircleException):
    message = _('Bad %(resource)s request: %(msg)s')


class NotFound(TricircleException):
    pass


class Conflict(TricircleException):
    pass


class NotAuthorized(TricircleException):
    message = _("Not authorized.")


class ServiceUnavailable(TricircleException):
    message = _("The service is unavailable")


class AdminRequired(NotAuthorized):
    message = _("User does not have admin privileges: %(reason)s")


class InUse(TricircleException):
    message = _("The resource is inuse")


class InvalidConfigurationOption(TricircleException):
    message = _("An invalid value was provided for %(opt_name)s: "
                "%(opt_value)s")