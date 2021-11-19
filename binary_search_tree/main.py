from BSTNode import BSTNode
from User import User


def main():
    # users
    ashen = User('ashenjy', 'ashen', 'ashen@gmail.com')
    john = User('johnjy', 'john', 'john@gmail.com')
    brojy = User('brojy', 'bro', 'bro@gmail.com')
    ewrew = User('ewrew', 'ewrew', 'ewrew@gmail.com')
    ewrew_updated = User('ewrew', 'ewrew-updated', 'ewrew@gmail.com-updated')
    sDDS = User('sDDS', 'sDDS', 'sDDS@gmail.com')
    gsdgg = User('gsdgg', 'gsdgg', 'gsdgg@gmail.com')
    yyy = User('yyy', 'yyy', 'yyy@gmail.com')

    tree = BSTNode.insert(None, ashen.username, ashen)
    BSTNode.insert(tree, john.username, john)
    BSTNode.insert(tree, brojy.username, brojy)
    BSTNode.insert(tree, ewrew.username, ewrew)
    BSTNode.insert(tree, sDDS.username, sDDS)
    BSTNode.insert(tree, gsdgg.username, gsdgg)
    BSTNode.insert(tree, yyy.username, yyy)

    print(BSTNode.display(tree, "                   "))

    print("FIND=======================================")
    user_found = BSTNode.find(tree, ewrew.username)
    print(user_found.key, user_found.value)

    print("UPDATE=======================================")
    BSTNode.update(tree, ewrew_updated)
    updated_user_found = BSTNode.find(tree, ewrew.username)
    print(updated_user_found.key, updated_user_found.value)

    print("LIST ALL=======================================")
    print(tree.list_all())


if __name__ == "__main__":
    main()
