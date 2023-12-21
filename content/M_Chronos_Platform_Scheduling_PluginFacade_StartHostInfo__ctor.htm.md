# PluginFacade.StartHostInfo - конструктор
Создаёт экземпляр класса, с указанием параметров запуска processHost и
pluginsFolderPath.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public StartHostInfo(
    	IProcessHost processHost,
    	string pluginsFolderPath
    )
VB __Копировать
     Public Sub New ( 
    	processHost As IProcessHost,
    	pluginsFolderPath As String
    )
C++ __Копировать
     public:
    StartHostInfo(
    	IProcessHost^ processHost, 
    	String^ pluginsFolderPath
    )
F# __Копировать
     new : 
            processHost : IProcessHost * 
            pluginsFolderPath : string -> StartHostInfo
#### Параметры
processHost [IProcessHost](T_Chronos_Platform_Processes_IProcessHost.htm)
    Интерфейс запуска дочерних процессов.
pluginsFolderPath
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Папка, в которой осуществляется поиск плагинов. Поиск также выполняется в подпапках первого уровня. 
## __См. также
#### Ссылки
[PluginFacade.StartHostInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
