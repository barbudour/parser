# IFileConverter.TryGetRequestAsync - метод
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке или null, если параметры файла не найдены по идентификатору версии.
Используйте метод для физических файлов, информация по которым может быть
найдена по указанному идентификатору версии. Для виртуальных файлов создайте
объект запроса через конструктор [Tessa.FileConverters.FileConverterRequest].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<IFileConverterRequest> TryGetRequestAsync(
    	string eventName,
    	FileConverterFormat outputFormat,
    	Guid versionID,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetRequestAsync ( 
    	eventName As String,
    	outputFormat As FileConverterFormat,
    	versionID As Guid,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IFileConverterRequest)
C++ __Копировать
    Task<IFileConverterRequest^>^ TryGetRequestAsync(
    	String^ eventName, 
    	FileConverterFormat outputFormat, 
    	Guid versionID, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetRequestAsync : 
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
eventName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Алиас события, для которого выполняется предпросмотр. Список стандартных алиасов можно получить из класса [Tessa.FileConverters.FileConverterEventNames]. Если указано значение null/пустая строка, то используется константа [Tessa.FileConverters.FileConverterEventNames.Unknown]. 
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
Запрос на выполнение операции по конвертации заданной версии или null, если
параметры файла не найдены по идентификатору версии.
## __См. также
#### Ссылки
[IFileConverter - ](T_Tessa_FileConverters_IFileConverter.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
