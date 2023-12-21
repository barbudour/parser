# CardRequestExtensions.SetTemplateWasRepaired - метод
Устанавливает признак того, что карточка шаблона была исправлена после
изменения схемы данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTemplateWasRepaired(
    	this Card card,
    	bool hasRepairMessages
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateWasRepaired ( 
    	card As Card,
    	hasRepairMessages As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateWasRepaired(
    	Card^ card, 
    	bool hasRepairMessages
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateWasRepaired : 
            card : Card * 
            hasRepairMessages : bool -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, для которой требуется установить значение признака.
hasRepairMessages
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что карточка шаблона была исправлена после изменения схемы данных. При установке значения false флаг удаляется из структуры карточки. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Card](T_Tessa_Cards_Card.htm). При вызове метода для экземпляра
следует опускать первый параметр. Дополнительные сведения см. в разделе
[Методы расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
