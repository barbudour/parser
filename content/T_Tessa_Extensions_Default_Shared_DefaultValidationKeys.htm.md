# DefaultValidationKeys - класс
Ключи валидации, используемые в типовом решении.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DefaultValidationKeys
VB __Копировать
     Public NotInheritable Class DefaultValidationKeys
C++ __Копировать
     public ref class DefaultValidationKeys abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DefaultValidationKeys = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultValidationKeys
##  __Методы
[Register](M_Tessa_Extensions_Default_Shared_DefaultValidationKeys_Register.htm)|
Регистрирует все стандартные ключи валидации посредством заданного метода.  
---|---  
## __Поля
[CancelDialog](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_CancelDialog.htm)|
Служебный ключ валидации, используемый для передачи флага прерывающего
обработку диалога.  
---|---  
[MainProcessStarted](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_MainProcessStarted.htm)|
Пересчет маршрута недоступен, т.к. основной процесс запущен.  
[RecalcWithChanges](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_RecalcWithChanges.htm)|
Маршрут обновлен.  
[RecalcWithoutChanges](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_RecalcWithoutChanges.htm)|
Маршрут не изменен.  
[StageAdded](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_StageAdded.htm)|
Этап {0} был добавлен{1}.
{0} - Название этапа.
{1} - Строка " (скрытый)", если этап является скрытым, иначе -
[Empty](https://learn.microsoft.com/dotnet/api/system.string.empty).  
[StageDeleted](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_StageDeleted.htm)|
Этап {0} был удален{1}.
{0} - Название этапа.
{1} - Строка " (скрытый)", если этап является скрытым, иначе -
[Empty](https://learn.microsoft.com/dotnet/api/system.string.empty).  
[StageModified](F_Tessa_Extensions_Default_Shared_DefaultValidationKeys_StageModified.htm)|
Этап {0} {1} был изменен{2}.
{0} - Актуальное название этапа.
{1} - Строка "(переименован из "<Старое название этапа>")", если название
этапа было изменено, иначе
[Empty](https://learn.microsoft.com/dotnet/api/system.string.empty).
{1} - Строка " (скрытый)", если этап является скрытым, иначе -
[Empty](https://learn.microsoft.com/dotnet/api/system.string.empty).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
