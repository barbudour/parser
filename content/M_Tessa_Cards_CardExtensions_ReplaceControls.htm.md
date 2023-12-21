# CardExtensions.ReplaceControls(IEnumerable<CardTypeBlock>,
IEnumerable<CardTypeBlock>) - метод
Заменить все контролы указанных блоков на контролы переданных блоков.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ReplaceControls(
    	this IEnumerable<CardTypeBlock> target,
    	IEnumerable<CardTypeBlock> source
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ReplaceControls ( 
    	target As IEnumerable(Of CardTypeBlock),
    	source As IEnumerable(Of CardTypeBlock)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ReplaceControls(
    	IEnumerable<CardTypeBlock^>^ target, 
    	IEnumerable<CardTypeBlock^>^ source
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ReplaceControls : 
            target : IEnumerable<CardTypeBlock> * 
            source : IEnumerable<CardTypeBlock> -> unit 
#### Параметры
target
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)>
    Целевые блоки.
source
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)>
    Исходные блоки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)>.
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
[ReplaceControls -
перегрузка](Overload_Tessa_Cards_CardExtensions_ReplaceControls.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
