# CardRequestExtensions.TryGetAdditionalFiles - метод
Возвращает список дополнительных файлов [CardFile](T_Tessa_Cards_CardFile.htm)
в ответе на запрос на экспорт карточки, или null, если строки не были заданы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ListStorage<CardFile> TryGetAdditionalFiles(
    	this CardGetResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetAdditionalFiles ( 
    	response As CardGetResponse
    ) As ListStorage(Of CardFile)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ListStorage<CardFile^>^ TryGetAdditionalFiles(
    	CardGetResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetAdditionalFiles : 
            response : CardGetResponse -> ListStorage<CardFile> 
#### Параметры
response [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
    Ответ на запрос на экспорт карточки.
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFile](T_Tessa_Cards_CardFile.htm)>  
Список дополнительных файлов [CardFile](T_Tessa_Cards_CardFile.htm) в ответе
на запрос на экспорт карточки, или null, если строки не были заданы.
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
