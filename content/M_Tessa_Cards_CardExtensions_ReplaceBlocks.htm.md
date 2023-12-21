# CardExtensions.ReplaceBlocks(IEnumerable<CardTypeForm>,
IEnumerable<CardTypeForm>) - метод
Заменить все блоки указанных форм на блоки переданных форм.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ReplaceBlocks(
    	this IEnumerable<CardTypeForm> target,
    	IEnumerable<CardTypeForm> source
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ReplaceBlocks ( 
    	target As IEnumerable(Of CardTypeForm),
    	source As IEnumerable(Of CardTypeForm)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ReplaceBlocks(
    	IEnumerable<CardTypeForm^>^ target, 
    	IEnumerable<CardTypeForm^>^ source
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ReplaceBlocks : 
            target : IEnumerable<CardTypeForm> * 
            source : IEnumerable<CardTypeForm> -> unit 
#### Параметры
target
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)>
    Целевые формы.
source
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)>
    Исходные формы.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)>.
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
[ReplaceBlocks -
перегрузка](Overload_Tessa_Cards_CardExtensions_ReplaceBlocks.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
