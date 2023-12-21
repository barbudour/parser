# INumberDirectorBase.AvailableEventTypes - свойство
Доступные типы событий, происходящие с номерами. Изменение этой коллекции
позволяет отключить обработку некоторых событий для всех карточек, к которым
применим текущий объект.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    SealableList<NumberEventType> AvailableEventTypes { get; }
VB __Копировать
     ReadOnly Property AvailableEventTypes As SealableList(Of NumberEventType)
    	Get
C++ __Копировать
    property SealableList<NumberEventType^>^ AvailableEventTypes {
    	SealableList<NumberEventType^>^ get ();
    }
F# __Копировать
     abstract AvailableEventTypes : SealableList<NumberEventType> with get
#### Значение свойства
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[INumberDirectorBase - ](T_Tessa_Cards_Numbers_INumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
