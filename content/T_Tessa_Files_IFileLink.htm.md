# IFileLink - интерфейс
Ссылка на файл.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileLink : IEquatable<IFileLink>
VB __Копировать
     Public Interface IFileLink
    	Inherits IEquatable(Of IFileLink)
C++ __Копировать
     public interface class IFileLink : IEquatable<IFileLink^>
F# __Копировать
     type IFileLink = 
        interface
            interface IEquatable<IFileLink>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileLink>
##  __Свойства
[FileID](P_Tessa_Files_IFileLink_FileID.htm)| Идентификатор файла, на который
делается ссылка.  
---|---  
[Uri](P_Tessa_Files_IFileLink_Uri.htm)| Ссылка, используемая для открытия
файла.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileLink>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
