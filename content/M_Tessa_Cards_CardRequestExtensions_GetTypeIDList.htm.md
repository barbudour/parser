# CardRequestExtensions.GetTypeIDList(CardResponse) - метод
Возвращает список идентификаторов типов карточек в виде массива. Размер
массива определяется по количеству элементов в запросе. Массив не равен null.
Элементы возвращаемого массива равны null, если для идентификатора карточки,
переданного в запросе на соответствующей позиции, не найден идентификатор.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid?[] GetTypeIDList(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetTypeIDList ( 
    	response As CardResponse
    ) As Guid?()
C++ __Копировать
     public:
    [ExtensionAttribute]
    static array<Nullable<Guid>>^ GetTypeIDList(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetTypeIDList : 
            response : CardResponse -> Nullable<Guid>[] 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на запрос к сервису карточек.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>[]  
Список идентификаторов типов карточек в виде массива. Элементы возвращаемого
массива равны null, если для идентификатора карточки, переданного в запросе на
соответствующей позиции, не найден идентификатор.
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
[GetTypeIDList -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_GetTypeIDList.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
