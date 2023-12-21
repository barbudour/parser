# PluginGracefulLauncher.HasGracefulProcessesRunning - метод
Возвращает признак того, что присутствуют работающие процессы плагинов,
поддерживающих вежливую остановку.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasGracefulProcessesRunning()
VB __Копировать
     Public Function HasGracefulProcessesRunning As Boolean
C++ __Копировать
     public:
    bool HasGracefulProcessesRunning()
F# __Копировать
     member HasGracefulProcessesRunning : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если присутствует хотя бы один работающий процесс плагина,
поддерживающего вежливую остановку; false в противном случае.
## __Заметки
Метод выполняет очистку списка процессов плагинов, которые уже были завершены.
## __См. также
#### Ссылки
[PluginGracefulLauncher -
](T_Chronos_Platform_Scheduling_PluginGracefulLauncher.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
