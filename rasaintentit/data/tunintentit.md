<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 
<!--- lookup table list for course codes.  --> 
## lookup:courses  <!-- no list to specify lookup table file -->
currencies.txt


## intent:bye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely

## intent:name
- My name is [Alice](name)  <!--- Square brackets contain the value of entity while the text inside the parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)

## intent:startDate
- When does [TIEY4](course) start
- When does [TIEY5](course) start
- When does [TIETA3](course) start
- When does [FILP5A](course) begin
- When does [KKSULUK1](course) begin
- When will [YKYYHT4B](course) begin
- When will [ITIP1](course) begin
- When will [ITIP2](course) begin
- When will [KASA10](course) begin
- When does [PSYP2](course) begin
- When will [KATLAP21](course) start
- When will [BTK2020](course) start
- When will [JOVP1](course) start
- When will [KKSUYTK](course) start
- When is [MTTTP1](course)

## intent:creditsMin
- How many points [TIEY6](course)
- How many credits [OOPE](course)
- How many ECTS [KKENYHT](course)
- How many student credits [MTTMY1](course)
- How many student points [POLPOP0](course)
- How many student credits from [TERKANP1](course)
- How many student points from [TIEP1](course)
- How many ECTS from [SOS1](course)
- How many student credits is [LUOYA200](course)
- How many points is [TAYJ12](course)
- How many credits is [DPIS](course)
- How many ECTS is [JOVTETUS3](course)
- How many student credits is [JOVTS5](course)
- How many student points is [JMMETUS](course)

## intent:paikka
-Where is [TERY1](course)
-Where is course [YKYYHT4A](course)
-Where is class [HISJATKO](course)
-Where is lecture [STYP1A](course)
-Where is the classroom [HTIS54](course)
-Where can I find [KKENMP3](course)
-How to get to [TERKAP1](course)
-Where [TERHOIA6](course)
-Location [PSYA8](course)
-Find [TERTIETO2](course)
-How to find [SOS3]
-How can I find [KKSUPRO](course)
-Which classroom is [KKRUHY](course)
-What is the classroom for [HALTVA12](course)
-Which room is [FYSI1010](course)
-I'd like to find [STYP1B](course)
-Where can I find [STYA5](course)

## intent:opetusajat
-Schedule [KKRUNTEK](course)
-[KKES1](course) schedule
-[KKRUBMT](course) weekly schedule
-[KKRA5](course) weekly
-What is the schedule for [BTK0011](course)
-What is the schedule [KKENPMP3](course)
-When are classes for [LÄÄKA030](course)
-Classes [BIO2200](course)
-When are classes [BTK4030](course)
-Teaching times [KEMI61350](course)
-Teaching hours [LUOYY006](course)
-Teaching [DPIS2](course)
-[TAYJ12](course) teaching
-Week [TIEH0](course)
-Lectures [MTTMA3B](course)
-When are lectures [TIEVA36](course)
-Hours weekly [DPLAOPS](course)


## intent:kieli
-Teaching language [LTLY01](course)
-Lecture language [KIRP2](course)
-What is the teaching language in [SUOA4](course)
-Teaching language in [RANS3](course)
-What language is [RANSV5](course)
-Is [IGSY004](course) in english
-Is [KKENMP3](course) in finnish
-[KKSU1](course) language
-[JOVP2](course) teaching language
-Is [KIRS1](course) taught in english
-Is [HTIS60](course) taught in english
-Can I pass [VIROP1](course) in english
-Which language is [ITS25](course)


## intent:periodi
-Period [LTLY01](course)
-Semester [LTLY01](course)
-Quarter [LTLY01](course)
-Academic term [LTLY01](course)
-[LTLY01](course) semester
-[LTLY01](course) academic term
-[LTLY01](course) quarter
-This semester [LTLY01](course)
-What period [LTSA4](course)
-What study period [LTLY01](course)
-What study period is [LTLY01](course) in
-What period will [LTLY01](course) begin
-[LTLY01](course) period
-Is [LTLY01](course) this period
-Which period is [LTLY01](course)
-Which period will [LTLY01](course) begin
-What period will [LTLY01](course) begin
-[LTLY01](course) curriculum
-When is [LTLY01](course) in the curriulum
-The period of [LTLY01](course)
-Study period of [LTLY01](course)
-Semester [LTLY01](course)
-Which semester will [LTLY01](course) start
-Which semester is [LTLY01](course)
-Is [LTLY01](course) this semester
-What semester is [LTLY01](course)
-Academic term [LTLY01](course)
-Which academic term will [LTLY01](course) begin
-Which academic term is [LTLY01](course)
-[LTLY01](course) academic term
-Which semester will [LTLY01](course) begin
-The period of [LTLY01](course)
-The semester of [LTLY01](course)
-The academic term of [LTLY01](course)
-The quarter of [LTLY01](course)
-Which quarter is [LTLY01](course)
-What is the quarter of [LTLY01](course)
-Which quarter will [LTLY01](course) begin
