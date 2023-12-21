# IApplicationModel.AttachMonitor - метод
Устанавливает мониторинг установки приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AttachMonitor(
    	[NotNullAttribute] IInstallationProcessMonitor monitor
    )
VB __Копировать
     Sub AttachMonitor ( 
    	<NotNullAttribute> monitor As IInstallationProcessMonitor
    )
C++ __Копировать
     void AttachMonitor(
    	[NotNullAttribute] IInstallationProcessMonitor^ monitor
    )
F# __Копировать
     abstract AttachMonitor : 
            [<NotNullAttribute>] monitor : IInstallationProcessMonitor -> unit 
#### Параметры
monitor
[IInstallationProcessMonitor](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
     Монитор установки приложения 
## __См. также
#### Ссылки
[IApplicationModel - ](T_Tessa_Applications_IApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
