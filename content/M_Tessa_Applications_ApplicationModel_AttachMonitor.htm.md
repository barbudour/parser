# ApplicationModel.AttachMonitor - метод
Устанавливает мониторинг установки приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void AttachMonitor(
    	IInstallationProcessMonitor monitor
    )
VB __Копировать
     Public Sub AttachMonitor ( 
    	monitor As IInstallationProcessMonitor
    )
C++ __Копировать
     public:
    virtual void AttachMonitor(
    	IInstallationProcessMonitor^ monitor
    ) sealed
F# __Копировать
     abstract AttachMonitor : 
            monitor : IInstallationProcessMonitor -> unit 
    override AttachMonitor : 
            monitor : IInstallationProcessMonitor -> unit 
#### Параметры
monitor
[IInstallationProcessMonitor](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
     Монитор установки приложения 
#### Реализации
[IApplicationModel.AttachMonitor(IInstallationProcessMonitor)](M_Tessa_Applications_IApplicationModel_AttachMonitor.htm)  
##  __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
