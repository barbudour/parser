# IApplicationLaunchingStrategy - интерфейс
Описание интерфейса стратегии запуска приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationLaunchingStrategy
VB __Копировать
     Public Interface IApplicationLaunchingStrategy
C++ __Копировать
     public interface class IApplicationLaunchingStrategy
F# __Копировать
     type IApplicationLaunchingStrategy = interface end
##  __Методы
[CreateProcess](M_Tessa_Applications_IApplicationLaunchingStrategy_CreateProcess.htm)|
Осуществляет создание процесса приложения  
---|---  
[UpdateApplicationAsync](M_Tessa_Applications_IApplicationLaunchingStrategy_UpdateApplicationAsync.htm)|
Осуществляет обновление приложения  
[UpdateAvailableAsync](M_Tessa_Applications_IApplicationLaunchingStrategy_UpdateAvailableAsync.htm)|
Проверяет необходимость обновления приложения. Возвращает признак наличия
обновления приложения и действительную разрядность приложения на момент
проверки, если обновление доступно (иначе нельзя опираться на возвращённое
значение).  
## __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
