def logs():
        data = [{
                'timestamp' : '2021-11-09T15:32:37.912Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
        Order Created orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb origin=a301faae-b0d0-466e-9d0f-a3ed050ee78c target=2f928536-f44f-43f1-a0b3-66ca986dfb8c customer=Cadix order="{
          "origin": "7d47f8cd-edc0-492d-9e58-09865d2d63b0",
          "target": "5ea0132c-181c-4f87-9d55-498540a6fb3d",
          "userId": "U0002",
          "requestedDropoffTime": "2022-01-01T10:15:30+01:00",
          "estimatedCargoWeight": "1.40",
          "containerId": "C0002",
          "contentlist": [
                {
                  "externalIdentifier": "I0001",
                  "specimenMaterial": "FrozenSection",
                  "specimenUrgency": "Critical"
                }
          ]
        }"
                '''
        },{
                'timestamp' : '2021-11-09T15:33:37.000Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
        Flight Reserved orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f uavId=10ff6a53-efcd-41ea-85a0-4c54d0f104f9
                '''
        },{
                'timestamp' : '2021-11-09T15:33:40.000Z',
                'type' : 'FLIGHT',
                'id' : 'ad30c4fe-885b-4b32-9de2-264eeb655d7f',
                'message' : '''
        Drone at origin flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f uavId=10ff6a53-efcd-41ea-85a0-4c54d0f104f9 location=a301faae-b0d0-466e-9d0f-a3ed050ee78c
                '''
        },{
                'timestamp' : '2021-11-09T15:34:30.000Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
        Cargo received orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb
                '''
        },{
                'timestamp' : '2021-11-09T15:34:40.000Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
        Cargo loaded orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb
                '''
        },{
                'timestamp' : '2021-11-09T15:34:42.000Z',
                'type' : 'FLIGHT',
                'id' : 'ad30c4fe-885b-4b32-9de2-264eeb655d7f',
                'message' : r'''
        Flightplan uploaded flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f originalFlightPlan="{
          "version": "1.1.0",
          "flightPoints": [
                {
                  "latitude": 50.79255133602314,
                  "longitude": 5.193454027175904,
                  "altitudeAMSL": 0,
                  "timeUTC": "2021-11-08T13:41:39.000",
                  "additionalProperties": {}
                },
                {
                  "latitude": 50.79254892769045,
                  "longitude": 5.193475484848023,
                  "altitudeAMSL": 70,
                  "timeUTC": "2021-11-08T13:42:21.000"
                },
                {
                  "latitude": 50.792510619004666,
                  "longitude": 5.197080373764039,
                  "altitudeAMSL": 70,
                  "timeUTC": "2021-11-08T13:43:12.000"
                },
                {
                  "latitude": 50.79433447016962,
                  "longitude": 5.19705891609192,
                  "altitudeAMSL": 70,
                  "timeUTC": "2021-11-08T13:43:53.000"
                },
                {
                  "latitude": 50.79437327855864,
                  "longitude": 5.19330382347107,
                  "altitudeAMSL": 70,
                  "timeUTC": "2021-11-08T13:44:45.000"
                },
                {
                  "latitude": 50.7925692879648,
                  "longitude": 5.1931965351104745,
                  "altitudeAMSL": 70,
                  "timeUTC": "2021-11-08T13:45:29.000"
                },
                {
                  "latitude": 50.7925692879648,
                  "longitude": 5.1931965351104745,
                  "altitudeAMSL": 0,
                  "timeUTC": "2021-11-08T13:45:29.000"
                }
          ]
        }" translatedFlightPlan="// Initialization
        Metric
        dim east
        dim north
        dim absolute
        [pidLoopSelect]=0
        takeoff
        climb 0.000
        waitClimb 0.000
        [targetspeed]=0.13
        climb 70.000
        flyTo (5.19348 E, 50.79255 N)
        [targetspeed]=17.89
        flyTo (5.19708 E, 50.79251 N)
        [targetspeed]=17.81
        flyTo (5.19706 E, 50.79433 N)
        [targetspeed]=18.27
        flyTo (5.19330 E, 50.79437 N)
        hoverAt (5.19320 E, 50.79257 N)
        climb 10.000
        waitClimb 10.000
        circuit (5.19320 E, 50.79257 N), 0, 0
        repeat -1
        // Patterns and Emergency Scenarios
        fixed

        definePattern 0
        climb 10
        waitClimb 10
        return

        definePattern 1
        climb 20
        waitClimb 20
        return

        definePattern 2
        hoverAt (40, 0)
        wait 25
        hoverAt (0, 0)
        return

        definePattern 3
        hoverAt (0, 0)
        repeat -1

        definePattern 4
        hoverAt [home]
        repeat -1

        definePattern 5
        buildAbsoluteWaypoint [east], [north] // build new waypoint at location (97W, 50N) and place on stack
        pop [absolute] // pops waypoint off stack into new field
        flyTo [absolute]
        circuit [absolute], 0, 0
        repeat -1

        definePattern 6
        circuit (0, 0), 0, 0
        return

        definePattern 7
        return

        definePattern 8
        return

        definePattern 9
        return

        definePattern 10
        return

        definePattern 11
        return

        definePattern 12
        return

        definePattern 13
        return

        definePattern 14
        return

        definePattern 15
        wait 0   // pause thread until payload button activates this
        [heliStopEngine] = 1
        repeat -1


        definePattern rcFailed
        circuit [home], 0, 0
        repeat -1

        definePattern gpsFailed
        repeat -1

        definePattern gcsFailed
        circuit [home], 0, 0
        repeat -1

        thread 1
        skipInRange [SERVO_CH5], 2600, 2800, 3
        [ch5SwitchType]=1
        repeat -2
        [ch5SwitchType]=6
        repeat -4"
                '''
        },{
                'timestamp' : '2021-11-09T15:34:45.123Z',
                'type' : 'FLIGHT',
                'id' : 'ad30c4fe-885b-4b32-9de2-264eeb655d7f',
                'message' : '''
        Drone Departed orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f uavId=10ff6a53-efcd-41ea-85a0-4c54d0f104f9 location=a301faae-b0d0-466e-9d0f-a3ed050ee78c
                '''
        },{
                'timestamp' : '2021-11-09T15:34:45.123Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
        Drone Departed orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f uavId=10ff6a53-efcd-41ea-85a0-4c54d0f104f9 location=a301faae-b0d0-466e-9d0f-a3ed050ee78c
                '''
        },{
                'timestamp' : ' 2021-11-09T15:34:50.123Z ',
                'type' : 'FLIGHT',
                'id' : 'ad30c4fe-885b-4b32-9de2-264eeb655d7f',
                'message' : r'''
        Skeys Telemetry body="class Trace {
        gpsAltitude: null
        gpsGDOP: null
        gpsNumberOfSatellites: null
        metaData: []
        operationDescription: null
        operationId: null
        operationalStatus: null
        operatorId: null
        pilotPosition: null
        providerExtraDetails: null
        providerId: X
        registrationId: null
        status: null
        telemetry: null
        traceTimestamp: 2021-11-09T15:32:39.155Z
        uavGroundSpeed: null
        uavHeading: 38.2706744
        uavHorizontalAccuracy: null
        uavHorizontalVelocity: class Speed {
                a0: null
                a1: null
                a2: null
                speedValue: 27.272092996639135
                type: null
                unitOfMeasure: METERS_PER_SECOND
        }
        uavId: 10ff6a53-efcd-41ea-85a0-4c54d0f104f9
        uavModel: null
        uavPosition: class Position {
                a0: null
                a1: null
                a2: null
                altitude: class Altitude {
                        altitude: 480.0
                        reference: W84
                        source: drone
                        unitOfMeasure: METERS
                }
                altitudes: [class Altitude {
                        altitude: 480.0
                        reference: W84
                        source: drone
                        unitOfMeasure: METERS
                }]
                coordinates: class Coordinates {
                        latitude: 50.7946726
                        longitude: 5.20474205
                }
                source: null
                type: null
        }
        uavSerialNumber: null
        uavSize: null
        uavSizeUnit: null
        uavSpeed: null
        uavSpeedAccuracy: null
        uavType: null
        uavVerticalAccuracy: null
        uavVerticalVelocity: class Speed {
                a0: null
                a1: null
                a2: null
                speedValue: -0.0
                type: null
                unitOfMeasure: METERS_PER_SECOND
        }"
                '''
        },{
                'timestamp' : '2021-11-09T15:37:50.123Z',
                'type' : 'FLIGHT',
                'id' : 'ad30c4fe-885b-4b32-9de2-264eeb655d7f',
                'message' : '''
        Drone Arrived orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f uavId=10ff6a53-efcd-41ea-85a0-4c54d0f104f9 location=2f928536-f44f-43f1-a0b3-66ca986dfb8c
                '''
        },{
                'timestamp' : '2021-11-09T15:37:50.123Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
        Drone Arrived orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb flightId=ad30c4fe-885b-4b32-9de2-264eeb655d7f uavId=10ff6a53-efcd-41ea-85a0-4c54d0f104f9 location=2f928536-f44f-43f1-a0b3-66ca986dfb8c
                '''
        },{
                'timestamp' : '2021-11-09T15:40:50.123Z',
                'type' : 'ORDER',
                'id' : '692cf3ee-a17f-40fd-aafc-8a1160d962cb',
                'message' : '''
         Cargo Picked Up orderId=692cf3ee-a17f-40fd-aafc-8a1160d962cb location=2f928536-f44f-43f1-a0b3-66ca986dfb8c cargoId=68577ddf-028b-4f1b-9b7d-a1de9748f344
                '''
        }]
        return data
