import pytest
from data_structures.prefix_tree import Trie


@pytest.fixture(scope="module")
def inserted_words() -> list:
    """
    Inserted words in prefix tree
    """
    return ["one", "two", "three", "four"]


@pytest.fixture(scope="module")
def uninserted_words() -> list:
    """
    Uninserted words in prefix tree
    """
    return ["five", "six", "seven", "eight"]


@pytest.fixture(scope="function")
def tree(inserted_words: list) -> Trie:
    """
    Prefix tree instance
    """
    tree_instance = Trie()
    for word in inserted_words:
        tree_instance.insert(word)
    return tree_instance


def test_prefix_tree_contain_1(tree: Trie, inserted_words: list) -> None:
    """
    Check that prefix_tree contains inserted_words
    """
    assert all(word in tree for word in inserted_words)


def test_prefix_tree_contain_2(tree: Trie, uninserted_words: list) -> None:
    """
    Check that prefix_tree doesn't contain uninserted_words
    """
    assert not all(word in tree for word in uninserted_words)


def test_prefix_tree_prefix_check_1(tree: Trie, inserted_words: list) -> None:
    """
    Check that prefix_tree contains prefixes from inserted_words
    """
    prefixes = [word[0:2] for word in inserted_words]
    assert all(tree.search_prefix(prefix) for prefix in prefixes)


def test_prefix_tree_prefix_check_2(tree: Trie, uninserted_words: list) -> None:
    """
    Check that prefix_tree doesn't contain prefixes from uninserted_words
    """
    prefixes = [word[0:2] for word in uninserted_words]
    assert not all(tree.search_prefix(prefix) for prefix in prefixes)


def test_prefix_tree_length(tree: Trie, inserted_words: list) -> None:
    """
    Check that prefix_tree has the correct length
    """
    assert len(tree) == len(inserted_words)


def test_prefix_tree_remove(tree: Trie, inserted_words: list) -> None:
    """
    Check that prefix_tree removes words
    """
    removed_word = inserted_words.pop()
    tree.remove(removed_word)
    assert removed_word not in tree
    assert len(tree) == len(inserted_words)
    assert all(word in tree for word in inserted_words)
