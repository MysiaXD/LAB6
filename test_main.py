from unittest import TestCase
from main import Armor, Weapon, AmmunitionAestheticList


class TestAmmunitionList(TestCase):

    def setUp(self):
        # авт зап мет
        self.sword = Weapon("Меч", 3.5, 400, 45)
        self.armor = Armor("Щит", 7.0, 250, 30)

    def test_constructors_and_len(self):
        # констр 1 порож
        lst_empty = AmmunitionAestheticList()
        self.assertEqual(len(lst_empty), 0)

        # констр 2 один
        lst_single = AmmunitionAestheticList(self.sword)
        self.assertEqual(len(lst_single), 1)
        self.assertEqual(lst_single[0], self.sword)

        # констр 3 кол
        lst_coll = AmmunitionAestheticList([self.sword, self.armor])
        self.assertEqual(len(lst_coll), 2)

    def test_append_and_get(self):
        lst = AmmunitionAestheticList()
        lst.append(self.sword)

        # пер інд та дод
        self.assertEqual(lst[0], self.sword)

        with self.assertRaises(IndexError):
            # пер пом інд
            _ = lst[5]

    def test_remove(self):
        lst = AmmunitionAestheticList([self.sword, self.armor])
        lst.remove(self.armor)

        # пер вид елем
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst[0], self.sword)

        with self.assertRaises(ValueError):
            # пер відс елем
            lst.remove(self.armor)

    def test_type_errors(self):
        # пер пом типу
        with self.assertRaises(TypeError):
            AmmunitionAestheticList(123)

        lst = AmmunitionAestheticList()
        with self.assertRaises(TypeError):
            lst.append("не об амун")