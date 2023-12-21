# NumberContextInitializationFlags - перечисление
Флаги, определяющие результат инициализации контекста события, происходящего с
номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum NumberContextInitializationFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration NumberContextInitializationFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class NumberContextInitializationFlags
F# __Копировать
     [<FlagsAttribute>]
    type NumberContextInitializationFlags
##  __Члены
None| 0|  С контекстом не было выполнено действий.  
---|---|---  
DirectorInitialized| 1|  В контексте было инициализировано свойство
[Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm).  
BuilderInitialized| 2|  В контексте было инициализировано свойство
[Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm).  
EventTypeInitialized| 4|  В контексте было инициализировано свойство
[EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm).  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
