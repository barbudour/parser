# ISynchronizationTarget - интерфейс
Описание интерфейса целевого объекта синхронизации.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISynchronizationTarget
VB __Копировать
     Public Interface ISynchronizationTarget
C++ __Копировать
     public interface class ISynchronizationTarget
F# __Копировать
     type ISynchronizationTarget = interface end
##  __Методы
[GetSynchronizationStrategy](M_Tessa_Applications_Synchronization_ISynchronizationTarget_GetSynchronizationStrategy.htm)|
Возвращает стратегию синхронизации файлов  
---|---  
[TryGetApplicationPackageAsync](M_Tessa_Applications_Synchronization_ISynchronizationTarget_TryGetApplicationPackageAsync.htm)|
Возвращает пакет приложения содержащий файлы которые содержатся в целевом
объекте синхронизации. В случае ошибки получения или отсутствия приложения в
целевом объекте возвращает null. Ошибки получения пакета приложения
записываются в validationResultBuilder  
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
