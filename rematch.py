import re
   
pattern = r'^(?P<region>[a-z0-9]+)-(?P<projectCode>[a-z0-9]+)-(?P<stage>dev|ci|stg|prd)(-?)(?P<devName>[a-z0-9-]+)*$'
match = re.match(pattern, 'ew1-124-stg-plrer')

if not match:
    print('Invalid namespace, must match {}'.format(pattern))

region = match.group('region')
projectCode = match.group('projectCode')
stage = match.group(3)
dev = match.group('devName')
print(region, project, stage, dev)

