# CardControlTypeFlags - перечисление
Флаги элемента управления, описывающие его поведение.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum CardControlTypeFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration CardControlTypeFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class CardControlTypeFlags
F# __Копировать
     [<FlagsAttribute>]
    type CardControlTypeFlags
##  __Члены
None| 0|  Флаги отсутствуют.  
---|---|---  
UseInCards| 1|  Элемент управления может использоваться в карточках.  
UseInFiles| 2|  Элемент управления может использоваться в файлах.  
UseInTasks| 4|  Элемент управления может использоваться в заданиях.  
UseEverywhere| 7|  Элемент управления может использоваться в карточках, файлах
и заданиях.  
SpanByDefault| 8|  Растянуть по ширине по умолчанию при добавлении нового
контрола этого типа.  
HideCaptionByDefault| 16|  Скрыть заголовок по умолчанию при добавлении нового
контрола этого типа.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
