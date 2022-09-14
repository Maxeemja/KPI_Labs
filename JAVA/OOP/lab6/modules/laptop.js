/** @module laptop */

import Device from './device.js';

/**
 * Class representing a laptop.
 * @extends Device
 */
 export default class Laptop extends Device {
  constructor(power, radiation, status) {
    super(power, radiation, status);
  }
}
