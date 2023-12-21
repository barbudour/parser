# DefaultGlobalMutex - конструктор
Создаёт экземпляр класса с указанием глобально уникального имени мьютекса.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public DefaultGlobalMutex(
    	string name
    )
VB __Копировать
     Public Sub New ( 
    	name As String
    )
C++ __Копировать
     public:
    DefaultGlobalMutex(
    	String^ name
    )
F# __Копировать
     new : 
            name : string -> DefaultGlobalMutex
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Глобально уникальное имя объекта синхронизации. Не должно быть равно null или пустой строке. Обычно не зависит от регистра символов. 
## __См. также
#### Ссылки
[DefaultGlobalMutex - ](T_Chronos_Platform_IPC_DefaultGlobalMutex.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
