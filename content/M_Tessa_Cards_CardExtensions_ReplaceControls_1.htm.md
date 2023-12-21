# CardExtensions.ReplaceControls(CardTypeBlock, CardTypeBlock) - метод
Заменить контролы блока на контролы исходного блока.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ReplaceControls(
    	this CardTypeBlock target,
    	CardTypeBlock source
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ReplaceControls ( 
    	target As CardTypeBlock,
    	source As CardTypeBlock
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ReplaceControls(
    	CardTypeBlock^ target, 
    	CardTypeBlock^ source
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ReplaceControls : 
            target : CardTypeBlock * 
            source : CardTypeBlock -> unit 
#### Параметры
target [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)
    Целевой блок.
source [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)
    Исходный блок.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
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
