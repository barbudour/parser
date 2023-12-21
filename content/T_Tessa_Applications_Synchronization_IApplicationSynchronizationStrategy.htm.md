# IApplicationSynchronizationStrategy - интерфейс
Описание интерфейса стратегии синхронизации приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationSynchronizationStrategy
VB __Копировать
     Public Interface IApplicationSynchronizationStrategy
C++ __Копировать
     public interface class IApplicationSynchronizationStrategy
F# __Копировать
     type IApplicationSynchronizationStrategy = interface end
##  __Методы
[CreateFileAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_CreateFileAsync.htm)|
Создает новый файл с параметрами и содержимым, заданными в content  
---|---  
[DeleteFileAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_DeleteFileAsync.htm)|
Удаляет файл заданный в file  
[OnSynchronizationCompletedAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_OnSynchronizationCompletedAsync.htm)|
Вызывается при завершении синхронизации элементов  
[ReplaceFileAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_ReplaceFileAsync.htm)|
Заменяет файл с параметрами и содержимым, заданными в content  
[StartSynchronizationAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_StartSynchronizationAsync.htm)|
Вызывается при запуске процесса синхронизации  
## __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
