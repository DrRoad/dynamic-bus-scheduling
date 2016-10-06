#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2016 Eleftherios Anagnostopoulos for Ericsson AB (EU FP7 CityPulse Project)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import requests
import json

from bson import ObjectId

from src.common.variables import route_generator_host, route_generator_port, route_generator_request_timeout


class JSONResponseEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return o.__dict__


def get_route_between_two_bus_stops(starting_bus_stop, ending_bus_stop):
    """
    :param starting_bus_stop: {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}}
    :param ending_bus_stop: {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}}
    :return: {'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
              'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
              'route': {'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
                        'distances_from_starting_node', 'times_from_starting_node',
                        'distances_from_previous_node', 'times_from_previous_node'}}
    """
    url = 'http://' + route_generator_host + ':' + route_generator_port + '/get_route_between_two_bus_stops'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {'starting_bus_stop': starting_bus_stop,
            'ending_bus_stop': ending_bus_stop}
    json_data = json.dumps(data, cls=JSONResponseEncoder)
    request = requests.post(url, data=json_data, headers=headers, timeout=route_generator_request_timeout)
    response = json.loads(request.text)
    return response


def get_route_between_two_bus_stop_names(starting_bus_stop_name, ending_bus_stop_name):
    """
    :param starting_bus_stop_name: string
    :param ending_bus_stop_name: string
    :return: {'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
              'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
              'route': {'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
                        'distances_from_starting_node', 'times_from_starting_node',
                        'distances_from_previous_node', 'times_from_previous_node'}}
    """
    url = 'http://' + route_generator_host + ':' + route_generator_port + '/get_route_between_two_bus_stop_names'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {'starting_bus_stop_name': starting_bus_stop_name,
            'ending_bus_stop_name': ending_bus_stop_name}
    request = requests.post(url, data=data, headers=headers, timeout=route_generator_request_timeout)
    response = json.loads(request.text)
    return response


def get_route_between_multiple_bus_stops(bus_stops):
    """
    :param bus_stops: [{'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}}]
    :return: [{'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
               'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
               'route': {'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
                         'distances_from_starting_node', 'times_from_starting_node',
                         'distances_from_previous_node', 'times_from_previous_node'}}]
    """
    url = 'http://' + route_generator_host + ':' + route_generator_port + '/get_route_between_multiple_bus_stops'
    headers = {'content-type': 'application/json'}
    data = {'bus_stops': bus_stops}
    json_data = json.dumps(data, cls=JSONResponseEncoder)
    request = requests.post(url, data=json_data, headers=headers, timeout=route_generator_request_timeout)
    response = json.loads(request.text)
    return response


def get_route_between_multiple_bus_stop_names(bus_stop_names):
    """
    :param bus_stop_names: [string]
    :return: [{'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
               'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
               'route': {'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
                         'distances_from_starting_node', 'times_from_starting_node',
                         'distances_from_previous_node', 'times_from_previous_node'}}]
    """
    url = 'http://' + route_generator_host + ':' + route_generator_port + '/get_route_between_multiple_bus_stop_names'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {'bus_stop_names': bus_stop_names}
    request = requests.post(url, data=data, headers=headers, timeout=route_generator_request_timeout)
    response = json.loads(request.text)
    return response


def get_waypoints_between_two_bus_stops(starting_bus_stop_name, ending_bus_stop_name):
    """
    :param starting_bus_stop_name: string
    :param ending_bus_stop_name: string
    :return: {'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
              'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
              'waypoints': [[{'_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
                              'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
                              'max_speed', 'road_type', 'way_id', 'traffic_density'}]]}
    """
    url = 'http://' + route_generator_host + ':' + route_generator_port + '/find_bus_stop_waypoints_document'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {'starting_bus_stop_name': starting_bus_stop_name,
            'ending_bus_stop_name': ending_bus_stop_name}
    request = requests.post(url, data=data, headers=headers, timeout=route_generator_request_timeout)
    response = json.loads(request.text)
    return response


def get_waypoints_between_multiple_bus_stops(bus_stop_names):
    """
    :param bus_stop_names: [string]
    :return: [{'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
               'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
               'waypoints': [[{'_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
                               'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
                               'max_speed', 'road_type', 'way_id', 'traffic_density'}]]}]
    """
    url = 'http://' + route_generator_host + ':' + route_generator_port + '/get_waypoints_between_multiple_bus_stops'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {'bus_stop_names': bus_stop_names}
    request = requests.post(url, data=data, headers=headers, timeout=route_generator_request_timeout)
    response = json.loads(request.text)
    return response


# def get_multiple_routes_between_bus_stops(starting_bus_stop_name, ending_bus_stop_name, number_of_routes):
#     url = 'http://' + route_generator_host + ':' + route_generator_port + '/get_multiple_routes_between_bus_stops'
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     data = {'starting_bus_stop_name': starting_bus_stop_name,
#             'ending_bus_stop_name': ending_bus_stop_name,
#             'number_of_routes': number_of_routes}
#     request = requests.post(url, data=data, headers=headers, timeout=60)
#
#     # response = {'starting_bus_stop': {'osm_id', 'name', 'point': {'longitude', 'latitude'}},
#     #             'ending_bus_stop': {'osm_id', 'name', 'point': {'longitude', 'latitude'}},
#     #             'routes': [{'total_distance', 'total_time', 'node_osm_ids', 'points',
#                               'distances_from_starting_node', 'times_from_starting_node',
#                               'distances_from_previous_node', 'times_from_previous_node'}]}
#     response = json.loads(request.text)
#
#     starting_bus_stop = response.get('starting_bus_stop')
#     ending_bus_stop = response.get('ending_bus_stop')
#     routes = response.get('routes')
#
#     for route in routes:
#         total_distance = route.get('total_distance')
#         total_time = route.get('total_time')
#         node_osm_ids = route.get('node_osm_ids')
#         points = route.get('points')
#         distances_from_starting_node = route.get('distances_from_starting_node')
#         times_from_starting_node = route.get('times_from_starting_node')
#         distances_from_previous_node = route.get('distances_from_previous_node')
#         times_from_previous_node = route.get('times_from_previous_node')
#
#         # output = '\nRequest: get_multiple_routes_between_bus_stops' + \
#         output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
#                  '\nending_bus_stop: ' + str(ending_bus_stop) + \
#                  '\ntotal_distance: ' + str(total_distance) +\
#                  '\ntotal_time: ' + str(total_time) +\
#                  '\nnode_osm_ids: ' + str(node_osm_ids) +\
#                  '\npoints: ' + str(points) +\
#                  '\ndistances_from_starting_node: ' + str(distances_from_starting_node) +\
#                  '\ntimes_from_starting_node: ' + str(times_from_starting_node) +\
#                  '\ndistances_from_previous_node: ' + str(distances_from_previous_node) +\
#                  '\ntimes_from_previous_node: ' + str(times_from_previous_node)
#
#         print output


# def get_multiple_routes_between_multiple_bus_stops(bus_stop_names, number_of_routes):
#     url = 'http://' + route_generator_host + ':' + route_generator_port + \
#           '/get_multiple_routes_between_multiple_bus_stops'
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     data = {'bus_stop_names': bus_stop_names,
#             'number_of_routes': number_of_routes}
#     request = requests.post(url, data=data, headers=headers, timeout=60)
#     response = json.loads(request.text)
#
#     # response = [{'starting_bus_stop': {'osm_id', 'name', 'point': {'longitude', 'latitude'}},
#     #              'ending_bus_stop': {'osm_id', 'name', 'point': {'longitude', 'latitude'}},
#     #              'routes': [{'total_distance', 'total_time', 'node_osm_ids', 'points',
#     #                          'distances_from_starting_node', 'times_from_starting_node',
#     #                          'distances_from_previous_node', 'times_from_previous_node'}]}]
#
#     for intermediate_response in response:
#         starting_bus_stop = intermediate_response.get('starting_bus_stop')
#         ending_bus_stop = intermediate_response.get('ending_bus_stop')
#         intermediate_routes = intermediate_response.get('routes')
#
#         for intermediate_route in intermediate_routes:
#             total_distance = intermediate_route.get('total_distance')
#             total_time = intermediate_route.get('total_time')
#             node_osm_ids = intermediate_route.get('node_osm_ids')
#             points = intermediate_route.get('points')
#             distances_from_starting_node = intermediate_route.get('distances_from_starting_node')
#             times_from_starting_node = intermediate_route.get('times_from_starting_node')
#             distances_from_previous_node = intermediate_route.get('distances_from_previous_node')
#             times_from_previous_node = intermediate_route.get('times_from_previous_node')
#
#             # output = '\nRequest: get_route_between_multiple_bus_stop_names' + \
#             output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
#                      '\nending_bus_stop: ' + str(ending_bus_stop) + \
#                      '\ntotal_distance: ' + str(total_distance) +\
#                      '\ntotal_time: ' + str(total_time) +\
#                      '\nnode_osm_ids: ' + str(node_osm_ids) +\
#                      '\npoints: ' + str(points) +\
#                      '\ndistances_from_starting_node: ' + str(distances_from_starting_node) +\
#                      '\ntimes_from_starting_node: ' + str(times_from_starting_node) +\
#                      '\ndistances_from_previous_node: ' + str(distances_from_previous_node) +\
#                      '\ntimes_from_previous_node: ' + str(times_from_previous_node)
#
#             print output
