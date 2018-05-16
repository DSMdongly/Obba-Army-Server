MUSIC_CHART_GET_SPEC = {
    'tags': ['음원 차트'],
    'description': '멜론(melon), 지니(genie), 벅스(bugs)의 TOP 100 음원 차트를 조회',
    'parameters': [
        {
            'name': 'site_name',
            'description': '조회하고자 하는 음원 차트 사이트 (멜론: melon, 지니: genie, 벅스: bugs)',
            'in': 'query',
            'type': 'str',
            'required': True
        },

        {
            'name': 'page_index',
            'description': '페이지 기반 조회를 위한 현재 사용자의 위치 정보 중 현재 페이지의 인덱스 (기본값 1)',
            'in': 'query',
            'type': 'int',
            'required': False
        },

        {
            'name': 'page_length',
            'description': '페이지 기반 조회를 위한 현재 사용자의 위치 정보 중 조회하고자 하는 페이지의 길이 (기본값 10)',
            'in': 'query',
            'type': 'int',
            'required': False
        }
    ],

    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                'application/json': [
                    {
                        "id": "5af264395c4fef5db9a34558",
                        "title": "주지마",
                        "artist": "로꼬",
                        "album": "건반 위의 하이에나 Part.4",
                        "rank": {
                            "melon": 1,
                            "genie": 1,
                            "bugs": 1
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a3455a",
                        "title": "지나오다",
                        "artist": "닐로(Nil_O)",
                        "album": "About You",
                        "rank": {
                            "melon": 2,
                            "genie": 3,
                            "bugs": 6
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a3455c",
                        "title": "잊을만하면",
                        "artist": "크러쉬(Crush)",
                        "album": "잊을만하면",
                        "rank": {
                            "melon": 3,
                            "genie": 4,
                            "bugs": 3
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a3455e",
                        "title": "What is Love?",
                        "artist": "TWICE (트와이스)",
                        "album": "What is Love?",
                        "rank": {
                            "melon": 4,
                            "genie": 5,
                            "bugs": 8
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a34560",
                        "title": "You",
                        "artist": "멜로망스(MeloMance)",
                        "album": "투유 프로젝트 - 슈가맨2 Part.2",
                        "rank": {
                            "melon": 5,
                            "genie": 6,
                            "bugs": 11
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a34562",
                        "title": "붕붕 (Feat. 식케이) (Prod. GroovyRoom)",
                        "artist": "김하온(HAON)",
                        "album": "고등래퍼2 Final",
                        "rank": {
                            "melon": 6,
                            "genie": None,
                            "bugs": 10
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a34564",
                        "title": "花요일 (Blooming Day)",
                        "artist": "EXO-CBX (첸백시)",
                        "album": "Blooming Days - The 2nd Mini Album",
                        "rank": {
                            "melon": 7,
                            "genie": 32,
                            "bugs": 80
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a34566",
                        "title": "별이 빛나는 밤",
                        "artist": "마마무(Mamamoo)",
                        "album": "Yellow Flower",
                        "rank": {
                            "melon": 8,
                            "genie": 10,
                            "bugs": 27
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a34568",
                        "title": "욕심",
                        "artist": "멜로망스(MeloMance)",
                        "album": "욕심",
                        "rank": {
                            "melon": 9,
                            "genie": 8,
                            "bugs": 9
                        }
                    },

                    {
                        "id": "5af264395c4fef5db9a3456a",
                        "title": "밤 (Time for the moon night)",
                        "artist": "여자친구(GFRIEND)",
                        "album": "여자친구 The 6th Mini Album 'Time for the moon night'",
                        "rank": {
                            "melon": 10,
                            "genie": 2,
                            "bugs": 2
                        }
                    }
                ]
            }
        },

        '400': {
            'description': '비정상적인 site_name 값에 의한 실패 (melon: 멜론, genie: 지니, bugs: 벅스)'
        }
    }
}
