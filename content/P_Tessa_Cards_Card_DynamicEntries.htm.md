# Card.DynamicEntries - свойство
Объект, позволяющий обратиться напрямую от строковой секции карточки к
значению поля через позднее связывание и автоматически устанавливающий
системную информацию об изменённых полях.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object DynamicEntries { get; }
VB __Копировать
     Public ReadOnly Property DynamicEntries As Object
    	Get
C++ __Копировать
     public:
    property Object^ DynamicEntries {
    	Object^ get ();
    }
F# __Копировать
     member DynamicEntries : Object with get
#### Значение свойства
[Object](https://learn.microsoft.com/dotnet/api/system.object)
##  __Заметки
Обращение к DynamicEntries немного быстрее, чем к Dynamic.Entries за счёт
кэширования выражений средой DLR.
Также использование DynamicEntries позволяет не устанавливать информацию об
изменённых полях вручную, т.к. любое поле, значение которого изменяется,
заносится в список изменённых.
##  __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
