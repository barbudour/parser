# CardRequestExtensions.TryGetTemplateCardID - метод
Возвращает идентификатор карточки шаблона, по которой требуется создать
карточку, или null, если идентификатор не был задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid? TryGetTemplateCardID(
    	this CardNewRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTemplateCardID ( 
    	request As CardNewRequest
    ) As Guid?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<Guid> TryGetTemplateCardID(
    	CardNewRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTemplateCardID : 
            request : CardNewRequest -> Nullable<Guid> 
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос на создание карточки по шаблону.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Идентификатор карточки шаблона, по которой требуется создать карточку, или
null, если идентификатор не был задан.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
