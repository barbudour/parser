# KrErrorHelper - класс
Предоставляет вспомогательные методы для формирования сообщений об ошибках
выполнения маршрутов документов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrErrorHelper
VB __Копировать
     Public NotInheritable Class KrErrorHelper
C++ __Копировать
     public ref class KrErrorHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrErrorHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrErrorHelper
##  __Методы
[AssertKrSatellte](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_AssertKrSatellte.htm)|
Проверят, что тип указанной карточки равен
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm),
если это не так, то создаёт исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception).  
---|---  
[ButtonSqlVisibilityError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_ButtonSqlVisibilityError.htm)|
Формирует сообщение, содержащее информацию об ошибке, возникшей при выполнении
SQL условия видимости кнопки вторичного процесса.  
[ButtonVisibilityError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_ButtonVisibilityError.htm)|
Формирует сообщение, содержащее информацию об ошибке, возникшей при выполнении
условия видимости кнопки вторичного процесса.  
[DesignTimeError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_DesignTimeError.htm)|  
[FormatEmptyRoute](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_FormatEmptyRoute.htm)|
Форматирование сообщения о том, что в маршруте нет активных этапов с
дополнительным выводом кнопки.  
[FormatErrorMessageTrace(String,
String)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_FormatErrorMessageTrace.htm)|
Формирует сообщение, содержащее информацию о месте возникновения ошибки.  
[FormatErrorMessageTrace(String, String, String,
String)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_FormatErrorMessageTrace_1.htm)|
Формирует сообщение, содержащее информацию о месте возникновения ошибки.  
[FormatErrorMessageTrace(String, String, String, String,
String)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_FormatErrorMessageTrace_2.htm)|
Формирует сообщение, содержащее информацию о месте возникновения ошибки.  
[GetTraceTextFromExecutionUnit](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_GetTraceTextFromExecutionUnit.htm)|  
[GetTraceTextFromStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_GetTraceTextFromStage.htm)|  
[PerformerNotSpecified](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_PerformerNotSpecified.htm)|  
[PlannedNotSpecified](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_PlannedNotSpecified.htm)|  
[ProcessStartingForDifferentCardID](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_ProcessStartingForDifferentCardID.htm)|  
[RuntimeError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_RuntimeError.htm)|  
[SecondaryProcessExecutionError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_SecondaryProcessExecutionError.htm)|
Формирует сообщение, содержащее информацию об ошибке, возникшей при выполнении
условия выполнения вторичного процесса.  
[SecondaryProcessSqlExecutionError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_SecondaryProcessSqlExecutionError.htm)|
Формирует сообщение, содержащее информацию об ошибке, возникшей при выполнении
SQL условия выполнения вторичного процесса.  
[SqlDesignTimeError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_SqlDesignTimeError.htm)|  
[SqlPerformersError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_SqlPerformersError.htm)|
Формирует сообщение, содержащее информацию об ошибке, возникшей при получении
SQL-исполнителей.  
[SqlRuntimeError](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_SqlRuntimeError.htm)|  
[TimeLimitNotSpecified](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_TimeLimitNotSpecified.htm)|  
[TimeLimitOrPlannedNotSpecified](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_TimeLimitOrPlannedNotSpecified.htm)|  
[UnexpectedError(IKrExecutionUnit)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_UnexpectedError.htm)|  
[UnexpectedError(Stage)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_UnexpectedError_1.htm)|  
[WarnStageHandlerIsNull](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_WarnStageHandlerIsNull.htm)|  
[WarnStageTypeIsNull](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper_WarnStageTypeIsNull.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
