# CardRequestExtensions.TryGetConverterFormat(IDictionary<String, Object>) -
метод
Возвращает формат, в который должно быть сконвертировано содержимое, или null,
если конвертация не требуется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static FileConverterFormat? TryGetConverterFormat(
    	this IDictionary<string, Object> requestInfo
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetConverterFormat ( 
    	requestInfo As IDictionary(Of String, Object)
    ) As FileConverterFormat?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<FileConverterFormat> TryGetConverterFormat(
    	IDictionary<String^, Object^>^ requestInfo
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetConverterFormat : 
            requestInfo : IDictionary<string, Object> -> Nullable<FileConverterFormat> 
#### Параметры
requestInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Свойство request.Info для запроса на загрузку содержимого файла [CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm). 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)>  
Формат, в который должно быть сконвертировано содержимое, или null, если
конвертация не требуется.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
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
[TryGetConverterFormat -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_TryGetConverterFormat.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
