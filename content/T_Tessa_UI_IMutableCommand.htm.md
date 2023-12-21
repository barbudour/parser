# IMutableCommand - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMutableCommand
VB __Копировать
     Public Interface IMutableCommand
C++ __Копировать
     public interface class IMutableCommand
F# __Копировать
     type IMutableCommand = interface end
##  __Свойства
[CanExecute](P_Tessa_UI_IMutableCommand_CanExecute.htm)|  Делегат,
определяющий доступность выполнения команд, которые были созданы для этого
объекта. По умолчанию делегат всегда возвращает true. Если задать значение
null, то также возвращается true. Изменение делегата отражается как на уже
созданный командах, так и на ещё не созданных.  
---|---  
[Execute](P_Tessa_UI_IMutableCommand_Execute.htm)|  Делегат, определяющий
действие, выполняемое командами, которые были созданы для этого объекта. По
умолчанию делегат не выполняет никаких действий. Если задать значение null, то
действий также не выполняется. Изменение делегата отражается как на уже
созданный командах, так и на ещё не созданных.  
## __Методы
[CreateCommand](M_Tessa_UI_IMutableCommand_CreateCommand.htm)|  Создаёт и
возвращает команду, которая сопоставлена с актуальными делегатами
[Execute](P_Tessa_UI_IMutableCommand_Execute.htm) и
[CanExecute](P_Tessa_UI_IMutableCommand_CanExecute.htm).  
---|---  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
