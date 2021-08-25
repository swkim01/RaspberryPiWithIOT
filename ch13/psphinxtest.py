import sys
from pocketsphinx import *
import pyaudio
import time

hmm = 'cmusphinx-en-us-ptm-5.2/'
dic = 'dictionary.dic'
lm = 'language_model.lm'
grammar = 'grammar.jsgf'
bufsize = 512

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', hmm)
config.set_string('-lm', lm)
config.set_string('-dict', dic)
# Predetermined grammar file can be used in place of language model.
#config.set_string('-jsgf', grammar)

decoder = Decoder(config)

pyAudio = pyaudio.PyAudio()

def getCommand(debug=False):
    global pyAudio, bufsize, decoder
    # We're going to set up the stream from pyAudio that well be using to get the user's speech from the microphone.
    stream = pyAudio.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=bufsize)
    # Let the use know that we're ready for them to speak
    print('Need more input: ')
    # This is a flag that we'll use in a bit to determine whether we are going from silence to speech
    # or from speech to silence.
    utteranceStarted = False
    # This will tell PocketSphinx to start decoding the "utterance".  When we are finished with our audio
    # we will tell PocketSphinx that the utterance is over.
    decoder.start_utt()
    # We want this to loop for as long as it takes to get the full sentence from the user.  We only exit with a
    # return statement when we have our best guess of what the person said.
    while True:
        try:
        # This takes a small sound bite from the microphone to process.
            buf = stream.read(bufsize)
        except Exception as e:
            pass
        # If we've got something from the microphone, we should begin processing it.
        if buf:
            decoder.process_raw(buf, False, False)
            inSpeech = decoder.get_in_speech()
            # The following checks for the transition from silence to speech.
            # We're going to set a flag to reflect this.
            if inSpeech and not utteranceStarted:
                utteranceStarted = True
            # The following checks for the transition from speech to silence.
            # This is our cue to check what was said and do something useful with it.
            if not inSpeech and utteranceStarted:
                # We tell PocketSphinx that the user is finished saying what they wanted
                # to say, and that it should makes it's best guess as to what thay was.
                decoder.end_utt()
                # The following will get a hypothesis object with, amongst other things,
                # the string of words that PocketSphinx thinks the user said.
                hypothesis = decoder.hyp()
                if hypothesis is not None:
                    bestGuess = hypothesis.hypstr
                    print('I just heard you say:"{}"'.format(bestGuess))
                    # We are done with the microphone for now so we'll close the stream.
                    #stream.stop_stream()
                    stream.close()
                    # We have what we came for! A string representing what the user said.
                    # We'll now return it to the runMain function so that it can be
                    # processed and some meaning can be gleamed from it.
                    return bestGuess
            # The following is here for debugging to see what the decoder thinks we're saying as we go
            if debug and decoder.hyp() is not None:
                print(decoder.hyp().hypstr)

if __name__ == '__main__':
    while True:
        try:
            command = getCommand().lower()
            print(command)
            time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            sys.exit()
