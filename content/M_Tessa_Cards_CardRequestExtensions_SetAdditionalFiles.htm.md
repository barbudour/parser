# CardRequestExtensions.SetAdditionalFiles - метод
Устанавливает список дополнительных файлов
[CardFile](T_Tessa_Cards_CardFile.htm) в ответе на запрос на экспорт карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetAdditionalFiles(
    	this CardGetResponse response,
    	ListStorage<CardFile> additionalFiles
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetAdditionalFiles ( 
    	response As CardGetResponse,
    	additionalFiles As ListStorage(Of CardFile)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetAdditionalFiles(
    	CardGetResponse^ response, 
    	ListStorage<CardFile^>^ additionalFiles
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetAdditionalFiles : 
            response : CardGetResponse * 
            additionalFiles : ListStorage<CardFile> -> unit 
#### Параметры
response [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
    Ответ на запрос на экспорт карточки.
additionalFiles
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFile](T_Tessa_Cards_CardFile.htm)>
     Список дополнительных файлов [CardFile](T_Tessa_Cards_CardFile.htm). Если равен null, то информация удаляется. 
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
