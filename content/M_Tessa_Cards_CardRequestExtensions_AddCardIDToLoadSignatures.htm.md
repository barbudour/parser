# CardRequestExtensions.AddCardIDToLoadSignatures - метод
Добавляет идентификатор карточки в список идентификаторов, для которых будут
загружены подписи для файлов, помимо текущей загруженной карточки. Используйте
для виртуальных файлов, относящихся к другим карточкам, которые добавлены в
загруженную карточку. Подписи загружаются в CardGetExtension.AfterRequest на
этапе ExtensionStage.Platform, поэтому список идентификаторов должен быть
установлен раньше. Возвращает признак того, что идентификатор был добавлен,
т.к. отсутствовал в списке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool AddCardIDToLoadSignatures(
    	this ICardGetExtensionContext context,
    	Guid cardID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AddCardIDToLoadSignatures ( 
    	context As ICardGetExtensionContext,
    	cardID As Guid
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool AddCardIDToLoadSignatures(
    	ICardGetExtensionContext^ context, 
    	Guid cardID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddCardIDToLoadSignatures : 
            context : ICardGetExtensionContext * 
            cardID : Guid -> bool 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст по загрузке карточки.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой должны быть загружены подписи.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если идентификатор был добавлен, т.к. отсутствовал в списке; false в
противном случае.
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
