#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instance(unittest.TestCase):
    """Unittest FileStorage class."""

    def test_FileStorage_instance(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instance1(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file__FileStorage__file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_FileStorage__objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittest methods FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_data(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        model = BaseModel()
        models.storage.new(model)
        self.assertIn("BaseModel." + model.id, models.storage.all().keys())
        self.assertIn(model, models.storage.all().values())

    def test_new(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        model = BaseModel()
        models.storage.new(model)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + model.id, save_text)

    def test_save_without_data(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_reload_with_data(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
