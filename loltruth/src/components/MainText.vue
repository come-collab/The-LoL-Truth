
<template>
    <div>
    <h1> League of legend truth based on data</h1>
    <p>This website have for goal to explain to people why League of Legend is top notch in terms of competition
    And why the dream of becoming a pro player/high rank player is extremely difficult to reach
    The whole website fetching of data, process of treating those data's and code is available on <a href = "https://github.com/come-collab">GitHub </a> 
    </p>
    <button @click="openit"><strong>Tech Sidenote :</strong></button>
    <p id="demo" style="display : none"> 
    This site comes with a scrapper. The data is taken from multiples sources League of Legend API,
    and op.gg website. The study, the ideas, the data visualisation is done by me and is available on github , most of the intelligence of
    the app is on datascrapper.py file. If you want to learn more about that feel free to check it out but even if you are not into Tech
    this website is for you 
    </p>
    <p> <strong>Idea explanation :</strong>The whole point is to help people to have more realistic goals on LoL and help them enjoy the game more without being devoured by the 
      unrealistic need to be a high elo player. This website is going to show what the majority of high elo player share in commun and why they
      are at the place they are at and that a big part of that is inner skill.
      The idea came from a video of the very famous LoL Coach LS who said that every pro player he ever encountered reach high elo in less than two years of playing the game
      thats why i lead this study, to help people understand that on such a hard game reaching top level is not for everybody.
      in this first graph you will see that one of those thing is the first rank they ever reach. Of course all the accounts selected are mains and not smurf.
      Enjoy !
    </p>
    </div>
</template>


<script>
import {Myfunction} from '../smallscript'

export default {
  name : 'MainText',  
  methods : {
    openit : function(){
        Myfunction.openit();
    }    
  }
};
</script>

