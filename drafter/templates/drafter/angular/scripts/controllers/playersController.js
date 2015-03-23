'use strict';

/**
 * @ngdoc function
 * @name fantasyLcs.controller:playersController
 * @description
 * # playersController
 * Controller of the players
 */
angular.module('fantasyLcs').controller('playersController', ['$scope', '$filter', 'pageData', function ($scope, $filter, pageData) {
    $scope.sharedData = pageData.get();

	$scope.weekShown = 0;
	$scope.curPosition = '';
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
			title: 'Name',
			id: 'name',
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
	$scope.positions = $scope.sharedData.positions;
	$scope.getNumber = function(num) {
		return new Array(num);
	};

    $scope.changePosition = function (position) {
        $scope.curPosition = position;
		$scope.playerOrder();
    };

	$scope.changeWeekShown = function (weekShown) {
		$scope.weekShown = weekShown;
		$scope.playerOrder();
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
		$scope.playerOrder();
	};

	$scope.playerOrder = function() {
		$scope.sharedData.sortedProPlayers = $filter('orderBy')($scope.sharedData.proPlayers, $scope.sortMethod, $scope.sortingInfo.descending);
	};

	$scope.sortMethod = function (player) {
		if ($scope.sortingInfo.by === 'pointsPerGame') {
			return player.statsByWeek[$scope.weekShown].pointsPerGame;
		} else if ($scope.sortingInfo.by === 'points') {
			return player.statsByWeek[$scope.weekShown].totalPoints;
		} else if ($scope.sortingInfo.by === 'name') {
			return player.name;
		} else if ($scope.sortingInfo.by === 'team') {
			return $scope.sharedData.proTeams[player.proTeamId].shortName;
		}
	};

	$scope.getTeamName = function(player) {
		return $filter('getByProperty')($scope.sharedData.proTeams, 'id', player.proTeamId)[0].shortName;
	};

	$scope.playerOrder();
}]);