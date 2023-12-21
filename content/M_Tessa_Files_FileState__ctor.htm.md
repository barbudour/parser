# FileState - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileState(
    	string name,
    	IFileCategory category,
    	IFileType type,
    	IFile origin
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	category As IFileCategory,
    	type As IFileType,
    	origin As IFile
    )
C++ __Копировать
     public:
    FileState(
    	String^ name, 
    	IFileCategory^ category, 
    	IFileType^ type, 
    	IFile^ origin
    )
F# __Копировать
     new : 
            name : string * 
            category : IFileCategory * 
            type : IFileType * 
            origin : IFile -> FileState
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя файла. Не может быть равно null.
category [IFileCategory](T_Tessa_Files_IFileCategory.htm)
    Категория файла или null, если файл не имеет категории.
type [IFileType](T_Tessa_Files_IFileType.htm)
    Тип файла. Не может быть равен null.
origin [IFile](T_Tessa_Files_IFile.htm)
     Исходный файл, из которого был скопирован текущий файл, или null, если текущий файл не был скопирован. 
## __См. также
#### Ссылки
[FileState - ](T_Tessa_Files_FileState.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
