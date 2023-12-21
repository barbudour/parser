# StageTypeFormatterBase.DefaultDateFormatting - метод
Задаёт отображаемый строк исполнения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DefaultDateFormatting(
    	DateTime? planned,
    	double? timeLimit,
    	IStageTypeFormatterContext context
    )
VB __Копировать
     Protected Shared Sub DefaultDateFormatting ( 
    	planned As DateTime?,
    	timeLimit As Double?,
    	context As IStageTypeFormatterContext
    )
C++ __Копировать
     protected:
    static void DefaultDateFormatting(
    	Nullable<DateTime> planned, 
    	Nullable<double> timeLimit, 
    	IStageTypeFormatterContext^ context
    )
F# __Копировать
     static member DefaultDateFormatting : 
            planned : Nullable<DateTime> * 
            timeLimit : Nullable<float> * 
            context : IStageTypeFormatterContext -> unit 
#### Параметры
planned
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
    Дата выполнения.
timeLimit
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Double](https://learn.microsoft.com/dotnet/api/system.double)>
    Срок, рабочие дни.
context
[IStageTypeFormatterContext](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext.htm)
    Контекст форматтера этапа.
##  __См. также
#### Ссылки
[StageTypeFormatterBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)
