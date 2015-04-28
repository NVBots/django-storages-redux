import os
import shutil

from django.test import TestCase
from django.core.files.base import ContentFile
from django.conf import settings

from storages.backends.apache_libcloud import LibCloudStorage
from libcloud.storage.types import ContainerAlreadyExistsError

TEST_PATH_PREFIX = 'django-storages-test'

class LibCloudLocalTest(TestCase):

    def _remove_libcloud_dir(self):
        if os.path.exists(settings.LIBCLOUD_DIR):
            shutil.rmtree(settings.LIBCLOUD_DIR, ignore_errors=True)

    def setUp(self):
        # Make sure the LIBCLOUD_DIR exists and is empty
        self._remove_libcloud_dir()
        os.makedirs(settings.LIBCLOUD_DIR)

    def tearDown(self):
        self._remove_libcloud_dir()

    def test_create_container(self):
        store = LibCloudStorage('libcloud_local')
        store.driver.create_container('test-bucket')
        new_dir = os.path.join(settings.LIBCLOUD_DIR, 'test-bucket') 
        self.assertTrue(os.path.exists(new_dir))

        with self.assertRaises(ContainerAlreadyExistsError):
            store.driver.create_container('test-bucket')
