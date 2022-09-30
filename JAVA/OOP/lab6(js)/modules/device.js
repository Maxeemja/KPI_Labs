/** @module device */

import Set from './set.js';

/** Class representing a device */
export default class Device {
  /**
   * @param {Number} power power consumed by the device
   * @param {Number} radiation electromagnetic radiation , created by the device
   * @param {Boolean} status powered on / off;
   */
  constructor(power, radiation, status) {
    if (parseFloat(power) < 0 || parseFloat(radiation) < 0 || typeof(status)!='boolean') {
      throw new Error('Invalid arguments in Tool');
    }
    this.power = power;
    this.rad = radiation;
    this.status = status;
    if(status == true){
      Set.setOfDevices.push(this);
    }
  }
}
