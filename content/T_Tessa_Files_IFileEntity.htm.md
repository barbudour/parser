# IFileEntity - интерфейс
Базовый интерфейс для всех объектов в API файлов, которые идентифицируются по
идентификатору [Guid](https://learn.microsoft.com/dotnet/api/system.guid) и
связаны с источником [IFileSource](T_Tessa_Files_IFileSource.htm).
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileEntity : IEquatable<IFileEntity>, 
    	INotifyPropertyChanged
VB __Копировать
     Public Interface IFileEntity
    	Inherits IEquatable(Of IFileEntity), INotifyPropertyChanged
C++ __Копировать
     public interface class IFileEntity : IEquatable<IFileEntity^>, 
    	INotifyPropertyChanged
F# __Копировать
     type IFileEntity = 
        interface
            interface IEquatable<IFileEntity>
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileEntity>
##  __Свойства
[ID](P_Tessa_Files_IFileEntity_ID.htm)| Идентификатор объекта.  
---|---  
[Source](P_Tessa_Files_IFileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileEntity>)  
---|---  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
