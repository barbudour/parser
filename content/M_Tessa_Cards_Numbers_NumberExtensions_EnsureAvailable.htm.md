# NumberExtensions.EnsureAvailable - метод
Гарантирует, что объект
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm) в
коллекции доступных типов событий
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)
будет содержать тип действия eventType. Если коллекция защищена от изменений и
тип события в ней отсутствовал, то метод возвращает false.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool EnsureAvailable(
    	this INumberDirectorBase director,
    	NumberEventType eventType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function EnsureAvailable ( 
    	director As INumberDirectorBase,
    	eventType As NumberEventType
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool EnsureAvailable(
    	INumberDirectorBase^ director, 
    	NumberEventType^ eventType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member EnsureAvailable : 
            director : INumberDirectorBase * 
            eventType : NumberEventType -> bool 
#### Параметры
director [INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm)
    Базовый интерфейс для объектов, реализующих произвольное взаимодействие с номерами карточек.
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
    Тип события, который должен присутствовать в коллекции доступных типов событий.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в коллекцию доступных типов событий был добавлен заданный тип
события eventType, если ранее он там отсутствовал; false, если добавить тип
невозможно, т.к. коллекция защищена от изменений.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
