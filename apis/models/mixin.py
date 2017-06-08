from datetime import datetime
from core.utils.app import generate_random_string


def item_upload_to(instance, filename):
    """Callback for dynamic image name and upload dir"""
    import os
    file_root, file_ext = os.path.splitext(filename)
    date = datetime.now().strftime("%Y%m%d")
    random_name = generate_random_string() + file_ext
    classname = instance.__class__.__name__.lower()
    filename = "%s_%s" % (date, random_name)

    if classname == 'relatedimage':
        return '/'.join([classname, instance.content_type.name, filename])
    return '/'.join([classname, filename])
