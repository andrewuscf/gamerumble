'use strict';

angular.module('fantasyLcs').factory('pageData', function () {
	var sharedData = {};

	return {
		get: function (fieldName) {
			if (fieldName) {
				return sharedData[fieldName];
			} else {
				return sharedData;
			}
		},
		set: function (key, value) {
			sharedData[key] = value;
		},
		setSecondary: function (key, secondary, value) {
			if (sharedData[key]) {
				sharedData[key][secondary] = value;
			}
		}
	};
});