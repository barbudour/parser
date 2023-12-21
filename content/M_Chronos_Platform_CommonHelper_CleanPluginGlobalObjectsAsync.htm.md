# CommonHelper.CleanPluginGlobalObjectsAsync - метод
Очищает глобальные объекты синхронизации, задействуемые для плагина.
Вызывается хост-процессом перед запуском дочерних процессов всех найденных
плагинов. Для плагинов, добавляемых при перепланировании, не вызывается.
Актуально только для Linux.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask CleanPluginGlobalObjectsAsync(
    	PluginRemoteCreationInfo pluginCreationInfo,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CleanPluginGlobalObjectsAsync ( 
    	pluginCreationInfo As PluginRemoteCreationInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    static ValueTask CleanPluginGlobalObjectsAsync(
    	PluginRemoteCreationInfo^ pluginCreationInfo, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CleanPluginGlobalObjectsAsync : 
            pluginCreationInfo : PluginRemoteCreationInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
pluginCreationInfo
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)
    Информация для создания объекта плагина.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
