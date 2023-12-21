# CardRequestExtensions.SetInstanceIDList - метод
Устанавливает список идентификаторов карточек с указанием типа экземпляра
таких карточек в запросе к сервису карточек
[CardRequest](T_Tessa_Cards_CardRequest.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetInstanceIDList(
    	this CardRequest request,
    	ICollection<Guid> instanceIDList,
    	CardInstanceType instanceType = CardInstanceType.Card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetInstanceIDList ( 
    	request As CardRequest,
    	instanceIDList As ICollection(Of Guid),
    	Optional instanceType As CardInstanceType = CardInstanceType.Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetInstanceIDList(
    	CardRequest^ request, 
    	ICollection<Guid>^ instanceIDList, 
    	CardInstanceType instanceType = CardInstanceType::Card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetInstanceIDList : 
            request : CardRequest * 
            instanceIDList : ICollection<Guid> * 
            ?instanceType : CardInstanceType 
    (* Defaults:
            let _instanceType = defaultArg instanceType CardInstanceType.Card
    *)
    -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
instanceIDList
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Список идентификаторов карточек. Значение null определяет, что список идентификаторов должен быть удалён. 
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm) (Optional)
    Тип экземпляра для заданных идентификаторов карточек.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardRequest](T_Tessa_Cards_CardRequest.htm). При вызове метода
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
