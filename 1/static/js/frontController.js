/**
 * Created by tavern on 13-11-30.
 */

var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource', 'ngSanitize', 'ngAnimate'])
    .controller('generalCTRL', ['$scope', '$location', function ($scope, $location) {

    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/post/:id', {
                controller: 'postViewCTRL',
                templateUrl: '/static/templates/post/front_view.html'
            })
            .when('/', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            });
    }]);


var post = angular.module('blog.post', [])
    .factory('postService', function ($resource) {
        return $resource('/post/:id', {'id': '@id'}, {
            getlist: { method: 'get', isArray: false, url: '/post'}
        });
    })
    .controller('postListCTRL', ['$scope', 'postService', function ($scope, postService) {
        postService.getlist(function (content) {
            $scope.posts = content.posts
        });
    }])
    .controller('postViewCTRL', ['$scope', 'postService', '$route', function ($scope, postService, $route) {
        $scope.post = postService.get({id: $route.current.params.id});

    }]);