"""
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the array.

Return the number of possible array that can be printed as a string s using the mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
Example 4:

Input: s = "2020", k = 30
Output: 1
Explanation: The only possible array is [20,20]. [2020] is invalid because 2020 > 30. [2,020] is ivalid because 020 contains leading zeros.
Example 5:

Input: s = "1234567890", k = 90
Output: 34
 

Constraints:

1 <= s.length <= 10^5.
s consists of only digits and doesn't contain leading zeros.
1 <= k <= 10^9.
"""

from functools import lru_cache
import sys
sys.setrecursionlimit(10**9) 
class Solution:
    def numberOfArrays(self, string: str, k: int) -> int:
        def valid(string):
            if len(string) >= len_k:
                return False
            return str(int(string)) == string and 1 <= int(string) <= k

        @lru_cache(None)
        def dfs(string):
            if not string:
                return 0
            res = valid(string)
            for i in range(1, len_k):
                pre = string[:i]
                if valid(pre):
                    res = (res + dfs(string[i:])) % M
            return res % M

        len_k = len(str(k)) + 1
        M = 10**9 + 7
        return dfs(string)


class Solution:
    def numberOfArrays(self, string: str, k: int) -> int:
        def valid(string):
            if len(string) >= len_k:
                return False
            return str(int(string)) == string and 1 <= int(string) <= k

        def dfs(string):
            if string in memo:
                return memo[string]
            if not string:
                return 0
            res = valid(string)
            for i in range(1, len_k):
                pre = string[:i]
                if valid(pre):
                    res = (res + dfs(string[i:])) % M
            memo[string] = res % M
            return memo[string]

        memo = dict()
        len_k = len(str(k)) + 1
        M = 10**9 + 7
        return dfs(string)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        def dfs(i, memo):
            if i == len(s): 
                return 1
            if s[i] == '0': 
                return 0
            if i in memo: 
                return memo[i]
            memo[i] = 0
            for j in range(i, len(s)):
                if int(s[i: j + 1]) > k:
                    break
                memo[i] += dfs(j + 1, memo)    
            return memo[i]    
        return dfs(0, {}) % (10 ** 9 + 7) 


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        def valid(string):
            return str(int(string)) == string and 1 <= int(string) <= k

        length = len(s)
        len_k = len(str(k))
        dp = [0]*(length + 1)
        dp[0] = 1
        dp[1] = 1
        M = 10**9 + 7
        for i in range(1, length):
            for j in range(len_k):
                if i-j >= 0 and valid(s[i-j:i+1]):
                    dp[i+1] += dp[i-j]
        return dp[-1] % M


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        l=len(str(k))
        dp = [0]*(len(s)+l) #+l to avoid messy condition checks for last l elements
        dp[-l]=1    #when we select string till last element
        for i in range(len(s)-1,-1,-1):
            #no number starting from 0 is allowed, so skip it
            if s[i]=='0': 
                continue
            #number starting from index i and having length from 1 to l-1,a s they all are valid
            for j in range(i,i+l-1): #他这里没有跳出，所以一直加到i+l-1位的所有dp组合
                dp[i]+=dp[j+1]
            #if length is same then check for validity
            if i+l-1<len(s) and int(s[i:i+l])<=k:
                dp[i]+=dp[i+l]
            dp[i]%=1000000007
        return dp[0]

        
S = Solution()
# string = "1000"
# k = 10000
# print(S.numberOfArrays(string, k))
# string = "1000"
# k = 10
# print(S.numberOfArrays(string, k))
# string = "1317"
# k = 2000
# print(S.numberOfArrays(string, k))
# string = "2020"
# k = 30
# print(S.numberOfArrays(string, k))
# string = "1234567890"
# k = 90
# print(S.numberOfArrays(string, k))
string = "2553462832281151811513004352253111"
k = 456
print(S.numberOfArrays(string, k))
string =  "66153185069117926039227476645815448036422959939965573665332831839194857039876470233233526437547808882949173684843372078392754315996957168102754450371104920703432442530694454458553024201285661092271018337915959684950885087204914301269398966261820517564295168294607290537125573578345412239368314955746400796703225919840835335422503676455324943557991838639460042007398404687626771767355314017437674846086233273693475852221715521633102480842574443861776408075612261384384510033035024845796449274732166579828088929153756445582610968271471369961794231498069210721601741886471214754432812704360667555226856884136370565731333266543387651530688244609916526962034364730934245347060670432613364390744656613153551693106048121564428001292157235028311633624455278158093073470625559619365823301720636355511210319788667605453673599064455167395672850882728502903057002873981165101314173446933226175264245513323373867123669881730949050950455948410101193270203135836782285220117732177395075264944998039944251774285793483479450737012919582515973955649919880766933360702975161069225348574286745272857132174493170411549403501364314742824018819676987314777214423348225221610319828004158149878309048283177633332071358802544710602486289413882469235615476309912646945147233049293496768262018042209491771772576754236423466576310887385923533309351992430393208759330117802263372778024832115993895679170238777102297212844290504040310295395527291690262142060172416843872603429662208771168181878921434993134262740496224329008840227014264755768808209552494484960539042194649575681461569519730918206752021753030410560678643549765680419736763455480202934188253342586047491103911666225415540119374187462448010218624012163882949473250930604480248767935129920283107454225112642205797649152276683871117647362080765364562263821108853681821864643120469416005963180775547299557012559614498607492963910503928954666482602322716359784298132614389896491319325875574340198923713415933654423186112115128397537183319734690406274574410655255458821350981444479129346354700043041536174604003695280893800584413411262851415166439310223850189601366836038084687028523871235045580882316242545508228663895525071420716105014651368379674864512561593620105364605407896588390602184427145725055709186011104744545127154748711740935112208173575716471446188324914679475782621018273079606614336528458531507133801250244637361907199244462222014314024725523472051478004930706659035805353541502817812713318788639169466676651680681106474986339590039208287884845078833463589041930471945965427028761702175310809241377626024597491440975578230849829528649388677244364913810930555770481562290358241555112122648722219659207943162852269117779863085453710292797835998904878344789981904653986235699926046683250979794516724706370733136060409034930319363483890979286326279855485007247779724994483574606010568477610926399153471160180154137650307559465712570879016390454236393261521961239542791882196158097816886743357544634547898426672619241636535357502050305862201448381405828757509868392567904418221001411950843993632693237484895387150156341366130265956541446495164772699083375338549755837503412007409630806216760674529444794211132617625257758665849878179671358048430422083316410595290580913330173254669644903301829228188794815327794498886835617443653458277243737713085281244797613231363641348133563928854761113874385228634865040237413969786375122899398420324721887335698694200061275593340771842675723162131774297261687388710837259695474559624844393762250266757424715832048680263857232593361265296130864024158791775725797222963214914649320289965639585662563228136376813117742654621135933567150270331819287437776974792407525327741162527528230699468856553277747298932733559242393484538554784712422129217172765278352388978472000848983322077760185377880507087087075601845701793257735115974724328561894709382598052613784884925250806427419908846384642879511158826683820850455733219985990939152539424770561068822564272852910974404437765925786732507012868737662326269403041227106739306974329943027484122219810892123751396557649252452635588408541612457552072898722899801970028007284064044005236304677604157730205347515224254039432521799308224902077817402907023289430135139489200261658338784307335740641247447957857610052980760371410007948765380952989793245630029603125989673050741231206654862869930187934747068081349176075330429055524852445524399431867761484387845095132415936343708542610158670650276510747434696449533399939412752947619103533986471726428117660664677859378604293088878494327970341075008860237304262802864841167230400301375624634171450483783540926623505920634486484039144370530312119302537435771899572710975361835267570075533710695046488217870379447303552341299316002545640593199098094783859007169858981619958164767613666336189840402632884795639369643884175724029013661890555347370664507119371660119537386822402211858904624122362142981658361082607496476356970875055552728846605586409210045850757053269528551063363490638939058332332424714632882159254205342604498084771854620258696372224860113619942828768484770081604933510439291101739456563956527723748841268018764969608862774348734669445488173729111077234132919513719044022797767363386577166697386750634483694039798280786690388443090395607514398423000720412954791277908233913509636571879859175495584446450017046704065561654874316274253057577416564036748523078232783205069734583104376781143569858875452808595872867067111745844529400480671514293055367561842416481091090242246753893585884732554223893180055412651795241311083054536112561520466055858360622502427628240060215319329685490023741805031519664274168618931782052426437266434434538734398113301868329052523657154162841207089739976616100256062990153734505332145214964957168751139618447188694256129070093483849838512197977920014354542922715705435428397749286828541331963489371817748933724984780467530460947423247446331985630900111113644112596264315442503441007457844463440646404385864011615889767751104851093588094543263636507765465253730061084168341021879573584424898737388993250189639731428251030679296082873058730112572713002126317184020512579735028404771825569355265228397405480701390914271255160120010668433661739931661818413665180434190789318778699850448375627001390870056183911814035276193494141035989960597001733557126351341375558023172642822771596939332715475075217024331832672942008515979997305323917174672438867082454303230436517514736157867292159953516736716529737929829004811180828391020286312247198409001391572933125347144339254164782379583639481021052494510015152995473432048463993511323527916271411577043839133281917896336502001010869102551562767513327577042753338162588546156205901664597134719182865317449576372299322976239745992932947561603617082032025564805553414205812372112740793535066512274141006993269512588268934498791511095449473512616315394846782798794736362286034592703180014602234987377061724839441064972923376310790758236231071654091012166307758763565344392700544813387524915836359079210513775397392073662159491191778085009727266873582455457572094920552935120558408113058584223268660381201287062116537175655328779368207153274932942255306476318498479099609836965059410142067435841219046156525380791362786839500830435918686221387943374141082931119865414714825901443333581096457141406454980370343703806569683360952950427127869709649682311441881201669623055750740293972408336827172212819261495015310670455906797410275042650820048363455002642214060434693744883385603188895052937598925572402433966227322274907534555024267534028211622439056767273265229931351219304355296785332570874457313085827313999208064307588625118707539536100058616454799997839883118108590732494741496616894608786857654517704238470726002780500812530411833124731557753859258070422103772847914827889016305131222432545871727211572475324536599485572221692423442980993698881291453023333113004702728962431413230157205199732961851294021028269881250799983615578985144119533930119769450716503017319517744755468645766888276772092057477521968417528640453197262369001492331670601842342934474517225200055462327205251334468989260094818110084071197354993096178527369779836504273602729877301209009091348419712857383477197585388384976033846446772159947622596472544676611254269223777237360049923415764764871979169833514095279708597968287319285831399730856781928839017940155633862741846816143459627779118669245307347856275214515406870043098246803556346842531357132719697502907691747639781876957198652617795471707131013691692266573973864150717632513104280120897747349402760288164958686971785244725368489288937142258623761919083836033746471874324022378823515898132526301466626633477170388121250831590791002220116084137455686622565816875530192666577756751653732221420009605312438545508279900082224729279685393791547515591368307655864067512712613852490342862169375187656907241527976806700159905828202180299122659153976218592708592789120209113849124145313111854457100475793351450864985478821847903310100074510237975395613125746311700416960939062325396233609341152014937406237633801450959507268"
k = 1000000000
print(S.numberOfArrays(string, k))