# FileSystemGlobalStorage.ProcessLockFilePath - свойство
Полный путь к файлу, имя которого уникально для текущего процесса и хранилища.
Наличие такого файла означает, что хранилище используется процессом.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected string ProcessLockFilePath { get; }
VB __Копировать
     Protected ReadOnly Property ProcessLockFilePath As String
    	Get
C++ __Копировать
     protected:
    property String^ ProcessLockFilePath {
    	String^ get ();
    }
F# __Копировать
     member ProcessLockFilePath : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[FileSystemGlobalStorage - ](T_Tessa_Platform_IPC_FileSystemGlobalStorage.htm)
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
