/* Lever-up service worker: app-schil vooraf in de cache, de rest (plaatjes, lettertype) bij eerste gebruik.
   De pagina zelf komt eerst van het netwerk (nieuwe versie meteen) en alleen offline uit de cache; plaatjes en lettertype komen uit de cache en worden op de achtergrond ververst.
   Verander VERSION om de oude cache bij het volgende bezoek leeg te gooien. */
var VERSION="lever-up-v11";
var CORE=[
  "lever-up.html",
  "manifest.webmanifest",
  "assets/icons/icon-192.png",
  "assets/icons/icon-512.png",
  "assets/icons/apple-touch-icon.png",
  "assets/lev/avatar.webp",
  "assets/lev/face-cheer.webp",
  "assets/muscles/m/back-body.png",
  "assets/muscles/m/back-calves.png",
  "assets/muscles/m/back-forearms.png",
  "assets/muscles/m/back-glutes.png",
  "assets/muscles/m/back-hamstrings.png",
  "assets/muscles/m/back-lats.png",
  "assets/muscles/m/back-lower_back.png",
  "assets/muscles/m/back-rear_delt.png",
  "assets/muscles/m/back-triceps.png",
  "assets/muscles/m/back-upper_back.png",
  "assets/muscles/m/front-abs.png",
  "assets/muscles/m/front-biceps.png",
  "assets/muscles/m/front-body.png",
  "assets/muscles/m/front-calves.png",
  "assets/muscles/m/front-chest.png",
  "assets/muscles/m/front-forearms.png",
  "assets/muscles/m/front-front_delt.png",
  "assets/muscles/m/front-hip_flexors.png",
  "assets/muscles/m/front-obliques.png",
  "assets/muscles/m/front-quads.png"
];
self.addEventListener("install",function(e){
  e.waitUntil(caches.open(VERSION).then(function(c){
    return Promise.all(CORE.map(function(u){return c.add(u).catch(function(){});}));
  }).then(function(){return self.skipWaiting();}));
});
self.addEventListener("activate",function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.filter(function(k){return k!==VERSION;}).map(function(k){return caches.delete(k);}));
  }).then(function(){return self.clients.claim();}));
});
self.addEventListener("fetch",function(e){
  var req=e.request,url=new URL(req.url);
  if(req.method!=="GET")return;
  var own=url.origin===self.location.origin,font=/fonts\.(googleapis|gstatic)\.com$/.test(url.hostname);
  if(!own&&!font)return;
  var nav=req.mode==="navigate",key=nav?"lever-up.html":req;
  if(nav){
    /* de pagina zelf: eerst het netwerk (nieuwe versie meteen), de cache alleen als je offline bent */
    e.respondWith(fetch(req).then(function(r){
      if(r&&r.ok){var copy=r.clone();caches.open(VERSION).then(function(c){c.put(key,copy);});}
      return r;
    }).catch(function(){return caches.open(VERSION).then(function(c){return c.match(key,{ignoreSearch:true});}).then(function(hit){return hit||new Response("Offline",{status:503,headers:{"Content-Type":"text/plain"}});});}));
    return;
  }
  e.respondWith(caches.open(VERSION).then(function(c){
    return c.match(key,{ignoreSearch:own}).then(function(hit){
      var net=fetch(req).then(function(r){
        if(r&&(r.ok||r.type==="opaque"))c.put(key,r.clone());
        return r;
      }).catch(function(){return null;});
      return hit||net.then(function(r){return r||new Response("Offline",{status:503,headers:{"Content-Type":"text/plain"}});});
    });
  }));
});
