/**
 * Project Tracker
 * Backend for a simple CRUD example application to track different projects
 *
 * OpenAPI spec version: v1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

import * as models from './models';

/**
 * contact for this project or customer
 */
export interface Contact {
    /**
     * internal id of contact, gets created by system
     */
    id?: number;

    /**
     * name of contact
     */
    name?: string;

    /**
     * mail adress of contact
     */
    mail?: string;

    /**
     * role of this contact
     */
    role?: string;

}