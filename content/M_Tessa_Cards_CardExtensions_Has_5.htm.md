# CardExtensions.Has(CardTypeColumnFlags, CardTypeColumnFlags) - метод
Возвращает признак того, что заданный флаг установлен.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool Has(
    	this CardTypeColumnFlags flags,
    	CardTypeColumnFlags flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function Has ( 
    	flags As CardTypeColumnFlags,
    	flag As CardTypeColumnFlags
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool Has(
    	CardTypeColumnFlags flags, 
    	CardTypeColumnFlags flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member Has : 
            flags : CardTypeColumnFlags * 
            flag : CardTypeColumnFlags -> bool 
#### Параметры
flags [CardTypeColumnFlags](T_Tessa_Cards_CardTypeColumnFlags.htm)
    Установленные флаги.
flag [CardTypeColumnFlags](T_Tessa_Cards_CardTypeColumnFlags.htm)
     Флаг, который требуется проверить. Если указано несколько флагов, то проверяется, что все из них установлены. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что заданный флаг установлен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeColumnFlags](T_Tessa_Cards_CardTypeColumnFlags.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Has - перегрузка](Overload_Tessa_Cards_CardExtensions_Has.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
