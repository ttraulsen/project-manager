# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.comment import Comment
from swagger_server.models.contact import Contact
from swagger_server.models.message import Message
from swagger_server.models.project import Project
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_projects_delete(self):
        """
        Test case for projects_delete

        You shouldn't delete the entire List
        """
        project = Project()
        response = self.client.open('/project-tracker/projects',
                                    method='DELETE',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_get(self):
        """
        Test case for projects_get

        List all projects
        """
        response = self.client.open('/project-tracker/projects',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_comments_delete(self):
        """
        Test case for projects_id_comments_delete

        You can't delete the entire List
        """
        project = Comment()
        response = self.client.open('/project-tracker/projects/{id}/comments'.format(id=56),
                                    method='DELETE',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_comments_get(self):
        """
        Test case for projects_id_comments_get

        List all comments on this project
        """
        response = self.client.open('/project-tracker/projects/{id}/comments'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_comments_patch(self):
        """
        Test case for projects_id_comments_patch

        You can't put the entire List
        """
        project = Comment()
        response = self.client.open('/project-tracker/projects/{id}/comments'.format(id=56),
                                    method='PATCH',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_comments_post(self):
        """
        Test case for projects_id_comments_post

        Create a new comment
        """
        project = Comment()
        response = self.client.open('/project-tracker/projects/{id}/comments'.format(id=56),
                                    method='POST',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_comments_put(self):
        """
        Test case for projects_id_comments_put

        You can't put the entire List
        """
        project = Comment()
        response = self.client.open('/project-tracker/projects/{id}/comments'.format(id=56),
                                    method='PUT',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_contacts_delete(self):
        """
        Test case for projects_id_contacts_delete

        You can't delete the entire List
        """
        project = Contact()
        response = self.client.open('/project-tracker/projects/{id}/contacts'.format(id=56),
                                    method='DELETE',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_contacts_get(self):
        """
        Test case for projects_id_contacts_get

        List all contacts associated with this project
        """
        response = self.client.open('/project-tracker/projects/{id}/contacts'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_contacts_patch(self):
        """
        Test case for projects_id_contacts_patch

        You can't put the entire List
        """
        project = Contact()
        response = self.client.open('/project-tracker/projects/{id}/contacts'.format(id=56),
                                    method='PATCH',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_contacts_post(self):
        """
        Test case for projects_id_contacts_post

        Add a new contact
        """
        project = Contact()
        response = self.client.open('/project-tracker/projects/{id}/contacts'.format(id=56),
                                    method='POST',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_contacts_put(self):
        """
        Test case for projects_id_contacts_put

        You can't put the entire List
        """
        project = Contact()
        response = self.client.open('/project-tracker/projects/{id}/contacts'.format(id=56),
                                    method='PUT',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_delete(self):
        """
        Test case for projects_id_delete

        Delete a project
        """
        response = self.client.open('/project-tracker/projects/{id}'.format(id=3.4),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_get(self):
        """
        Test case for projects_id_get

        get specific project by id
        """
        response = self.client.open('/project-tracker/projects/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_post(self):
        """
        Test case for projects_id_post

        update an existing project
        """
        project = Project()
        response = self.client.open('/project-tracker/projects/{id}'.format(id=3.4),
                                    method='POST',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_id_put(self):
        """
        Test case for projects_id_put

        update an existing project
        """
        project = Project()
        response = self.client.open('/project-tracker/projects/{id}'.format(id=3.4),
                                    method='PUT',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_patch(self):
        """
        Test case for projects_patch

        You shouldn't put the entire List
        """
        project = Project()
        response = self.client.open('/project-tracker/projects',
                                    method='PATCH',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_post(self):
        """
        Test case for projects_post

        Create a new project
        """
        project = Project()
        response = self.client.open('/project-tracker/projects',
                                    method='POST',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_projects_put(self):
        """
        Test case for projects_put

        You shouldn't put the entire List
        """
        project = Project()
        response = self.client.open('/project-tracker/projects',
                                    method='PUT',
                                    data=json.dumps(project),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
