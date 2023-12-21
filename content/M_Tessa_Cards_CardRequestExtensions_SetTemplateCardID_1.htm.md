# CardRequestExtensions.SetTemplateCardID(CardNewRequest, Nullable<Guid>) -
метод
Устанавливает идентификатор карточки шаблона, по которому требуется создать
карточку. При этом в запросе должен быть установлен идентификатор типа
карточки [CardTypeID](P_Tessa_Cards_CardNewRequest_CardTypeID.htm), равный
типу карточки шаблона
[TemplateTypeID](F_Tessa_Cards_CardHelper_TemplateTypeID.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTemplateCardID(
    	this CardNewRequest request,
    	Guid? cardID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateCardID ( 
    	request As CardNewRequest,
    	cardID As Guid?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateCardID(
    	CardNewRequest^ request, 
    	Nullable<Guid> cardID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateCardID : 
            request : CardNewRequest * 
            cardID : Nullable<Guid> -> unit 
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос на создание карточки по шаблону.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор карточки шаблона, по которой требуется создать карточку.
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
[SetTemplateCardID -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetTemplateCardID.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
