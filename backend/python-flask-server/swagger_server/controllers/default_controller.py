import connexion
from swagger_server.models.comment import Comment
from swagger_server.models.contact import Contact
from swagger_server.models.message import Message
from swagger_server.models.project import Project
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def projects_delete(project):
    """
    You shouldn&#39;t delete the entire List
    
    :param project: The project you want to delete
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Project.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_get():
    """
    List all projects
    

    :rtype: List[Project]
    """
    return 'do some magic!'


def projects_id_comments_delete(id, project):
    """
    You can&#39;t delete the entire List
    
    :param id: Project id
    :type id: int
    :param project: The comment you want to delete
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Comment.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_comments_get(id):
    """
    List all comments on this project
    
    :param id: Project id
    :type id: int

    :rtype: List[Comment]
    """
    return 'do some magic!'


def projects_id_comments_patch(id, project):
    """
    You can&#39;t put the entire List
    
    :param id: Project id
    :type id: int
    :param project: The comment you want to update
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Comment.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_comments_post(id, project):
    """
    Create a new comment
    
    :param id: Project id
    :type id: int
    :param project: The comment you want to create
    :type project: dict | bytes

    :rtype: Message
    """
    if connexion.request.is_json:
        project = Comment.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_comments_put(id, project):
    """
    You can&#39;t put the entire List
    
    :param id: Project id
    :type id: int
    :param project: The comment you want to update
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Comment.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_contacts_delete(id, project):
    """
    You can&#39;t delete the entire List
    
    :param id: Project id
    :type id: int
    :param project: The contact you want to delete
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Contact.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_contacts_get(id):
    """
    List all contacts associated with this project
    
    :param id: Project id
    :type id: int

    :rtype: List[Contact]
    """
    return 'do some magic!'


def projects_id_contacts_patch(id, project):
    """
    You can&#39;t put the entire List
    
    :param id: Project id
    :type id: int
    :param project: The contact you want to update
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Contact.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_contacts_post(id, project):
    """
    Add a new contact
    
    :param id: Project id
    :type id: int
    :param project: The comment you want to create
    :type project: dict | bytes

    :rtype: Message
    """
    if connexion.request.is_json:
        project = Contact.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_contacts_put(id, project):
    """
    You can&#39;t put the entire List
    
    :param id: Project id
    :type id: int
    :param project: The contact you want to update
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Contact.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_delete(id):
    """
    Delete a project
    
    :param id: The project id you want to delete.
    :type id: float

    :rtype: Message
    """
    return 'do some magic!'


def projects_id_get(id):
    """
    get specific project by id
    
    :param id: Project id
    :type id: int

    :rtype: Project
    """
    return 'do some magic!'


def projects_id_post(id, project):
    """
    update an existing project
    
    :param id: The project id
    :type id: float
    :param project: the project you want to update
    :type project: dict | bytes

    :rtype: Message
    """
    if connexion.request.is_json:
        project = Project.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_id_put(id, project):
    """
    update an existing project
    
    :param id: The project id
    :type id: float
    :param project: the project you want to update
    :type project: dict | bytes

    :rtype: Message
    """
    if connexion.request.is_json:
        project = Project.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_patch(project):
    """
    You shouldn&#39;t put the entire List
    
    :param project: The project you want to update
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Project.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_post(project):
    """
    Create a new project
    
    :param project: The project you want to create
    :type project: dict | bytes

    :rtype: Message
    """
    if connexion.request.is_json:
        project = Project.from_dict(connexion.request.get_json())
    return 'do some magic!'


def projects_put(project):
    """
    You shouldn&#39;t put the entire List
    
    :param project: The project you want to update
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Project.from_dict(connexion.request.get_json())
    return 'do some magic!'
