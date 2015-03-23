'use strict';

/**
 * @ngdoc function
 * @name fantasyLcs.controller:headerControllrt
 * @description
 * # headerController
 * Controller of the header items
 */
angular.module('fantasyLcs').controller('headerController', ['$scope', '$location', function ($scope, $location) {
	$scope.isActive = function (viewLocation) {
		return viewLocation === $location.path();
	};
}]);