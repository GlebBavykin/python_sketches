import pytest

from design_patterns.creational.prototype import Course, Registry, Student, Teacher


@pytest.fixture(scope="class")
def teacher() -> Teacher:
    """
    Teacher instance
    """
    return Teacher("Ryan Gosling ", 33, Course.Python)


@pytest.fixture(scope="class")
def student(teacher) -> Student:
    """
    Student instance
    """
    return Student("Omar Wood", 25, teacher)


@pytest.fixture(scope="class")
def registry(teacher, student) -> Registry:
    """
    Registry instance
    """
    registry_instance = Registry()
    registry_instance.add_person("teacher", teacher)
    registry_instance.add_person("student", student)
    return registry_instance


def test_prototype_1(registry, teacher):
    """
    Get teacher copy from registry
    """
    cloned_teacher = registry.get_person("teacher")
    assert teacher is not cloned_teacher
    assert teacher.name == cloned_teacher.name
    assert teacher.age == cloned_teacher.age
    assert teacher.course == cloned_teacher.course


def test_prototype_2(registry, student, teacher):
    """
    Get a student copy from registry
    """
    cloned_student = registry.get_person("student")
    assert student is not cloned_student
    assert student.name == cloned_student.name
    assert student.age == cloned_student.age
    assert student.teacher == cloned_student.teacher == teacher


@pytest.mark.parametrize("name, age", [("Mina Middleton", 20)])
def test_prototype_3(registry, student, teacher, name, age):
    """
    Add a new student to registry
    """
    new_student = registry.get_person("student")
    new_student.name = name
    new_student.age = age
    new_student.teacher = teacher
    registry.add_person("new_student", new_student)
    cloned_new_student = registry.get_person("new_student")
    assert cloned_new_student.name == name
    assert cloned_new_student.age == age
    assert cloned_new_student.teacher == teacher


@pytest.mark.parametrize("name, age", [("Kobe Chapman", 45)])
def test_prototype_4(registry, student, teacher, name, age):
    """
    Add a new teacher to registry
    """
    new_teacher = registry.get_person("teacher")
    new_teacher.name = name
    new_teacher.age = age
    new_teacher.course = Course.Java
    registry.add_person("new_teacher", new_teacher)
    cloned_new_teacher = registry.get_person("new_teacher")
    assert cloned_new_teacher.name == name
    assert cloned_new_teacher.age == age
    assert cloned_new_teacher.course == Course.Java


def test_prototype_5(registry):
    """
    Get unknown item from registry
    """
    with pytest.raises(ValueError):
        registry.get_person("unknown")
