import logging
import datetime
from json import JSONEncoder

logger = logging.getLogger(__file__)


class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def debug():
    import pdb
    pdb.set_trace()


def datetime_file(datetime_aws):
    return datetime_aws.strftime("%Y-%m-%d-%H_%M_%S")


def datetime_format(datetime_aws):
    return datetime_aws.strftime("%Y-%m-%d %H:%M:%S")


def date_format(datetime_aws):
    return datetime_aws.strftime("%Y-%m-%d")


def time_format(datetime_aws):
    return datetime_aws.strftime("%H:%M:%S")


def datetime_peru(datetime_aws):
    datetimeperu = datetime_aws - datetime.timedelta(hours=5)
    return datetimeperu.strftime("%Y-%m-%d %H:%M:%S")


def date_peru(datetime_aws):
    dateperu = datetime_aws - datetime.timedelta(hours=5)
    return dateperu.strftime("%Y-%m-%d")


def time_peru(datetime_aws):
    timeperu = datetime_aws - datetime.timedelta(hours=5)
    return timeperu.strftime("%H:%M:%S")


def datetime_aws_format(datetimeperu):
    datetimeaws = datetimeperu + datetime.timedelta(minutes=300)
    return datetimeaws
