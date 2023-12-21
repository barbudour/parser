# ISynchronizationSource - интерфейс
Описание интерфейса источника синхронизации
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISynchronizationSource
VB __Копировать
     Public Interface ISynchronizationSource
C++ __Копировать
     public interface class ISynchronizationSource
F# __Копировать
     type ISynchronizationSource = interface end
##  __Методы
[TryCreateSynchronizationEnumerableAsync](M_Tessa_Applications_Synchronization_ISynchronizationSource_TryCreateSynchronizationEnumerableAsync.htm)|
Осуществляет попытку создания перечислителя файлов необходимых для
синхронизации элементов между файлами находящимися в источнике и текущем
состоянии пакета приложения находящегося в состоянии currentState. В случае
если не при создании произошли ошибки, то ошибки помещаются в
validationResultBuilder, и возвращается null  
---|---  
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
