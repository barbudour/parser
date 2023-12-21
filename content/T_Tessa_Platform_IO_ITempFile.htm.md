# ITempFile - интерфейс
Информация по временному файлу.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITempFile : IDisposable, 
    	ISealable
VB __Копировать
     Public Interface ITempFile
    	Inherits IDisposable, ISealable
C++ __Копировать
     public interface class ITempFile : IDisposable, 
    	ISealable
F# __Копировать
     type ITempFile = 
        interface
            interface IDisposable
            interface ISealable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[FolderPath](P_Tessa_Platform_IO_ITempFile_FolderPath.htm)| Полный путь к
папке с временным файлом.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Name](P_Tessa_Platform_IO_ITempFile_Name.htm)|  Имя временного файла. Может
не быть уникальным, т.к. он располагается во временной папке с уникальным
именем.  
[Path](P_Tessa_Platform_IO_ITempFile_Path.htm)| Полный путь к временному
файлу.  
##  __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[Rename](M_Tessa_Platform_IO_ITempFile_Rename.htm)| Переименовывает временный
файл.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
