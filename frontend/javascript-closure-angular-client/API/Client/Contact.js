goog.provide('API.Client.Contact');

/**
 * contact for this project or customer
 * @record
 */
API.Client.Contact = function() {}

/**
 * internal id of contact, gets created by system
 * @type {!number}
 * @export
 */
API.Client.Contact.prototype.id;

/**
 * name of contact
 * @type {!string}
 * @export
 */
API.Client.Contact.prototype.name;

/**
 * mail adress of contact
 * @type {!string}
 * @export
 */
API.Client.Contact.prototype.mail;

/**
 * role of this contact
 * @type {!string}
 * @export
 */
API.Client.Contact.prototype.role;

