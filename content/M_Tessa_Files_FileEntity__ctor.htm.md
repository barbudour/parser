# FileEntity - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected FileEntity(
    	Guid id,
    	IFileSource source
    )
VB __Копировать
     Protected Sub New ( 
    	id As Guid,
    	source As IFileSource
    )
C++ __Копировать
     protected:
    FileEntity(
    	Guid id, 
    	IFileSource^ source
    )
F# __Копировать
     new : 
            id : Guid * 
            source : IFileSource -> FileEntity
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла или версии файла.
source [IFileSource](T_Tessa_Files_IFileSource.htm)
     Объект, обеспечивающий взаимодействие текущего объекта с подсистемой, в которой он был создан, например, с карточкой. 
## __См. также
#### Ссылки
[FileEntity - ](T_Tessa_Files_FileEntity.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
