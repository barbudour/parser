# CardExtensions.SetNormalized - метод
Устанавливает заданные флаги с учётом нормализации. При указании флага flag
как Allow автоматически сбрасывает соответствующий флаг Prohibit, и наоборот.
Результат применяется к flags и возвращается в результате метода.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardPermissionFlags SetNormalized(
    	this CardPermissionFlags flags,
    	CardPermissionFlags flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetNormalized ( 
    	flags As CardPermissionFlags,
    	flag As CardPermissionFlags
    ) As CardPermissionFlags
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardPermissionFlags SetNormalized(
    	CardPermissionFlags flags, 
    	CardPermissionFlags flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetNormalized : 
            flags : CardPermissionFlags * 
            flag : CardPermissionFlags -> CardPermissionFlags 
#### Параметры
flags [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Флаги, в которые требуется записать нормализованные флаги flag.
flag [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Флаги, которые требуется записать в flags с учётом нормализации.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Нормализованные флаги.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm). При
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
