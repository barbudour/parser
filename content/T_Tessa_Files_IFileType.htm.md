# IFileType - интерфейс
Тип файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileType : IEquatable<IFileType>
VB __Копировать
     Public Interface IFileType
    	Inherits IEquatable(Of IFileType)
C++ __Копировать
     public interface class IFileType : IEquatable<IFileType^>
F# __Копировать
     type IFileType = 
        interface
            interface IEquatable<IFileType>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileType>
##  __Свойства
[Caption](P_Tessa_Files_IFileType_Caption.htm)|  Отображаемое имя типа файла,
которое видит пользователь. Не может быть равно null, пустой строке или
строке, состоящей из пробелов.  
---|---  
[ID](P_Tessa_Files_IFileType_ID.htm)| Уникальный идентификатор типа файла.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileType>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
