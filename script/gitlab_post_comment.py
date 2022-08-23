#!/usr/bin/env python3
import os
import sys
from urllib import parse, request

iid = os.environ['PR_GITLAB_IID']

if 'GITLAB_TOKEN' in os.environ:
    token = os.environ['GITLAB_TOKEN'];
else:
    token=("".join(open("%s/private/gitlab-token" % os.environ['HOME']))).strip()

if len(sys.argv) > 1:
    if sys.argv[1] == "-":
        review_body = "".join(sys.stdin)
    elif os.path.isfile(sys.argv[1]):
        review_body = "".join(open(sys.argv[1]))
    else:
        review_body = sys.argv[1]

    blob = parse.urlencode({'body': review_body.replace("\n", "\r\n").replace('"', '\"').encode('utf-8')})
    blob = blob.encode('utf-8')
    request = request.Request(f"https://gitlab.cern.ch/api/v4/projects/cms-nanoAOD%2Fjsonpog-integration/merge_requests/{iid}/notes", blob, headers={'PRIVATE-TOKEN': token})
    request.get_method = lambda: 'POST'
    response = request.urlopen(request)
    data = response.read().decode('utf-8')
    print(data)

