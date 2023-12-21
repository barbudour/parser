# CardRequestExtensions.SetFileMapping - метод
Устанавливает список объектов с маппингом для контента файлов
[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm) в ответе на
запрос на экспорт карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetFileMapping(
    	this CardGetResponse response,
    	ListStorage<CardFileContentMapping> fileMapping
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetFileMapping ( 
    	response As CardGetResponse,
    	fileMapping As ListStorage(Of CardFileContentMapping)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetFileMapping(
    	CardGetResponse^ response, 
    	ListStorage<CardFileContentMapping^>^ fileMapping
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetFileMapping : 
            response : CardGetResponse * 
            fileMapping : ListStorage<CardFileContentMapping> -> unit 
#### Параметры
response [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
    Ответ на запрос на экспорт карточки.
fileMapping
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm)>
     Список объектов с маппингом для контента файлов [CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm). Если равен null, то информация удаляется. 
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
