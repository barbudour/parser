# PluginLauncherResolver.Resolve - метод
Получает ссылку на зарегистрированный объект
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm) по
указанному ключу.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IPluginLauncher Resolve(
    	PluginLauncherKey key
    )
VB __Копировать
     Public Function Resolve ( 
    	key As PluginLauncherKey
    ) As IPluginLauncher
C++ __Копировать
     public:
    IPluginLauncher^ Resolve(
    	PluginLauncherKey^ key
    )
F# __Копировать
     member Resolve : 
            key : PluginLauncherKey -> IPluginLauncher 
#### Параметры
key [PluginLauncherKey](T_Chronos_Platform_Scheduling_PluginLauncherKey.htm)
    Ключ зарегистрированного объекта [IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm).
#### Возвращаемое значение
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm)  
Ссылка на зарегистрированный объект
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm).
##  __См. также
#### Ссылки
[PluginLauncherResolver -
](T_Chronos_Platform_Scheduling_PluginLauncherResolver.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
