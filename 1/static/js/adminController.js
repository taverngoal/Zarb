/**
 * Created by tavern on 13-11-30.
 */
var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource'])
    .controller('generalCTRL', ['$scope', '$location', function ($scope, $location) {

    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/post/list', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/list.html'
            }).when('/post/new', {
                controller: 'postFormCTRL',
                templateUrl: '/static/templates/post/form.html'
            }).when('/post/edit/:id', {
                controller: 'deviceListCTRL',
                templateUrl: '/Device/GridView'
            });
    }]);

var post = angular.module('blog.post', [])
    .factory('postService', function ($resource) {
        return $resource('/post/:id', {'id': '@id'}, {
            getlist: { method: 'get', isArray: false, url: '/post'}
        });
    })
    .controller('postListCTRL', ['$scope', 'postService', '$http', function ($scope, postService, $http) {
        postService.getlist(function (content) {
            $scope.posts = content.posts
        });
    }])
    .controller('postFormCTRL', ['$scope', 'postService', '$location', function ($scope, postService, $location) {
        var editor = new UE.ui.Editor();
        editor.render("postNew");
        $scope.post = new postService();

        $scope.submit = function () {
            $scope.post.content = editor.getContent();
            $scope.post.$save(function (content) {
                if (content.success) {
                    $location.path("/post/list")
                    $(".alert-success").alert();
                } else {

                }
            });
        };
    }]);