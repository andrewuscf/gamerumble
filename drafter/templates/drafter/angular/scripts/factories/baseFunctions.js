'use strict';

angular.module('fantasyLcs').factory('baseFunctions', ['$filter', 'pageData', 'serverCalls', function ($filter, pageData, serverCalls) {
	var sharedData = pageData.get(),
		functions = {};

	functions.getFantasyLcsData = function () {
        return serverCalls.getFantasyLcsData().success(function (data) {
            pageData.set('proMatches', data.proMatches);

			var proTeams = [];
			angular.forEach(data.proTeams, function (team) {
				var newObj = team,
					allWeeksObj = {},
					totalPointsForAllWeeks = 0,
					totalGamesForAllWeeks = 0;

				angular.forEach(newObj.statsByWeek, function (week, key) {
					totalPointsForAllWeeks += week.totalPoints = functions.calculateTeamPointsForWeek(week);
					totalGamesForAllWeeks += week.totalGames = functions.numberOfGamesPlayed(newObj, key);
					if (week.totalGames > 0) {
						week.pointsPerGame = week.totalPoints / week.totalGames;
					} else {
						week.pointsPerGame = 0;
					}
				});

				allWeeksObj.totalPoints = totalPointsForAllWeeks;
				allWeeksObj.totalGames = totalGamesForAllWeeks;
				allWeeksObj.pointsPerGame = totalPointsForAllWeeks / totalGamesForAllWeeks;

				newObj.statsByWeek[0] = allWeeksObj;

				if(allWeeksObj.totalPoints !== 0) {
					proTeams.push(newObj);
				}
			});
			pageData.set('proTeams', proTeams);

			var proPlayers = [];
			angular.forEach(data.proPlayers, function (player) {
				var newObj = player,
					allWeeksObj = {},
					totalPointsForAllWeeks = 0,
					totalGamesForAllWeeks = 0;

				angular.forEach(newObj.statsByWeek, function (week, key) {
					totalPointsForAllWeeks += week.totalPoints = functions.calculatePointsForWeek(week);
					totalGamesForAllWeeks += week.totalGames = functions.numberOfGamesPlayedForPlayers(newObj.proTeamId, key);
					if (week.totalGames > 0) {
						week.pointsPerGame = week.totalPoints / week.totalGames;
					} else {
						week.pointsPerGame = 0;
					}
				});

				allWeeksObj.totalPoints = totalPointsForAllWeeks;
				allWeeksObj.totalGames = totalGamesForAllWeeks;
				allWeeksObj.pointsPerGame = totalPointsForAllWeeks / totalGamesForAllWeeks;

				newObj.statsByWeek[0] = allWeeksObj;

				if(allWeeksObj.totalPoints !== 0) {
					proPlayers.push(newObj);
				}
			});
			pageData.set('proPlayers', proPlayers);
			pageData.set('numberOfWeeksPlayed', functions.numberOfWeeksPlayed());
        });
	};

	/*
	functions.getNALoLEsportsData = function (){
		return serverCalls.getNALoLEsportsData().success(function (data) {
			console.log('na data', data);
		});
	};
	functions.getEULoLEsportsData = function (){
		return serverCalls.getEULoLEsportsData().success(function (data) {
			console.log('eu data', data);
		});
	};
	*/



	functions.getLeagueData = function (){
		return serverCalls.getLeagueData().success(function (data) {
			pageData.set('pointsPerStat', data.pointsPerStat);
		});
	};

	/*
	functions.calculatePoints = function (player, weekShown) {
		var totalPoints = 0;

		if (weekShown === 0) {
			angular.forEach(player.statsByWeek, function (week) {
				totalPoints += functions.calculatePointsForWeek(week);
			});
		} else {
			totalPoints += functions.calculatePointsForWeek(player.statsByWeek[weekShown]);
		}
		return parseFloat(totalPoints);
	};
	*/

	functions.calculatePointsForWeek = function (week) {
		var totalPoints = 0;

		totalPoints += week.assists.actualValue * sharedData.pointsPerStat.assists;
		totalPoints += week.deaths.actualValue * sharedData.pointsPerStat.deaths;
		totalPoints += week.doubleKills.actualValue * sharedData.pointsPerStat.doubleKills;
		totalPoints += week.killOrAssistBonus.actualValue * sharedData.pointsPerStat.killOrAssistBonus;
		totalPoints += week.kills.actualValue * sharedData.pointsPerStat.kills;
		totalPoints += week.minionKills.actualValue * sharedData.pointsPerStat.minionKills;
		totalPoints += week.pentaKills.actualValue * sharedData.pointsPerStat.pentaKills;
		totalPoints += week.quadraKills.actualValue * sharedData.pointsPerStat.quadraKills;
		totalPoints += week.tripleKills.actualValue * sharedData.pointsPerStat.tripleKills;

		return totalPoints;
	};

	functions.calculateTeamPointsForWeek = function (week) {
		var totalPoints = 0;

		totalPoints += week.firstBlood.actualValue * sharedData.pointsPerStat.firstBlood;
		totalPoints += week.towerKills.actualValue * sharedData.pointsPerStat.towerKills;
		totalPoints += week.baronKills.actualValue * sharedData.pointsPerStat.baronKills;
		totalPoints += week.dragonKills.actualValue * sharedData.pointsPerStat.dragonKills;
		totalPoints += week.matchVictory.actualValue * sharedData.pointsPerStat.matchVictory;
		totalPoints += week.matchDefeat.actualValue * sharedData.pointsPerStat.matchDefeat;

		return totalPoints;
	};

	functions.numberOfGamesPlayed = function (team, week) {
		var whichWeek = team.statsByWeek[week];

		if(whichWeek.totalGames) {
			return whichWeek.totalGames;
		} else {
			return whichWeek.matchDefeat.actualValue + whichWeek.matchVictory.actualValue;
		}
	};

	functions.numberOfGamesPlayedForPlayers = function (proTeamId, week) {
		var team = $filter('getByProperty')(sharedData.proTeams, 'id', proTeamId)[0];
		return functions.numberOfGamesPlayed(team, week);
	};

	functions.numberOfWeeksPlayed = function () {
		var weeksPlayed = [];
		angular.forEach(sharedData.proMatches, function (match) {
			if (match.complete && weeksPlayed[match.week-1] !== true) {
				weeksPlayed[match.week-1] = match.complete;
			}
		});
		if (weeksPlayed.length > 5) {
			return weeksPlayed.length;
		} else {
			return 6;
		}
	};

	return functions;
}]);