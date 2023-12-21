# CardRequestExtensions.GetInstanceIDList - метод
Получает список идентификаторов карточек с указанием типа экземпляра таких
карточек. Если список не был установлен, то возвращается пустой список, не
равный null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<Guid> GetInstanceIDList(
    	this CardRequest request,
    	out CardInstanceType? instanceType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetInstanceIDList ( 
    	request As CardRequest,
    	<OutAttribute> ByRef instanceType As CardInstanceType?
    ) As List(Of Guid)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<Guid>^ GetInstanceIDList(
    	CardRequest^ request, 
    	[OutAttribute] Nullable<CardInstanceType>% instanceType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetInstanceIDList : 
            request : CardRequest * 
            instanceType : Nullable<CardInstanceType> byref -> List<Guid> 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
instanceType
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)>
     Тип экземпляра для заданных идентификаторов карточек или null, если тип экземпляра не был установлен. 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Список идентификаторов карточек. Если список не был установлен, то
возвращается пустой список, не равный null.
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
