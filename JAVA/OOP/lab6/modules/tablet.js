/** @module tablet */

import Device from './device.js';

/**
 * Class representing a phone.
 * @extends Device
 */
 export default class Tablet extends Device {
  constructor(power, radiation, status) {
    super(power, radiation, status);
  }
}
