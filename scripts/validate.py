# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Script to validate OSV data sources."""
import argparse
import yaml

VULNERABILITY_EXTENSION = '.yaml'

def validate(vuln):
    with open(vuln) as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    print(vuln)


def main():
    parser = argparse.ArgumentParser(description='Validate OSV files')
    parser.add_argument('files', metavar='f', type=string, nargs='+',
                        help='file to analyze')

    args = parser.parse_args()

    for changed in args:
        if changed.endswith(VULNERABILITY_EXTENSIONS) and changed.startswith("OSV"):
            validate(changed)


if __name__ == '__main__':
    main()
