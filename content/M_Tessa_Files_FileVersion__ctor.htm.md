# FileVersion - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileVersion(
    	Guid id,
    	string name,
    	long size,
    	int number,
    	FileVersionState state,
    	DateTime created,
    	Guid createdByID,
    	string createdByName,
    	IFileContent content,
    	FileContentSource contentSource,
    	IFileErrorInfo errorInfo,
    	IFile file,
    	byte[] hash = null,
    	Guid? linkID = null
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	size As Long,
    	number As Integer,
    	state As FileVersionState,
    	created As DateTime,
    	createdByID As Guid,
    	createdByName As String,
    	content As IFileContent,
    	contentSource As FileContentSource,
    	errorInfo As IFileErrorInfo,
    	file As IFile,
    	Optional hash As Byte() = Nothing,
    	Optional linkID As Guid? = Nothing
    )
C++ __Копировать
     public:
    FileVersion(
    	Guid id, 
    	String^ name, 
    	long long size, 
    	int number, 
    	FileVersionState state, 
    	DateTime created, 
    	Guid createdByID, 
    	String^ createdByName, 
    	IFileContent^ content, 
    	FileContentSource contentSource, 
    	IFileErrorInfo^ errorInfo, 
    	IFile^ file, 
    	array<unsigned char>^ hash = nullptr, 
    	Nullable<Guid> linkID = nullptr
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            size : int64 * 
            number : int * 
            state : FileVersionState * 
            created : DateTime * 
            createdByID : Guid * 
            createdByName : string * 
            content : IFileContent * 
            contentSource : FileContentSource * 
            errorInfo : IFileErrorInfo * 
            file : IFile * 
            ?hash : byte[] * 
            ?linkID : Nullable<Guid> 
    (* Defaults:
            let _hash = defaultArg hash null
            let _linkID = defaultArg linkID null
    *)
    -> FileVersion
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя файла [Name](P_Tessa_Files_IFileObject_Name.htm) на момент создания версии. 
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Начальный разер файла или версии файла в байтах. При изменении размера контента content свойство [Size](P_Tessa_Files_FileObject_Size.htm) будет синхронно изменяться. Значение не может быть отрицательным. Значение [UnknownSize](F_Tessa_Files_FileContent_UnknownSize.htm) определяет, что размер неизвестен. 
number [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Порядковый номер версии файла, отсчитываемый от 1.
state [FileVersionState](T_Tessa_Files_FileVersionState.htm)
    Состояние версии файла.
created [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата создания версии.
createdByID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор пользователя, который создал версию.
createdByName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя пользователя, который создал версию.
content [IFileContent](T_Tessa_Files_IFileContent.htm)
    Контент версии файла.
contentSource [FileContentSource](T_Tessa_Files_FileContentSource.htm)
    Местоположение контента версии файла.
errorInfo [IFileErrorInfo](T_Tessa_Files_IFileErrorInfo.htm)
     Информация по ошибке, возникшей при сохранении версии файла, или null, если ошибок не было. 
file [IFile](T_Tessa_Files_IFile.htm)
     Файл, к которому относится версия. Свойства файла имеют текущее состояние, а не таковое на момент создания версии. 
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[] (Optional)
     Хеш контента файла или версии файла, или null, если хеш не вычислен. 
linkID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Внешний идентификатор версии файла или null, если такой идентификатор не задан. Может использоваться в расширениях для связи с содержимым во внешнем местоположении. 
## __См. также
#### Ссылки
[FileVersion - ](T_Tessa_Files_FileVersion.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
