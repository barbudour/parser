# CardExtensionContextExtensions.CardTypeIs(ICardExtensionContext, Guid, Guid,
Guid, Guid) - метод
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CardTypeIs(
    	this ICardExtensionContext context,
    	Guid typeID1,
    	Guid typeID2,
    	Guid typeID3,
    	Guid typeID4
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CardTypeIs ( 
    	context As ICardExtensionContext,
    	typeID1 As Guid,
    	typeID2 As Guid,
    	typeID3 As Guid,
    	typeID4 As Guid
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool CardTypeIs(
    	ICardExtensionContext^ context, 
    	Guid typeID1, 
    	Guid typeID2, 
    	Guid typeID3, 
    	Guid typeID4
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CardTypeIs : 
            context : ICardExtensionContext * 
            typeID1 : Guid * 
            typeID2 : Guid * 
            typeID3 : Guid * 
            typeID4 : Guid -> bool 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст расширения, для которого выполняется проверка.
typeID1 [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Одно из возможных значений идентификатора типа карточки, который требуется проверить.
typeID2 [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Одно из возможных значений идентификатора типа карточки, который требуется проверить.
typeID3 [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Одно из возможных значений идентификатора типа карточки, который требуется проверить.
typeID4 [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Одно из возможных значений идентификатора типа карточки, который требуется проверить.
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
