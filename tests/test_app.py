from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmação)
    assert response.json() == {
        'message': 'Olá, Mundo!'
    }  # Corrigido para 'message'


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # Assert (afirmação)
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }  # Assert (afirmação)

    def test_read_users(client):
        response = client.get('users/')

        assert response.status_code == HTTPStatus.OK  # Assert (afirmação)
        assert response.json() == {
            'users': [
                {
                    'username': 'testusername',
                    'email': 'test@test.com',
                    'id': 1,
                }
            ]
        }

    def test_update_user(client):
        response = client.put(
            'users/1',
            json={
                'username': 'bob',
                'email': 'bob@example.com',
                'password': 'password',
                'id': 1,
            },
        )
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {
            'username': 'bob',
            'email': 'bob@example.com',
            'id': 1,
        }

    def test_delete_user(client):
        response = client.delete('users/1')

        assert response.json() == {
            'message': 'Usuário deletado com sucesso'
        }
        assert response.status_code == HTTPStatus.OK
