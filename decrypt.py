from attacks.crt import CRTAttack
from attacks.wiener_attack import WienerAttack
from attacks.basic_factor import BasicFactorAttack
from attacks.attack import Attack

decrypt_attack_params = {'c':0, 'd':0, 'n':0}
def decrypt(decrypt_attack_params):
    c = decrypt_attack_params['c']
    d = decrypt_attack_params['d']
    n = decrypt_attack_params['n']
    out_int = pow(c, d, n)
    out_hex = hex(out_int)[2:]
    asc = bytes.fromhex(out_hex).decode('utf-8')
    return asc

class DecryptAttack(Attack):
    def __init__(self):
        self.params = decrypt_attack_params
        self.func = decrypt
        self.out = "M"

ATTACKS = [BasicFactorAttack, WienerAttack, CRTAttack, DecryptAttack]

class InvalidKeyError(Exception):
    pass

class Key(object):
    def __init__(self, p=None, q=None, d=None, n=None, c=None, e=None):
        self.p = p
        self.q = q
        self.d = d
        self.n = n
        self.c = c
        self.e = e

    def decide(self):
        args = {}
        for var in self.__dict__.keys():
            if self.__dict__[var]:
                args[var] = self.__dict__[var]
        for attack in ATTACKS:
            temp_attack = attack()
            if temp_attack.should_work(args):
                input_args = {}
                for param in temp_attack.params:
                    input_args[param] = args[param]
                out = temp_attack.func(input_args)
                if out != -1:
                    self.display(out, temp_attack)

    def display(self, out, attack):
        if attack.out == "D":
            if self.c and self.n:
                print(decrypt({'c':self.c, 'd':out, 'n':self.n}))
            else:
                print("Private Key: " + str(out))
        elif attack.out == "M":
            print(out)

e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
c = 225175934161594228135276539151300635650154382949275610703955895454397972800078177010645120694514429238852436900491673897049738868395450588115023690042698618062429449915158642982464013827556037197674747411586501561443167188341892522829441271789447291650951307375998344078663824671416916330711386511022057733100

Key(e=e,n=n,c=c).decide()

e = 3 
c1= 261345950255088824199206969589297492768083568554363001807292202086148198766487319457166401926551545151109098026058996468948583731482236623951529859018133353522151510006730449989443117787242210474753186824315213163862872301057620706372687683778738002221613793950793184020407053794922945550049200005037356171576
n1= 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
c2= 147535246350781145803699087910221608128508531245679654307942476916759248537598403170076106575630165699159010125776778381148067440734881737955254787125295274917003578395507098724379568787243084218395137286419938619988307436493129916091673165202128342184862232497202397084217570750383567539697438549939198300065
n2= 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309 
c3= 633230627388596886579908367739501184580838393691617645602928172655297372371614169085264699618154094108843199162386941382733831426893824086661881305133495694806288896065436554805338983106467014166909503023325865458774387526138478589388919787421461199308731526630536118270660740318460662900203271623078968788197
n3= 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723 

Key(e=e, c=[c1, c2, c3], n=[n1, n2, n3]).decide()

c = 0x58ae101736022f486216e290d39e839e7d02a124f725865ed1b5eea7144a4c40828bd4d14dcea967561477a516ce338f293ca86efc72a272c332c5468ef43ed5d8062152aae9484a50051d71943cf4c3249d8c4b2f6c39680cc75e58125359edd2544e89f54d2e5cbed06bb3ed61e5ca7643ebb7fa04638aa0a0f23955e5b5d9
d = 0x496747c7dceae300e22d5c3fa7fd1242bda36af8bc280f7f5e630271a92cbcbeb7ae04132a00d5fc379274cbce8c353faa891b40d087d7a4559e829e513c97467345adca3aa66550a68889cf930ecdfde706445b3f110c0cb4a81ca66f8630ed003feea59a51dc1d18a7f6301f2817cb53b1fb58b2a5ad163e9f1f9fe463b901
N = 0xb197d3afe713816582ee988b276f635800f728f118f5125de1c7c1e57f2738351de8ac643c118a5480f867b6d8756021911818e470952bd0a5262ed86b4fc4c2b7962cd197a8bd8d8ae3f821ad712a42285db67c85983581c4c39f80dbb21bf700dbd2ae9709f7e307769b5c0e624b661441c1ddb62ef1fe7684bbe61d8a19e7

Key(c=c, d=d, n=N).decide()
