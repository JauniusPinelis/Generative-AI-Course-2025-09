**Generatyviojo DI technologija: sistemų ir agentų kūrimas (be programavimo)**

## **Įvadas**

Generatyvusis DI yra plati technologija, kuri jau pakeitė pasaulį ir vis dar jį keičia.
Tikriausiai visi esame naudojęsi ir likę sužavėti „ChatGPT“, tačiau generatyvusis DI – kur kas daugiau nei vien ši paslauga.
Jis keičia daugelį sričių ir kartais atrodo kaip grėsmė mūsų darbui – net iki galimo žmonių pakeitimo darbo vietoje.

Vis dėlto kviečiu į tai žvelgti ne kaip į grėsmę, o kaip į galimybę.
Daugelis mano kolegų programuotojų jaučiasi apimti nerimo, matydami tiek daug puikių įrankių, galinčių juos pakeisti, tačiau dažnai pamiršta, kiek naujų galimybių atsiveria.
IT industrija kelerius metus stagnavo, o tik dabar įmonės pradeda kurti DI agentus ir integruoti juos į savo procesus.
Matome vis daugiau „DI startuolių“, į kuriuos plūsta investicijos, ir augančią „DI inžinierių“ paklausą –
specialistų, galinčių integruoti generatyviojo DI technologijas į esamas sistemas ir procesus.

Tai ne pirmasis kursas, tačiau šį kursą išskiria tai, kad mes praleidžiame „Python programavimo“ mokymąsi ir tiesiogiai fokusuojamės į generatyviojo DI sąvokas bei veikiančių prototipų ir produktų kūrimą.
Naudosime ne tik automatizavimo platformas, bet ir „agentinio programavimo“ įrankius, tokius kaip Cursor ir Claude Code.
Programavimo patirtis naudinga, bet nebūtina – pagrindinį kodą paliksime įrankiams, o aš išmokysiu „agentinio programavimo“ technikų, leidžiančių sukurti ir įdiegti minimalius produktus be programavimo žinių.

Kurso pabaigoje suprasite daugumą naujausių generatyviojo DI krypčių ir technikų.
Kursas intensyvus ir techninis, tačiau jis padės perprasti, kaip veikia daugelis gamybinių „DI produktų“, ir suteiks patirties, reikalingos pradėti įgyvendinti savo generatyviojo DI idėjas.
Kursas apims daugumą šiuo metu aktualių temų ir „buzzword’ų“:
atvirojo kodo modelių naudojimą, struktūruotą išvestį, įrankių kvietimą (tool calling), derinimą (fine‑tuning), MCP, DI agentus, agentų kūrimo karkasus, halucinacijų valdymo technikas ir kt.

Tikrų generatyviojo DI ekspertų dar nedaug (prisimenate, kad „ChatGPT 3.5“ pasirodė tik prieš maždaug 2,5 metų),
tačiau mokysitės iš (ir kartu su) žmogaus, praktiškai dirbančio su generatyviojo DI technologijomis „Danske Bank“.
Kursą laikysiu praktišku ir dalinsiuosi gerosiomis praktikomis (ir nesėkmėmis), sukauptomis dirbant su generatyviuoju DI profesionaliai.

---

## **1 savaitė: Generatyviojo DI pagrindai**

### **1 diena: Įvadas į generatyvųjį DI**
- Kurso apžvalga, tikslai ir mokymosi kelias
- ChatGPT naudojimas ir praktinės taikymo sritys
- Kas yra didelės apimties kalbos modelis (LLM)
- DI platformos ir ekosistemos supratimas
- Gen‑AI kaip transformuojanti technologija
- LLM pagrindinės sąvokos ir galimybės
- **Praktika:** ChatGPT tyrinėjimas ir promptų (užklausų) eksperimentai

### **2 diena: LLM modeliai ir ekonomika**
- ChatGPT modelių variantai: GPT‑4o, GPT‑4.1, GPT‑4o mini
- Kainodara pagal ženklus (tokenus): įvesties ir išvesties kaštai
- Įrankiai LLM’uose ir jų paskirtis
- Žiniatinklio paieškos įrankių integracija ir galimybės
- Atminties įrankiai ir pokalbių išlaikymas
- **Praktika:** Kaštų skaičiavimo pratimai ir modelių palyginimas

### **3 diena: LLM galimybės ir ribotumai**
- ChatGPT Code Interpreter įrankiai ir duomenų analizė
- Pagrindinės LLM silpnybės
- LLM kaip tikimybių modeliai: kaip jie iš tikro veikia
- Halucinacijos: atpažinimas ir mažinimo strategijos
- Žinių ribos ir mokymo duomenų apribojimai
- Konteksto dydžio apribojimai ir atminties limitai
- **Praktika:** Halucinacijų identifikavimas ir modelių ribų testavimas

### **4 diena: Promptų inžinerijos įvaldymas**
- Pažangios promptų technikos ir gerosios praktikos
- Konteksto valdymas ir pokalbio eiga
- Sisteminės instrukcijos vs vartotojo užklausos
- Vieno pavyzdžio vs kelių pavyzdžių (one‑shot / few‑shot) strategijos
- Mąstymo grandinės (Chain‑of‑Thought) technika sudėtingiems uždaviniams
- Darbas su tekstiniais failais ir dokumentų apdorojimas
- LLM kaštai ir optimizavimo strategijos
- Praktiniai patarimai efektyviam ChatGPT naudojimui
- **Praktika:** Promptų dirbtuvės su realiais scenarijais

---

## **2 savaitė: Alternatyvios DI platformos**

### **1 diena: Google AI Studio ir samprotavimo modeliai**
- Google AI platformos apžvalga ir galimybės
- Įvadas į samprotavimo (reasoning) modelius ir jų taikymą
- Google AI Studio sąsaja ir funkcijos
- Gemini modelių šeima ir jų stiprybės
- Praktinis Google AI Studio tyrinėjimas
- **Praktika:** Kurkite ir testuokite promptus su Google AI Studio

### **2 diena: Išsami LLM platformų apžvalga**
- Anthropic ir Claude LLM šeima
- Claude išskirtinės galimybės ir bendravimo stilius
- xAI „Grok“ platforma ir realaus laiko galimybės
- LLM proxy paslaugos ir jų nauda
- OpenRouter platforma prieigai prie kelių modelių
- **Praktika:** Lyginamoji analizė naudojant skirtingas platformas

### **3 diena: Atvirojo kodo LLM ekosistema**
- Komerciniai vs atvirojo kodo modeliai: privalumai ir trūkumai
- Kodėl LLM yra brangūs ir kas lemia kaštus
- Techniniai reikalavimai modeliams lokaliai paleisti
- Hugging Face ekosistema ir bendruomenės modeliai
- Modelių licencijavimas ir naudojimo teisės
- **Praktika:** Hugging Face modelių saugyklos tyrinėjimas

### **4 diena: Vietinis DI su Ollama**
- Parsisiuntimas ir diegimas iš `https://ollama.com/`
- Atvirojo kodo modelių paleidimas asmeniniame kompiuteryje
- Aparatinės įrangos reikalavimai ir apribojimai
- Verslo taikymo sritys ir panaudojimo atvejai
- Privatumo privalumai dirbant lokaliai
- **Praktika:** Vietinių modelių diegimas ir paleidimas su Ollama

---

## **3 savaitė: Vibe Coding – DI pagrįsta kūrimo praktika**

### **1 diena: Įvadas į Vibe Coding**
- Kas yra Vibe Coding: Andrej Karpathy 2025 m. paradigma
- Kodo generavimas iš natūralios kalbos
- Vibe coding su GitHub Copilot ir Visual Studio Code
- Pagrindinių programų kūrimas naudojant natūralią kalbą
- Derinimas ir klaidų taisymas su DI pagalba
- Esamų programų atnaujinimas naudojant vibe coding
- **Praktika:** Kurkite paprastas programas natūralios kalbos užklausomis

### **2 diena: Vibe Coding įrankiai ir platformos**
- GitHub Copilot: įvadas ir galimybės
- Cursor: DI‑pirmas kodo redaktorius
- Claude Code – pagalbininkas kūrimui
- Gemini CLI – DI integracija komandinei eilutei
- Privalumai ir galimos rizikos IT aplinkoje
- **Praktika:** Praktinis darbas su keliais vibe coding įrankiais

### **3 diena: Įrankiai ir API**
- Pakartojimas: kas yra įrankis generatyviajame DI
- LLM ir sistemų‑su‑sistemomis sąveika
- Įvadas į REST API ir jų vaidmenį
- Kaip DI agentai bendrauja su išorinėmis sistemomis
- **Praktika:** API sąvokų tyrinėjimas praktiniuose pavyzdžiuose

### **4 diena: Praktinis programos kūrimas**
- Projektas: orų prognozės svetainė su vibe coding
- Sistemų analizė ir architektūros planavimas
- Front‑end vs back‑end sąvokos
- Skirtingų sistemos komponentų koordinavimas
- **Praktika:** Baigkite orų programą su DI pagalba

---

## **4 savaitė: Model Context Protocol (MCP)**

### **1 diena: DI kaip paslauga (AI as a Service) revoliucija**
- API sąvokų pakartojimas ir šiuolaikinės taikymo sritys
- Technologija kaip paslauga (TaaS) verslo modeliai
- Programų kūrimas su Lovable.AI platforma
- Builder.AI: pamokos iš industrijos skandalų
- Nocode/low‑code DI kūrimo ateitis
- **Praktika:** Programų kūrimo tyrinėjimas su Lovable.AI

### **2 diena: Model Context Protocol iškilimas**
- Kas yra MCP: Anthropic 2024 m. proveržis
- Kodėl reikia MCP: integracijos problemos sprendimas
- Kaip MCP suteikia įrankius DI sistemoms
- Technologijos tampa „LLM draugiškos“
- Anthropic įtaka DI ekosistemai
- **Praktika:** MCP veikimo supratimas per praktinius pavyzdžius

### **3 diena: MCP įrankių galia**
- Įrankių turgavietė: `https://smithery.ai/`
- Vystymo aplinkų įgalinimas su Gmail MCP
- Context7 MCP – naujausios dokumentacijos prieiga
- Saugumo klausimai ir MCP diegimo spąstai
- **Praktika:** Bazinių MCP įrankių diegimas ir konfigūravimas

### **4 diena: MCP praktikoje**
- Praktinės MCP diegimo dirbtuvės
- Cursor/VSCode įgalinimas su Context7
- Kaip įveikti pasenusių LLM žinių ribas
- Įvadas į Streamlit – greitam programų kūrimui
- Pavyzdinių pokalbių botų kūrimas su Streamlit ir Context7
- **Praktika:** Veikiantis pokalbių botas su Vibe MCP įrankiais

---

## **5 savaitė: RAG – Retrieval Augmented Generation**

### **1 diena: RAG pagrindai**
- Kas yra Retrieval Augmented Generation (RAG)
- Kodėl RAG yra plačiausiai naudojama LLM technika industrijoje
- Konteksto valdymas ir informacijos paieška
- Pagrindiniai RAG įgyvendinimo iššūkiai
- Kaip paversti LLM srities ekspertais naudojant RAG
- **Praktika:** RAG koncepcijos demonstracija ir tyrinėjimas

### **2 diena: Duomenų iššūkiai ir LangChain sprendimai**
- Skirtingi duomenų formatai: txt, md, pdf, html iššūkiai
- Kaip LangChain karkasas sprendžia duomenų sudėtingumą
- Strategijos, kaip suteikti žinias ir duomenis DI
- Kritinė teisingų, aukštos kokybės duomenų svarba
- **Praktika:** Duomenų paruošimo ir formatavimo pratimai

### **3 diena: Duomenų bazės ir vektorinė saugykla**
- Įvadas į duomenų bazių sąvokas
- PostgreSQL diegimas ir paleidimas
- PostgreSQL vartotojo sąsaja vs serverio architektūra
- Reliacinės duomenų bazės supratimas
- Duomenys vs schema: struktūrinės sąvokos
- LLM įterpiniai (embeddings) ir vektorinės DB
- **Praktika:** PostgreSQL diegimas ir sąvokų tyrinėjimas

### **4 diena: Praktinis RAG įgyvendinimas**
- Srities eksperto pokalbių botai su LangChain ir Streamlit
- Skirtingų DI modelių naudojimas LangChain karkase
- Žinių bazių integravimo strategijos
- **Praktika:** Veikianti RAG sistema konkrečiai sričiai

---

## **6 savaitė: DI agentai ir automatizavimas**

### **1 diena: Nocode/Low‑code automatizavimo platformos**
- Įvadas į n8n automatizavimo platformą
- RAG sistemų kūrimas be kodo n8n aplinkoje
- n8n integracijos su įvairiomis paslaugomis ir API
- Vaizdinių darbo eigos (workflow) kūrimas ir valdymas
- **Praktika:** Automatizuotų darbo eigų kūrimas su n8n

### **2 diena: DI agentų era**
- Kas apibrėžia DI agentą
- 2025-ieji: metai, kai DI agentai tampa masiniai
- Kodėl verslui reikia DI agentų konkurenciniam pranašumui
- Auganti „DI inžinierių“ paklausa
- LLM vs DI agentas: skirtumų supratimas
- DI agentai vs DI sistemos: architektūriniai skirtumai
- **Praktika:** Konceptualių DI agentų darbo eigų projektavimas

### **3 diena: OpenAI Agent SDK ir karkasai**
- Įvadas į DI agentų karkasus ir jų būtinybę
- Kodėl reikalingi standartizuoti karkasai
- „Gilaus tyrimo“ (deep research) agentų analizė ir kūrimas su OpenAI SDK
- Agentų architektūra ir projektavimo šablonai
- **Praktika:** Eksperimentai su OpenAI agentų SDK įrankiais

### **4 diena: Duomenų analizės agento praktika**
- PostgreSQL duomenų bazės pakartojimas ir integracija
- Pavyzdinių duomenų bazių atkūrimas ir darbas su jomis
- Streamlit agentai natūraliems kalbos užklausoms į DB
- Išmanių duomenų analizės darbo eigų kūrimas
- **Praktika:** Pilna duomenų analitiko agento sistema

---

## **7 savaitė: Modelių mokymas ir derinimas (fine‑tuning)**

### **1 diena: Modelių mokymo teorija**
- Kodėl mokymas nuo nulio yra itin sudėtingas
- Fine‑tuning kaip praktiška alternatyva
- Kada ir kodėl rinktis fine‑tuning, o kada alternatyvas
- Fine‑tuning vs RAG: tinkamo požiūrio pasirinkimas
- Fine‑tuning iššūkiai
- Baziniai modeliai vs instrukciniai modeliai
- Įvadas į Hugging Face ekosistemą
- **Praktika:** Hugging Face modelių saugyklos tyrinėjimas

### **2 diena: Pasiruošimas fine‑tuning**
- Giluminė Hugging Face platformos analizė
- Duomenų rinkinių svarba ir parinkimas
- Modelių klasifikacijos ir atrankos kriterijai
- Ollama integracija ir jos reikalingumas
- Google Colab sąsiuviniai ir GPU reikalavimai
- **Praktika:** Duomenų rinkinių analizė ir paruošimas

### **3 diena: Fine‑tuning su Unsloth karkasu**
- Fine‑tuning kaip paslauga per OpenAI
- Įvadas į Unsloth karkasą ir jo privalumus
- Unsloth dokumentacijos ir resursų supratimas
- Tinkamo bazinio modelio pasirinkimas fine‑tuningui
- Llama 3.2 derinimas su Unsloth
- Derinto modelio testavimas ir vertinimas
- Modelių paleidimas su Ollama
- **Praktika:** Pilna fine‑tuning darbo eiga su Unsloth

### **4 diena: Praktinis fine‑tuning**
- Duomenų rinkinių modifikavimo ir optimizavimo technikos
- Praktinis darbas su Unsloth karkasu
- Modelių vertinimas ir našumo testavimas
- Naujų modelių įkėlimas į Hugging Face
- **Praktika:** Nuoseklus fine‑tuning projektas nuo A iki Z

---

## **8 savaitė: Multimodalis DI ir pažangios taikymo sritys**

### **1 diena: Kompiuterinė rega ir vaizdų generavimas**
- Multimodalių DI modelių supratimas ir galimybės
- Kompiuterinės regos pagrindai ne programuotojams
- Vaizdų analizė su GPT‑4 Vision
- Vaizdų generavimas su DALL‑E, Midjourney ir alternatyvomis
- Praktiniai verslo pritaikymo atvejai
- Vaizdų analizės programos be kodo
- **Praktika:** Vaizdų analizės ir generavimo darbo eigos

### **2 diena: Balsas ir garso DI**
- Teksto į kalbą (TTS) technologijos
- Kalbos į tekstą (STT) ir transkripcijos paslaugos
- Balso klonavimas ir sintezė
- OpenAI balso modeliai ir galimybės
- ElevenLabs profesionaliam balso generavimui
- Balsu valdomos programos kūrimas
- Garso turinio generavimas įvairiems scenarijams
- **Praktika:** Balsu grįstų programų ir turinio kūrimas

### **3 diena: Video apdorojimas ir generavimas**
- DI pagrįsta video analizė ir supratimas
- Video generavimo įrankiai ir platformos
- Sora, Veo3 ir kitos pažangios video DI platformos
- Automatinis video montavimas ir postprodukcija
- Mokomojo turinio kūrimas su DI pagalba
- Video transkribavimas ir santraukos
- **Praktika:** Video kūrimas ir redagavimas su DI įrankiais

### **4 diena: Pažangi multimodalė integracija**
- Teksto, vaizdo, balso ir video galimybių derinimas
- Išsamių multimodalių DI asistentų kūrimas
- Dokumentų apdorojimas su vizijos modeliais
- Realaus pasaulio multimodalės taikymo sritys
- Ateities tendencijos multimodalaus DI raidoje
- Kurso apibendrinimas ir tolesni žingsniai
- **Praktika:** Integruotas multimodalus DI sprendimas


