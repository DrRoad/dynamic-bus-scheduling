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
import time
from src.common.logger import log
from src.route_generator.route_generator_client import get_route_between_two_bus_stop_names, \
    get_route_between_multiple_bus_stop_names, get_waypoints_between_two_bus_stops, get_waypoints_between_multiple_bus_stops


def test_get_route_between_two_bus_stop_names(starting_bus_stop_name, ending_bus_stop_name):
    """
    :param starting_bus_stop_name: string
    :param ending_bus_stop_name: string
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_route_between_two_bus_stop_names: starting')
    start_time = time.time()

    # response = {'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #             'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #             'route': {'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
    #                       'distances_from_starting_node', 'times_from_starting_node',
    #                       'distances_from_previous_node', 'times_from_previous_node'}}
    response = get_route_between_two_bus_stop_names(starting_bus_stop_name=starting_bus_stop_name,
                                                    ending_bus_stop_name=ending_bus_stop_name)

    starting_bus_stop = response.get('starting_bus_stop')
    ending_bus_stop = response.get('ending_bus_stop')
    route = response.get('route')
    total_distance = route.get('total_distance')
    total_time = route.get('total_time')
    node_osm_ids = route.get('node_osm_ids')
    points = route.get('points')
    edges = route.get('edges')
    distances_from_starting_node = route.get('distances_from_starting_node')
    times_from_starting_node = route.get('times_from_starting_node')
    distances_from_previous_node = route.get('distances_from_previous_node')
    times_from_previous_node = route.get('times_from_previous_node')

    output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
             '\nending_bus_stop: ' + str(ending_bus_stop) + \
             '\ntotal_distance: ' + str(total_distance) +\
             '\ntotal_time: ' + str(total_time) +\
             '\nnode_osm_ids: ' + str(node_osm_ids) +\
             '\npoints: ' + str(points) +\
             '\nedges: ' + str(edges) +\
             '\ndistances_from_starting_node: ' + str(distances_from_starting_node) +\
             '\ntimes_from_starting_node: ' + str(times_from_starting_node) +\
             '\ndistances_from_previous_node: ' + str(distances_from_previous_node) +\
             '\ntimes_from_previous_node: ' + str(times_from_previous_node)

    print output

    elapsed_time = time.time() - start_time
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_route_between_two_bus_stop_names: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


def test_get_route_between_multiple_bus_stop_names(bus_stop_names):
    """
    :param bus_stop_names: [string]
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_route_between_multiple_bus_stop_names: starting')
    start_time = time.time()

    # response = [{'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #              'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #              'route': {'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
    #                        'distances_from_starting_node', 'times_from_starting_node',
    #                        'distances_from_previous_node', 'times_from_previous_node'}}]
    response = get_route_between_multiple_bus_stop_names(bus_stop_names=bus_stop_names)

    for intermediate_response in response:
        starting_bus_stop = intermediate_response.get('starting_bus_stop')
        ending_bus_stop = intermediate_response.get('ending_bus_stop')
        intermediate_route = intermediate_response.get('route')
        total_distance = intermediate_route.get('total_distance')
        total_time = intermediate_route.get('total_time')
        node_osm_ids = intermediate_route.get('node_osm_ids')
        points = intermediate_route.get('points')
        edges = intermediate_route.get('edges')
        distances_from_starting_node = intermediate_route.get('distances_from_starting_node')
        times_from_starting_node = intermediate_route.get('times_from_starting_node')
        distances_from_previous_node = intermediate_route.get('distances_from_previous_node')
        times_from_previous_node = intermediate_route.get('times_from_previous_node')

        output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                 '\nending_bus_stop: ' + str(ending_bus_stop) + \
                 '\ntotal_distance: ' + str(total_distance) +\
                 '\ntotal_time: ' + str(total_time) +\
                 '\nnode_osm_ids: ' + str(node_osm_ids) +\
                 '\npoints: ' + str(points) +\
                 '\nedges: ' + str(edges) +\
                 '\ndistances_from_starting_node: ' + str(distances_from_starting_node) +\
                 '\ntimes_from_starting_node: ' + str(times_from_starting_node) +\
                 '\ndistances_from_previous_node: ' + str(distances_from_previous_node) +\
                 '\ntimes_from_previous_node: ' + str(times_from_previous_node)

        print output

    elapsed_time = time.time() - start_time
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_route_between_multiple_bus_stop_names: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


def test_get_waypoints_between_two_bus_stops(starting_bus_stop_name, ending_bus_stop_name):
    """
    :param starting_bus_stop_name: string
    :param ending_bus_stop_name:  string
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='find_bus_stop_waypoints_document: starting')
    start_time = time.time()

    # response = {'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #             'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #             'waypoints': [[{'_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #                             'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #                             'max_speed', 'road_type', 'way_id', 'traffic_density'}]]}
    response = get_waypoints_between_two_bus_stops(starting_bus_stop_name, ending_bus_stop_name)

    starting_bus_stop = response.get('starting_bus_stop')
    ending_bus_stop = response.get('ending_bus_stop')
    waypoints = response.get('waypoints')

    output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
             '\nending_bus_stop: ' + str(ending_bus_stop)
    print output

    for separate_waypoints in waypoints:
        print 'waypoints: ' + str(separate_waypoints)

    elapsed_time = time.time() - start_time
    log(module_name='route_generator_test', log_type='INFO',
        log_message='find_bus_stop_waypoints_document: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


def test_get_waypoints_between_multiple_bus_stops(bus_stop_names):
    """
    :param bus_stop_names: [string]
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_waypoints_between_multiple_bus_stops: starting')
    start_time = time.time()

    # response = [{'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #              'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #              'waypoints': [[{'_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #                              'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #                              'max_speed', 'road_type', 'way_id', 'traffic_density'}]]}]
    response = get_waypoints_between_multiple_bus_stops(bus_stop_names)

    for intermediate_response in response:
        starting_bus_stop = intermediate_response.get('starting_bus_stop')
        ending_bus_stop = intermediate_response.get('ending_bus_stop')
        waypoints = intermediate_response.get('waypoints')

        output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                 '\nending_bus_stop: ' + str(ending_bus_stop)
        print output

        for separate_waypoints in waypoints:
            print 'waypoints: ' + str(separate_waypoints)

    elapsed_time = time.time() - start_time
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_waypoints_between_multiple_bus_stops: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


if __name__ == '__main__':
    bus_stop_names = ['Centralstationen', 'Stadshuset', 'Skolgatan', 'Ekonomikum', 'Studentstaden', 'Rickomberga',
                      'Oslogatan', 'Reykjaviksgatan', 'Ekebyhus', 'Sernanders väg', 'Flogsta centrum',
                      'Sernanders väg', 'Ekebyhus', 'Reykjaviksgatan', 'Oslogatan', 'Rickomberga',
                      'Studentstaden', 'Ekonomikum', 'Skolgatan', 'Stadshuset', 'Centralstationen']

    # test_get_route_between_two_bus_stop_names(
    #     starting_bus_stop_name='Ekebyhus',
    #     ending_bus_stop_name='Sernanders väg'
    # )

    # test_get_route_between_multiple_bus_stop_names(bus_stop_names=bus_stop_names)

    # test_get_waypoints_between_two_bus_stops(
    #     starting_bus_stop_name='Ekebyhus',
    #     ending_bus_stop_name='Sernanders väg'
    # )

    # test_get_waypoints_between_multiple_bus_stops(bus_stop_names=bus_stop_names)

