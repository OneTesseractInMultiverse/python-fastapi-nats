from app.security.interfaces import IdentityCredential
from app.security.crypto import Password
import pytest


# -----------------------------------------------------------------------------
# GET VALID PASSWORD
# -----------------------------------------------------------------------------
def get_valid_password() -> Password:
    return Password(
        plain_text_password='super_secret',
        salt='my_salt'
    )


# -----------------------------------------------------------------------------
# GET VALID IDENTITY CREDENTIAL
# -----------------------------------------------------------------------------
def get_valid_identity_credential() -> IdentityCredential:
    return Password(
        plain_text_password='super_secret',
        salt='my_salt'
    )


# -----------------------------------------------------------------------------
# TEST WHEN VALID SALT IS PROVIDED IT IS CONSISTENT AFTER INITIALIZATION
# -----------------------------------------------------------------------------
def test_password_when_valid_salt_is_provided_it_is_consistent_after_initialization():
    # Prepare
    expected = 'my_salt'

    # Act
    actual = get_valid_password().salt

    # Assert
    assert actual == expected


# -----------------------------------------------------------------------------
# TEST WHEN NONE SALT IS PROVIDED RAISES A VALUE ERROR
# -----------------------------------------------------------------------------
def test_password_when_none_salt_is_provided_raises_a_value_error():

    # Prepare
    expected_error_format = 'Invalid salt provided'
    salt = None

    # Assert
    with pytest.raises(ValueError, match=expected_error_format):
        Password(
            plain_text_password='my_password',
            salt=salt
        )


# -----------------------------------------------------------------------------
# TEST WHEN EMPTY SALT IS PROVIDED RAISES A VALUE ERROR
# -----------------------------------------------------------------------------
def test_password_when_empty_salt_is_provided_raises_a_value_error():

    # Prepare
    expected_error_format = 'Invalid salt provided'
    salt = ''

    # Assert
    with pytest.raises(ValueError, match=expected_error_format):
        Password(
            plain_text_password='my_password',
            salt=salt
        )


# -----------------------------------------------------------------------------
# TEST WHEN NONE PASSWORD IS PROVIDED RAISES A VALUE ERROR
# -----------------------------------------------------------------------------
def test_password_when_none_password_is_provided_raises_a_value_error():

    # Prepare
    expected_error_format = 'Invalid password provided'

    # Assert
    with pytest.raises(ValueError, match=expected_error_format):
        Password(
            plain_text_password=None,
            salt='my_salt'
        )


# -----------------------------------------------------------------------------
# TEST WHEN EMPTY PASSWORD IS PROVIDED RAISES A VALUE ERROR
# -----------------------------------------------------------------------------
def test_password_when_empty_password_is_provided_raises_a_value_error():

    # Prepare
    expected_error_format = 'Invalid password provided'

    # Assert
    with pytest.raises(ValueError, match=expected_error_format):
        Password(
            plain_text_password='',
            salt='my_salt'
        )


# -----------------------------------------------------------------------------
# TEST WHEN GIVEN SAME PASSWORD AND SAME SALT THE HASH IS CONSISTENT
# -----------------------------------------------------------------------------
def test_password_when_given_same_password_and_same_salt_the_hash_is_not_the_same():

    # Prepare
    password_1 = get_valid_password()
    password_2 = get_valid_password()

    # Assert
    assert password_1.password_hash != password_2.password_hash


# -----------------------------------------------------------------------------
# TEST WHEN GIVEN SAME PASSWORD AND SAME SALT THE HASH IS CONSISTENT
# -----------------------------------------------------------------------------
def test_password_when_given_same_password_and_same_salt_password_verifies_correctly():

    # Prepare
    password_hash = '$argon2id$v=19$m=65536,t=2,p=1$xZ/2WMequJtBMqRjp7F1Yg$NPENoE37OIcz6YD6Rk7rJSXxnWE6rOBaBkzk4m8OO8w'
    password = get_valid_password()
    # Act
    actual = password.verify(stored_hash=password_hash)

    # Assert
    assert actual


# -----------------------------------------------------------------------------
# TEST WHEN NO STORED HASH IS PROVIDED ARGUMENT ERROR IS RAISED
# -----------------------------------------------------------------------------
def test_password_when_no_stored_hash_is_provided_argument_error_is_raised():

    # Prepare
    expected_error_format = 'stored_hash is required'
    password = get_valid_password()
    # Assert
    with pytest.raises(ValueError, match=expected_error_format):
        password.verify()


# -----------------------------------------------------------------------------
# TEST WHEN EMPTY STORED HASH IS PROVIDED ARGUMENT ERROR IS RAISED
# -----------------------------------------------------------------------------
def test_password_when_empty_stored_hash_is_provided_argument_error_is_raised():

    # Prepare
    expected_error_format = 'stored_hash cannot be an empty string'
    password = get_valid_password()
    # Assert
    with pytest.raises(ValueError, match=expected_error_format):
        password.verify(stored_hash='')


# -----------------------------------------------------------------------------
# TEST WHEN GIVEN SAME PASSWORD AND SAME SALT THE HASH IS CONSISTENT
# -----------------------------------------------------------------------------
def test_identity_credential_when_given_same_password_and_same_salt_password_verifies_correctly():

    # Prepare
    password_hash = '$argon2id$v=19$m=65536,t=2,p=1$xZ/2WMequJtBMqRjp7F1Yg$NPENoE37OIcz6YD6Rk7rJSXxnWE6rOBaBkzk4m8OO8w'
    password: IdentityCredential = get_valid_identity_credential()
    # Act
    actual = password.verify(stored_hash=password_hash)

    # Assert
    assert actual
