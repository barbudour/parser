# PluginLauncherResolver.Register - метод
Регистрирует указанный объект
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm) в
контейнере и возвращает ключ, по которому можно будет получить ссылку на этот
объект.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginLauncherKey Register(
    	IPluginLauncher launcher
    )
VB __Копировать
     Public Function Register ( 
    	launcher As IPluginLauncher
    ) As PluginLauncherKey
C++ __Копировать
     public:
    PluginLauncherKey^ Register(
    	IPluginLauncher^ launcher
    )
F# __Копировать
     member Register : 
            launcher : IPluginLauncher -> PluginLauncherKey 
#### Параметры
launcher [IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm)
    Объект, который будет зарегистрирован в контейнере.
#### Возвращаемое значение
[PluginLauncherKey](T_Chronos_Platform_Scheduling_PluginLauncherKey.htm)  
Ключ зарегистрированного объекта
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm).
##  __См. также
#### Ссылки
[PluginLauncherResolver -
](T_Chronos_Platform_Scheduling_PluginLauncherResolver.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
