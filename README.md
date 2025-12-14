# Weightlifting Programming Generator

## High Level Overview

            training_program_template.txt
                    |
                    |
                    V
Best lifts --> [Program] --> Formatted Program w/ numbers calculated

- [ ] Create and store the template
    - The goal of the template file should be to be easily modifiable and readable
    - but it also needs to keep the same schema rules so it can be ingested into python very easily
- [ ] ingest the template
- [ ] find delimiters for exercises
- [ ] do the math 
- [ ] replace 
- [ ] output formatter or save to file 

Other ideas:
    - might be nice to have some user data stored locally
    - create a user profile file
    - construct a User object from that
    - pass User object into the generator