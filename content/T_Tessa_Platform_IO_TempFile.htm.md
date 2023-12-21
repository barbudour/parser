# TempFile - класс
Класс, позволяющий создавать временные файлы.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TempFile
VB __Копировать
     Public NotInheritable Class TempFile
C++ __Копировать
     public ref class TempFile abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TempFile = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TempFile
##  __Методы
[Acquire](M_Tessa_Platform_IO_TempFile_Acquire.htm)|  Получает информацию по
временному файлу, которая может использоваться для его создания. Для
временного файла уже создаётся папка, поэтому файл можно сразу использовать по
пути [Path](P_Tessa_Platform_IO_ITempFile_Path.htm). Файл рекомендуется
удалить вызовом его метода
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose). Временный файл будет удалён при очередном запуске
приложения спустя сутки после того, как он не использовался.  
---|---  
[AcquireFolder(FileSpecialFolder)](M_Tessa_Platform_IO_TempFile_AcquireFolder_1.htm)|
Создаёт папку, которая предоставляет быстрый доступ ко множеству временных
файлов [ITempFile](T_Tessa_Platform_IO_ITempFile.htm) с отличающимися в
пределах этой папки именами. Физически на диске папка на создается. Папку
рекомендуется удалить вызовом её метода
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) или вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для всех полученных из неё файлов. При создании временной
папки в [Temp](T_Tessa_Platform_IO_FileSpecialFolder.htm) или
[Dumps](T_Tessa_Platform_IO_FileSpecialFolder.htm) она будет удалена при
очередном запуске приложения спустя сутки после того, как она не
использовалась.  
[AcquireFolder(String)](M_Tessa_Platform_IO_TempFile_AcquireFolder.htm)|
Создаёт папку, которая предоставляет быстрый доступ ко множеству временных
файлов [ITempFile](T_Tessa_Platform_IO_ITempFile.htm) с отличающимися в
пределах этой папки именами. Физически на диске папка на создается. Папку
рекомендуется удалить вызовом её метода
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) или вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для всех полученных из неё файлов.  
## __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
