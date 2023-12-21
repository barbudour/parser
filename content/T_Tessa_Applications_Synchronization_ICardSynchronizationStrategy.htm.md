# ICardSynchronizationStrategy - интерфейс
Описание интерфейса стратегии синхронизации приложения с карточкой приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardSynchronizationStrategy : IApplicationSynchronizationStrategy
VB __Копировать
     Public Interface ICardSynchronizationStrategy
    	Inherits IApplicationSynchronizationStrategy
C++ __Копировать
     public interface class ICardSynchronizationStrategy : IApplicationSynchronizationStrategy
F# __Копировать
     type ICardSynchronizationStrategy = 
        interface
            interface IApplicationSynchronizationStrategy
        end
Implements
    [IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm)
##  __Методы
[CreateFileAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_CreateFileAsync.htm)|
Создает новый файл с параметрами и содержимым, заданными в content  
(Унаследован от
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm))  
---|---  
[DeleteFileAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_DeleteFileAsync.htm)|
Удаляет файл заданный в file  
(Унаследован от
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm))  
[OnSynchronizationCompletedAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_OnSynchronizationCompletedAsync.htm)|
Вызывается при завершении синхронизации элементов  
(Унаследован от
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm))  
[ReplaceFileAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_ReplaceFileAsync.htm)|
Заменяет файл с параметрами и содержимым, заданными в content  
(Унаследован от
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm))  
[StartSynchronizationAsync](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_StartSynchronizationAsync.htm)|
Вызывается при запуске процесса синхронизации  
(Унаследован от
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
