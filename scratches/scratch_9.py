

**(8 of 8) Get VNC Demonstration Capture System deployable**


The goal is to get this done by 5pm so we can have our friends do it after work

* (4) Build a development system that just runs when started
    * We can run with cd vnc-core-envs && make dev
    * (3) We can immediately connect with open vnc://localhost:5899
        * [3] On startup, run an agent that connects and records a {timestamp, reward, done} dump
            * Run random_agent on startup
            * Make a new recording_agent.py
            * Open a file
            * json encode each step
            * Dump each step to file
            * Close file
    * (1) When we disconnect, the recordings are written to a folder
        * Outputs:
            * 1) `vnc_recorder.py` => observations.fbs
            * 2) `vnc_recorder.py` => actions.fbs
            * 3) `recording_agent.py` => {timestamp, reward, done} json dump
        * Find location where files go currently
        * Mount into a local directory
        * Get them to go to a folder that's visible to the demonstrator
            * Set up an /tmp/demos volume and write to it
        * Let user kill with ctrl+c
        * Let user set which game they want to play
* (2)Build a vnc_reader.py in gym-demonstration
    * [1] Get it to run without rewards
    * [1] Takes in the directory with three files
        * Reads files
        * Outputs rewards synced to observations
    * Make a generator with the same format as our existing reader
        * observations (did gdb do these? probably, lives in reader)
        * actions
        * [1]  {timestamp, reward, done} json dump
* (1) Build a production system that just runs when started
    * Get it built and running
    * Deploy to quay.io as gym-vnc-demonstration
    * Test it
* Package up recordings and give them to Dario
    * Put items in correct folders
    * Ensure that each folder can be replayed with our vnc-player
        * bin/vnc_playback.py -d ~/Dropbox/OpenAI/VNCDemonstrations/catherio-1
        * catherio-1/
        * esrogs-1/
            * No screen for the first few minutes, but that seems ok (lots of subsequent data
        * hdnsk-1/
            * Frozen screen for first 20 seconds, loses a few points there, seems ok
        * taylorific-1/
        * whatupdave-1/
    * Include gym-vnc dependency in gym-demonstration
    * tar.gz all folders and send public link to Dario
    * Get reader working at 30fps
    * Sit with Dario and make sure he can use it





Murphyproof

Record the first 150 minutes of VNCPong

* (1) Record 50 minutes of VNCPong demonstrations ourselves
    * Tom and Catherio each play for 25 minutes
    * Send to Dario and ask for feedback
    * [1] Update instructions for recording  Demonstration Capture Instructions for VNC Atari games (Mac OSX) (https://quip.com/yWvUAAFIZ96W)

* (2) Get 6 people to each do 25 minutes on each game
    * Ask our friends to use it
    * help them when they get stuck

