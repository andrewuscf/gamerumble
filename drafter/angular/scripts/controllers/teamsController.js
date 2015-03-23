'use strict';

/**
 * @ngdoc function
 * @name fantasyLcs.controller:teamsController
 * @description
 * # teamsController
 * Controller of the teams
 */
angular.module('fantasyLcs').controller('teamsController', ['$scope', '$filter', 'pageData', function ($scope, $filter, pageData) {
	$scope.sharedData = pageData.get();

	console.log('$scope.sharedData', $scope.sharedData);

	$scope.weekShown = 0;
	$scope.sortingInfo = {
		by: 'pointsPerGame',
		descending: true
	};

	$scope.tableHeaders = [
		{
			title: 'Team',
			id: 'team',
			glyphicon: 'glyphicon glyphicon-sort-by-alphabet',
			glyphiconAlt: 'glyphicon glyphicon-sort-by-alphabet-alt'
		},
		{
			title: 'Points',
			id: 'points',
			glyphicon: 'glyphicon-sort-by-attributes',
			glyphiconAlt: 'glyphicon-sort-by-attributes-alt'
		},
		{
			title: 'PPG',
			id: 'pointsPerGame',
			glyphicon: 'glyphicon-sort-by-attributes',
			glyphiconAlt: 'glyphicon-sort-by-attributes-alt'
		},
	];

	$scope.getNumber = function(num) {
		return new Array(num);
	};

	$scope.changeWeekShown = function (weekShown) {
		$scope.weekShown = weekShown;
		$scope.order();
	};

	$scope.changeOrder = function(by, direction) {
		if ($scope.sortingInfo.by === by) {
			$scope.sortingInfo.descending = !$scope.sortingInfo.descending;
		} else {
			if (by === 'pointsPerGame' || by === 'points') {
				$scope.sortingInfo.descending = true;
			} else if (by === 'name' || by === 'team') {
				$scope.sortingInfo.descending = false;
			}
			$scope.sortingInfo.by = by;
		}
		if (direction){
			$scope.sortingInfo.descending = direction;
		}
		$scope.order();
	};

	$scope.order = function() {
		$scope.sharedData.sortedProTeams = $filter('orderBy')($scope.sharedData.proTeams, $scope.sortMethod, $scope.sortingInfo.descending);
	};

	$scope.sortMethod = function (team) {
		if ($scope.sortingInfo.by === 'pointsPerGame') {
			return team.statsByWeek[$scope.weekShown].pointsPerGame;
		} else if ($scope.sortingInfo.by === 'points') {
			return team.statsByWeek[$scope.weekShown].totalPoints;
		} else if ($scope.sortingInfo.by === 'team') {
			return team.shortName;
		}
	};

	$scope.order();
}]);
