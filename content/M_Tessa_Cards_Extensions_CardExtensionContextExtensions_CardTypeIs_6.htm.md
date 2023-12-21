# CardExtensionContextExtensions.CardTypeIs(ICardExtensionContext, Guid[]) -
метод
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CardTypeIs(
    	this ICardExtensionContext context,
    	params Guid[] typeIDs
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CardTypeIs ( 
    	context As ICardExtensionContext,
    	ParamArray typeIDs As Guid()
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool CardTypeIs(
    	ICardExtensionContext^ context, 
    	... array<Guid>^ typeIDs
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CardTypeIs : 
            context : ICardExtensionContext * 
            typeIDs : Guid[] -> bool 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст расширения, для которого выполняется проверка.
typeIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
    Массив из возможных значений идентификатора типа карточки, который требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если идентификатор типа карточки равен одному из заданных значений;
false в противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensionContextExtensions -
](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm)
[CardTypeIs -
перегрузка](Overload_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
