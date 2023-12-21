# CardRequestExtensions.SetConverterFormat(CardGetFileContentRequest,
FileConverterFormat) - метод
Устанавливает, что загружаемое содержимое должно быть сконвертировано в
указанный формат.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetConverterFormat(
    	this CardGetFileContentRequest request,
    	FileConverterFormat format
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetConverterFormat ( 
    	request As CardGetFileContentRequest,
    	format As FileConverterFormat
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetConverterFormat(
    	CardGetFileContentRequest^ request, 
    	FileConverterFormat format
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetConverterFormat : 
            request : CardGetFileContentRequest * 
            format : FileConverterFormat -> unit 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос на загрузку содержимого файла.
format [FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат результирующего файла, в который выполняется преобразование.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[SetConverterFormat -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetConverterFormat.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
