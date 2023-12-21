# CardRequestExtensions.SetTemplateCardID(Dictionary<String, Object>,
Nullable<Guid>) - метод
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
    	this Dictionary<string, Object> requestInfo,
    	Guid? cardID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateCardID ( 
    	requestInfo As Dictionary(Of String, Object),
    	cardID As Guid?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateCardID(
    	Dictionary<String^, Object^>^ requestInfo, 
    	Nullable<Guid> cardID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateCardID : 
            requestInfo : Dictionary<string, Object> * 
            cardID : Nullable<Guid> -> unit 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Информация в запросе на создание карточки по шаблону.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор карточки шаблона, по которой требуется создать карточку.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
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
