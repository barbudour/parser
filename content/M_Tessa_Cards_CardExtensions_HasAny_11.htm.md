# CardExtensions.HasAny(CardTypeTableControlFlags, CardTypeTableControlFlags)
- метод
Возвращает признак того, что один из заданных флагов установлен.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasAny(
    	this CardTypeTableControlFlags flags,
    	CardTypeTableControlFlags flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasAny ( 
    	flags As CardTypeTableControlFlags,
    	flag As CardTypeTableControlFlags
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasAny(
    	CardTypeTableControlFlags flags, 
    	CardTypeTableControlFlags flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasAny : 
            flags : CardTypeTableControlFlags * 
            flag : CardTypeTableControlFlags -> bool 
#### Параметры
flags [CardTypeTableControlFlags](T_Tessa_Cards_CardTypeTableControlFlags.htm)
    Установленные флаги.
flag [CardTypeTableControlFlags](T_Tessa_Cards_CardTypeTableControlFlags.htm)
     Флаг или флаги, которые требуется проверить. Если указано несколько флагов, то проверяется, что хотя бы один из них установлен. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что один или несколько заданных флагов установлены.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardTypeTableControlFlags](T_Tessa_Cards_CardTypeTableControlFlags.htm). При
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
[HasAny - перегрузка](Overload_Tessa_Cards_CardExtensions_HasAny.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
