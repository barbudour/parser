# File - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public File(
    	Guid id,
    	string name,
    	long size,
    	IFileCategory category,
    	IFileType type,
    	IFileContent content,
    	IFileSource source,
    	DateTime? modified = null,
    	Guid? modifiedByID = null,
    	string modifiedByName = null,
    	IFilePermissions permissions = null,
    	bool isLocal = true,
    	IFile origin = null,
    	byte[] hash = null
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	size As Long,
    	category As IFileCategory,
    	type As IFileType,
    	content As IFileContent,
    	source As IFileSource,
    	Optional modified As DateTime? = Nothing,
    	Optional modifiedByID As Guid? = Nothing,
    	Optional modifiedByName As String = Nothing,
    	Optional permissions As IFilePermissions = Nothing,
    	Optional isLocal As Boolean = true,
    	Optional origin As IFile = Nothing,
    	Optional hash As Byte() = Nothing
    )
C++ __Копировать
     public:
    File(
    	Guid id, 
    	String^ name, 
    	long long size, 
    	IFileCategory^ category, 
    	IFileType^ type, 
    	IFileContent^ content, 
    	IFileSource^ source, 
    	Nullable<DateTime> modified = nullptr, 
    	Nullable<Guid> modifiedByID = nullptr, 
    	String^ modifiedByName = nullptr, 
    	IFilePermissions^ permissions = nullptr, 
    	bool isLocal = true, 
    	IFile^ origin = nullptr, 
    	array<unsigned char>^ hash = nullptr
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            size : int64 * 
            category : IFileCategory * 
            type : IFileType * 
            content : IFileContent * 
            source : IFileSource * 
            ?modified : Nullable<DateTime> * 
            ?modifiedByID : Nullable<Guid> * 
            ?modifiedByName : string * 
            ?permissions : IFilePermissions * 
            ?isLocal : bool * 
            ?origin : IFile * 
            ?hash : byte[] 
    (* Defaults:
            let _modified = defaultArg modified null
            let _modifiedByID = defaultArg modifiedByID null
            let _modifiedByName = defaultArg modifiedByName null
            let _permissions = defaultArg permissions null
            let _isLocal = defaultArg isLocal true
            let _origin = defaultArg origin null
            let _hash = defaultArg hash null
    *)
    -> File
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя файла.
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Начальный разер файла или версии файла в байтах. При изменении размера контента content свойство [Size](P_Tessa_Files_FileObject_Size.htm) будет синхронно изменяться. Значение не может быть отрицательным. Значение [UnknownSize](F_Tessa_Files_FileContent_UnknownSize.htm) определяет, что размер неизвестен. 
category [IFileCategory](T_Tessa_Files_IFileCategory.htm)
    Категория файла или null, если файл не имеет категории.
type [IFileType](T_Tessa_Files_IFileType.htm)
    Тип файла.
content [IFileContent](T_Tessa_Files_IFileContent.htm)
    Контент файла.
source [IFileSource](T_Tessa_Files_IFileSource.htm)
     Объект, обеспечивающий взаимодействие файла с подсистемой, в которой он был создан, например, с карточкой. 
modified
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
(Optional)
    Дата и время последнего изменения файла.
modifiedByID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
    Идентификатор пользователя изменившего файл.
modifiedByName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя пользователя изменившего файл.
permissions [IFilePermissions](T_Tessa_Files_IFilePermissions.htm) (Optional)
     Разрешения на действие с файлом или null, если используются разрешения по умолчанию. 
isLocal [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что файл был загружен локально и отсутствует во внешней подсистеме. 
origin [IFile](T_Tessa_Files_IFile.htm) (Optional)
     Исходный файл, из которого был скопирован текущий файл, или null, если текущий файл не был скопирован. 
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[] (Optional)
     Хеш контента файла или версии файла, или null, если хеш не вычислен. 
## __См. также
#### Ссылки
[File - ](T_Tessa_Files_File.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
