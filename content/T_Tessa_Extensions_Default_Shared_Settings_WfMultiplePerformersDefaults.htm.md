# WfMultiplePerformersDefaults - перечисление
Режим по умолчанию для флажков, которые устанавливаются в задаче при выборе
нескольких исполнителей.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public enum WfMultiplePerformersDefaults
VB __Копировать
     Public Enumeration WfMultiplePerformersDefaults
C++ __Копировать
     public enum class WfMultiplePerformersDefaults
F# __Копировать
     type WfMultiplePerformersDefaults
##  __Члены
MergeIntoSingleTask| 0|  Объединить список персональных ролей в единственную
задачу.  
---|---|---  
CreateMultipleTasks| 1|  Создать по одной задаче на каждую роль. Ответственный
исполнитель не назначается.  
Default| 1|  Значение по умолчанию. В текущей версии платформы это
CreateMultipleTasks.  
CreateMultipleTasksWithMajorPerformer| 2|  Создать по одной задаче на каждую
роль, причём первая роль назначается ответственным исполнителем.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
