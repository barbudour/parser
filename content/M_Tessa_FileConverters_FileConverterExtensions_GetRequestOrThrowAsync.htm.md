# FileConverterExtensions.GetRequestOrThrowAsync - метод
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке. Возвращаемое значение гарантированно не равно null. Если параметры
файла не найдены по идентификатору версии, то выбрасывается исключение.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<IFileConverterRequest> GetRequestOrThrowAsync(
    	this IFileConverter fileConverter,
    	string eventName,
    	FileConverterFormat outputFormat,
    	Guid versionID,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetRequestOrThrowAsync ( 
    	fileConverter As IFileConverter,
    	eventName As String,
    	outputFormat As FileConverterFormat,
    	versionID As Guid,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IFileConverterRequest)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<IFileConverterRequest^>^ GetRequestOrThrowAsync(
    	IFileConverter^ fileConverter, 
    	String^ eventName, 
    	FileConverterFormat outputFormat, 
    	Guid versionID, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetRequestOrThrowAsync : 
            fileConverter : IFileConverter * 
            eventName : string * 
            outputFormat : FileConverterFormat * 
            versionID : Guid * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IFileConverterRequest> 
#### Параметры
fileConverter [IFileConverter](T_Tessa_FileConverters_IFileConverter.htm)
    Объект, выполнющий преобразование файлов из одного формата в другой.
eventName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Алиас события, для которого выполняется предпросмотр. Список стандартных алиасов можно получить из класса [FileConverterEventNames](T_Tessa_FileConverters_FileConverterEventNames.htm). Если указано значение null/пустая строка, то используется константа [Unknown](F_Tessa_FileConverters_FileConverterEventNames_Unknown.htm). 
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Выходной формат файла.
versionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии преобразуемого файла.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, передаваемая в параметры конвертации, или null, если дополнительная информация отсутствует. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)>  
Запрос на выполнение операции по конвертации заданной версии. Возвращаемое
значение гарантированно не равно null.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [IFileConverter](T_Tessa_FileConverters_IFileConverter.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Параметры файла не найдены по идентификатору версии.  
---|---  
##  __См. также
#### Ссылки
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
