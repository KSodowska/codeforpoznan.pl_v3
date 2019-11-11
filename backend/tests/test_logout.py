from http import HTTPStatus
import pytest


def test_logout_user_with_valid_access_token(client, tokens):
    """Test logout with fresh access token."""
    rv = client.delete('/auth/logout/',
                       headers={'Authorization': 'Bearer {}'
                                .format(tokens["access"])})
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert response['msg'] == 'Successfully logged out'


@pytest.mark.parametrize('url', ['/auth/logout/', '/auth/revoke-refresh-token/'])
def test_logout_user_without_token(client, url):
    """Test logout with no token provided."""
    rv = client.delete(url)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response['msg'] == 'Missing Authorization Header'


def test_revoke_refresh_token(client, tokens):
    """Test revoke refresh token."""
    rv = client.delete(
        "/auth/revoke-refresh-token/",
        headers={"Authorization": "Bearer {}".format(tokens["refresh"])}
    )

    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert response["msg"] == "Refresh token successfully revoked"
