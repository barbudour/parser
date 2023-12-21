# PluginFacade.OnPluginImported - метод
Вызывается после импортирования плагина, указываемого в параметре e.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void OnPluginImported(
    	PluginImportEventArgs e
    )
VB __Копировать
     Protected Overridable Sub OnPluginImported ( 
    	e As PluginImportEventArgs
    )
C++ __Копировать
     protected:
    virtual void OnPluginImported(
    	PluginImportEventArgs^ e
    )
F# __Копировать
     abstract OnPluginImported : 
            e : PluginImportEventArgs -> unit 
    override OnPluginImported : 
            e : PluginImportEventArgs -> unit 
#### Параметры
e
[PluginImportEventArgs](T_Chronos_Platform_Scheduling_PluginImportEventArgs.htm)
    Аргументы события.
##  __Заметки
По умолчанию вызывает событие
[PluginImported](E_Chronos_Platform_Scheduling_PluginFacade_PluginImported.htm).
Может быть переопределён в производных классах.
## __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
