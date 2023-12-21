# Card.Entries - свойство
Объект, позволяющий обратиться напрямую от строковой секции карточки к
значению поля и автоматически устанавливающий системную информацию об
изменённых полях.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardEntryData Entries { get; }
VB __Копировать
     Public ReadOnly Property Entries As CardEntryData
    	Get
C++ __Копировать
     public:
    property CardEntryData^ Entries {
    	CardEntryData^ get ();
    }
F# __Копировать
     member Entries : CardEntryData with get
#### Значение свойства
[CardEntryData](T_Tessa_Cards_CardEntryData.htm)
##  __Заметки
Использование Entries позволяет не устанавливать информацию об изменённых
полях вручную, т.к. любое поле, значение которого изменяется, заносится в
список изменённых.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
