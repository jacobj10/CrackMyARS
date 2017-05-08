from attacks.crt import crt
from attacks.wiener_attack import wiener
from attacks.basic_factor import basic_factor
from attacks.decrypt import decrypt

from utils.key import Key

import gmpy

def test_crt():
    e = 3 
    c1= 261345950255088824199206969589297492768083568554363001807292202086148198766487319457166401926551545151109098026058996468948583731482236623951529859018133353522151510006730449989443117787242210474753186824315213163862872301057620706372687683778738002221613793950793184020407053794922945550049200005037356171576
    n1= 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
    c2= 147535246350781145803699087910221608128508531245679654307942476916759248537598403170076106575630165699159010125776778381148067440734881737955254787125295274917003578395507098724379568787243084218395137286419938619988307436493129916091673165202128342184862232497202397084217570750383567539697438549939198300065
    n2= 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309 
    c3= 633230627388596886579908367739501184580838393691617645602928172655297372371614169085264699618154094108843199162386941382733831426893824086661881305133495694806288896065436554805338983106467014166909503023325865458774387526138478589388919787421461199308731526630536118270660740318460662900203271623078968788197
    n3= 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723 
    out = crt({'e':e, 'c':[c1, c2, c3], 'n':[n1, n2, n3]})
    assert(out == "broadcast_with_small_e_is_killer_90446192802")

def test_wiener():
    e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
    n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
    c = 225175934161594228135276539151300635650154382949275610703955895454397972800078177010645120694514429238852436900491673897049738868395450588115023690042698618062429449915158642982464013827556037197674747411586501561443167188341892522829441271789447291650951307375998344078663824671416916330711386511022057733100
    d = wiener({'e':e, 'n':n})
    out = decrypt({'c':c, 'd':d, 'n':n, 'e':e})
    assert(out == "flag{Are_any_RSA_vals_good_65199450210}")

def test_basic_factor():
    e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
    n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
    c = 225175934161594228135276539151300635650154382949275610703955895454397972800078177010645120694514429238852436900491673897049738868395450588115023690042698618062429449915158642982464013827556037197674747411586501561443167188341892522829441271789447291650951307375998344078663824671416916330711386511022057733100
    d = basic_factor({'e':e, 'n':n})
    out = decrypt({'c':c, 'd':d, 'n':n, 'e':e})
    assert(out == "flag{Are_any_RSA_vals_good_65199450210}")

test_crt()
test_wiener()
test_basic_factor()

x = Key()
x.add_multiple_n_from_file(['tests/publics/key1.pem', 'tests/publics/key2.pem', 'tests/publics/key3.pem'])
x.add_multiple_c_from_file(['tests/ciphertexts/flag1', 'tests/ciphertexts/flag2', 'tests/ciphertexts/flag3'])
print(x.decide())

x = Key()
x.add_pem('tests/sosig/sausage.pem')
x.c_from_file('tests/sosig/flag.enc')
print(x.decide())

x = Key()
x.add_pem('tests/fone/ohofone-50.pem')
x.c_from_file('tests/fone/flag.enc')
print(x.decide())

x = Key()
x.add_pem('tests/Burning_CTF/public-key.pem')
x.c_from_file('tests/Burning_CTF/flag.txt')
print(x.decide())
