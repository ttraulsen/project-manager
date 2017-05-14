goog.provide('API.Client.Project');

/**
 * core object, the projects to track
 * @record
 */
API.Client.Project = function() {}

/**
 * internal id of project, gets created by system
 * @type {!number}
 * @export
 */
API.Client.Project.prototype.id;

/**
 * id of parent project so projects can be organized
 * @type {!number}
 * @export
 */
API.Client.Project.prototype.parent;

/**
 * @type {!string}
 * @export
 */
API.Client.Project.prototype.name;

/**
 * id of customer this project is done for
 * @type {!number}
 * @export
 */
API.Client.Project.prototype.customer;

/**
 * start date of project
 * @type {!Date}
 * @export
 */
API.Client.Project.prototype.startdate;

/**
 * end date of project
 * @type {!Date}
 * @export
 */
API.Client.Project.prototype.enddate;

/**
 * type of this project
 * @type {!string}
 * @export
 */
API.Client.Project.prototype.type;

/**
 * kind of project
 * @type {!string}
 * @export
 */
API.Client.Project.prototype.kind;

/** @enum {string} */
API.Client.Project.TypeEnum = { 
  Kundenprojekt: 'Kundenprojekt',
  internes Projekt: 'internes Projekt',
  untergeordnet: 'untergeordnet',
  offen: 'offen',
}
/** @enum {string} */
API.Client.Project.KindEnum = { 
  Beratung: 'Beratung',
  SBF: 'SBF',
  RA / RRD: 'RA / RRD',
  SBF / RA / RRD: 'SBF / RA / RRD',
  Sonstiges: 'Sonstiges',
}
