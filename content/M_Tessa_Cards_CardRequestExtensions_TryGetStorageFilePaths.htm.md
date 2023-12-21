# CardRequestExtensions.TryGetStorageFilePaths - метод
Возвращает объекты с информацией о пути и имени файлов, которые должны быть
записаны в отдельные файлы, относительно структуры карточки
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<IStorageContentMapping> TryGetStorageFilePaths(
    	this CardGetResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetStorageFilePaths ( 
    	response As CardGetResponse
    ) As IList(Of IStorageContentMapping)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IList<IStorageContentMapping^>^ TryGetStorageFilePaths(
    	CardGetResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetStorageFilePaths : 
            response : CardGetResponse -> IList<IStorageContentMapping> 
#### Параметры
response [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
    Ответ на запрос на экспорт карточки.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IStorageContentMapping](T_Tessa_Platform_Storage_IStorageContentMapping.htm)>
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm). При вызове
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
