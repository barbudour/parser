# ProcessRefContainer - конструктор
Создаёт экземпляр класса, осуществляющий хранение объектов
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm) в файле
изолированного хранилища с указанным именем.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public ProcessRefContainer(
    	string filename
    )
VB __Копировать
     Public Sub New ( 
    	filename As String
    )
C++ __Копировать
     public:
    ProcessRefContainer(
    	String^ filename
    )
F# __Копировать
     new : 
            filename : string -> ProcessRefContainer
#### Параметры
filename [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя файла, уникальное для изолированного хранилища.
##  __Заметки
Имя должно быть корректным именем файла, причём в системе для текущего
пользователя не должно существовать процессов, которые используют класс
[ProcessRefContainer](T_Chronos_Platform_Processes_ProcessRefContainer.htm) с
тем же именем, но для доступа к другому хранилищу.
## __См. также
#### Ссылки
[ProcessRefContainer - ](T_Chronos_Platform_Processes_ProcessRefContainer.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
