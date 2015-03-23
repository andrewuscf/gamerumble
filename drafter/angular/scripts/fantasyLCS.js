'use strict';

/**
 * @ngdoc overview
 * @name fantasyLcs
 * @description
 * # fantasyLcs
 *
 * Main module of the application.
 */

var fantasyLCS = angular.module('fantasyLcs', ['ngRoute']);


fantasyLCS.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
	$locationProvider.html5Mode(true);

    $routeProvider
        .when('/', {
            templateUrl: 'views/players.html',
            controller: 'playersController',
            resolve: {
                getFantasyLcsData: fantasyLCS.getFantasyLcsData
            }
        })
        .when('/teams', {
            templateUrl: 'views/teams.html',
            controller: 'teamsController',
            resolve: {
                getFantasyLcsData: fantasyLCS.getFantasyLcsData
            }
        })
        .otherwise({
            redirectTo: '/'
        });
}]);

fantasyLCS.run(['pageData', function (pageData) {
    pageData.set('data', '');

	pageData.set('pointsPerStat', {
		kills: 2,
		deaths: -0.5,
		assists: 1.5,
		minionKills: 0.01,
		doubleKills: 0,
		tripleKills: 2,
		quadraKills: 3,
		pentaKills: 5,
		killOrAssistBonus: 2,
		firstBlood: 2,
		towerKills: 1,
		baronKills: 2,
		dragonKills: 1,
		matchVictory: 2,
		matchDefeat: 0
	});

	pageData.set('positions', [
		{
			title: 'All',
			id: ''
		},
		{
			title: 'Top',
			id: 'Top Lane'
		},
		{
			title: 'Jungle',
			id: 'Jungler'
		},
		{
			title: 'Mid',
			id: 'Mid Lane'
		},
		{
			title: 'ADC',
			id: 'AD Carry'
		},
		{
			title: 'Support',
			id: 'Support'
		}
	]);

}]);

fantasyLCS.getFantasyLcsData = ['$q', 'baseFunctions', function ($q, baseFunctions) {
    var allCalls = [];

	allCalls.push(baseFunctions.getFantasyLcsData());

	return $q.all(allCalls); //this is to ensure that the page waits to load until all the server calls are complete
}];