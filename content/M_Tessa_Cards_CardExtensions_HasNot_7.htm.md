# CardExtensions.HasNot(CardTypeCustomControlFlags,
CardTypeCustomControlFlags) - метод
Возвращает признак того, что заданный флаг не установлен.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasNot(
    	this CardTypeCustomControlFlags flags,
    	CardTypeCustomControlFlags flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasNot ( 
    	flags As CardTypeCustomControlFlags,
    	flag As CardTypeCustomControlFlags
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasNot(
    	CardTypeCustomControlFlags flags, 
    	CardTypeCustomControlFlags flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasNot : 
            flags : CardTypeCustomControlFlags * 
            flag : CardTypeCustomControlFlags -> bool 
#### Параметры
flags
[CardTypeCustomControlFlags](T_Tessa_Cards_CardTypeCustomControlFlags.htm)
    Установленные флаги.
flag
[CardTypeCustomControlFlags](T_Tessa_Cards_CardTypeCustomControlFlags.htm)
     Флаг, который требуется проверить. Если указано несколько флагов, то проверяется, что нет ни одного установленного флага. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что заданный флаг не установлен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardTypeCustomControlFlags](T_Tessa_Cards_CardTypeCustomControlFlags.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[HasNot - перегрузка](Overload_Tessa_Cards_CardExtensions_HasNot.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
