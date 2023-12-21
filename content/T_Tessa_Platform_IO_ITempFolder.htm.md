# ITempFolder - интерфейс
Информация по папке, которая предоставляет быстрый доступ ко множеству
временных файлов [ITempFile](T_Tessa_Platform_IO_ITempFile.htm) с
отличающимися в пределах этой папки именами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITempFolder : IDisposable
VB __Копировать
     Public Interface ITempFolder
    	Inherits IDisposable
C++ __Копировать
     public interface class ITempFolder : IDisposable
F# __Копировать
     type ITempFolder = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[FolderPath](P_Tessa_Platform_IO_ITempFolder_FolderPath.htm)| Путь ко
временной папке.  
---|---  
[IsDisposed](P_Tessa_Platform_IO_ITempFolder_IsDisposed.htm)|  Признак того,
что папка была освобождена, а её содержимое - удалено. Для такой папки нельзя
получать новые файлы.  
## __Методы
[AcquireFile](M_Tessa_Platform_IO_ITempFolder_AcquireFile.htm)|  Получает
информацию по временному файлу из текущей папки. При освобождении папки файл
будет удалён. При освобождении всех файлов удаляется папка. Вызывать на файле
Dispose не требуется, он будет вызван автоматически, но если вызвать Dispose
для всех файлов, то физически папка будет удалена и действий по освобождению
папки не потребуется.  
---|---  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
##  __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
