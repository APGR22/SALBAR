// Copyright © 2023 APGR22

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <stdio.h>

#define EMPTY 0

int file_exists(char * file);

//just a check with a slight drop in performance
int check_threading(char * stopthread, FILE * file, FILE * file_output, char * output);

long long size_of_file(char * filename, FILE * file);