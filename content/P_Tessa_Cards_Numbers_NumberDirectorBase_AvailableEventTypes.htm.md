# NumberDirectorBase.AvailableEventTypes - свойство
Доступные типы событий, происходящие с номерами. Изменение этой коллекции
позволяет отключить обработку некоторых событий для всех карточек, к которым
применим текущий объект.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableList<NumberEventType> AvailableEventTypes { get; }
VB __Копировать
     Public ReadOnly Property AvailableEventTypes As SealableList(Of NumberEventType)
    	Get
C++ __Копировать
     public:
    virtual property SealableList<NumberEventType^>^ AvailableEventTypes {
    	SealableList<NumberEventType^>^ get () sealed;
    }
F# __Копировать
     abstract AvailableEventTypes : SealableList<NumberEventType> with get
    override AvailableEventTypes : SealableList<NumberEventType> with get
#### Значение свойства
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)>
#### Реализации
[INumberDirectorBase.AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberDirectorBase - ](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
