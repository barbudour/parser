# FileObject - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected FileObject(
    	Guid id,
    	string name,
    	long size,
    	IFileContent content,
    	IFileSource source,
    	byte[] hash = null
    )
VB __Копировать
     Protected Sub New ( 
    	id As Guid,
    	name As String,
    	size As Long,
    	content As IFileContent,
    	source As IFileSource,
    	Optional hash As Byte() = Nothing
    )
C++ __Копировать
     protected:
    FileObject(
    	Guid id, 
    	String^ name, 
    	long long size, 
    	IFileContent^ content, 
    	IFileSource^ source, 
    	array<unsigned char>^ hash = nullptr
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            size : int64 * 
            content : IFileContent * 
            source : IFileSource * 
            ?hash : byte[] 
    (* Defaults:
            let _hash = defaultArg hash null
    *)
    -> FileObject
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла или версии файла.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя файла или версии файла.
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Начальный разер файла или версии файла в байтах. При изменении размера контента content свойство [Size](P_Tessa_Files_FileObject_Size.htm) будет синхронно изменяться. Значение не может быть отрицательным. Значение [UnknownSize](F_Tessa_Files_FileContent_UnknownSize.htm) определяет, что размер неизвестен. 
content [IFileContent](T_Tessa_Files_IFileContent.htm)
    Контент файла или версии файла.
source [IFileSource](T_Tessa_Files_IFileSource.htm)
     Объект, обеспечивающий взаимодействие текущего объекта с подсистемой, в которой он был создан, например, с карточкой. 
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[] (Optional)
     Хеш контента файла или версии файла, или null, если хеш не вычислен. 
## __См. также
#### Ссылки
[FileObject - ](T_Tessa_Files_FileObject.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
