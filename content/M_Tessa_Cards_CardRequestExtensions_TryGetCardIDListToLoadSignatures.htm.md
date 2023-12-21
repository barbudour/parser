# CardRequestExtensions.TryGetCardIDListToLoadSignatures - метод
Возвращает список идентификаторов карточек, для которых будут загружены
подписи для файлов, помимо текущей загруженной карточки, или null, если список
не был создан или был очищен.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<Guid> TryGetCardIDListToLoadSignatures(
    	this ICardGetExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetCardIDListToLoadSignatures ( 
    	context As ICardGetExtensionContext
    ) As IList(Of Guid)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IList<Guid>^ TryGetCardIDListToLoadSignatures(
    	ICardGetExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetCardIDListToLoadSignatures : 
            context : ICardGetExtensionContext -> IList<Guid> 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст по загрузке карточки.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Список идентификаторов карточек, для которых будут загружены подписи для
файлов, помимо текущей загруженной карточки, или null, если список не был
создан или был очищен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
