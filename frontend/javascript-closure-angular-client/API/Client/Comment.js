goog.provide('API.Client.Comment');

/**
 * comment to a project
 * @record
 */
API.Client.Comment = function() {}

/**
 * internal id of comment, gets created by system
 * @type {!number}
 * @export
 */
API.Client.Comment.prototype.id;

/**
 * id of project this comment is about
 * @type {!number}
 * @export
 */
API.Client.Comment.prototype.project;

/**
 * actual comment
 * @type {!string}
 * @export
 */
API.Client.Comment.prototype.comment;

/**
 * timestamp of this comment
 * @type {!Date}
 * @export
 */
API.Client.Comment.prototype.timestamp;

/**
 * id of the user this comment came from
 * @type {!number}
 * @export
 */
API.Client.Comment.prototype.user;

