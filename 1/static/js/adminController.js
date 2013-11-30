/**
 * Created by tavern on 13-11-30.
 */
var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource'])
    .controller('generalCTRL', ['$scope', '$location', function ($scope, $location) {
        var path = $location.path();
        $scope.module = path.substr(1, path.substr(1).indexOf('/'));
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
                controller: 'postFormCTRL',
                templateUrl: '/static/templates/post/form.html'
            }).otherwise({ redirectTo: '/home/' });
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
    .controller('postFormCTRL', ['$scope', 'postService', '$location', '$route', function ($scope, postService, $location, $route) {
        var id = $route.current.params.id;
        $scope.isEdit = id != undefined;
        var editor = new UE.ui.Editor();
        editor.render("postNew");
        if (id == undefined)
            $scope.post = new postService();
        else
            $scope.post = postService.get({ id: id }, function (content) {
                editor.setContent(content.content);
            });
        $scope.submit = function () {
            $scope.post.content = editor.getContent();
            $scope.post.$save(function (content) {
                if (content.success) {
                    $location.path("/post/list");
                    $(".alert-success").alert();
                } else {

                }
            });
        };

        $scope.delete = function () {
            postService.delete({id: Number(id)}, function (content) {
                if (content.success) {
                    $location.path("/post/list");
                } else {

                }
            });
        }
    }]);