goog.provide('API.Client.Status');

/**
 * status of project. There can be different owners of statuses - customer, internal etc.
 * @record
 */
API.Client.Status = function() {}

/**
 * internal id of status, gets created by system
 * @type {!number}
 * @export
 */
API.Client.Status.prototype.id;

/**
 * owner of status to differentiate between status by customer and internal status
 * @type {!string}
 * @export
 */
API.Client.Status.prototype.owner;

/**
 * status code, normally a number between 01 and 99, should be formatted as 00
 * @type {!number}
 * @export
 */
API.Client.Status.prototype.code;

/**
 * name of status, for example \"planned\", \"staffed\", \"finished\"
 * @type {!string}
 * @export
 */
API.Client.Status.prototype.status;

