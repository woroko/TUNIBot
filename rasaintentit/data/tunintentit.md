<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 



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
- Where is [TERY1](course)
- Where is course [YKYYHT4A](course)
- Where is class [HISJATKO](course)
- Where is lecture [STYP1A](course)
- Where is the classroom [HTIS54](course)
- Where can I find [KKENMP3](course)
- How to get to [TERKAP1](course)
- Where [TERHOIA6](course)
- Location [PSYA8](course)
- Find [TERTIETO2](course)
- How to find [SOS3]
- How can I find [KKSUPRO](course)
- Which classroom is [KKRUHY](course)
- What is the classroom for [HALTVA12](course)
- Which room is [FYSI1010](course)
- I'd like to find [STYP1B](course)
- Where can I find [STYA5](course)

## intent:opetusajat
- Schedule [KKRUNTEK](course)
- [KKES1](course) schedule
- [KKRUBMT](course) weekly schedule
- [KKRA5](course) weekly
- What is the schedule for [BTK0011](course)
- What is the schedule [KKENPMP3](course)
- When are classes for [LÄÄKA030](course)
- Classes [BIO2200](course)
- When are classes [BTK4030](course)
- Teaching times [KEMI61350](course)
- Teaching hours [LUOYY006](course)
- Teaching [DPIS2](course)
- [TAYJ12](course) teaching
- Week [TIEH0](course)
- Lectures [MTTMA3B](course)
- When are lectures [TIEVA36](course)
- Hours weekly [DPLAOPS](course)


## intent:kieli
- Teaching language [LTLY01](course)
- Lecture language [KIRP2](course)
- What is the teaching language in [SUOA4](course)
- Teaching language in [RANS3](course)
- What language is [RANSV5](course)
- Is [IGSY004](course) in english
- Is [KKENMP3](course) in finnish
- [KKSU1](course) language
- [JOVP2](course) teaching language
- Is [KIRS1](course) taught in english
- Is [HTIS60](course) taught in english
- Can I pass [VIROP1](course) in english
- Which language is [ITS25](course)


## intent:periodi
- Period [KATTAP11](course)
- Semester [JKKYTVP11](course)
- Quarter [HALHAA13](course)
- Academic term [HALJUA21](course)
- [HALJUS99](course) semester
- [KATMAP11](course) academic term
- [POLKAA99](course) quarter
- This semester [LFS04](course)
- What period [NORDIF4](course)
- What study period [JKKYINA15](course)
- What study period is [VENS4](course) in
- What period will [RANA7](course) begin
- [MEDU01](course) period
- Is [JOVTS5](course) this period
- Which period is [ENGP8](course)
- Which period will [MVKS02](course) begin
- What period will [ITIP5](course) begin
- [KIRA1](course) curriculum
- When is [SAKP2](course) in the curriulum
- The period of [TSEKP3](course)
- Study period of [TRSU07](course)
- Semester [TRMU2](course)
- Which semester will [IGS006](course) start
- Which semester is [JOUJOVTS](course)
- Is [FONEP2](course) this semester
- What semester is [KIRS1/A4](course)
- Academic term [KIRA3C2](course)
- Which academic term will [TERKANP3](course) begin
- Which academic term is [TERY4](course)
- [PSYP5](course) academic term
- Which semester will [YKYYHT5](course) begin
- The period of [LATAP2](course)
- The semester of [YKYYV07](course)
- The academic term of [TERHOIA6](course)
- The quarter of [PGHMTS](course)
- Which quarter is [TERVAL4](course)
- What is the quarter of [SOCYKV2/RES012](course)
- Which quarter will [KKRA1](course) begin

## intent:poikkeusajat
- Exceptions [HALHAA15](course)
- Exception [JKKYORP1](course)
- What are the exceptions for [POLPOP03](course)
- [KATMAP11](course) exceptions
- [DPEDUB.1B](course) exception
- Exceptions in teaching hours[KASLOM10](course)
- Exceptions in teaching times [MTTTS17](course)
- Are there any exceptions in teaching [TIETS05](course)
- What exceptions are there in [BTK2036](course)
- Lecture exceptions [MOLI](course)
- Does [ENGP6](course) have exceptions in teaching hours
- Were there exceptions in lectures [VENP4/VENK2](course)
- Teaching times exceptions for [ESPFP1](course)
- What were the exceptions of teaching in [JOVP1](course)
- Does the schedule for [MEDU10](course) have any exceptions?
- When were the exceptions for [RANA7](course)
- The exceptions in lessons for [KIRP3](course)
- Special teaching times for [SAKA5](course)
- Is there anything special I should know about the course schedule for [ESPFP0](course)
- [TSEKP1](course) special lecture hours
- Special schedule [SUOA8](course)
- Will there be lectures in holidays in [VENP2](course)
- Holiday exceptions [SUKKP5B](course)
- Course break teaching times [JOUJOVTS](course)
- Do we have a lecture during holiday in [JOVVAL](course)
- Cancelled lectures [SUOR1/A6](course)
- Will [MEDU07](course) lectures be cancelled during holiday
- Will [HTIY004](course) have a lecture every week

<!--- toistaiseksi nimetty "nimi" vaikka APIssa se on "name". intetti name on jo käytössä, mitä tehdä?  --> 
## intent:nimi
- What is the name of [POHA1](course)
- [RANSV5](course) name
- Name [MVKS36/31](course)
- What is the full name of [TRSU05](course)
- What is [DPIT1](course) called
- What is the course code [DPLSSEM](course) called
- What course is [MEDU07](course)
- [ENGA10](course) named
- What's [DPCMTJ4](course) named
- Name of [FONEA4](course)

## intent:degreeProgrammeCode
- 

<!--- lookup table list for course codes.  --> 
## lookup:course  <!-- no list to specify lookup table file -->
- data/course_codes.txt