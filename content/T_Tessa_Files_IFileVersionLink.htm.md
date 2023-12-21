# IFileVersionLink - интерфейс
Ссылка на версию файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileVersionLink : IEquatable<IFileVersionLink>
VB __Копировать
     Public Interface IFileVersionLink
    	Inherits IEquatable(Of IFileVersionLink)
C++ __Копировать
     public interface class IFileVersionLink : IEquatable<IFileVersionLink^>
F# __Копировать
     type IFileVersionLink = 
        interface
            interface IEquatable<IFileVersionLink>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileVersionLink>
##  __Свойства
[FileID](P_Tessa_Files_IFileVersionLink_FileID.htm)| Идентификатор файла, на
версию которого делается ссылка.  
---|---  
[Uri](P_Tessa_Files_IFileVersionLink_Uri.htm)| Ссылка, используемая для
открытия версии файла.  
[VersionID](P_Tessa_Files_IFileVersionLink_VersionID.htm)| Идентификатор
версии файла, на которую делается ссылка.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileVersionLink>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
