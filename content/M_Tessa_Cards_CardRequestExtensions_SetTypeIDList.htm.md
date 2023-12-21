# CardRequestExtensions.SetTypeIDList - метод
Устанавливает список идентификаторов типов карточек в ответе на запрос к
сервису карточек [CardResponse](T_Tessa_Cards_CardResponse.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTypeIDList(
    	this CardResponse response,
    	ICollection<Guid?> typeIDList
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTypeIDList ( 
    	response As CardResponse,
    	typeIDList As ICollection(Of Guid?)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTypeIDList(
    	CardResponse^ response, 
    	ICollection<Nullable<Guid>>^ typeIDList
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTypeIDList : 
            response : CardResponse * 
            typeIDList : ICollection<Nullable<Guid>> -> unit 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на запрос к сервису карточек.
typeIDList
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>
     Список идентификаторов типов карточек. Значение null определяет, что список идентификаторов должен быть удалён. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponse](T_Tessa_Cards_CardResponse.htm). При вызове метода
для экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
