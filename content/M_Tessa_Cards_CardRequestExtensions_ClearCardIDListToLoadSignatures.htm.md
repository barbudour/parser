# CardRequestExtensions.ClearCardIDListToLoadSignatures - метод
Очищает список идентификаторов карточек, для которых будут загружены подписи
для файлов. Возвращает признак того, что список присутствовал перед вызовом
метода.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ClearCardIDListToLoadSignatures(
    	this ICardGetExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ClearCardIDListToLoadSignatures ( 
    	context As ICardGetExtensionContext
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool ClearCardIDListToLoadSignatures(
    	ICardGetExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ClearCardIDListToLoadSignatures : 
            context : ICardGetExtensionContext -> bool 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст по загрузке карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если список присутствовал перед вызовом метода; false в противном
случае.
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
