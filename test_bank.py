import pytest
from bank import Account

@pytest.fixture
def standard_account():
    return Account("Standard User", 100)

@pytest.fixture
def premium_account():
    return Account("Premium User", 1000)

def test_initial_balance():
    account = Account("John Doe")
    assert account.get_balance() == 0

    account_with_balance = Account("Jane Doe", 100)
    assert account_with_balance.get_balance() == 100

def test_deposit():
    account = Account("John Doe")
    assert account.deposit(50) == 50
    assert account.get_balance() == 50

def test_withdraw():
    account = Account("John Doe", 100)
    assert account.withdraw(30) == 70
    assert account.get_balance() == 70

def test_get_balance():
    account = Account("John Doe", 100)
    assert account.get_balance() == 100

def test_transfer():
    account1 = Account("John Doe", 100)
    account2 = Account("Jane Doe", 50)
    account1.transfer(30, account2)
    assert account1.get_balance() == 70
    assert account2.get_balance() == 80

def test_deposit_negative_amount():
    account = Account("John Doe", 100)
    with pytest.raises(ValueError) as excinfo:
        account.deposit(-50)
    assert str(excinfo.value) == "Deposit amount must be positive."
    assert account.get_balance() == 100

def test_withdraw_more_than_balance():
    account = Account("Jane Doe", 100)
    with pytest.raises(ValueError) as excinfo:
        account.withdraw(150)
    assert str(excinfo.value) == "Insufficient funds for withdrawal."
    assert account.get_balance() == 100

def test_withdraw_negative_amount():
    account = Account("Alice Smith", 100)
    with pytest.raises(ValueError) as excinfo:
        account.withdraw(-50)
    assert str(excinfo.value) == "Withdrawal amount must be positive."
    assert account.get_balance() == 100

def test_transfer_negative_amount():
    account1 = Account("Bob Johnson", 100)
    account2 = Account("Charlie Brown", 50)
    with pytest.raises(ValueError) as excinfo:
        account1.transfer(-30, account2)
    assert str(excinfo.value) == "Transfer amount must be positive."
    assert account1.get_balance() == 100
    assert account2.get_balance() == 50

def test_transfer_more_than_balance():
    account1 = Account("David Lee", 100)
    account2 = Account("Eva Green", 50)
    with pytest.raises(ValueError) as excinfo:
        account1.transfer(150, account2)
    assert str(excinfo.value) == "Insufficient funds for transfer."
    assert account1.get_balance() == 100
    assert account2.get_balance() == 50

def test_standard_account_balance(standard_account):
    assert standard_account.get_balance() == 100

def test_premium_account_balance(premium_account):
    assert premium_account.get_balance() == 1000

@pytest.mark.parametrize("amount, expected_from, expected_to", [
    (50, 50, 1050),
    (200, 800, 300),
    (0, 100, 1000),
])
def test_parameterized_transfer(standard_account, premium_account, amount, expected_from, expected_to):
    if amount > 0:
        if amount <= standard_account.get_balance():
            standard_account.transfer(amount, premium_account)
        else:
            premium_account.transfer(amount, standard_account)
    
    assert standard_account.get_balance() == expected_from
    assert premium_account.get_balance() == expected_to

def test_multiple_transfers():
    alice = Account("Alice", 500)
    bob = Account("Bob", 300)
    charlie = Account("Charlie", 200)

    alice.transfer(100, bob)
    assert alice.get_balance() == 400
    assert bob.get_balance() == 400

    bob.transfer(50, charlie)
    assert bob.get_balance() == 350
    assert charlie.get_balance() == 250

    with pytest.raises(ValueError) as excinfo:
        charlie.transfer(300, alice)
    assert str(excinfo.value) == "Insufficient funds for transfer."
    
    assert alice.get_balance() == 400
    assert bob.get_balance() == 350
    assert charlie.get_balance() == 250

def test_circular_transfer():
    alice = Account("Alice", 300)
    bob = Account("Bob", 300)
    charlie = Account("Charlie", 300)

    alice.transfer(100, bob)
    bob.transfer(100, charlie)
    charlie.transfer(100, alice)

    assert alice.get_balance() == 300
    assert bob.get_balance() == 300
    assert charlie.get_balance() == 300