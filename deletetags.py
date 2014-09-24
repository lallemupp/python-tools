# coding=utf-8
""""
Copyright 2014 Love Löfdahl

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
__author__  = "Love Löfdahl"
import git
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Deletes all tags locally and remote that contains the provided search pattern')
        print('usage: python deletetags.py <root folder of git> <search pattern>')
        sys.exit(1)
    folder = str(sys.argv[1])
    search_pattern = sys.argv[2]
    repo = git.Repo(folder)
    if repo.bare:
        print('Repo is bare. Will now exit.')
        sys.exit(1)
    origin = repo.remotes.origin
    tags = repo.tags
    for tag in tags:
        if search_pattern in tag.name:
            print('deleting tag with name: ' + tag.name)
            repo.delete_tag(tag)
            origin.push(':' + tag.name)
            print(tag.name + ' was deleted')
    print('All tags containing: ' + search_pattern + ' has been deleted both locally and remote')
