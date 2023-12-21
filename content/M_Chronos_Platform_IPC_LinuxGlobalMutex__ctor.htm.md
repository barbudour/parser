# LinuxGlobalMutex - конструктор
Создаёт экземпляр класса с указанием глобально уникального имени мьютекса.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     public LinuxGlobalMutex(
    	string name
    )
VB __Копировать
     Public Sub New ( 
    	name As String
    )
C++ __Копировать
     public:
    LinuxGlobalMutex(
    	String^ name
    )
F# __Копировать
     new : 
            name : string -> LinuxGlobalMutex
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Глобально уникальное имя объекта синхронизации. Не должно быть равно null или пустой строке. Обычно не зависит от регистра символов. 
## __См. также
#### Ссылки
[LinuxGlobalMutex - ](T_Chronos_Platform_IPC_LinuxGlobalMutex.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
