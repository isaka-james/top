
from flask import Flask, make_response, request, jsonify

import requests as req

app = Flask(__name__)

# Let lose some memory for a project's sake
__author__ = "isaka-james & help from vicent-laizer"
__project_name__ = "toppers-nation"
__version_project__ = 0.1



def get_individual(position):
  delay=0
  percent=0

  if position<=10:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 
<defs id="defs4">
  <clipPath id="clip">
   <path id="path10" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
 </defs>
 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g id="g11992">
    <g id="g10152"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 209.707, 119.99)" id="g6367"/>
   <g id="g11992-9">
    <g id="g10152-1"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 168.486, 122.211)" id="g6367-8"/>
   <g id="g11992-97">
    <g id="g10152-14"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 151.438, 131.492)" id="g6367-2"/>
   <g transform="matrix(0.411473, 0, 0, 0.269218, 35.4901, 75.4365)" id="g4891">
    <path stroke-miterlimit="4" stroke-width="1.06667" fill-rule="evenodd" fill="#cecdb6"   id="path14311" d="m73.58067,7.56509l-5.71963,-177.41129l-33.78037,-25.08874l-33.93347,25.08874l-5.56653,177.41127l79,0.00002z"/>
    <g id="g62591">
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#bc8810"  d="m46.53384,-167.58389a12.54946,12.54946 0 0 1 -12.54946,12.54947a12.54946,12.54946 0 0 1 -12.54946,-12.54947a12.54946,12.54946 0 0 1 12.54946,-12.54946a12.54946,12.54946 0 0 1 12.54946,12.54946z" id="circle62593"/>
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#fddd10"  d="m44.65142,-167.58389a10.66704,10.66704 0 0 1 -10.66704,10.66705a10.66704,10.66704 0 0 1 -10.66704,-10.66705a10.66704,10.66704 0 0 1 10.66704,-10.66704a10.66704,10.66704 0 0 1 10.66704,10.66704z" id="circle62595"/>
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-width="0.7" fill-rule="nonzero" fill="#dbb110" clip-rule="nonzero"  id="path62597" d="m33.98549,-179.60522c-3.15262,-0.00039 -6.27327,1.28938 -8.50285,3.51849c-2.22958,2.22913 -3.52045,5.35019 -3.5207,8.50284c0.00025,3.15267 1.29112,6.27372 3.5207,8.50284c2.22958,2.22911 5.35023,3.51889 8.50285,3.5185c3.15231,-0.00025 6.27166,-1.29174 8.50062,-3.52071c2.22896,-2.22896 3.52046,-5.3483 3.52071,-8.50063c-0.00025,-3.15231 -1.29175,-6.27165 -3.52071,-8.50062c-2.22896,-2.22896 -5.34831,-3.52046 -8.50062,-3.52071zm0,0.79272c2.93447,0.00022 5.86314,1.21537 7.9382,3.29041c2.07505,2.07506 3.29018,5.00373 3.29042,7.9382c-0.00023,2.93449 -1.21537,5.86316 -3.29042,7.93821c-2.07506,2.07505 -5.00372,3.29019 -7.9382,3.29041c-2.93499,0.00038 -5.86496,-1.21318 -7.94042,-3.2882c-2.07544,-2.07501 -3.29019,-5.00548 -3.29042,-7.94042c0.00024,-2.93492 1.21498,-5.8654 3.29042,-7.94041c2.07546,-2.07502 5.00543,-3.28858 7.94042,-3.2882z"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.50255" stroke="#b3b3b3" fill="none"  d="m34.08067,-194.93494l-33.93347,25.08874l-5.56653,177.41127l79,0.00002l-5.71962,-177.41129l-33.78038,-25.08874z" id="path5037" />
   </g>
   <g id="g11992-3">
    <g id="g10152-6"/>
   </g>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950" d="m38.46967,35.91946l0,0c-1.44073,0 -2.5336,0.71107 -2.60059,1.59218l-2.69347,35.42602c-0.06699,0.88111 1.15986,1.59218 2.60059,1.59218l13.73721,0l13.73721,0c1.44073,0 2.66758,-0.71107 2.60059,-1.59218l-2.69347,-35.42602c-0.06699,-0.88111 -1.15986,-1.59218 -2.60059,-1.59218l0,0l-11.04374,0l-11.04375,0z"/>
   <g transform="matrix(0.0324556, 0, 0, 0.0209405, 156.376, 128.527)" id="g4807">
    <g id="g4635"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3414.34442,-4284.77409l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3414.35082,-4222.8751l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5" />
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 52.5098, 118.763)" id="g6367-0"/>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950-7" d="m38.51651,35.88499l0,0c-1.44073,0 -2.5336,0.71107 -2.60059,1.59218l-2.69347,35.42602c-0.06699,0.88111 1.15986,1.59218 2.60059,1.59218l13.73721,0l13.73721,0c1.44073,0 2.66758,-0.71107 2.60059,-1.59218l-2.69347,-35.42602c-0.06699,-0.88111 -1.15986,-1.59218 -2.60059,-1.59218l0,0l-11.04374,0l-11.04375,0z"/>
   <g transform="matrix(0.0324556, 0, 0, 0.0209405, 156.423, 128.492)" id="g4807-3">
    <g id="g4635-0"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3414.34442,-4284.77409l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3414.35082,-4222.8751l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5-2" />
   </g>
   <g id="g11992-9-0">
    <g id="g10152-1-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 11.2892, 120.984)" id="g6367-8-3"/>
   <g id="g11992-97-7">
    <g id="g10152-14-9"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, -5.75887, 130.265)" id="g6367-2-9"/>
   <path stroke-miterlimit="4" stroke="#030315" fill="#040420"   id="path5943" d="m32.84217,74.46229l33.34085,0l-1.98906,-38.50617l-29.42572,0l-1.92606,38.50617z"/>
   <g id="g11992-4">
    <g id="g10152-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 86.3851, 125.102)" id="g6367-9"/>
   <g id="g11992-9-5">
    <g id="g10152-1-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 45.1645, 127.323)" id="g6367-8-5"/>
   <g id="g11992-97-0">
    <g id="g10152-14-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0539345, 0, 0, 0.0218037, 28.1164, 136.604)" id="g6367-2-5"/>
   <g transform="matrix(0.0324556, 0, 0, 0.0209405, 232.306, 131.78)" id="g4635-0-6"/>
   <g stroke="#040420" transform="matrix(0.0324556, 0, 0, 0.0209405, 91.6244, 128.061)" id="g4807-5">
    <g stroke="#040420" id="g4635-07"/>
   </g>
   <g id="g5169-7">
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m49.59547,40.1468l-3.9811,1.70568l0,0.9795l3.9811,-1.70568l3.9811,1.70568l0.00001,-0.9795l-3.98111,-1.70568z" id="path5142-5"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m49.59547,38.18779l-3.9811,1.70568l0,0.9795l3.9811,-1.70568l3.9811,1.70568l0.00001,-0.9795l-3.98111,-1.70568z" id="path5142-9-3"  />
   </g>
   <g id="g4804">
    <ellipse stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="0.63745" stroke="#d4aa00" fill="#ffcc00" cx="49.55785" cy="46.27144" rx="1.1953" ry="0.10052" id="path4583"/>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819" d="m43.69238,46.69646l0.06348,0.63652l6.37178,2.39662l0.28141,-0.78451l-6.71667,-2.24864z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815" d="m54.09714,49.62577c0,0 0.12997,0.41558 0.38437,0.50155c0.32333,0.10926 1.07988,-0.10747 1.07988,-0.10747l2.81868,0.96727c0,0 -0.21304,0.82525 -0.5857,1.14639c-0.36056,0.31072 -1.48256,0.65679 -1.48256,0.65679l-1.68389,-1.75542c0,0 -1.09068,0.05749 -1.55577,-0.09553c-0.35106,-0.1155 -0.78704,-0.5732 -0.78704,-0.5732l-1.11291,-0.81143l-8.2583,-2.93823l-0.54687,-0.19571l0.26899,-0.41114l0.55243,0.17695l10.90867,3.43918z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.183134, -0.063063, -0.0966579, 0.119483, 72.6539, 110.618)" y="-357.2411" x="344.53074" height="7" width="3" id="rect4817"/>
    </g>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845-6" transform="matrix(-0.207076, 0, 0, 0.135104, 73.0886, 116.619)">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819-7" d="m85.84267,-519.8151l0.30656,4.71135l30.77021,17.73909l1.35896,-5.80668l-32.43573,-16.64376z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815-6" d="m136.08865,-498.1332c0,0 0.62766,3.07603 1.85616,3.71231c1.56141,0.8087 5.21491,-0.79549 5.21491,-0.79549l13.6118,7.15945c0,0 -1.0288,6.10825 -2.82842,8.48528c-1.74121,2.29987 -7.15946,4.86136 -7.15946,4.86136l-8.13173,-12.99309c0,0 -5.26702,0.4255 -7.51301,-0.7071c-1.69533,-0.85492 -3.8007,-4.24264 -3.8007,-4.24264l-5.37437,-6.006l-39.88046,-21.74793l-2.64092,-1.44862l1.29901,-3.04311l2.66774,1.30974l52.67945,25.45584z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.884377, -0.466774, -0.466774, 0.884377, 0, 0)" y="-503.88413" x="166.71887" height="7" width="3" id="rect4817-0"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m52.13071,48.89401l-2.62821,2.5008l-2.62821,-2.5008c0,0 -0.33182,-1.89155 2.60311,-1.99122c2.93493,-0.09967 2.65332,1.99122 2.65332,1.99122z" id="path4953-5-7"  />
    <circle stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="path4775-5" cx="49.5025" cy="52.83367" r="1.10622"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m46.9841,47.52072c0,0 -0.44044,-1.99626 2.51839,-1.97238c2.95883,0.02388 2.51839,1.97238 2.51839,1.97238l-2.51839,3.57011l-2.51839,-3.57011z" id="path4951-0"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m51.19382,46.11161c0,0 0.32792,-2.26891 -1.7388,-2.23308c-2.06671,0.03583 -1.7388,2.23308 -1.7388,2.23308l1.78627,5.03326l1.69133,-5.03326z" id="path4796-2-1"  />
    <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="rect4777-6" width="3.5203" height="0.60797" x="47.74235" y="50.78684" ry="2.25"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m50.29697,47.10276c0.08609,-1.00191 -0.12812,-3.00929 -0.12812,-3.00929c0,0 -0.05146,-1.07475 -0.64061,-1.07475c-0.58916,0 -0.64061,1.07475 -0.64061,1.07475c0,0 -0.20734,2.00714 -0.12812,3.00929c0.09778,1.23697 0.74299,3.68408 0.74299,3.68408c0,0 0.68808,-2.4459 0.79448,-3.68408z" id="path4779-1-3"  />
   </g>
   <g id="g4770">
    <path stroke-miterlimit="4" stroke-width="8" stroke="#ffcc00" fill-rule="evenodd" fill="none"  d="m32.8921,71.7701c16.56612,0 29.45053,-16.20182 16.62126,-16.20182c-12.82927,0 0.05361,16.20182 16.61972,16.20182" id="path3730-3" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#1a1a1a" fill-rule="evenodd" fill="none"  d="m32.8921,71.7701c16.56612,0 29.45053,-16.20182 16.62126,-16.20182c-12.82927,0 0.05361,16.20182 16.61972,16.20182" id="path3730-3-9" />
    <path stroke-width="1px" fill="#ffcc00" d="m49.51646,66.94786l-1.09362,-0.82751l0.57357,-0.32754c0,0 0.32722,0.23852 0.48302,0.36209c0.19174,0.15207 0.55554,0.46647 0.55554,0.46647l-0.51852,0.32649z" id="path4749"  />
    <path stroke-width="1px" fill="#ffcc00" d="m50.60105,66.12224l-1.08783,-0.8388l-0.41522,0.41417c0,0 0.28415,0.27811 0.44981,0.40507c0.17643,0.13521 0.57628,0.37738 0.57628,0.37738l0.47696,-0.35782z" id="path4749-1"  />
   </g>
  </g>
 </g>
</svg>
    '''
    percent=80
    delay=7

  elif position<=30:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 
<defs id="defs4">
  <clipPath id="clip">
   <path id="path10" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5311-8" xlink:href="#linearGradient4116" />
  <linearGradient id="linearGradient4116">
   <stop stop-color="#777777" offset="0" id="stop4118"/>
   <stop stop-color="#ffffff" offset="0.5" id="stop4124"/>
   <stop stop-color="#777777" offset="1" id="stop4120"/>
  </linearGradient>
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5313-6" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5315-1" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5317-1" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5319-0" xlink:href="#linearGradient4116" />
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5311-8-4" xlink:href="#linearGradient4116" />
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5313-6-4" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5315-1-3" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5317-1-3" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5319-0-8" xlink:href="#linearGradient4116" />
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5311-8-7" xlink:href="#linearGradient4116" />
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5313-6-45" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5315-1-9" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5317-1-0" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5319-0-82" xlink:href="#linearGradient4116" />
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5311-8-1" xlink:href="#linearGradient4116" />
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5313-6-8" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5315-1-4" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5317-1-30" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5319-0-88" xlink:href="#linearGradient4116" />
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5311-8-9" xlink:href="#linearGradient4116" />
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5313-6-2" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5315-1-45" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5317-1-03" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5319-0-3" xlink:href="#linearGradient4116" />
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5311-8-4-2" xlink:href="#linearGradient4116" />
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5313-6-4-0" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5315-1-3-7" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5317-1-3-8" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5319-0-8-3" xlink:href="#linearGradient4116" />
  <linearGradient y2="-0.02234" x2="0.57703" y1="0.53611" x1="0.94021" id="linearGradient5759" xlink:href="#linearGradient4116" />
  <linearGradient y2="1.18003" x2="0.5007" y1="0.14993" x1="-0.201" id="linearGradient5761" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.67165" x2="1.69357" y1="-0.1229" x1="0.10991" id="linearGradient5763" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82908" x2="0.31361" y1="-0.27509" x1="0.15755" id="linearGradient5765" xlink:href="#linearGradient4116" />
  <linearGradient y2="0.82395" x2="0.54989" y1="-0.07303" x1="0.09205" id="linearGradient5767" xlink:href="#linearGradient4116" />
 </defs>
 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g id="g4707-4">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="0.81617" stroke="#000000" fill="#e6e6e6"  id="path2244-8" d="m60.38467,60.28878l-2.20005,0.88912l0.76574,1.42322l-2.13462,-0.88106l-2.19023,0.88177l0.88078,-1.43364l-2.11938,-0.87825l2.67897,-0.00498l0.88038,-1.42456l0.77491,1.43057l2.66349,-0.00217l0,0z"/>
    <path stroke-width="0.27206px" stroke="#000000" fill="#e6e6e6"  d="m57.6898,60.30844l-0.82327,0.62633l-0.77883,-0.6208" id="path2246-2" />
    <path stroke-width="0.27206px" stroke="#000000" fill="#e6e6e6"  d="m55.56447,61.15016l1.30206,-0.2154l-0.03167,0.75473" id="path2248-7" />
    <path stroke-width="0.27206px" stroke="#000000" fill="#e6e6e6"  d="m56.86653,60.93476l1.27337,0.23288" id="path2250-0" />
   </g>
   <g id="g11992">
    <g id="g10152"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0512289, 0, 0, 0.018471, 203.91, 122.848)" id="g6367"/>
   <g id="g11992-9">
    <g id="g10152-1"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0512289, 0, 0, 0.018471, 164.757, 124.729)" id="g6367-8"/>
   <g id="g11992-97">
    <g id="g10152-14"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0512289, 0, 0, 0.018471, 148.564, 132.591)" id="g6367-2"/>
   <g transform="matrix(0.390832, 0, 0, 0.228067, 38.4325, 85.1044)" id="g4891">
    <path stroke-miterlimit="4" stroke-width="1.06667" fill-rule="evenodd" fill="#cecdb6"   id="path14311" d="m68.28594,-48.07516l-5.71963,-177.41129l-33.78037,-25.08874l-33.93347,25.08874l-5.56653,177.41127l79,0.00002z"/>
    <g id="g62591">
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#bc8810"  d="m41.23911,-223.22414a12.54946,12.54946 0 0 1 -12.54946,12.54947a12.54946,12.54946 0 0 1 -12.54946,-12.54947a12.54946,12.54946 0 0 1 12.54946,-12.54946a12.54946,12.54946 0 0 1 12.54946,12.54946z" id="circle62593"/>
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#fddd10"  d="m39.35669,-223.22414a10.66704,10.66704 0 0 1 -10.66704,10.66705a10.66704,10.66704 0 0 1 -10.66704,-10.66705a10.66704,10.66704 0 0 1 10.66704,-10.66704a10.66704,10.66704 0 0 1 10.66704,10.66704z" id="circle62595"/>
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-width="0.7" fill-rule="nonzero" fill="#dbb110" clip-rule="nonzero"  id="path62597" d="m28.69076,-235.24547c-3.15262,-0.00039 -6.27327,1.28938 -8.50285,3.51849c-2.22958,2.22913 -3.52045,5.35019 -3.5207,8.50284c0.00025,3.15267 1.29112,6.27372 3.5207,8.50284c2.22958,2.22911 5.35023,3.51889 8.50285,3.5185c3.15231,-0.00025 6.27166,-1.29174 8.50062,-3.52071c2.22896,-2.22896 3.52046,-5.3483 3.52071,-8.50063c-0.00025,-3.15231 -1.29175,-6.27165 -3.52071,-8.50062c-2.22896,-2.22896 -5.34831,-3.52046 -8.50062,-3.52071zm0,0.79272c2.93447,0.00022 5.86314,1.21537 7.9382,3.29041c2.07505,2.07506 3.29018,5.00373 3.29042,7.9382c-0.00023,2.93449 -1.21537,5.86316 -3.29042,7.93821c-2.07506,2.07505 -5.00372,3.29019 -7.9382,3.29041c-2.93499,0.00038 -5.86496,-1.21318 -7.94042,-3.2882c-2.07544,-2.07501 -3.29019,-5.00548 -3.29042,-7.94042c0.00024,-2.93492 1.21498,-5.8654 3.29042,-7.94041c2.07546,-2.07502 5.00543,-3.28858 7.94042,-3.2882z"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.50255" stroke="#b3b3b3" fill="none"  d="m28.78594,-250.57519l-33.93347,25.08874l-5.56653,177.41127l79,0.00002l-5.71962,-177.41129l-33.78038,-25.08874z" id="path5037" />
   </g>
   <path stroke-width="1px" stroke="#000000" fill="#1a1a1a"   id="path5943" d="m33.84955,71.58934l31.66686,0l-0.91163,-16.02339l-29.87227,0l-0.88295,16.02339z"/>
   <g id="g5482">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7"           d="m49.68298,67.43878l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5311-8)"  d="m-3503.15005,-4461.1413l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5313-6)"  d="m-3503.14997,-4514.9483l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5315-1)"  d="m-3503.14997,-4514.9483l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5317-1)"  d="m-3471.52306,-4558.47907l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5319-0)"  d="m-3451.24487,-4498.08329l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m49.68298,70.32299l0,-0.82406l-1.34685,0.25465" id="path4954-6" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m48.85058,68.83225l0.8324,0.66668l0.8324,-0.66668" id="path4956-0" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m49.68298,69.49893l1.34684,0.25465" id="path4958-1" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3"           d="m49.68298,67.43878l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
   <g id="g5482-7">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7-1"           d="m49.68298,61.72754l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464-5" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5311-8-4)"  d="m-3503.15005,-4834.05704l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3-1" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5313-6-4)"  d="m-3503.14997,-4887.86404l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6-2" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5315-1-3)"  d="m-3503.14997,-4887.86404l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3-9" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5317-1-3)"  d="m-3471.52306,-4931.39481l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8-1" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5319-0-8)"  d="m-3451.24487,-4870.99903l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7-2" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m49.68298,64.61175l0,-0.82406l-1.34685,0.25465" id="path4954-6-3" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m48.85058,63.12101l0.8324,0.66668l0.8324,-0.66668" id="path4956-0-1" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m49.68298,63.78769l1.34684,0.25465" id="path4958-1-5" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3-2"           d="m49.68298,61.72754l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
   <g id="g5482-1">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7-7"           d="m56.76377,64.58886l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464-4" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5311-8-7)"  d="m-3234.1149,-4647.22703l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3-7" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5313-6-45)"  d="m-3234.11482,-4701.03403l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6-6" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5315-1-9)"  d="m-3234.11482,-4701.03403l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3-1" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5317-1-0)"  d="m-3202.48791,-4744.5648l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8-8" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5319-0-82)"  d="m-3182.20972,-4684.16902l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7-7" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m56.76376,67.47307l0,-0.82406l-1.34685,0.25465" id="path4954-6-6" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m55.93137,65.98233l0.8324,0.66668l0.8324,-0.66668" id="path4956-0-6" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m56.76377,66.64901l1.34684,0.25465" id="path4958-1-8" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3-4"           d="m56.76377,64.58886l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
   <g id="g5482-0">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7-6"           d="m42.60219,64.58886l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464-1" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5311-8-1)"  d="m-3772.18509,-4647.22703l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3-76" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5313-6-8)"  d="m-3772.18501,-4701.03403l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6-5" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5315-1-4)"  d="m-3772.18501,-4701.03403l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3-11" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5317-1-30)"  d="m-3740.5581,-4744.5648l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8-16" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5319-0-88)"  d="m-3720.27991,-4684.16902l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7-4" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m42.60219,67.47307l0,-0.82406l-1.34685,0.25465" id="path4954-6-7" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m41.76979,65.98233l0.8324,0.66668l0.8324,-0.66668" id="path4956-0-4" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m42.60219,66.64901l1.34684,0.25465" id="path4958-1-0" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3-41"           d="m42.60219,64.58886l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
   <g id="g5482-5">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7-0"           d="m49.68298,56.01629l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464-9" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5311-8-9)"  d="m-3503.15005,-5206.97277l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3-4" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5313-6-2)"  d="m-3503.14997,-5260.77977l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6-65" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5315-1-45)"  d="m-3503.14997,-5260.77977l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3-4" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5317-1-03)"  d="m-3471.52306,-5304.31054l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8-3" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5319-0-3)"  d="m-3451.24487,-5243.91476l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7-5" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m49.68298,58.9005l0,-0.82406l-1.34685,0.25465" id="path4954-6-1" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m48.85058,57.40976l0.8324,0.66668l0.8324,-0.66668" id="path4956-0-5" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m49.68298,58.07644l1.34684,0.25465" id="path4958-1-2" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3-9"           d="m49.68298,56.01629l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
   <g id="g5482-1-6">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7-7-6"           d="m56.76376,58.87761l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464-4-7" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5759)"  d="m-3234.11514,-5020.14287l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3-7-7" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5761)"  d="m-3234.11506,-5073.94987l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6-6-4" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5763)"  d="m-3234.11506,-5073.94987l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3-1-0" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5765)"  d="m-3202.48815,-5117.48064l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8-8-6" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5767)"  d="m-3182.20996,-5057.08486l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7-7-3" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m56.76376,61.76182l0,-0.82406l-1.34685,0.25465" id="path4954-6-6-1" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m55.93136,60.27108l0.8324,0.66668l0.8324,-0.66668" id="path4956-0-6-0" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m56.76376,60.93776l1.34684,0.25465" id="path4958-1-8-2" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3-4-5"           d="m56.76376,58.87761l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
   <g id="g5482-0-8">
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="2" fill-rule="nonzero" fill="#f2f2f2"  id="path4952-7-6-1"           d="m42.60219,58.87761l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
    <g id="g5464-1-3" transform="matrix(0.0263192, 0, 0, 0.0153151, 141.883, 138.646)">
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5311-8-4-2)"  d="m-3772.18533,-5020.14287l-79.06742,55.01997l79.0675,-108.82697l-0.00008,53.807z" id="path2180-8-0-67-3-76-6" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5313-6-4-0)"  d="m-3772.18525,-5073.94987l-51.17362,16.62726l-76.76023,-58.19546l127.93385,41.5682z" id="path2182-0-9-0-6-5-7" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5315-1-3-7)"  d="m-3772.18525,-5073.94987l-32.0793,-44.15323l32.07924,-90.36427l0.00006,134.5175z" id="path2184-3-0-54-3-11-0" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5317-1-3-8)"  d="m-3740.55834,-5117.48064l96.30682,1.96259l-127.93373,41.56818l31.62691,-43.53077z" id="path2186-6-6-9-8-16-3" />
     <path stroke-width="0.43163" fill-rule="evenodd" fill="url(#linearGradient5319-0-8-3)"  d="m-3720.28015,-5057.08486l27.16226,91.96195l-79.06736,-108.82696l51.9051,16.86501z" id="path2188-5-4-4-7-4-8" />
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m42.60218,61.76182l0,-0.82406l-1.34685,0.25465" id="path4954-6-7-1" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none" d="m41.76979,60.27108l0.8324,0.66668l0.8324,-0.66668" id="path4956-0-4-1" />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#4d4d4d" fill="none"  d="m42.60219,60.93776l1.34684,0.25465" id="path4958-1-0-1" />
    <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.8" stroke="#4d4d4d" fill-rule="nonzero" fill="none"  id="path4952-9-3-41-7"           d="m42.60219,58.87761l0.8324,1.39347l2.53472,0.03006l-2.02027,0.89127l0.73415,1.41205l-2.08099,-0.84264l-2.08099,0.84264l0.73414,-1.41205l-2.02027,-0.89127l2.53472,-0.03006l0.8324,-1.39347z"/>
   </g>
  </g>
 </g>
</svg>
    '''
    percent=66.6665
    delay=6

  elif position<=50:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 

 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g transform="matrix(0, 0.0554881, -0.105969, 0, 150.632, 136.191)" id="g3155">
    <g id="g7414">
     <rect stroke-width="0.94547" stroke="#000000" fill="#546738" y="950.33607" x="-1513.89015" height="177.27805" width="183.54514" id="rect7416"/>
    </g>
    <path fill-rule="evenodd" fill="#141e50"  d="m-1876.59732,1100.14361l-84.15434,-56.05245l84.85353,-58.0835c100.21618,0.0658 160.80742,-8.74365 304.85157,-17.50967l0.3562,150.36022c-144.19414,-8.31987 -195.96913,-18.24519 -305.90695,-18.7146l-0.00001,0z" id="path3751" />
    <path fill-rule="evenodd" fill="#141e3c"  d="m-1866.08164,980.95092c0.11023,5.22516 0.27171,31.93409 -0.0879,126.10599l285.24488,15.9888l-0.3437,-159.1875l-284.81329,17.09271l0.00001,0z" id="path3753" />
    <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#969696"  id="path3755"     d="m-1915.91858,1027.87878c8.25331,0 14.94394,7.07196 14.94394,15.79566c0,8.7237 -6.69063,15.79565 -14.94394,15.79565c-8.25332,0 -14.94394,-7.07195 -14.94394,-15.79565c0,-8.7237 6.69063,-15.79566 14.94394,-15.79566z"/>
    <path fill-rule="evenodd" fill="#151f3c"  d="m-1835.97699,979.609c0.02064,-0.00068 0.04186,0.00069 0.0625,0c-0.03277,-1.55354 -0.0625,-1.9375 -0.0625,-1.9375l0,1.9375z" id="path3749"/>
    <path stroke-miterlimit="4" stroke-width="5.68412" stroke="#e9f000" fill="none"   id="path1920" d="m-1846.03585,1052.68419l-9.77525,-10.43937l11.29048,-11.25721"/>
    <path stroke-miterlimit="4" stroke-width="5.68412" stroke="#e9f000" fill="none"   id="path4579" d="m-1832.07651,1054.29964l-10.28033,-11.9546l11.79556,-11.76229"/>
    <g id="g10083">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#c8c8c8" d="m-1822.19938,1041.98665c3.72352,0 6.74203,10.87356 6.74203,24.28677c0,13.41321 -3.01851,24.28677 -6.74203,24.28677c-3.72352,0 -6.74202,-10.87356 -6.74202,-24.28677c0,-13.41321 3.01851,-24.28677 6.74202,-24.28677z"     id="path11806" />
     <path stroke-miterlimit="4" stroke-width="0.11844" stroke="#000000" fill-rule="evenodd" fill="#c8c8c8"   id="path11817" d="m-1763.22964,1024.19918c-17.38565,-11.5194 -37.19076,-15.81504 -39.34368,-15.41534l-0.48812,0.0906l0.60859,-2.07323l0.24849,0.42544c0.25059,0.42905 60.39963,13.86436 55.32508,30.07451c-5.03855,16.09519 0.99203,-1.61126 -16.35036,-13.102l0,0.00002z"/>
     <path stroke-miterlimit="4" stroke-width="0.11844" stroke="#000000" fill-rule="evenodd" fill="#c8c8c8"   id="path11808" d="m-1820.02544,1089.19194c21.8411,-22.15879 59.79175,-20.46556 68.58273,-32.83845c8.6757,-12.21064 8.63961,-20.43376 -9.29936,-31.12811c-18.12562,-10.80563 -54.38631,-6.10908 -54.40121,13.34062c-0.0149,19.10763 29.89879,16.33331 50.22788,18.27085c6.60458,-2.91434 2.97939,-0.96343 8.54209,-6.17228c-37.78053,-1.90533 -61.97779,-3.07729 -50.40055,-15.86131c11.65736,-12.87249 20.71567,-13.8599 40.61859,-7.68847c19.93548,6.18152 14.18963,15.84896 8.919,23.86882c-5.32843,8.10783 -30.31793,18.27186 -63.08974,-8.02943"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#929292" d="m-1822.35019,1046.44476c3.07734,0 5.57201,8.80104 5.57201,19.65768c0,10.85664 -2.49467,19.65768 -5.57201,19.65768c-3.07734,0 -5.57201,-8.80104 -5.57201,-19.65768c0,-10.85664 2.49467,-19.65768 5.57201,-19.65768z"     id="path11804" />
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="3.26734" stroke="#969696" fill="#c8c8c8"   d="m-1746.78181,1042.36331c0,0.16571 -1.18893,0.3002 -2.65385,0.3002c-1.46493,0 -2.65385,-0.13449 -2.65385,-0.3002c0,-0.16572 1.18892,-0.30021 2.65385,-0.30021c1.46492,0 2.65385,0.13449 2.65385,0.30021zm0,-2.34868c0,0.16572 -1.18893,0.30021 -2.65385,0.30021c-1.46493,0 -2.65385,-0.13449 -2.65385,-0.30021c0,-0.16571 1.18892,-0.3002 2.65385,-0.3002c1.46492,0 2.65385,0.13449 2.65385,0.3002zm0,-2.36868c0,0.16572 -1.18893,0.30021 -2.65385,0.30021c-1.46493,0 -2.65385,-0.13449 -2.65385,-0.30021c0,-0.16571 1.18892,-0.3002 2.65385,-0.3002c1.46492,0 2.65385,0.13449 2.65385,0.3002zm0,-2.36868c0,0.16572 -1.18893,0.30021 -2.65385,0.30021c-1.46493,0 -2.65385,-0.13449 -2.65385,-0.30021c0,-0.16571 1.18892,-0.3002 2.65385,-0.3002c1.46492,0 2.65385,0.13449 2.65385,0.3002z" id="path10911"/>
     <path fill-rule="evenodd" fill="#969696"   id="path10932" d="m-1783.80885,1019.5257l-0.17858,-5.44643l-0.80357,-1.51786l1.16072,-0.80357l0.80357,1.42858l-0.44643,0.98214l0.08928,5.26786l-0.62499,0.0893l0,-0.00002z"/>
     <path fill-rule="evenodd" fill="#969696"   id="path11819" d="m-1782.3724,1060.13284l0.09247,-4.40677l0.70861,0.11275l-0.17273,4.25753l-0.62834,0.0365l-0.00001,-0.00001z"/>
    </g>
    <rect stroke-width="0.94547" stroke="#000000" fill="#546738" id="rect1923" width="183.54514" height="177.27805" x="-1308.59196" y="845.11778"/>
    <g id="g1935">
     <path fill-rule="evenodd" fill="#ffffff"  d="m-1340.28271,1034.57434l0.25254,21.05348l-160.46701,-0.50508l-0.32252,-20.29586l160.53699,-0.25254z" id="path2241" />
     <path fill-rule="evenodd" fill="#ffffff"  d="m-1339.93041,1010.30135l0,20.04333l-161.22463,-0.50508l0.4351,-19.79079l160.78953,0.25254z" id="path2249" />
    </g>
    <g id="g3262">
     <path fill-rule="evenodd" fill="#344023"  d="m-1132.78074,933.18372l0.25254,21.05349l-160.46701,-0.5051l-0.32252,-20.29585l160.53699,-0.25254z" id="path3242" />
     <path fill-rule="evenodd" fill="#344123"  d="m-1132.42844,908.91073l0,20.04333l-161.22463,-0.50508l0.4351,-19.79079l160.78953,0.25254z" id="path3250" />
    </g>
    <g id="g4747">
     <rect stroke-width="0.94547" stroke="#000000" fill="#546738" y="757.75379" x="-1514.06355" height="177.27805" width="183.54514" id="rect4749"/>
    </g>
    <g id="g2215">
     <path fill-rule="evenodd" fill="#c8bd00"  d="m-1340.54423,840.78512l0.25254,21.05348l-160.46701,-0.50508l-0.32252,-20.29586l160.53699,-0.25254z" id="path3741" />
     <path fill-rule="evenodd" fill="#c8bc00"  d="m-1340.19193,816.51213l0,20.04333l-161.22463,-0.50508l0.4351,-19.79079l160.78953,0.25254z" id="path3771" />
    </g>
    <g id="g10159">
     <path fill-rule="evenodd" fill="#151f3c"  d="m-1831.38356,787.10218c0.02064,-0.00068 0.04186,0.00068 0.0625,0c-0.03276,-1.55354 -0.0625,-1.9375 -0.0625,-1.9375l0,1.9375z" id="path1905"/>
     <path fill-rule="evenodd" fill="#526738"  d="m-1870.99373,904.60633l-84.15434,-56.05245l90.56782,-56.65493c100.21618,0.0657 155.09312,-10.17222 299.13723,-18.93824l0.35624,150.36022c-144.19414,-8.31987 -195.96912,-18.2452 -305.90694,-18.7146l-0.00001,0z" id="path2852" />
     <path fill-rule="evenodd" fill="#20240b"  d="m-1852.19705,783.56665c0.11946,5.22516 -0.22537,35.62807 -0.61508,129.79997l277.49107,14.14181l-0.37251,-159.1875l-276.50348,15.24572z" id="path2760" />
     <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#cdb900"  id="path2762"     d="m-1910.31501,832.34151c8.25331,0 14.94394,7.07196 14.94394,15.79566c0,8.7237 -6.69063,15.79565 -14.94394,15.79565c-8.25332,0 -14.94394,-7.07195 -14.94394,-15.79565c0,-8.7237 6.69063,-15.79566 14.94394,-15.79566z"/>
     <g id="g9109" transform="matrix(0.691372, 0, 0, 0.901159, 372.514, 195.228)">
      <path stroke-width="0.58093px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   id="path8220" d="m-3068.60734,764.51771l13.98593,-7.09125l-12.23769,-10.24291c-17.81049,-2.74177 -13.32823,-3.92972 -21.85301,-10.24292l-43.70602,-45.69915l-2.62235,2.36376l66.43314,70.91247z"/>
      <path stroke-width="0.58093px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   id="path9107" d="m-3067.89306,684.8129l13.98593,7.09125l-15.09483,11.67148c-18.52478,3.45606 -9.75681,1.07258 -18.99587,8.81435l-43.70602,45.69915l-2.62235,-2.36376l66.43314,-70.91247z"/>
      <g id="g7275" transform="matrix(0, -0.289025, 0.233427, 0, -550.903, 33.6231)">
       <path stroke-width="0.79555px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   id="path4585" d="m-2393.35828,-10933.0231c-15.4406,-58.29352 -18.5211,-29.30755 -18.0694,-97.21527c0.4518,-67.90771 6.5869,-54.35013 24.2045,-145.13203c14.0038,103.64862 17.8068,80.08358 17.3551,147.9913c-0.4517,67.90772 -17.1409,60.72561 -23.4902,94.356z"/>
       <g id="g6367">
        <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   d="m-2393.67467,-10938.70835l10.73531,-119.65337l7.85714,-102.85714l15,102.85714l-33.59245,119.65337z" id="path5472"/>
        <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   d="m-2392.00103,-10938.1982l24.8477,-117.80638l0.7143,-85l11.4286,97.85714l-36.9906,104.94924z" id="path5474"/>
        <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   d="m-2391.33743,-10936.51473l35.80706,-76.847l0,-106.42857l-8.57146,96.42858l-27.2356,86.84699z" id="path5476"/>
       </g>
       <g transform="matrix(-1, 0, 0, 1, -2073.65, 1.21096)" id="g6380">
        <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   d="m315.77777,-10940.13692l10.73531,-119.65337l0,-104.28571l22.85714,104.28571l-33.59245,119.65337z" id="path6382"/>
        <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   d="m317.45141,-10939.62677l24.8477,-117.80638l-2.8571,-85.71428l12.85714,99.28571l-34.84774,104.23495z" id="path6384"/>
        <path stroke-width="1px" stroke="#000000" fill-rule="evenodd" fill="#ccb700"   d="m318.11501,-10937.9433l35.09278,-78.27557l-2.14288,-107.14285l-5.7143,98.57143l-27.2356,86.84699z" id="path6386"/>
       </g>
       <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="4" stroke="#000000" fill="#ccb700" d="m-2338.67397,-10903.2189c0,31.55912 -24.30454,57.14285 -54.28572,57.14285c-29.98117,0 -54.28571,-25.58373 -54.28571,-57.14285c0,-31.55913 24.30454,-57.14286 54.28571,-57.14286c29.98118,0 54.28572,25.58373 54.28572,57.14286z"     id="path4581" />
       <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="4" stroke="#000000" fill="#ccb700" d="m-2354.36153,-10957.17616c0,3.76835 -16.82884,6.82321 -37.58828,6.82321c-20.75943,0 -37.58827,-3.05486 -37.58827,-6.82321c0,-3.76836 16.82884,-6.82321 37.58827,-6.82321c20.75944,0 37.58828,3.05485 37.58828,6.82321z"     id="path4583" />
      </g>
      <path stroke-miterlimit="4" stroke-width="5.68412" stroke="#f00000" fill="none"  d="m-3171.16269,734.73804l-10.28033,-11.9546l11.79556,-11.76229" id="path7331" />
      <path stroke-miterlimit="4" stroke-width="5.68412" stroke="#f00000" fill="none"  d="m-3183.85142,734.73804l-10.28033,-11.9546l11.79556,-11.76229" id="path8218" />
     </g>
    </g>
    <g id="g2232">
     <path fill-rule="evenodd" fill="#c8ba00"  d="m-1611.10098,770.21114l19.28571,-1.07142l1.07143,157.5l-19.64285,-0.89286l-0.71429,-155.53572z" id="path1892" />
     <path fill-rule="evenodd" fill="#c8bc00"  d="m-1634.7801,771.82529l19.50868,-1.25001l-0.17857,154.64397l-18.97297,-1.07064l-0.35714,-152.32332z" id="path3757" />
    </g>
    <g id="g2872">
     <path fill-rule="evenodd" fill="#ffffff"  d="m-1615.24097,966.87336l19.10714,-1.25l0.71428,155.89286l-19.46428,-1.07144l-0.35714,-153.57142z" id="path5931" />
     <path fill-rule="evenodd" fill="#ffffff"  d="m-1639.63438,967.77321l19.68726,-0.89286l0,153.03682l-19.68726,-0.71349l0,-151.43047z" id="path5933" />
    </g>
   </g>
  </g>
 </g>
</svg>
    '''
    percent=53.3332
    delay=5

  elif position<=100:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 
<defs id="defs4">
  <clipPath id="clip">
   <path id="path10" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
  <clipPath id="clip-4">
   <path  d="m0,-200l0,800l300,0l0,-800l-300,0z" id="path10-7"/>
  </clipPath>
  <polygon points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 " transform="scale(53)" id="star-6"/>
  <clipPath id="clip-7">
   <path  d="m0,-200l0,800l300,0l0,-800l-300,0z" id="path10-4"/>
  </clipPath>
  <polygon points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 " transform="scale(53)" id="star-68"/>
  <clipPath id="clip-4-9">
   <path id="path10-7-1" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star-6-4" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
 </defs>
 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g id="g5717-4">
    <path stroke-width="1px" fill="#ffcc00" d="m34.11963,67.50998l15.41631,-4.69774l15.35947,4.67412l-0.14563,-3.00744l-15.21384,-4.67064l-15.27562,4.69124l-0.14069,3.01046z" id="path5049-2-8-0"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m34.26218,64.94208l15.269,-4.64924l15.26368,4.645" id="path5534-1"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m34.1627,67.04846l15.37322,-4.67758l15.34879,4.67013" id="path5536-4"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#dbb110" fill="none" d="m64.78549,65.02076l-2.22241,1.31385l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-1.69104,1.00387l-1.70537,-1.00387l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.24586,-1.32772" id="path5415-5-1-2"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m34.11963,67.50998l15.41631,-4.69774l15.35947,4.67412l-0.14563,-3.00744l-15.21384,-4.67064l-15.27562,4.69124l-0.14069,3.01046z" id="path5049-2-7"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m49.53579,59.84658l0.00016,2.96567" id="path5555-3"  />
   </g>
   <g id="g6076-49">
    <path stroke-width="1px" fill="#aa0000" d="m34.30523,63.53868l15.23056,-4.64358l15.18607,4.62399l-0.16338,-3.01385l-15.02286,-4.57581l-15.08943,4.59293l-0.14097,3.01632z" id="path5049-2-8-0-4-6-8"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m34.46275,60.96382l15.06828,-4.58812l15.05276,4.58081" id="path5534-1-6-3-7"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m34.33261,63.07957l15.20315,-4.62583l15.16451,4.61406" id="path5536-4-5-1-7"  />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m34.30523,63.53868l15.23056,-4.64358l15.18607,4.62399l-0.16338,-3.01385l-15.02286,-4.57581l-15.08943,4.59293l-0.14097,3.01632z" id="path5049-2-7-1-2-8"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.36549,62.5524l15.17027,-4.5744l15.11382,4.5579" id="path6057-5" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.40335,62.02532l15.13242,-4.52307l15.08709,4.51054" id="path6059-7" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.391,61.51465l15.14476,-4.48813l15.07101,4.46776" id="path6061-0" />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m49.53563,55.92943l0.00016,2.96567" id="path5555-3-2-1-86"  />
   </g>
   <g id="g11992">
    <g id="g10152"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 195.651, 121.656)" id="g6367"/>
   <g id="g11992-9">
    <g id="g10152-1"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 156.904, 123.891)" id="g6367-8"/>
   <g id="g11992-97">
    <g id="g10152-14"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 140.878, 133.228)" id="g6367-2"/>
   <g transform="matrix(0.386786, 0, 0, 0.270856, 31.8866, 76.8316)" id="g4891">
    <path stroke-miterlimit="4" stroke-width="1.06667" fill-rule="evenodd" fill="#cecdb6"   id="path14311" d="m85.07228,-1.32659l-5.71963,-177.41129l-33.78037,-25.08874l-33.93347,25.08874l-5.56653,177.41127l79,0.00002z"/>
    <g id="g62591">
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#bc8810"  d="m58.02544,-176.47557a12.54946,12.54946 0 0 1 -12.54946,12.54947a12.54946,12.54946 0 0 1 -12.54946,-12.54947a12.54946,12.54946 0 0 1 12.54946,-12.54946a12.54946,12.54946 0 0 1 12.54946,12.54946z" id="circle62593"/>
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#fddd10"  d="m56.14302,-176.47557a10.66704,10.66704 0 0 1 -10.66704,10.66705a10.66704,10.66704 0 0 1 -10.66704,-10.66705a10.66704,10.66704 0 0 1 10.66704,-10.66704a10.66704,10.66704 0 0 1 10.66704,10.66704z" id="circle62595"/>
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-width="0.7" fill-rule="nonzero" fill="#dbb110" clip-rule="nonzero"  id="path62597" d="m45.47709,-188.4969c-3.15262,-0.00039 -6.27327,1.28938 -8.50285,3.51849c-2.22958,2.22913 -3.52045,5.35019 -3.5207,8.50284c0.00025,3.15267 1.29112,6.27372 3.5207,8.50284c2.22958,2.22911 5.35023,3.51889 8.50285,3.5185c3.15231,-0.00025 6.27166,-1.29174 8.50062,-3.52071c2.22896,-2.22896 3.52046,-5.3483 3.52071,-8.50063c-0.00025,-3.15231 -1.29175,-6.27165 -3.52071,-8.50062c-2.22896,-2.22896 -5.34831,-3.52046 -8.50062,-3.52071zm0,0.79272c2.93447,0.00022 5.86314,1.21537 7.9382,3.29041c2.07505,2.07506 3.29018,5.00373 3.29042,7.9382c-0.00023,2.93449 -1.21537,5.86316 -3.29042,7.93821c-2.07506,2.07505 -5.00372,3.29019 -7.9382,3.29041c-2.93499,0.00038 -5.86496,-1.21318 -7.94042,-3.2882c-2.07544,-2.07501 -3.29019,-5.00548 -3.29042,-7.94042c0.00024,-2.93492 1.21498,-5.8654 3.29042,-7.94041c2.07546,-2.07502 5.00543,-3.28858 7.94042,-3.2882z"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.50255" stroke="#b3b3b3" fill="none"  d="m45.57228,-203.82662l-33.93347,25.08874l-5.56653,177.41127l79,0.00002l-5.71962,-177.41129l-33.78038,-25.08874z" id="path5037" />
   </g>
   <g id="g11992-3">
    <g id="g10152-6"/>
   </g>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950" d="m39.13223,34.66579l0,0c-1.35429,0 -2.38159,0.71539 -2.44456,1.60187l-2.53187,35.6415c-0.06297,0.88647 1.09028,1.60187 2.44456,1.60187l12.91304,0l12.91304,0c1.35429,0 2.50753,-0.71539 2.44456,-1.60187l-2.53187,-35.6415c-0.06297,-0.88647 -1.09028,-1.60187 -2.44456,-1.60187l0,0l-10.38117,0l-10.38117,0z"/>
   <g transform="matrix(0.0305084, 0, 0, 0.0210678, 145.52, 130.245)" id="g4807">
    <g id="g4635"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3268.65368,-4399.08917l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3268.66008,-4337.19018l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5" />
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 47.8852, 120.422)" id="g6367-0"/>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950-7" d="m39.17626,34.63111l0,0c-1.35429,0 -2.38159,0.71539 -2.44456,1.60187l-2.53187,35.6415c-0.06297,0.88647 1.09028,1.60187 2.44456,1.60187l12.91304,0l12.91304,0c1.35429,0 2.50753,-0.71539 2.44456,-1.60187l-2.53187,-35.6415c-0.06297,-0.88647 -1.09028,-1.60187 -2.44456,-1.60187l0,0l-10.38117,0l-10.38117,0z"/>
   <g transform="matrix(0.0305084, 0, 0, 0.0210678, 145.564, 130.21)" id="g4807-3">
    <g id="g4635-0"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3268.65368,-4399.08917l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3268.66008,-4337.19018l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5-2" />
   </g>
   <g id="g11992-9-0">
    <g id="g10152-1-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 9.13768, 122.656)" id="g6367-8-3"/>
   <g id="g11992-97-7">
    <g id="g10152-14-9"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, -6.88758, 131.993)" id="g6367-2-9"/>
   <path stroke-miterlimit="4" stroke="#030315" fill="#040420"   id="path5943" d="m33.84236,73.44307l31.34055,0l-1.86973,-38.74039l-27.66032,0l-1.8105,38.74039z"/>
   <g id="g11992-4">
    <g id="g10152-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 79.7281, 126.799)" id="g6367-9"/>
   <g id="g11992-9-5">
    <g id="g10152-1-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 40.9806, 129.034)" id="g6367-8-5"/>
   <g id="g11992-97-0">
    <g id="g10152-14-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 24.9553, 138.371)" id="g6367-2-5"/>
   <g transform="matrix(0.0305084, 0, 0, 0.0210678, 216.895, 133.518)" id="g4635-0-6"/>
   <g stroke="#040420" transform="matrix(0.0305084, 0, 0, 0.0210678, 84.6532, 129.776)" id="g4807-5">
    <g stroke="#040420" id="g4635-07"/>
   </g>
   <g id="g5169-7">
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m49.59053,38.91884l-3.74225,1.71606l0,0.98546l3.74225,-1.71606l3.74225,1.71606l0.00001,-0.98546l-3.74226,-1.71606z" id="path5142-5"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m49.59053,36.94792l-3.74225,1.71606l0,0.98546l3.74225,-1.71606l3.74225,1.71606l0.00001,-0.98546l-3.74226,-1.71606z" id="path5142-9-3"  />
   </g>
   <g id="g4804">
    <ellipse stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="0.63745" stroke="#d4aa00" fill="#ffcc00" cx="49.55517" cy="45.08074" rx="1.12359" ry="0.10113" id="path4583"/>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819" d="m44.04161,45.50835l0.05967,0.64039l5.98951,2.4112l0.26453,-0.78928l-6.3137,-2.26232z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815" d="m53.82213,48.45548c0,0 0.12218,0.41811 0.36131,0.5046c0.30393,0.10992 1.0151,-0.10813 1.0151,-0.10813l2.64957,0.97315c0,0 -0.20026,0.83027 -0.55056,1.15337c-0.33893,0.31261 -1.39361,0.66078 -1.39361,0.66078l-1.58286,-1.7661c0,0 -1.02524,0.05784 -1.46243,-0.09611c-0.33,-0.11621 -0.73982,-0.57668 -0.73982,-0.57668l-1.04614,-0.81637l-7.76284,-2.9561l-0.51406,-0.1969l0.25286,-0.41364l0.51928,0.17803l10.2542,3.4601z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.172146, -0.0634466, -0.0908588, 0.12021, 66.8208, 112.227)" y="-383.56921" x="332.60688" height="7" width="3" id="rect4817"/>
    </g>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845-6" transform="matrix(-0.194653, 0, 0, 0.135926, 67.2294, 118.264)">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819-7" d="m63.00819,-537.5333l0.30656,4.71135l30.77021,17.73909l1.35896,-5.80668l-32.43573,-16.64376z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815-6" d="m113.25417,-515.8514c0,0 0.62766,3.07603 1.85616,3.71231c1.56141,0.8087 5.21491,-0.79549 5.21491,-0.79549l13.6118,7.15945c0,0 -1.0288,6.10825 -2.82842,8.48528c-1.74121,2.29987 -7.15946,4.86136 -7.15946,4.86136l-8.13173,-12.99309c0,0 -5.26702,0.4255 -7.51301,-0.7071c-1.69533,-0.85492 -3.8007,-4.24264 -3.8007,-4.24264l-5.37437,-6.006l-39.88046,-21.74793l-2.64092,-1.44862l1.29901,-3.04311l2.66774,1.30974l52.67945,25.45584z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.884377, -0.466774, -0.466774, 0.884377, 0, 0)" y="-508.89517" x="195.18355" height="7" width="3" id="rect4817-0"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m51.97367,47.71926l-2.47053,2.51601l-2.47053,-2.51601c0,0 -0.31191,-1.90305 2.44693,-2.00333c2.75884,-0.10028 2.49413,2.00333 2.49413,2.00333z" id="path4953-5-7"  />
    <circle stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="path4775-5" cx="49.50314" cy="51.68288" r="0.91283"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m47.13583,46.33762c0,0 -0.41401,-2.0084 2.3673,-1.98438c2.78132,0.02403 2.3673,1.98438 2.3673,1.98438l-2.3673,3.59182l-2.3673,-3.59182z" id="path4951-0"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m51.09299,44.91994c0,0 0.30824,-2.28271 -1.63448,-2.24666c-1.94272,0.03604 -1.63448,2.24666 -1.63448,2.24666l1.6791,5.06387l1.58986,-5.06387z" id="path4796-2-1"  />
    <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="rect4777-6" width="3.3091" height="0.61167" x="47.84859" y="49.62361" ry="2.25"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m50.24995,45.91712c0.08093,-1.008 -0.12044,-3.02759 -0.12044,-3.02759c0,0 -0.04837,-1.08128 -0.60218,-1.08128c-0.55381,0 -0.60218,1.08128 -0.60218,1.08128c0,0 -0.1949,2.01934 -0.12044,3.02759c0.09192,1.24449 0.69841,3.70649 0.69841,3.70649c0,0 0.6468,-2.46078 0.74681,-3.70649z" id="path4779-1-3"  />
   </g>
   <g id="g11992-8">
    <g id="g10152-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 136.474, 120.749)" id="g6367-97"/>
   <g id="g11992-9-9">
    <g id="g10152-1-4"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 97.7267, 122.983)" id="g6367-8-8"/>
   <g id="g11992-97-09">
    <g id="g10152-14-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 81.7015, 132.32)" id="g6367-2-7"/>
   <g id="g11992-3-3">
    <g id="g10152-6-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, -11.2917, 119.514)" id="g6367-0-6"/>
   <g id="g11992-9-0-2">
    <g id="g10152-1-2-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, -50.0393, 121.749)" id="g6367-8-3-9"/>
   <g id="g11992-97-7-2">
    <g id="g10152-14-9-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, -66.0645, 131.085)" id="g6367-2-9-5"/>
   <g id="g11992-4-9">
    <g id="g10152-7-6"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, 20.5512, 125.892)" id="g6367-9-2"/>
   <g id="g11992-9-5-0">
    <g id="g10152-1-5-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, -18.1964, 128.126)" id="g6367-8-5-7"/>
   <g id="g11992-97-0-2">
    <g id="g10152-14-8-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0506987, 0, 0, 0.0219364, -34.2216, 137.463)" id="g6367-2-5-9"/>
   <g transform="matrix(0.0305084, 0, 0, 0.0210678, 157.718, 132.61)" id="g4635-0-6-0"/>
   <g stroke="#040420" transform="matrix(0.0305084, 0, 0, 0.0210678, 25.4762, 128.868)" id="g4807-5-1">
    <g stroke="#040420" id="g4635-07-8"/>
   </g>
   <g id="g5717">
    <path stroke-width="1px" fill="#ffcc00" d="m33.99029,71.4533l15.52322,-4.72665l15.57492,4.75886l-0.14613,-3.02777l-15.42895,-4.69677l-15.43089,4.69853l-0.09218,2.99378z" id="path5049-2-8"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m34.06319,68.91024l15.44556,-4.703l15.44991,4.70167" id="path5534"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.96492,71.01621l15.54857,-4.73093l15.54446,4.72967" id="path5536"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#dbb110" fill="none" d="m64.96725,69.4574l-0.10812,-0.57904l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-1.69104,1.00387l-1.70537,-1.00387l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.13285,0.71147" id="path5415-5-1"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m33.93451,71.47127l15.6307,-4.71241l15.52322,4.72665l-0.14613,-3.02777l-15.40635,-4.69402l-15.45348,4.69579l-0.14796,3.01176z" id="path5049-2"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m49.53595,63.76373l0,3.00396" id="path5555"  />
   </g>
   <path stroke-width="1px" stroke="#000000" fill="#1a1a1a"   id="path6263" d="m33.91783,71.96809l15.61473,-4.75451l15.57362,4.74017l-0.66154,-13.62487l-14.91154,-4.54381l-14.99306,4.56527l-0.62221,13.61775z"/>
   <g id="g5717-4-8">
    <path stroke-width="1px" fill="#ffcc00" d="m34.30523,63.53868l15.23056,-4.64358l15.18607,4.62399l-0.17798,-3.02001l-15.00809,-4.60795l-15.08959,4.63122l-0.14097,3.01632z" id="path5049-2-8-0-4"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m34.46275,60.96382l15.06827,-4.58812l15.05276,4.58081" id="path5534-1-6"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m34.33261,63.07957l15.20315,-4.62583l15.16451,4.61406" id="path5536-4-5"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#dbb110" fill="none" d="m64.61289,61.20556l-2.04996,1.21191l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-2.31848,1.37065l-0.411,-2.20115l-1.69104,1.00387l-1.70537,-1.00387l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.31848,-1.37065l-0.411,2.20115l-2.0687,-1.22299" id="path5415-5-1-2-9"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m34.30523,63.53868l15.23056,-4.64358l15.18607,4.62399l-0.16338,-3.01385l-15.0227,-4.6141l-15.08959,4.63122l-0.14097,3.01632z" id="path5049-2-7-1"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m49.53579,55.89114l0,3.00396" id="path5555-3-2"  />
   </g>
   <g id="g6076-1">
    <path stroke-width="1px" fill="#aa0000" d="m34.11964,67.50998l15.41631,-4.69774l15.35947,4.67412l-0.14563,-3.00744l-15.214,-4.63235l-15.27546,4.65295l-0.14069,3.01046z" id="path5049-2-8-0-4-6-7"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m34.26219,64.94208l15.269,-4.64924l15.26368,4.645" id="path5534-1-6-3-1"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m34.1627,67.04846l15.37322,-4.67758l15.31534,4.65995" id="path5536-4-5-1-8"  />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m34.11964,67.50998l15.41631,-4.69774l15.35947,4.67412l-0.14563,-3.00744l-15.214,-4.63235l-15.27546,4.65295l-0.14069,3.01046z" id="path5049-2-7-1-2-3"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.1916,66.52203l15.34432,-4.62689l15.30424,4.61533" id="path6057-0" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.1918,66.00575l15.34413,-4.58635l15.27465,4.56661" id="path6059-3" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.21146,65.48505l15.32446,-4.54139l15.25572,4.52252" id="path6061-7" />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m49.53579,59.84658l0.00016,2.96567" id="path5555-3-2-1-6"  />
   </g>
   <g id="g6076-4">
    <path stroke-width="1px" fill="#aa0000" d="m34.01289,71.45604l15.52322,-4.72665l15.52322,4.72665l-0.11703,-2.9983l-15.40635,-4.69402l-15.43089,4.69853l-0.09218,2.99378z" id="path5049-2-8-0-4-6-4"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m34.08578,68.91299l15.44556,-4.703l15.4406,4.69884" id="path5534-1-6-3-8"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m33.98752,71.01896l15.54857,-4.73093l15.52148,4.72267" id="path5536-4-5-1-3"  />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m33.9571,71.47402l15.579,-4.74463l15.55232,4.75612l-0.14613,-3.02777l-15.40635,-4.69402l-15.43089,4.69853l-0.14796,3.01176z" id="path5049-2-7-1-2-0"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.99112,70.49968l15.54496,-4.68739l15.47861,4.66791" id="path6057-7" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.03561,69.96963l15.50047,-4.63308l15.47456,4.62638" id="path6059-6" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m34.07168,69.44367l15.4644,-4.58286l15.44261,4.57792" id="path6061-1" />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m49.53595,63.76373l0.00016,2.96567" id="path5555-3-2-1-8"  />
   </g>
   <g id="g6320">
    <path stroke-width="1px" stroke="#bc8810" fill="#ffcc00" d="m49.53563,54.97795l14.97649,4.56658l-0.03644,-0.75491l-14.94006,-4.55221l-15.01687,4.57863l-0.03445,0.75406l15.05132,-4.59214z" id="path6299"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m49.53563,54.23741l0,0.74055" id="path6316" />
   </g>
  </g>
 </g>
</svg>
    '''
    percent=39.9999
    delay=4

  elif position<=150:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 
<defs id="defs4">
  <clipPath id="clip">
   <path id="path10" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
  <clipPath id="clip-4">
   <path  d="m0,-200l0,800l300,0l0,-800l-300,0z" id="path10-7"/>
  </clipPath>
  <polygon points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 " transform="scale(53)" id="star-6"/>
  <clipPath id="clip-7">
   <path  d="m0,-200l0,800l300,0l0,-800l-300,0z" id="path10-4"/>
  </clipPath>
  <polygon points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 " transform="scale(53)" id="star-68"/>
  <clipPath id="clip-4-9">
   <path id="path10-7-1" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star-6-4" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
 </defs>
 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g id="g6076-49">
    <path stroke-width="1px" fill="#aa0000" d="m33.67262,63.01276l16.36507,-4.47465l16.31727,4.45577l-0.17555,-2.90421l-16.1419,-4.40934l-16.21343,4.42584l-0.15147,2.90659z" id="path5049-2-8-0-4-6-8"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m33.84188,60.53157l16.1907,-4.42121l16.17403,4.41416" id="path5534-1-6-3-7"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m33.70205,62.57035l16.33562,-4.45754l16.2941,4.4462" id="path5536-4-5-1-7"  />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m33.67262,63.01276l16.36507,-4.47465l16.31727,4.45577l-0.17555,-2.90421l-16.1419,-4.40934l-16.21343,4.42584l-0.15147,2.90659z" id="path5049-2-7-1-2-8"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.73738,62.06236l16.30029,-4.40799l16.23964,4.39208" id="path6057-5" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.77805,61.55445l16.25962,-4.35852l16.21092,4.34644" id="path6059-7" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.76478,61.06236l16.27289,-4.32485l16.19363,4.30522" id="path6061-0" />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m50.03752,55.68033l0.00017,2.85778" id="path5555-3-2-1-86"  />
   </g>
   <g id="g11992">
    <g id="g10152"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 199.234, 130.804)" id="g6367"/>
   <g id="g11992-9">
    <g id="g10152-1"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 157.601, 132.957)" id="g6367-8"/>
   <g id="g11992-97">
    <g id="g10152-14"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 140.382, 141.954)" id="g6367-2"/>
   <g transform="matrix(0.415598, 0, 0, 0.261002, 23.271, 87.6099)" id="g4891">
    <path stroke-miterlimit="4" stroke-width="1.06667" fill-rule="evenodd" fill="#cecdb6"   id="path14311" d="m103.84717,-46.49011l-5.71963,-177.41129l-33.78037,-25.08874l-33.93347,25.08874l-5.56653,177.41127l79,0.00002z"/>
    <g id="g62591">
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#bc8810"  d="m76.80034,-221.63909a12.54946,12.54946 0 0 1 -12.54946,12.54947a12.54946,12.54946 0 0 1 -12.54946,-12.54947a12.54946,12.54946 0 0 1 12.54946,-12.54946a12.54946,12.54946 0 0 1 12.54946,12.54946z" id="circle62593"/>
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#fddd10"  d="m74.91792,-221.63909a10.66704,10.66704 0 0 1 -10.66704,10.66705a10.66704,10.66704 0 0 1 -10.66704,-10.66705a10.66704,10.66704 0 0 1 10.66704,-10.66704a10.66704,10.66704 0 0 1 10.66704,10.66704z" id="circle62595"/>
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-width="0.7" fill-rule="nonzero" fill="#dbb110" clip-rule="nonzero"  id="path62597" d="m64.25199,-233.66042c-3.15262,-0.00039 -6.27327,1.28938 -8.50285,3.51849c-2.22958,2.22913 -3.52045,5.35019 -3.5207,8.50284c0.00025,3.15267 1.29112,6.27372 3.5207,8.50284c2.22958,2.22911 5.35023,3.51889 8.50285,3.5185c3.15231,-0.00025 6.27166,-1.29174 8.50062,-3.52071c2.22896,-2.22896 3.52046,-5.3483 3.52071,-8.50063c-0.00025,-3.15231 -1.29175,-6.27165 -3.52071,-8.50062c-2.22896,-2.22896 -5.34831,-3.52046 -8.50062,-3.52071zm0,0.79272c2.93447,0.00022 5.86314,1.21537 7.9382,3.29041c2.07505,2.07506 3.29018,5.00373 3.29042,7.9382c-0.00023,2.93449 -1.21537,5.86316 -3.29042,7.93821c-2.07506,2.07505 -5.00372,3.29019 -7.9382,3.29041c-2.93499,0.00038 -5.86496,-1.21318 -7.94042,-3.2882c-2.07544,-2.07501 -3.29019,-5.00548 -3.29042,-7.94042c0.00024,-2.93492 1.21498,-5.8654 3.29042,-7.94041c2.07546,-2.07502 5.00543,-3.28858 7.94042,-3.2882z"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.50255" stroke="#b3b3b3" fill="none"  d="m64.34717,-248.99014l-33.93347,25.08874l-5.56653,177.41127l79,0.00002l-5.71962,-177.41129l-33.78038,-25.08874z" id="path5037" />
   </g>
   <g id="g11992-3">
    <g id="g10152-6"/>
   </g>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950" d="m38.85919,35.19026l0,0c-1.45517,0 -2.559,0.68937 -2.62666,1.54359l-2.72047,34.34487c-0.06766,0.85422 1.17149,1.54359 2.62666,1.54359l13.87493,0l13.87492,0c1.45517,0 2.69432,-0.68937 2.62666,-1.54359l-2.72047,-34.34487c-0.06766,-0.85422 -1.17149,-1.54359 -2.62666,-1.54359l0,0l-11.15446,0l-11.15446,0z"/>
   <g transform="matrix(0.032781, 0, 0, 0.0203014, 145.369, 139.08)" id="g4807">
    <g id="g4635"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3030.62559,-4979.72801l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3030.63199,-4917.82902l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5" />
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 40.4614, 129.614)" id="g6367-0"/>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950-7" d="m38.9065,35.15685l0,0c-1.45517,0 -2.559,0.68937 -2.62666,1.54359l-2.72047,34.34487c-0.06766,0.85422 1.17149,1.54359 2.62666,1.54359l13.87493,0l13.87492,0c1.45517,0 2.69432,-0.68937 2.62666,-1.54359l-2.72047,-34.34487c-0.06766,-0.85422 -1.17149,-1.54359 -2.62666,-1.54359l0,0l-11.15446,0l-11.15446,0z"/>
   <g transform="matrix(0.032781, 0, 0, 0.0203014, 145.416, 139.046)" id="g4807-3">
    <g id="g4635-0"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3030.62559,-4979.72801l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-3030.63199,-4917.82902l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5-2" />
   </g>
   <g id="g11992-9-0">
    <g id="g10152-1-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -1.17245, 131.768)" id="g6367-8-3"/>
   <g id="g11992-97-7">
    <g id="g10152-14-9"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -18.3914, 140.765)" id="g6367-2-9"/>
   <path stroke-miterlimit="4" stroke="#030315" fill="#040420"   id="path5943" d="m33.17527,72.55682l33.67508,0l-2.009,-37.33102l-29.72071,0l-1.94537,37.33102z"/>
   <g id="g11992-4">
    <g id="g10152-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 74.6762, 135.76)" id="g6367-9"/>
   <g id="g11992-9-5">
    <g id="g10152-1-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 33.0424, 137.913)" id="g6367-8-5"/>
   <g id="g11992-97-0">
    <g id="g10152-14-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 15.8234, 146.91)" id="g6367-2-5"/>
   <g transform="matrix(0.032781, 0, 0, 0.0203014, 222.06, 142.234)" id="g4635-0-6"/>
   <g stroke="#040420" transform="matrix(0.032781, 0, 0, 0.0203014, 79.9681, 138.628)" id="g4807-5">
    <g stroke="#040420" id="g4635-07"/>
   </g>
   <g id="g5169-7">
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m50.09652,39.28859l-4.02101,1.65363l0,0.94961l4.02101,-1.65363l4.02101,1.65363l0.00001,-0.94961l-4.02102,-1.65363z" id="path5142-5"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m50.09652,37.38936l-4.02101,1.65363l0,0.94961l4.02101,-1.65363l4.02101,1.65363l0.00001,-0.94961l-4.02102,-1.65363z" id="path5142-9-3"  />
   </g>
   <g id="g4804">
    <ellipse stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="0.63745" stroke="#d4aa00" fill="#ffcc00" cx="50.05852" cy="45.22632" rx="1.20728" ry="0.09745" id="path4583"/>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819" d="m44.13426,45.63837l0.06412,0.6171l6.43566,2.32348l0.28423,-0.76056l-6.78401,-2.18001z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815" d="m54.64332,48.47828c0,0 0.13128,0.4029 0.38822,0.48624c0.32657,0.10592 1.09071,-0.10419 1.09071,-0.10419l2.84694,0.93775c0,0 -0.21518,0.80006 -0.59157,1.11141c-0.36418,0.30124 -1.49742,0.63674 -1.49742,0.63674l-1.70077,-1.70184c0,0 -1.10161,0.05573 -1.57136,-0.09262c-0.35458,-0.11198 -0.79493,-0.5557 -0.79493,-0.5557l-1.12406,-0.78667l-8.34109,-2.84856l-0.55235,-0.18974l0.27169,-0.39859l0.55796,0.17155l11.01803,3.33423z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.184969, -0.0611384, -0.0976268, 0.115836, 60.8074, 121.717)" y="-480.57358" x="341.62142" height="7" width="3" id="rect4817"/>
    </g>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845-6" transform="matrix(-0.209152, 0, 0, 0.130981, 61.2465, 127.535)">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819-7" d="m25.70139,-627.52956l0.30656,4.71135l30.77021,17.73909l1.35896,-5.80668l-32.43573,-16.64376z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815-6" d="m75.94737,-605.84766c0,0 0.62766,3.07603 1.85616,3.71231c1.56141,0.8087 5.21491,-0.79549 5.21491,-0.79549l13.6118,7.15945c0,0 -1.0288,6.10825 -2.82842,8.48528c-1.74121,2.29987 -7.15946,4.86136 -7.15946,4.86136l-8.13173,-12.99309c0,0 -5.26702,0.4255 -7.51301,-0.7071c-1.69533,-0.85492 -3.8007,-4.24264 -3.8007,-4.24264l-5.37437,-6.006l-39.88046,-21.74793l-2.64092,-1.44862l1.29901,-3.04311l2.66774,1.30974l52.67945,25.45584z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.884377, -0.466774, -0.466774, 0.884377, 0, 0)" y="-571.07191" x="270.18471" height="7" width="3" id="rect4817-0"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m52.65717,47.76884l-2.65456,2.42448l-2.65456,-2.42448c0,0 -0.33515,-1.83382 2.6292,-1.93045c2.96435,-0.09663 2.67991,1.93045 2.67991,1.93045z" id="path4953-5-7"  />
    <circle stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="path4775-5" cx="50.00261" cy="51.58827" r="0.98294"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m47.45897,46.43747c0,0 -0.44485,-1.93534 2.54364,-1.91218c2.98849,0.02315 2.54364,1.91218 2.54364,1.91218l-2.54364,3.46115l-2.54364,-3.46115z" id="path4951-0"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m51.71089,45.07136c0,0 0.3312,-2.19966 -1.75623,-2.16493c-2.08743,0.03473 -1.75623,2.16493 -1.75623,2.16493l1.80417,4.87965l1.70828,-4.87965z" id="path4796-2-1"  />
    <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="rect4777-6" width="3.55559" height="0.58941" x="48.22482" y="49.60391" ry="2.25"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m50.80505,46.03227c0.08696,-0.97133 -0.12941,-2.91745 -0.12941,-2.91745c0,0 -0.05197,-1.04195 -0.64703,-1.04195c-0.59506,0 -0.64703,1.04195 -0.64703,1.04195c0,0 -0.20942,1.94588 -0.12941,2.91745c0.09876,1.19922 0.75044,3.57164 0.75044,3.57164c0,0 0.69498,-2.37125 0.80244,-3.57164z" id="path4779-1-3"  />
   </g>
   <g id="g11992-8">
    <g id="g10152-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 135.649, 129.929)" id="g6367-97"/>
   <g id="g11992-9-9">
    <g id="g10152-1-4"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 94.0156, 132.082)" id="g6367-8-8"/>
   <g id="g11992-97-09">
    <g id="g10152-14-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 76.7966, 141.079)" id="g6367-2-7"/>
   <g id="g11992-3-3">
    <g id="g10152-6-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -23.1236, 128.74)" id="g6367-0-6"/>
   <g id="g11992-9-0-2">
    <g id="g10152-1-2-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -64.7574, 130.893)" id="g6367-8-3-9"/>
   <g id="g11992-97-7-2">
    <g id="g10152-14-9-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -81.9764, 139.89)" id="g6367-2-9-5"/>
   <g id="g11992-4-9">
    <g id="g10152-7-6"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, 11.0912, 134.885)" id="g6367-9-2"/>
   <g id="g11992-9-5-0">
    <g id="g10152-1-5-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -30.5426, 137.038)" id="g6367-8-5-7"/>
   <g id="g11992-97-0-2">
    <g id="g10152-14-8-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0544752, 0, 0, 0.0211383, -47.7616, 146.035)" id="g6367-2-5-9"/>
   <g transform="matrix(0.032781, 0, 0, 0.0203014, 158.475, 141.359)" id="g4635-0-6-0"/>
   <g stroke="#040420" transform="matrix(0.032781, 0, 0, 0.0203014, 16.3831, 137.753)" id="g4807-5-1">
    <g stroke="#040420" id="g4635-07-8"/>
   </g>
   <g id="g6076-1">
    <path stroke-width="1px" fill="#aa0000" d="m33.47321,66.83959l16.56466,-4.52683l16.50358,4.50407l-0.15648,-2.89803l-16.34728,-4.46382l-16.41332,4.48367l-0.15117,2.90094z" id="path5049-2-8-0-4-6-7"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m33.62637,64.3651l16.40638,-4.4801l16.40066,4.47601" id="path5534-1-6-3-1"  />
    <path stroke-width="1px" stroke="#800000" fill="none" d="m33.51948,66.39485l16.51836,-4.50741l16.45617,4.49043" id="path5536-4-5-1-8"  />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m33.47321,66.83959l16.56466,-4.52683l16.50358,4.50407l-0.15648,-2.89803l-16.34728,-4.46382l-16.41332,4.48367l-0.15117,2.90094z" id="path5049-2-7-1-2-3"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.55053,65.88757l16.48731,-4.45856l16.44424,4.44742" id="path6057-0" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.55074,65.39007l16.4871,-4.4195l16.41245,4.40048" id="path6059-3" />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#550000" fill="none"  d="m33.57187,64.88832l16.46597,-4.37617l16.39211,4.35799" id="path6061-7" />
    <path stroke-width="1px" stroke="#550000" fill="none" d="m50.03769,59.45498l0.00017,2.85778" id="path5555-3-2-1-6"  />
   </g>
   <path stroke-width="1px" stroke="#000000" fill="#1a1a1a"   id="path6263" d="m33.25637,71.1355l16.77786,-4.58154l16.73369,4.56772l-0.61235,-11.47521l-16.12076,-4.40202l-16.18626,4.39249l-0.59217,11.49857z"/>
   <g id="g5717">
    <path stroke-width="1px" fill="#ffcc00" d="m33.33422,70.63944l16.67953,-4.5547l16.73508,4.58574l-0.15701,-2.91762l-16.57823,-4.5259l-16.58032,4.5276l-0.09904,2.88487z" id="path5049-2-8"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.41255,68.1889l16.59609,-4.53191l16.60076,4.53062" id="path5534"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.30696,70.21826l16.70677,-4.55882l16.70236,4.5576" id="path5536"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#dbb110" fill="none" d="m66.61864,68.71616l-0.11617,-0.55797l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-1.81701,0.96735l-1.8324,-0.96735l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.14274,0.68559" id="path5415-5-1"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m33.27429,70.65676l16.79502,-4.54097l16.67953,4.55469l-0.15701,-2.91762l-16.55396,-4.52325l-16.6046,4.52496l-0.15898,2.90219z" id="path5049-2"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m50.03787,63.22962l0,2.89467" id="path5555"  />
   </g>
   <g id="g5717-4-8">
    <path stroke-width="1px" fill="#ffcc00" d="m33.67262,63.01276l16.36507,-4.47465l16.31727,4.45577l-0.19124,-2.91014l-16.12603,-4.44031l-16.2136,4.46274l-0.15147,2.90659z" id="path5049-2-8-0-4"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.84188,60.53157l16.1907,-4.42121l16.17403,4.41416" id="path5534-1-6"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.70205,62.57035l16.33562,-4.45754l16.2941,4.4462" id="path5536-4-5"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#dbb110" fill="none" d="m66.23788,60.76452l-2.20266,1.16782l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-1.81701,0.96735l-1.8324,-0.96735l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.2228,-1.1785" id="path5415-5-1-2-9"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m33.67262,63.01276l16.36507,-4.47465l16.31727,4.45577l-0.17555,-2.90421l-16.14173,-4.44624l-16.2136,4.46274l-0.15147,2.90659z" id="path5049-2-7-1"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m50.03769,55.64343l0,2.89468" id="path5555-3-2"  />
   </g>
   <g id="g5717-4">
    <path stroke-width="1px" fill="#ffcc00" d="m33.4732,66.83959l16.56466,-4.52683l16.50358,4.50407l-0.15648,-2.89803l-16.34711,-4.50072l-16.41349,4.52057l-0.15117,2.90094z" id="path5049-2-8-0"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.62637,64.3651l16.40638,-4.4801l16.40066,4.47601" id="path5534-1"  />
    <path stroke-width="1px" stroke="#dbb110" fill="none" d="m33.51947,66.39485l16.51836,-4.50741l16.4921,4.50023" id="path5536-4"  />
    <path stroke-dashoffset="0" stroke-dasharray="3, 1" stroke-miterlimit="4" stroke="#dbb110" fill="none" d="m66.42333,64.44092l-2.38795,1.26606l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-2.49118,1.32079l-0.44162,-2.12107l-1.81701,0.96735l-1.8324,-0.96735l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.49118,-1.32079l-0.44162,2.12107l-2.41315,-1.27942" id="path5415-5-1-2"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m33.4732,66.83959l16.56466,-4.52683l16.50358,4.50407l-0.15648,-2.89803l-16.34711,-4.50072l-16.41349,4.52057l-0.15117,2.90094z" id="path5049-2-7"  />
    <path stroke-width="1px" stroke="#bc8810" fill="none" d="m50.03769,59.45498l0.00017,2.85778" id="path5555-3"  />
   </g>
  </g>
 </g>
</svg>
    '''
    percent=26.6666
    delay=3

  elif position<=200:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 
<defs id="defs4">
  <clipPath id="clip">
   <path id="path10" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
  <clipPath id="clip-4">
   <path  d="m0,-200l0,800l300,0l0,-800l-300,0z" id="path10-7"/>
  </clipPath>
  <polygon points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 " transform="scale(53)" id="star-6"/>
 </defs>
 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g id="g4918">
    <path stroke-width="1px" fill="#cccccc" d="m35.42961,68.79824l30.55677,0l-0.0766,-1.71798l-30.39592,0l-0.08426,1.71798z" id="path5606"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.48264,67.42386l30.40161,0" id="path5692-5"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.46562,67.76746l30.43566,0" id="path5692-1-5"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.45711,68.11105l30.45268,0" id="path5692-9-9"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.44008,68.45465l30.4697,0" id="path5692-3-8"  />
    <path stroke-width="1px" stroke="#666666" fill="none" d="m35.42961,68.79824l30.55677,0l-0.0766,-1.71798l-30.39592,0l-0.08426,1.71798z" id="path5606-8"  />
   </g>
   <g id="g11992">
    <g id="g10152"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 185.477, 106.48)" id="g6367"/>
   <g id="g11992-9">
    <g id="g10152-1"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 147.141, 108.497)" id="g6367-8"/>
   <g id="g11992-97">
    <g id="g10152-14"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 131.286, 116.926)" id="g6367-2"/>
   <g transform="matrix(0.382676, 0, 0, 0.244527, 23.4525, 66.0121)" id="g4891">
    <path stroke-miterlimit="4" stroke-width="1.06667" fill-rule="evenodd" fill="#cecdb6"   id="path14311" d="m110.65027,31.87537l-5.71963,-177.41129l-33.78037,-25.08874l-33.93347,25.08874l-5.56653,177.41127l79,0.00002z"/>
    <g id="g62591">
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#bc8810"  d="m83.60344,-143.27361a12.54946,12.54946 0 0 1 -12.54946,12.54947a12.54946,12.54946 0 0 1 -12.54946,-12.54947a12.54946,12.54946 0 0 1 12.54946,-12.54946a12.54946,12.54946 0 0 1 12.54946,12.54946z" id="circle62593"/>
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#fddd10"  d="m81.72102,-143.27361a10.66704,10.66704 0 0 1 -10.66704,10.66705a10.66704,10.66704 0 0 1 -10.66704,-10.66705a10.66704,10.66704 0 0 1 10.66704,-10.66704a10.66704,10.66704 0 0 1 10.66704,10.66704z" id="circle62595"/>
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-width="0.7" fill-rule="nonzero" fill="#dbb110" clip-rule="nonzero"  id="path62597" d="m71.05509,-155.29494c-3.15262,-0.00039 -6.27327,1.28938 -8.50285,3.51849c-2.22958,2.22913 -3.52045,5.35019 -3.5207,8.50284c0.00025,3.15267 1.29112,6.27372 3.5207,8.50284c2.22958,2.22911 5.35023,3.51889 8.50285,3.5185c3.15231,-0.00025 6.27166,-1.29174 8.50062,-3.52071c2.22896,-2.22896 3.52046,-5.3483 3.52071,-8.50063c-0.00025,-3.15231 -1.29175,-6.27165 -3.52071,-8.50062c-2.22896,-2.22896 -5.34831,-3.52046 -8.50062,-3.52071zm0,0.79272c2.93447,0.00022 5.86314,1.21537 7.9382,3.29041c2.07505,2.07506 3.29018,5.00373 3.29042,7.9382c-0.00023,2.93449 -1.21537,5.86316 -3.29042,7.93821c-2.07506,2.07505 -5.00372,3.29019 -7.9382,3.29041c-2.93499,0.00038 -5.86496,-1.21318 -7.94042,-3.2882c-2.07544,-2.07501 -3.29019,-5.00548 -3.29042,-7.94042c0.00024,-2.93492 1.21498,-5.8654 3.29042,-7.94041c2.07546,-2.07502 5.00543,-3.28858 7.94042,-3.2882z"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.50255" stroke="#b3b3b3" fill="none"  d="m71.15027,-170.62466l-33.93347,25.08874l-5.56653,177.41127l79,0.00002l-5.71962,-177.41129l-33.78038,-25.08874z" id="path5037" />
   </g>
   <g id="g11992-3">
    <g id="g10152-6"/>
   </g>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950" d="m40.40915,36.06387l0,0c-1.3399,0 -2.35628,0.64585 -2.41858,1.44615l-2.50496,32.1769c-0.0623,0.8003 1.07869,1.44615 2.41858,1.44615l12.7758,0l12.7758,0c1.3399,0 2.48088,-0.64585 2.41858,-1.44615l-2.50496,-32.1769c-0.0623,-0.8003 -1.07869,-1.44615 -2.41858,-1.44615l0,0l-10.27084,0l-10.27084,0z"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 135.878, 114.233)" id="g4807">
    <g id="g4635"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.37571,-3972.23236l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.38211,-3910.33337l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5" />
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 39.281, 105.365)" id="g6367-0"/>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950-7" d="m40.45271,36.03257l0,0c-1.3399,0 -2.35628,0.64585 -2.41858,1.44615l-2.50496,32.1769c-0.0623,0.8003 1.07869,1.44615 2.41858,1.44615l12.7758,0l12.7758,0c1.3399,0 2.48088,-0.64585 2.41858,-1.44615l-2.50496,-32.1769c-0.0623,-0.8003 -1.07869,-1.44615 -2.41858,-1.44615l0,0l-10.27084,0l-10.27084,0z"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 135.922, 114.202)" id="g4807-3">
    <g id="g4635-0"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.37571,-3972.23236l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.38211,-3910.33337l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5-2" />
   </g>
   <g id="g11992-9-0">
    <g id="g10152-1-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 0.945297, 107.382)" id="g6367-8-3"/>
   <g id="g11992-97-7">
    <g id="g10152-14-9"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -14.9096, 115.812)" id="g6367-2-9"/>
   <path stroke-miterlimit="4" stroke="#030315" fill="#040420"   id="path5943" d="m35.17549,71.07172l31.00746,0l-1.84986,-34.97454l-27.36634,0l-1.79126,34.97454z"/>
   <g id="g11992-4">
    <g id="g10152-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 70.7855, 111.123)" id="g6367-9"/>
   <g id="g11992-9-5">
    <g id="g10152-1-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 32.4498, 113.14)" id="g6367-8-5"/>
   <g id="g11992-97-0">
    <g id="g10152-14-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 16.5948, 121.569)" id="g6367-2-5"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 206.494, 117.188)" id="g4635-0-6"/>
   <g stroke="#040420" transform="matrix(0.0301842, 0, 0, 0.0190199, 75.6582, 113.81)" id="g4807-5">
    <g stroke="#040420" id="g4635-07"/>
   </g>
   <g id="g5169-7">
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m50.7563,39.9035l-3.70248,1.54925l0,0.88967l3.70248,-1.54925l3.70248,1.54925l0.00001,-0.88967l-3.70249,-1.54925z" id="path5142-5"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m50.7563,38.12416l-3.70248,1.54925l0,0.88967l3.70248,-1.54925l3.70248,1.54925l0.00001,-0.88967l-3.70249,-1.54925z" id="path5142-9-3"  />
   </g>
   <path stroke-width="1px" fill="#ffcc00"   id="path5604" d="m35.28212,69.31364l30.79703,0l-0.13618,-2.7166l-30.54048,0l-0.12036,2.71661z"/>
   <path stroke-miterlimit="4" stroke-width="3" stroke="#800000" fill="none"   id="path5692-6" d="m35.33026,67.93926l30.669,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-1-3" d="m35.35434,68.28285l30.65696,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-9-8" d="m35.31823,68.62645l30.71715,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-3-6" d="m35.33026,68.97004l30.72317,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-1-3-1" d="m35.39045,67.25206l30.58475,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-9-8-7" d="m35.3423,67.59566l30.64493,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-9-8-7-3" d="m35.36637,66.90847l30.57873,0"/>
   <g id="g4804">
    <ellipse stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="0.63745" stroke="#d4aa00" fill="#ffcc00" cx="50.72131" cy="45.46641" rx="1.11165" ry="0.0913" id="path4583"/>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819" d="m45.26635,45.85245l0.05904,0.57814l5.92585,2.17681l0.26171,-0.71255l-6.2466,-2.0424z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815" d="m54.94292,48.5131c0,0 0.12088,0.37747 0.35747,0.45555c0.3007,0.09924 1.00431,-0.09762 1.00431,-0.09762l2.62141,0.87856c0,0 -0.19813,0.74956 -0.54471,1.04125c-0.33533,0.28222 -1.3788,0.59655 -1.3788,0.59655l-1.56604,-1.59442c0,0 -1.01434,0.05221 -1.44689,-0.08677c-0.32649,-0.10491 -0.73195,-0.52063 -0.73195,-0.52063l-1.03502,-0.73701l-7.68034,-2.66875l-0.5086,-0.17776l0.25017,-0.37343l0.51376,0.16072l10.14522,3.12376z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.170317, -0.0572791, -0.0898932, 0.108524, 58.0154, 97.9665)" y="-348.78195" x="256.77636" height="7" width="3" id="rect4817"/>
    </g>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845-6" transform="matrix(-0.192584, 0, 0, 0.122713, 58.4196, 103.417)">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819-7" d="m12.18322,-471.37261l0.30656,4.71135l30.77021,17.73909l1.35896,-5.80668l-32.43573,-16.64376z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815-6" d="m62.4292,-449.69071c0,0 0.62766,3.07603 1.85616,3.71231c1.56141,0.8087 5.21491,-0.79549 5.21491,-0.79549l13.6118,7.15945c0,0 -1.0288,6.10825 -2.82842,8.48528c-1.74121,2.29987 -7.15946,4.86136 -7.15946,4.86136l-8.13173,-12.99309c0,0 -5.26702,0.4255 -7.51301,-0.7071c-1.69533,-0.85492 -3.8007,-4.24264 -3.8007,-4.24264l-5.37437,-6.006l-39.88046,-21.74793l-2.64092,-1.44862l1.29901,-3.04311l2.66774,1.30974l52.67945,25.45584z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.884377, -0.466774, -0.466774, 0.884377, 0, 0)" y="-426.66041" x="209.24988" height="7" width="3" id="rect4817-0"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m53.1141,47.84845l-2.44427,2.27144l-2.44427,-2.27144c0,0 -0.3086,-1.71806 2.42093,-1.80859c2.72952,-0.09053 2.46762,1.80859 2.46762,1.80859z" id="path4953-5-7"  />
    <circle stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="path4775-5" cx="50.66983" cy="51.42678" r="1.0036"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m48.32769,46.60111c0,0 -0.40961,-1.81317 2.34214,-1.79148c2.75176,0.02169 2.34214,1.79148 2.34214,1.79148l-2.34214,3.24267l-2.34214,-3.24267z" id="path4951-0"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m52.24279,45.32124c0,0 0.30497,-2.06081 -1.61711,-2.02827c-1.92207,0.03254 -1.61711,2.02827 -1.61711,2.02827l1.66125,4.57163l1.57296,-4.57163z" id="path4796-2-1"  />
    <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="rect4777-6" width="3.27393" height="0.55221" x="49.03287" y="49.56768" ry="2.25"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m51.4087,46.22149c0.08007,-0.91002 -0.11916,-2.73329 -0.11916,-2.73329c0,0 -0.04786,-0.97617 -0.59578,-0.97617c-0.54792,0 -0.59578,0.97617 -0.59578,0.97617c0,0 -0.19283,1.82305 -0.11916,2.73329c0.09094,1.12352 0.69099,3.34619 0.69099,3.34619c0,0 0.63992,-2.22157 0.73887,-3.34619z" id="path4779-1-3"  />
   </g>

   <path stroke-width="1px" stroke="#bc8810" fill="none"   id="path5604-4" d="m35.28212,69.31364l30.79703,0l-0.13618,-2.7166l-30.54048,0l-0.12036,2.71661z"/>
   <g id="g11992-8">
    <g id="g10152-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 126.929, 105.66)" id="g6367-97"/>
   <g id="g11992-9-9">
    <g id="g10152-1-4"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 88.5928, 107.677)" id="g6367-8-8"/>
   <g id="g11992-97-09">
    <g id="g10152-14-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 72.7379, 116.106)" id="g6367-2-7"/>
   <g id="g11992-3-3">
    <g id="g10152-6-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -19.267, 104.546)" id="g6367-0-6"/>
   <g id="g11992-9-0-2">
    <g id="g10152-1-2-2"/>
   </g>print
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -57.6027, 106.563)" id="g6367-8-3-9"/>
   <g id="g11992-97-7-2">
    <g id="g10152-14-9-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -73.4576, 114.992)" id="g6367-2-9-5"/>
   <g id="g11992-4-9">
    <g id="g10152-7-6"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 12.2375, 110.303)" id="g6367-9-2"/>
   <g id="g11992-9-5-0">
    <g id="g10152-1-5-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -26.0982, 112.32)" id="g6367-8-5-7"/>
   <g id="g11992-97-0-2">
    <g id="g10152-14-8-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -41.9532, 120.749)" id="g6367-2-5-9"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 147.946, 116.368)" id="g4635-0-6-0"/>
   <g stroke="#040420" transform="matrix(0.0301842, 0, 0, 0.0190199, 17.1102, 112.99)" id="g4807-5-1">
    <g stroke="#040420" id="g4635-07-8"/>
   </g>
  </g>
 </g>
</svg>
    '''
    percent=13.3333
    delay=2

  else:
    rank='''
<svg 
width="100" 
height="100"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cc="http://creativecommons.org/ns#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:svg="http://www.w3.org/2000/svg"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
version="1.0"> 
<defs id="defs4">
  <clipPath id="clip">
   <path id="path10" d="m0,-200l0,800l300,0l0,-800l-300,0z" />
  </clipPath>
  <polygon id="star" transform="scale(53)" points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 "/>
  <clipPath id="clip-4">
   <path  d="m0,-200l0,800l300,0l0,-800l-300,0z" id="path10-7"/>
  </clipPath>
  <polygon points="-0.95105652,-0.30901699 0.95105652,-0.30901699 -0.58778525,0.80901699 0,-1 0.58778525,0.80901699 " transform="scale(53)" id="star-6"/>
 </defs>
 <metadata id="metadata7">image/svg+xml</metadata>
 <g>
  <title>Layer 1</title>
  <g id="layer1"  >
   <g id="g4918">
    <path stroke-width="1px" fill="#cccccc" d="m35.42961,68.79824l30.55677,0l-0.0766,-1.71798l-30.39592,0l-0.08426,1.71798z" id="path5606"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.48264,67.42386l30.40161,0" id="path5692-5"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.46562,67.76746l30.43566,0" id="path5692-1-5"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.45711,68.11105l30.45268,0" id="path5692-9-9"  />
    <path stroke-width="1px" stroke="#999999" fill="none" d="m35.44008,68.45465l30.4697,0" id="path5692-3-8"  />
    <path stroke-width="1px" stroke="#666666" fill="none" d="m35.42961,68.79824l30.55677,0l-0.0766,-1.71798l-30.39592,0l-0.08426,1.71798z" id="path5606-8"  />
   </g>
   <g id="g11992">
    <g id="g10152"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 185.477, 106.48)" id="g6367"/>
   <g id="g11992-9">
    <g id="g10152-1"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 147.141, 108.497)" id="g6367-8"/>
   <g id="g11992-97">
    <g id="g10152-14"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 131.286, 116.926)" id="g6367-2"/>
   <g transform="matrix(0.382676, 0, 0, 0.244527, 23.4525, 66.0121)" id="g4891">
    <path stroke-miterlimit="4" stroke-width="1.06667" fill-rule="evenodd" fill="#cecdb6"   id="path14311" d="m110.65027,31.87537l-5.71963,-177.41129l-33.78037,-25.08874l-33.93347,25.08874l-5.56653,177.41127l79,0.00002z"/>
    <g id="g62591">
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#bc8810"  d="m83.60344,-143.27361a12.54946,12.54946 0 0 1 -12.54946,12.54947a12.54946,12.54946 0 0 1 -12.54946,-12.54947a12.54946,12.54946 0 0 1 12.54946,-12.54946a12.54946,12.54946 0 0 1 12.54946,12.54946z" id="circle62593"/>
     <path stroke-miterlimit="4" stroke-linejoin="round" fill="#fddd10"  d="m81.72102,-143.27361a10.66704,10.66704 0 0 1 -10.66704,10.66705a10.66704,10.66704 0 0 1 -10.66704,-10.66705a10.66704,10.66704 0 0 1 10.66704,-10.66704a10.66704,10.66704 0 0 1 10.66704,10.66704z" id="circle62595"/>
     <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-width="0.7" fill-rule="nonzero" fill="#dbb110" clip-rule="nonzero"  id="path62597" d="m71.05509,-155.29494c-3.15262,-0.00039 -6.27327,1.28938 -8.50285,3.51849c-2.22958,2.22913 -3.52045,5.35019 -3.5207,8.50284c0.00025,3.15267 1.29112,6.27372 3.5207,8.50284c2.22958,2.22911 5.35023,3.51889 8.50285,3.5185c3.15231,-0.00025 6.27166,-1.29174 8.50062,-3.52071c2.22896,-2.22896 3.52046,-5.3483 3.52071,-8.50063c-0.00025,-3.15231 -1.29175,-6.27165 -3.52071,-8.50062c-2.22896,-2.22896 -5.34831,-3.52046 -8.50062,-3.52071zm0,0.79272c2.93447,0.00022 5.86314,1.21537 7.9382,3.29041c2.07505,2.07506 3.29018,5.00373 3.29042,7.9382c-0.00023,2.93449 -1.21537,5.86316 -3.29042,7.93821c-2.07506,2.07505 -5.00372,3.29019 -7.9382,3.29041c-2.93499,0.00038 -5.86496,-1.21318 -7.94042,-3.2882c-2.07544,-2.07501 -3.29019,-5.00548 -3.29042,-7.94042c0.00024,-2.93492 1.21498,-5.8654 3.29042,-7.94041c2.07546,-2.07502 5.00543,-3.28858 7.94042,-3.2882z"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.50255" stroke="#b3b3b3" fill="none"  d="m71.15027,-170.62466l-33.93347,25.08874l-5.56653,177.41127l79,0.00002l-5.71962,-177.41129l-33.78038,-25.08874z" id="path5037" />
   </g>
   <g id="g11992-3">
    <g id="g10152-6"/>
   </g>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950" d="m40.40915,36.06387l0,0c-1.3399,0 -2.35628,0.64585 -2.41858,1.44615l-2.50496,32.1769c-0.0623,0.8003 1.07869,1.44615 2.41858,1.44615l12.7758,0l12.7758,0c1.3399,0 2.48088,-0.64585 2.41858,-1.44615l-2.50496,-32.1769c-0.0623,-0.8003 -1.07869,-1.44615 -2.41858,-1.44615l0,0l-10.27084,0l-10.27084,0z"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 135.878, 114.233)" id="g4807">
    <g id="g4635"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.37571,-3972.23236l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.38211,-3910.33337l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5" />
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 39.281, 105.365)" id="g6367-0"/>
   <path stroke-dashoffset="0" stroke-miterlimit="4" stroke-linejoin="round" stroke-linecap="round" stroke-width="4.86623" fill="none"   id="path4950-7" d="m40.45271,36.03257l0,0c-1.3399,0 -2.35628,0.64585 -2.41858,1.44615l-2.50496,32.1769c-0.0623,0.8003 1.07869,1.44615 2.41858,1.44615l12.7758,0l12.7758,0c1.3399,0 2.48088,-0.64585 2.41858,-1.44615l-2.50496,-32.1769c-0.0623,-0.8003 -1.07869,-1.44615 -2.41858,-1.44615l0,0l-10.27084,0l-10.27084,0z"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 135.922, 114.202)" id="g4807-3">
    <g id="g4635-0"/>
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.37571,-3972.23236l0,48.95159l120.454,-81.22015l121.0256,81.60664l0,-48.95156l-121.0256,-80.84161l-120.454,80.45509z" id="path4952-9-9" />
    <path stroke-miterlimit="4" stroke-width="0.62428" stroke="#800000" fill-rule="evenodd" fill="#aa0000"  d="m-2944.38211,-3910.33337l0.0001,48.95159l120.4539,-81.22015l121.0256,81.60664l0,-48.95157l-121.0256,-80.8416l-120.454,80.45509z" id="path4952-9-5-2" />
   </g>
   <g id="g11992-9-0">
    <g id="g10152-1-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 0.945297, 107.382)" id="g6367-8-3"/>
   <g id="g11992-97-7">
    <g id="g10152-14-9"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -14.9096, 115.812)" id="g6367-2-9"/>
   <path stroke-miterlimit="4" stroke="#030315" fill="#040420"   id="path5943" d="m35.17549,71.07172l31.00746,0l-1.84986,-34.97454l-27.36634,0l-1.79126,34.97454z"/>
   <g id="g11992-4">
    <g id="g10152-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 70.7855, 111.123)" id="g6367-9"/>
   <g id="g11992-9-5">
    <g id="g10152-1-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 32.4498, 113.14)" id="g6367-8-5"/>
   <g id="g11992-97-0">
    <g id="g10152-14-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 16.5948, 121.569)" id="g6367-2-5"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 206.494, 117.188)" id="g4635-0-6"/>
   <g stroke="#040420" transform="matrix(0.0301842, 0, 0, 0.0190199, 75.6582, 113.81)" id="g4807-5">
    <g stroke="#040420" id="g4635-07"/>
   </g>
   <g id="g5169-7">
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m50.7563,39.9035l-3.70248,1.54925l0,0.88967l3.70248,-1.54925l3.70248,1.54925l0.00001,-0.88967l-3.70249,-1.54925z" id="path5142-5"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#000000" fill="#aa0000" d="m50.7563,38.12416l-3.70248,1.54925l0,0.88967l3.70248,-1.54925l3.70248,1.54925l0.00001,-0.88967l-3.70249,-1.54925z" id="path5142-9-3"  />
   </g>
   <path stroke-width="1px" fill="#ffcc00"   id="path5604" d="m35.28212,69.31364l30.79703,0l-0.13618,-2.7166l-30.54048,0l-0.12036,2.71661z"/>
   <path stroke-miterlimit="4" stroke-width="3" stroke="#800000" fill="none"   id="path5692-6" d="m35.33026,67.93926l30.669,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-1-3" d="m35.35434,68.28285l30.65696,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-9-8" d="m35.31823,68.62645l30.71715,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-3-6" d="m35.33026,68.97004l30.72317,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-1-3-1" d="m35.39045,67.25206l30.58475,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-9-8-7" d="m35.3423,67.59566l30.64493,0"/>
   <path stroke-width="1px" stroke="#dbb110" fill="none"   id="path5692-9-8-7-3" d="m35.36637,66.90847l30.57873,0"/>
   <g id="g4804">
    <ellipse stroke-dashoffset="0" stroke-miterlimit="4" stroke-width="0.63745" stroke="#d4aa00" fill="#ffcc00" cx="50.72131" cy="45.46641" rx="1.11165" ry="0.0913" id="path4583"/>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819" d="m45.26635,45.85245l0.05904,0.57814l5.92585,2.17681l0.26171,-0.71255l-6.2466,-2.0424z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815" d="m54.94292,48.5131c0,0 0.12088,0.37747 0.35747,0.45555c0.3007,0.09924 1.00431,-0.09762 1.00431,-0.09762l2.62141,0.87856c0,0 -0.19813,0.74956 -0.54471,1.04125c-0.33533,0.28222 -1.3788,0.59655 -1.3788,0.59655l-1.56604,-1.59442c0,0 -1.01434,0.05221 -1.44689,-0.08677c-0.32649,-0.10491 -0.73195,-0.52063 -0.73195,-0.52063l-1.03502,-0.73701l-7.68034,-2.66875l-0.5086,-0.17776l0.25017,-0.37343l0.51376,0.16072l10.14522,3.12376z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.170317, -0.0572791, -0.0898932, 0.108524, 58.0154, 97.9665)" y="-348.78195" x="256.77636" height="7" width="3" id="rect4817"/>
    </g>
    <g stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" id="g4845-6" transform="matrix(-0.192584, 0, 0, 0.122713, 58.4196, 103.417)">
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"  id="path4819-7" d="m12.18322,-471.37261l0.30656,4.71135l30.77021,17.73909l1.35896,-5.80668l-32.43573,-16.64376z"/>
     <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00"   id="path4815-6" d="m62.4292,-449.69071c0,0 0.62766,3.07603 1.85616,3.71231c1.56141,0.8087 5.21491,-0.79549 5.21491,-0.79549l13.6118,7.15945c0,0 -1.0288,6.10825 -2.82842,8.48528c-1.74121,2.29987 -7.15946,4.86136 -7.15946,4.86136l-8.13173,-12.99309c0,0 -5.26702,0.4255 -7.51301,-0.7071c-1.69533,-0.85492 -3.8007,-4.24264 -3.8007,-4.24264l-5.37437,-6.006l-39.88046,-21.74793l-2.64092,-1.44862l1.29901,-3.04311l2.66774,1.30974l52.67945,25.45584z"/>
     <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" ry="1.5" transform="matrix(-0.884377, -0.466774, -0.466774, 0.884377, 0, 0)" y="-426.66041" x="209.24988" height="7" width="3" id="rect4817-0"/>
    </g>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m53.1141,47.84845l-2.44427,2.27144l-2.44427,-2.27144c0,0 -0.3086,-1.71806 2.42093,-1.80859c2.72952,-0.09053 2.46762,1.80859 2.46762,1.80859z" id="path4953-5-7"  />
    <circle stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="path4775-5" cx="50.66983" cy="51.42678" r="1.0036"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m48.32769,46.60111c0,0 -0.40961,-1.81317 2.34214,-1.79148c2.75176,0.02169 2.34214,1.79148 2.34214,1.79148l-2.34214,3.24267l-2.34214,-3.24267z" id="path4951-0"  />
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m52.24279,45.32124c0,0 0.30497,-2.06081 -1.61711,-2.02827c-1.92207,0.03254 -1.61711,2.02827 -1.61711,2.02827l1.66125,4.57163l1.57296,-4.57163z" id="path4796-2-1"  />
    <rect stroke-dashoffset="0" stroke-miterlimit="4" stroke-linecap="square" stroke-width="0.5" stroke="#040420" fill-rule="nonzero" fill="#ffcc00" id="rect4777-6" width="3.27393" height="0.55221" x="49.03287" y="49.56768" ry="2.25"/>
    <path stroke-miterlimit="4" stroke-width="0.5" stroke="#040420" fill="#ffcc00" d="m51.4087,46.22149c0.08007,-0.91002 -0.11916,-2.73329 -0.11916,-2.73329c0,0 -0.04786,-0.97617 -0.59578,-0.97617c-0.54792,0 -0.59578,0.97617 -0.59578,0.97617c0,0 -0.19283,1.82305 -0.11916,2.73329c0.09094,1.12352 0.69099,3.34619 0.69099,3.34619c0,0 0.63992,-2.22157 0.73887,-3.34619z" id="path4779-1-3"  />
   </g>

   <path stroke-width="1px" stroke="#bc8810" fill="none"   id="path5604-4" d="m35.28212,69.31364l30.79703,0l-0.13618,-2.7166l-30.54048,0l-0.12036,2.71661z"/>
   <g id="g11992-8">
    <g id="g10152-5"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 126.929, 105.66)" id="g6367-97"/>
   <g id="g11992-9-9">
    <g id="g10152-1-4"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 88.5928, 107.677)" id="g6367-8-8"/>
   <g id="g11992-97-09">
    <g id="g10152-14-7"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 72.7379, 116.106)" id="g6367-2-7"/>
   <g id="g11992-3-3">
    <g id="g10152-6-8"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -19.267, 104.546)" id="g6367-0-6"/>
   <g id="g11992-9-0-2">
    <g id="g10152-1-2-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -57.6027, 106.563)" id="g6367-8-3-9"/>
   <g id="g11992-97-7-2">
    <g id="g10152-14-9-2"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -73.4576, 114.992)" id="g6367-2-9-5"/>
   <g id="g11992-4-9">
    <g id="g10152-7-6"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, 12.2375, 110.303)" id="g6367-9-2"/>
   <g id="g11992-9-5-0">
    <g id="g10152-1-5-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -26.0982, 112.32)" id="g6367-8-5-7"/>
   <g id="g11992-97-0-2">
    <g id="g10152-14-8-0"/>
   </g>
   <g fill="#ffcc00" transform="matrix(0.0501599, 0, 0, 0.019804, -41.9532, 120.749)" id="g6367-2-5-9"/>
   <g transform="matrix(0.0301842, 0, 0, 0.0190199, 147.946, 116.368)" id="g4635-0-6-0"/>
   <g stroke="#040420" transform="matrix(0.0301842, 0, 0, 0.0190199, 17.1102, 112.99)" id="g4807-5-1">
    <g stroke="#040420" id="g4635-07-8"/>
   </g>
  </g>
 </g>
</svg>

    '''
    percent=0
    delay=0

  return rank,percent,delay


def get_full(rank, percent, delay, name,country, position):
  endl="th"

  if position==1:
    endl="st"
  elif position==2:
    endl="nd"
  elif position==3:
    endl="rd"
  

  full_svg=f'''
    <svg
      width="610"
      height="235"
      viewBox="0 0 610 235"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      
        <svg
          x="0"
          y="0"
          width="205"
          height="205"
          viewBox="0 0 110 110"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <rect
            x="0.5"
            y="0.5"
            rx="4.5"
            width="200"
            height="200"
            stroke="#e1e4e8"
            fill="#FFF"
            stroke-opacity="0"
            fill-opacity="1"
          />
          
{rank}  




  
          <text x="50%" y="18" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji" font-weight="bold" font-size="8" fill="#000">{name}</text>
          <text x="50%" y="85" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji" font-weight="bold" font-size="7" fill="#666">Position in {country}</text>
          <text x="50%" y="97" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji" font-weight="bold" font-size="10" fill="#666"> {position}<tspan font-size="6" dy="-2">{endl}</tspan></text>

          
    <style>
    @keyframes MultiLanguageRankAnimation {{
      from {{
        width: 0px;
      }}
      to {{
        width: {percent}px;
      }}
    }}
    #MultiLanguage-rank-progress{{
      animation: MultiLanguageRankAnimation {delay}s forwards ease-in-out;
    }}
    </style>
    <rect
      x="15"
      y="101"
      rx="1"
      width="80"
      height="3.2"
      opacity="0.3"
      fill="#0366d6"
    />
    <rect
      id="MultiLanguage-rank-progress"
      x="15"
      y="101"
      rx="1"
      height="3.2"
      fill="#0366d6"
    />
  
        </svg>
        
        <svg
          x="125"
          y="0"
          width="110"
          height="110"
          viewBox="0 0 110 110"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          
  
  
  
        </svg>
        
    </svg>
  '''

  return full_svg


def show_results(svg):
    response = make_response(svg)
    response.headers['Content-Type'] = 'image/svg+xml'
    response.headers['Content-Disposition'] = 'inline; filename=image.svg'

    return response


def wrong_inputs():
    the_rank, the_percent, the_delay = get_individual(305)
    
    svg_content = get_full(the_rank,the_percent, the_delay, "Unknown Username", "Unknown Country", "Unknown")

    return show_results(svg_content)




@app.route('/')
def generate_svg():
    # Extract query parameters
    name = request.args.get('name', 'Unknown Username')
    country = request.args.get('country', 'Unknown Country')



    # Define the countries
    countries = ['afghanistan', 'albania', 'algeria', 'angola', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahrain', 'bangladesh', 'belarus', 'belgium', 'benin', 'bolivia', 'botswana', 'brazil', 'bulgaria', 'burkina_faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'chad', 'chile', 'china', 'colombia', 'congo_brazzaville', 'congo_kinshasa', 'croatia', 'cuba', 'cyprus', 'czech_republic', 'denmark', 'dominican_republic', 'ecuador', 'egypt', 'el_salvador', 'estonia', 'ethiopia', 'finland', 'france', 'gabon', 'germany', 'ghana', 'greece', 'guatemala', 'guinea', 'haiti', 'honduras', 'hong_kong', 'hungary', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'ivory_coast', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'libya', 'lithuania', 'luxembourg', 'macau', 'macedonia', 'malawi', 'malaysia', 'mali', 'malta', 'mauritania', 'mexico', 'moldova', 'morocco', 'mozambique', 'myanmar', 'nepal', 'netherlands', 'new_zealand', 'nicaragua', 'niger', 'nigeria', 'norway', 'oman', 'pakistan', 'palestine', 'panama', 'papua_new_guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saudi_arabia', 'senegal', 'serbia', 'sierra_leone', 'singapore', 'slovakia', 'slovenia', 'somalia', 'south_africa', 'republic_of_korea', 'south_sudan', 'spain', 'sri_lanka', 'sudan', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'the_bahamas', 'togo', 'tunisia', 'turkey', 'turkmenistan', 'uae', 'uganda', 'uk', 'ukraine', 'united_states', 'uruguay', 'uzbekistan', 'venezuela', 'vietnam', 'worldwide', 'yemen', 'zambia', 'zimbabwe']

    long_names = {
      'afghanistan': 'Afghanistan',
      'albania': 'Albania',
      'algeria': 'Algeria',
      'angola': 'Angola',
      'argentina': 'Argentina',
      'armenia': 'Armenia',
      'australia': 'Australia',
      'austria': 'Austria',
      'azerbaijan': 'Azerbaijan',
      'bahrain': 'Bahrain',
      'bangladesh': 'Bangladesh',
      'belarus': 'Belarus',
      'belgium': 'Belgium',
      'benin': 'Benin',
      'bolivia': 'Bolivia',
      'botswana': 'Botswana',
      'brazil': 'Brazil',
      'bulgaria': 'Bulgaria',
      'burkina_faso': 'Burkina Faso',
      'burundi': 'Burundi',
      'cambodia': 'Cambodia',
      'cameroon': 'Cameroon',
      'canada': 'Canada',
      'chad': 'Chad',
      'chile': 'Chile',
      'china': 'China',
      'colombia': 'Colombia',
      'congo_brazzaville': 'Congo (Brazzaville)',
      'congo_kinshasa': 'Congo (Kinshasa)',
      'croatia': 'Croatia',
      'cuba': 'Cuba',
      'cyprus': 'Cyprus',
      'czech_republic': 'Czech Republic',
      'denmark': 'Denmark',
      'dominican_republic': 'Dominican Republic',
      'ecuador': 'Ecuador',
      'egypt': 'Egypt',
      'el_salvador': 'El Salvador',
      'estonia': 'Estonia',
      'ethiopia': 'Ethiopia',
      'finland': 'Finland',
      'france': 'France',
      'gabon': 'Gabon',
      'germany': 'Germany',
      'ghana': 'Ghana',
      'greece': 'Greece',
      'guatemala': 'Guatemala',
      'guinea': 'Guinea',
      'haiti': 'Haiti',
      'honduras': 'Honduras',
      'hong_kong': 'Hong Kong',
      'hungary': 'Hungary',
      'india': 'India',
      'indonesia': 'Indonesia',
      'iran': 'Iran',
      'iraq': 'Iraq',
      'ireland': 'Ireland',
      'israel': 'Israel',
      'italy': 'Italy',
      'ivory_coast': 'Ivory Coast',
      'japan': 'Japan',
      'jordan': 'Jordan',
      'kazakhstan': 'Kazakhstan',
      'kenya': 'Kenya',
      'kyrgyzstan': 'Kyrgyzstan',
      'laos': 'Laos',
      'latvia': 'Latvia',
      'lebanon': 'Lebanon',
      'libya': 'Libya',
      'lithuania': 'Lithuania',
      'luxembourg': 'Luxembourg',
      'macau': 'Macau',
      'macedonia': 'Macedonia',
      'malawi': 'Malawi',
      'malaysia': 'Malaysia',
      'mali': 'Mali',
      'malta': 'Malta',
      'mauritania': 'Mauritania',
      'mexico': 'Mexico',
      'moldova': 'Moldova',
      'morocco': 'Morocco',
      'mozambique': 'Mozambique',
      'myanmar': 'Myanmar',
      'nepal': 'Nepal',
      'netherlands': 'Netherlands',
      'new_zealand': 'New Zealand',
      'nicaragua': 'Nicaragua',
      'niger': 'Niger',
      'nigeria': 'Nigeria',
      'norway': 'Norway',
      'oman': 'Oman',
      'pakistan': 'Pakistan',
      'palestine': 'Palestine',
      'panama': 'Panama',
      'papua_new_guinea': 'Papua New Guinea',
      'paraguay': 'Paraguay',
      'peru': 'Peru',
      'philippines': 'Philippines',
      'poland': 'Poland',
      'portugal': 'Portugal',
      'qatar': 'Qatar',
      'romania': 'Romania',
      'russia': 'Russia',
      'rwanda': 'Rwanda',
      'saudi_arabia': 'Saudi Arabia',
      'senegal': 'Senegal',
      'serbia': 'Serbia',
      'sierra_leone': 'Sierra Leone',
      'singapore': 'Singapore',
      'slovakia': 'Slovakia',
      'slovenia': 'Slovenia',
      'somalia': 'Somalia',
      'south_africa': 'South Africa',
      'republic_of_korea': 'Republic of Korea',
      'south_sudan': 'South Sudan',
      'spain': 'Spain',
      'sri_lanka': 'Sri Lanka',
      'sudan': 'Sudan',
      'sweden': 'Sweden',
      'switzerland': 'Switzerland',
      'syria': 'Syria',
      'taiwan': 'Taiwan',
      'tajikistan': 'Tajikistan',
      'tanzania': 'Tanzania',
      'thailand': 'Thailand',
      'the_bahamas': 'The Bahamas',
      'togo': 'Togo',
      'tunisia': 'Tunisia',
      'turkey': 'Turkey',
      'turkmenistan': 'Turkmenistan',
      'uae': 'UAE',
      'uganda': 'Uganda',
      'uk': 'UK',
      'ukraine': 'Ukraine',
      'united_states': 'United States',
      'uruguay': 'Uruguay',
      'uzbekistan': 'Uzbekistan',
      'venezuela': 'Venezuela',
      'vietnam': 'Vietnam',
      'worldwide': 'Worldwide',
      'yemen': 'Yemen',
      'zambia': 'Zambia',
      'zimbabwe': 'Zimbabwe'
    }

    if country not in countries:
        # non-existing country!
        return wrong_inputs()

    if name:
      pass
    else:
      # username was not passed!
      return wrong_inputs()


    # Fetch the json from the server
    response = req.get(f"https://committers.top/rank_only/{country}.json")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        result_server = response.json()
        
        # Extract the "user" list from the JSON data
      
        # user => contains the public without contribution
        # user_public => public with contribution
        # user_private => private+public without contribution
      
        users = result_server.get("user_private", [])
        
        
    else:
        return wrong_inputs()

    
        
    # Find the index of "username" in the list
    user_index = users.index(f"{name}") if f"{name}" in users else -1
    
    # If "username" is found
    if user_index != -1:
        position=user_index+1
    else:
        return wrong_inputs()


    the_rank, the_percent, the_delay = get_individual(position)
    

    svg_content = get_full(the_rank,the_percent, the_delay, name, long_names[country], position)

    return show_results(svg_content)



if __name__ == "__main__":
    app.run(debug=True) #, port=5000, host="0.0.0.0"
