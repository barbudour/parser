# FileVersionLink - конструктор
Создаёт экземпляр класса с указанием его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileVersionLink(
    	Uri uri,
    	Guid fileID,
    	Guid versionID
    )
VB __Копировать
     Public Sub New ( 
    	uri As Uri,
    	fileID As Guid,
    	versionID As Guid
    )
C++ __Копировать
     public:
    FileVersionLink(
    	Uri^ uri, 
    	Guid fileID, 
    	Guid versionID
    )
F# __Копировать
     new : 
            uri : Uri * 
            fileID : Guid * 
            versionID : Guid -> FileVersionLink
#### Параметры
uri [Uri](https://learn.microsoft.com/dotnet/api/system.uri)
    Ссылка, используемая для открытия версии файла.
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, на версию которого делается ссылка.
versionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла, на которую делается ссылка.
##  __См. также
#### Ссылки
[FileVersionLink - ](T_Tessa_Files_FileVersionLink.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
